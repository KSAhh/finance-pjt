from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from django.conf import settings
import requests
from datetime import date
# from .serializers import ExchangeRatesSerializer
# from .models import ExchangeRates
from django.views.decorators.cache import cache_page
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import ExchangeRate
from .serializers import ExchangeRatesSerializer
API_KEY = settings.KOREAEXIM_API_KEY
# searchdate = date.searchdate()
searchdate = "2024-11-26"

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def save_exchange(request):
    URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': API_KEY,
        'data': 'AP01', # 환율
        'searchdate' : searchdate # 비영업일의 데이터, 혹은 영업당일 11시 이전에 해당일의 데이터를 요청할 경우 null 값이 반환
    }
    response = requests.get(URL, params=params, verify=False).json()
    # HTTP 200이지만 빈 데이터 또는 비정상 데이터 처리
    if not response:  # data가 빈 배열, 빈 객체 또는 None일 경우
        print("API 요청 성공, 하지만 반환된 데이터가 없습니다.")
        return Response({'detail': f"{searchdate}기준 비영업일의 데이터, 혹은 영업당일 11시 이전에 해당일의 데이터는 제공하지 않습니다."}, status=status.HTTP_204_NO_CONTENT)

    # 환율 데이터 저장
    for data in response:
        # 쉼표 제거 및 부동 소수점 변환
        deal_bas_r = float(data.get("deal_bas_r", "0").replace(',', '')) # 쉼표(,)가 포함된 문자열을 부동소수점 숫자로 변환
        ttb = float(data.get('ttb', "0").replace(",", ""))
        tts = float(data.get('tts', "0").replace(",", ""))


        # 100 단위 기준 통화 처리(일본, 인도네시아)
        if "(100)" in data.get("cur_unit"):
            data["cur_unit"] = data.get("cur_unit").replace("(100)", "").strip()
            deal_bas_r = round(deal_bas_r / 100, 4)
            ttb = round(ttb / 100, 4)
            tts = round(tts / 100, 4)

        # 한화 1000원당 해당 통화 가격 계산
        if deal_bas_r > 0:
            krw_to_cur = round(1000 / deal_bas_r, 2)
            cur_to_krw = round(deal_bas_r, 2)  # 외국 통화 1단위 -> 한화
            data['krw_to_cur'] = krw_to_cur
            data['cur_to_krw'] = cur_to_krw
        else: # 환율 정보가 없으면 DB에 저장하지 않음
            continue
        
        print(data)
        # 통화 코드 기준으로 DB에 존재 여부 확인
        exchange_rate = ExchangeRate.objects.filter(cur_unit=data.get('cur_unit')).first()
        # 존재한다면
        if exchange_rate:
            # 갱신 날짜 체크 -> 최신 데이터로 갱신
            if exchange_rate.updated_at != searchdate:
                data['cur_to_krw'], data['ttb'], data['tts'] = deal_bas_r, ttb, tts
                rate_serializer = ExchangeRatesSerializer(instance=exchange_rate, data=data)
                if rate_serializer.is_valid(raise_exception=True):
                    rate_serializer.save(updated_at=searchdate)
        # 존재하지 않으면 추가
        else:
            ExchangeRate.objects.create(
                cur_unit=data.get('cur_unit'),
                cur_nm=data.get("cur_nm"),
                ttb=ttb,
                tts=tts,
                cur_to_krw=deal_bas_r,
                krw_to_cur=data.get("krw_to_cur"),
                updated_at=searchdate,
            )
    return Response({"detail": f"Update date: {searchdate} Successfully saved."}, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def save_exchange(request):
#     URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
#     params = {
#         'authkey': API_KEY,
#         'data': 'AP01', # 환율
#         'searchdate' : searchdate # 비영업일의 데이터, 혹은 영업당일 11시 이전에 해당일의 데이터를 요청할 경우 null 값이 반환
#     }
#     response = requests.get(URL, params=params).json()
#     # HTTP 200이지만 빈 데이터 또는 비정상 데이터 처리
#     if not response:  # data가 빈 배열, 빈 객체 또는 None일 경우
#         print("API 요청 성공, 하지만 반환된 데이터가 없습니다.")
#         return Response({'detail': f"{searchdate}기준 비영업일의 데이터, 혹은 영업당일 11시 이전에 해당일의 데이터는 제공하지 않습니다."}, status=status.HTTP_204_NO_CONTENT)

#     # 환율 데이터 저장
#     for data in response:
#         # 쉼표 제거 및 부동 소수점 변환
#         deal_bas_r = float(data.get("deal_bas_r", "0").replace(',', '')) # 쉼표(,)가 포함된 문자열을 부동소수점 숫자로 변환
#         ttb = float(data.get('ttb', "0").replace(",", ""))
#         tts = float(data.get('tts', "0").replace(",", ""))


#         # 100 단위 기준 통화 처리(일본, 인도네시아)
#         if "(100)" in data.get("cur_unit"):
#             data["cur_unit"] = data.get("cur_unit").replace("(100)", "").strip()
#             deal_bas_r = round(deal_bas_r / 100, 4)
#             ttb = round(ttb / 100, 4)
#             tts = round(tts / 100, 4)

#         # 한화 1000원당 해당 통화 가격 계산
#         if deal_bas_r > 0:
#             krw_to_cur = round(1000 / deal_bas_r, 2)
#             cur_to_krw = round(deal_bas_r, 2)  # 외국 통화 1단위 -> 한화
#             data['krw_to_cur'] = krw_to_cur
#             data['cur_to_krw'] = cur_to_krw

#             # cur_to_krw = round(deal_bas_r, 2)  # 외국 통화 1단위 -> 한화
#             # data['krw_to_cur'] = krw_to_cur
#             # data['cur_to_krw'] = cur_to_krw
#         else: # 환율 정보가 없으면 DB에 저장하지 않음
#             continue

#         # 통화 코드 기준으로 DB에 존재 여부 확인
#         exchange_rate = ExchangeRate.objects.filter(cur_unit=data.get('cur_unit')).first()
        
#         # 존재한다면
#         if exchange_rate:
#             # 갱신 날짜 체크 -> 최신 데이터로 갱신
#             if exchange_rate.updated_at != searchdate:
#                 data['cur_to_krw'], data['ttb'], data['tts'] = deal_bas_r, ttb, tts
#                 rate_serializer = ExchangeRatesSerializer(instance=exchange_rate, data=data)
#                 if rate_serializer.is_valid(raise_exception=True):
#                     rate_serializer.save(updated_at=searchdate)

#         # 존재하지 않으면 추가
#         else:
#             ExchangeRate.objects.create(
#                 cur_unit=data.get('cur_unit'),
#                 cur_nm=data.get("cur_nm"),
#                 ttb=ttb,
#                 tts=tts,
#                 cur_to_krw=deal_bas_r,
#                 krw_to_cur=data.get("krw_to_cur"),
#                 updated_at=searchdate,
#             )

#     return Response({"detail": f"Update date: {searchdate} Successfully saved."}, status=status.HTTP_201_CREATED)


# DB에 저장된 환율 정보 응답
@api_view(['GET'])
@cache_page(60 * 60 * 10) # 캐싱 적용 / 60초 * 60분 * 10시간
def rate_list(request):
    exchanges = get_list_or_404(ExchangeRate)
    serializer = ExchangeRatesSerializer(exchanges, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
