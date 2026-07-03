# -*- coding: utf-8 -*-
"""
한국부동산원 '청약Home 분양정보 조회 서비스'(공공데이터포털) 호출 모듈.

APT(아파트) 분양공고는 공공분양/민간분양 모두 청약홈을 통해 단일하게 접수되므로,
이 API 하나로 공공+민간 분양정보를 함께 가져올 수 있습니다.

데이터 출처: 한국부동산원_청약홈 분양정보 조회 서비스 (공공데이터포털 #15098547)
https://www.data.go.kr/data/15098547/openapi.do
"""

import json
import urllib.error
import urllib.parse
import urllib.request

BASE_URL = "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail"

# 청약홈 공급지역명(SUBSCRPT_AREA_CODE_NM)에서 쓰는 시/도 축약 표기.
TARGET_REGIONS = ("서울", "경기")

# 주택상세구분코드명(HOUSE_DTL_SECD_NM)에 아래 단어가 포함되면 '공공분양'으로 분류합니다.
# (분류가 애매할 수 있어 메시지에는 원본 구분값도 함께 표시합니다.)
PUBLIC_HINTS = ("공공", "국민", "뉴:홈", "뉴홈", "신혼희망타운", "행복주택", "영구임대", "국민임대")

PER_PAGE = 100
MAX_PAGES = 30  # 안전장치: 지역당 최대 3,000건까지만 순회합니다.


def _normalize_key(service_key):
    """
    공공데이터포털 인증키는 Encoding(퍼센트 인코딩)/Decoding(원문) 두 형태로 발급됩니다.
    Encoding 값을 그대로 넣어도 이중 인코딩되지 않도록 한 번 디코딩해 둡니다.
    """
    if "%" in service_key:
        try:
            return urllib.parse.unquote(service_key)
        except Exception:  # noqa: BLE001
            return service_key
    return service_key


def _request(service_key, page, per_page, region_keyword):
    params = {
        "serviceKey": _normalize_key(service_key),
        "page": page,
        "perPage": per_page,
        "cond[SUBSCRPT_AREA_CODE_NM::EQ]": region_keyword,
    }
    url = BASE_URL + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            "Applyhome API HTTP {0}: {1}".format(exc.code, detail[:500])
        ) from exc

    try:
        data = json.loads(body)
    except ValueError as exc:
        raise RuntimeError(
            "Applyhome API 응답을 JSON으로 해석하지 못했습니다 "
            "(서비스키 오류/승인 대기 등을 의심해보세요): {0}".format(body[:500])
        ) from exc

    if not isinstance(data, dict) or "data" not in data:
        raise RuntimeError("Applyhome API 응답 형식이 예상과 다릅니다: {0}".format(body[:500]))
    return data


def fetch_region(service_key, region_keyword):
    """지정한 지역(예: '서울', '경기')의 APT 분양정보를 모두 가져옵니다."""
    rows = []
    page = 1
    while page <= MAX_PAGES:
        data = _request(service_key, page, PER_PAGE, region_keyword)
        page_rows = data.get("data") or []
        rows.extend(page_rows)
        total = data.get("totalCount", len(rows))
        if not page_rows or page * PER_PAGE >= total:
            break
        page += 1
    return rows


def fetch_seoul_gyeonggi(service_key):
    """서울 + 경기 지역 APT 분양정보를 모두 가져와 중복 제거 후 반환합니다."""
    merged = {}
    for region in TARGET_REGIONS:
        for row in fetch_region(service_key, region):
            area_name = row.get("SUBSCRPT_AREA_CODE_NM") or ""
            # cond 필터가 기대와 다르게 동작할 경우를 대비한 이중 확인.
            if not any(keyword in area_name for keyword in TARGET_REGIONS):
                continue
            merged[listing_key(row)] = row
    return list(merged.values())


def listing_key(row):
    return "{0}_{1}".format(row.get("HOUSE_MANAGE_NO", ""), row.get("PBLANC_NO", ""))


def classify(row):
    """공고를 '공공분양' 또는 '민간분양'으로 분류합니다 (HOUSE_DTL_SECD_NM 기반 추정)."""
    detail = row.get("HOUSE_DTL_SECD_NM") or ""
    if any(hint in detail for hint in PUBLIC_HINTS):
        return "공공분양"
    return "민간분양"


def detail_url(row):
    house_manage_no = row.get("HOUSE_MANAGE_NO")
    pblanc_no = row.get("PBLANC_NO")
    if house_manage_no and pblanc_no:
        return (
            "https://www.applyhome.co.kr/ap/apa/aaa/gnrlSpsuslnfoDtlInqireView.do"
            "?houseManageNo={0}&pblancNo={1}".format(house_manage_no, pblanc_no)
        )
    return "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do"
