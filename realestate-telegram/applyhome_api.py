# -*- coding: utf-8 -*-
"""
한국부동산원 '청약Home 분양정보 조회 서비스'(공공데이터포털) 호출 모듈.

주택유형별로 오퍼레이션(엔드포인트)이 나뉘어 있어 모두 조회합니다:
  - APT (아파트 — 공공분양/민간분양, 민간사전청약·신혼희망타운 포함)
  - 오피스텔 / 도시형생활주택 / 민간임대 / 생활숙박시설
  - APT 무순위·잔여세대
  - 공공지원 민간임대
  - 임의공급

APT 분양공고는 공공/민간 모두 청약홈을 통해 단일하게 접수되므로,
이 API로 공공+민간 분양정보를 함께 가져올 수 있습니다.

데이터 출처: 한국부동산원_청약홈 분양정보 조회 서비스 (공공데이터포털 #15098547)
https://www.data.go.kr/data/15098547/openapi.do
"""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE_URL = "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/"

# (엔드포인트 ID, 오퍼레이션명, 메시지에 표시할 그룹 이름)
# APT는 group이 None — 공고별로 공공분양/민간분양으로 나눠 표시합니다(classify 참고).
ENDPOINTS = [
    ("APT", "getAPTLttotPblancDetail", None),
    ("UrbtyOfctl", "getUrbtyOfctlLttotPblancDetail", "오피스텔·도시형·민간임대·생활숙박"),
    ("Remndr", "getRemndrLttotPblancDetail", "APT 무순위·잔여세대"),
    ("PblPvtRent", "getPblPvtRentLttotPblancDetail", "공공지원 민간임대"),
    ("OPT", "getOPTLttotPblancDetail", "임의공급"),
]

# 청약홈 공급지역명(SUBSCRPT_AREA_CODE_NM)에서 쓰는 시/도 축약 표기.
TARGET_REGIONS = ("서울", "경기")

# 주택상세구분코드명(HOUSE_DTL_SECD_NM)에 아래 단어가 포함되면 '공공분양'으로 분류합니다.
# (분류가 애매할 수 있어 메시지에는 원본 구분값도 함께 표시합니다.)
PUBLIC_HINTS = ("공공", "국민", "뉴:홈", "뉴홈", "신혼희망타운", "행복주택", "영구임대", "국민임대")

PER_PAGE = 100
MAX_PAGES = 30  # 안전장치: 엔드포인트×지역당 최대 3,000건까지만 순회합니다.


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


def _request(service_key, operation, page, per_page, region_keyword):
    params = {
        "serviceKey": _normalize_key(service_key),
        "page": page,
        "perPage": per_page,
        "cond[SUBSCRPT_AREA_CODE_NM::EQ]": region_keyword,
    }
    url = BASE_URL + operation + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            "Applyhome API({0}) HTTP {1}: {2}".format(operation, exc.code, detail[:500])
        ) from exc

    try:
        data = json.loads(body)
    except ValueError as exc:
        raise RuntimeError(
            "Applyhome API({0}) 응답을 JSON으로 해석하지 못했습니다 "
            "(서비스키 오류/승인 대기 등을 의심해보세요): {1}".format(operation, body[:500])
        ) from exc

    if not isinstance(data, dict) or "data" not in data:
        raise RuntimeError(
            "Applyhome API({0}) 응답 형식이 예상과 다릅니다: {1}".format(operation, body[:500])
        )
    return data


def _fetch_operation_region(service_key, operation, region_keyword):
    rows = []
    page = 1
    while page <= MAX_PAGES:
        data = _request(service_key, operation, page, PER_PAGE, region_keyword)
        page_rows = data.get("data") or []
        rows.extend(page_rows)
        total = data.get("totalCount", len(rows))
        if not page_rows or page * PER_PAGE >= total:
            break
        page += 1
    return rows


def fetch_seoul_gyeonggi(service_key):
    """
    모든 주택유형 엔드포인트에서 서울+경기 분양정보를 가져와 중복 제거 후 반환합니다.
    각 공고(dict)에는 출처 표시용 "_endpoint_id"와 "_group" 키가 추가됩니다.
    일부 엔드포인트만 실패하면 경고를 출력하고 계속하며, 전부 실패하면 예외를 냅니다.
    """
    merged = {}
    errors = []
    for endpoint_id, operation, group in ENDPOINTS:
        try:
            for region in TARGET_REGIONS:
                for row in _fetch_operation_region(service_key, operation, region):
                    area_name = row.get("SUBSCRPT_AREA_CODE_NM") or ""
                    # cond 필터가 기대와 다르게 동작할 경우를 대비한 이중 확인.
                    if not any(keyword in area_name for keyword in TARGET_REGIONS):
                        continue
                    row["_endpoint_id"] = endpoint_id
                    row["_group"] = group
                    merged[listing_key(row)] = row
        except Exception as exc:  # noqa: BLE001
            errors.append("{0}: {1}".format(operation, exc))
            sys.stderr.write("경고: {0} 조회 실패 — 건너뜀: {1}\n".format(operation, exc))
    if errors and not merged and len(errors) == len(ENDPOINTS):
        raise RuntimeError("모든 엔드포인트 조회 실패: {0}".format("; ".join(errors)[:1000]))
    return list(merged.values())


def listing_key(row):
    return "{0}_{1}_{2}".format(
        row.get("_endpoint_id", ""),
        row.get("HOUSE_MANAGE_NO", ""),
        row.get("PBLANC_NO", ""),
    )


def group_label(row):
    """공고가 표시될 그룹 이름. APT는 공공분양/민간분양으로 나눕니다."""
    if row.get("_group"):
        return row["_group"]
    return classify(row)


def classify(row):
    """APT 공고를 '공공분양' 또는 '민간분양'으로 분류합니다 (HOUSE_DTL_SECD_NM 기반 추정)."""
    detail = (row.get("HOUSE_DTL_SECD_NM") or "") + (row.get("HOUSE_SECD_NM") or "")
    if any(hint in detail for hint in PUBLIC_HINTS):
        return "공공분양"
    return "민간분양"


def house_type(row):
    """메시지에 표시할 주택 구분 문자열."""
    return row.get("HOUSE_DTL_SECD_NM") or row.get("HOUSE_SECD_NM") or "-"


def rcept_dates(row):
    """청약접수 시작/종료일. 엔드포인트에 따라 필드명이 달라 둘 다 확인합니다."""
    begin = row.get("RCEPT_BGNDE") or row.get("SUBSCRPT_RCEPT_BGNDE") or ""
    end = row.get("RCEPT_ENDDE") or row.get("SUBSCRPT_RCEPT_ENDDE") or ""
    return begin, end


def detail_url(row):
    # API가 모집공고 상세 URL(PBLANC_URL)을 주면 그대로 사용합니다.
    if row.get("PBLANC_URL"):
        return row["PBLANC_URL"]
    house_manage_no = row.get("HOUSE_MANAGE_NO")
    pblanc_no = row.get("PBLANC_NO")
    if row.get("_endpoint_id") == "APT" and house_manage_no and pblanc_no:
        return (
            "https://www.applyhome.co.kr/ap/apa/aaa/gnrlSpsuslnfoDtlInqireView.do"
            "?houseManageNo={0}&pblancNo={1}".format(house_manage_no, pblanc_no)
        )
    return "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do"
