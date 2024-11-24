import json
import re

# JSON 파일 로드
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# JSON 파일 경로
json_file_path = os.path.join(BASE_DIR, 'raw_data', 'products.json')


with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 666666666666666666666666666666666

# 조건 텍스트 간소화 함수
# def simplify_condition_text(condition):
#     # 특정 패턴을 간소화
#     condition = re.sub(r'\*?해당 상품을|가입 시|을 통해', '', condition)
#     condition = re.sub(r'\s+', ' ', condition).strip()  # 공백 정리
#     return condition

# # spcl_cnd 전처리 함수
# def preprocess_spcl_cnd(products):
#     for product in products:
#         fields = product['fields']
#         spcl_cnd = fields.get('spcl_cnd', '')

#         # 전처리된 우대 조건 저장 리스트
#         conditions = []

#         # 정규식으로 조건과 이자율 숫자 추출
#         for match in re.finditer(r'\*?\s*([^\n:]+):?\s*(연?\s*([\d.]+)%?)?', spcl_cnd):
#             raw_condition = match.group(1).strip()  # 원본 조건
#             details_raw = match.group(3)  # 숫자 부분 추출

#             # 조건 텍스트 간소화
#             condition = simplify_condition_text(raw_condition)

#             # 유효한 숫자인지 확인 후 변환
#             if details_raw and details_raw.replace('.', '', 1).isdigit():
#                 details = float(details_raw)  # 숫자로 변환
#             else:
#                 details = None  # 유효하지 않은 경우 None
            
#             # 조건 추가
#             conditions.append({
#                 "condition": condition,
#                 "details": details
#             })
        
#         # 전처리된 우대 조건 추가
#         fields['spcl_cnd_details'] = conditions

# 777777777777777777777777

# 조건 텍스트 간소화 함수
# def simplify_condition_text(condition):
#     # 특정 패턴을 간소화
#     condition = re.sub(r'\*?해당 상품을|가입 시|을 통해', '', condition)
#     condition = re.sub(r'\s+', ' ', condition).strip()  # 공백 정리
#     return condition

# # spcl_cnd 전처리 함수
# def preprocess_spcl_cnd(products):
#     for product in products:
#         fields = product['fields']
#         spcl_cnd = fields.get('spcl_cnd', '')

#         # 전처리된 우대 조건 저장 리스트
#         conditions = []

#         # 정규식으로 조건과 이자율 숫자 추출
#         for match in re.finditer(r'\*?\s*([^\n:]+):?\s*(연?\s*([\d.]+)%?)?', spcl_cnd):
#             raw_condition = match.group(1).strip()  # 원본 조건
#             details_raw = match.group(3)  # 숫자 부분 추출

#             # 조건 텍스트 간소화
#             condition = simplify_condition_text(raw_condition)

#             # 유효한 숫자인지 확인 후 변환
#             if details_raw and details_raw.replace('.', '', 1).isdigit():
#                 details = float(details_raw)  # 숫자로 변환
#             else:
#                 details = None  # 유효하지 않은 경우 None
            
#             # 유효한 조건과 숫자만 추가
#             if condition and condition != "p" and (details is not None or condition):  # 빈값이나 잘못된 조건 필터링
#                 conditions.append({
#                     "condition": condition,
#                     "details": details
#                 })
        
#         # 전처리된 우대 조건 추가
#         fields['spcl_cnd_details'] = conditions

# 888888888888888888888888888
# 조건 텍스트 간소화 함수
def simplify_condition_text(condition):
    # 특정 패턴을 간소화
    condition = re.sub(r'^\-*\s*', '', condition)  # 접두사 '-' 제거
    condition = re.sub(r'상품 가입 전\s*', '', condition)  # '상품 가입 전' 제거
    condition = re.sub(r'\s+', ' ', condition).strip()  # 공백 정리
    return condition

# spcl_cnd 전처리 함수
def preprocess_spcl_cnd(products):
    for product in products:
        fields = product['fields']
        spcl_cnd = fields.get('spcl_cnd', '')

        # 전처리된 우대 조건 저장 리스트
        conditions = []

        # 정규식으로 조건과 이자율 숫자 추출
        for match in re.finditer(r'\*?\s*([^\n:]+):?\s*(연?\s*([\d.]+)%?)?', spcl_cnd):
            raw_condition = match.group(1).strip()  # 원본 조건
            details_raw = match.group(3)  # 숫자 부분 추출

            # 조건 텍스트 간소화
            condition = simplify_condition_text(raw_condition)

            # 유효한 숫자인지 확인 후 변환
            if details_raw and details_raw.replace('.', '', 1).isdigit():
                details = float(details_raw)  # 숫자로 변환
            else:
                details = None  # 유효하지 않은 경우 None
            
            # 유효한 조건만 추가
            if condition and condition != "p" and (details is not None or condition):
                conditions.append({
                    "condition": condition,
                    "details": details
                })
        
        # 불필요한 항목 제거 (조건이 없거나 유효하지 않은 항목 제거)
        fields['spcl_cnd_details'] = [
            condition for condition in conditions
            if condition['condition'] and condition['details'] is not None
        ]

# JSON 데이터에 전처리 적용
preprocess_spcl_cnd(data)


# 결과 저장
with open('processed_products1.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("spcl_cnd 필드가 전처리된 JSON 파일이 생성되었습니다.")


# 9999999999999999999999999999999999999
# def simplify_condition_text(condition):
#     """
#     조건 텍스트 간소화
#     """
#     # 특정 패턴을 제거하여 간소화
#     condition = re.sub(r'^\-*\s*', '', condition)  # 접두사 '-' 제거
#     condition = re.sub(r'상품 가입 전\s*', '', condition)  # '상품 가입 전' 제거
#     condition = re.sub(r'\s+', ' ', condition).strip()  # 다중 공백 제거
#     return condition

# def preprocess_spcl_cnd(products):
#     """
#     spcl_cnd 필드 전처리 및 spcl_cnd_details 업데이트
#     """
#     for product in products:
#         fields = product['fields']
#         spcl_cnd = fields.get('spcl_cnd', '')

#         # 전처리된 우대 조건 저장 리스트
#         conditions = []

#         # 정규식으로 조건과 이자율 숫자 추출
#         for match in re.finditer(r'\*?\s*([^\n:]+):?\s*(연?\s*([\d.]+)%?)?', spcl_cnd):
#             raw_condition = match.group(1).strip()  # 원본 조건
#             details_raw = match.group(3)  # 숫자 부분 추출

#             # 조건 텍스트 간소화
#             condition = simplify_condition_text(raw_condition)

#             # 숫자 변환 (유효한 숫자만 처리)
#             if details_raw and details_raw.replace('.', '', 1).isdigit():
#                 details = float(details_raw)  # 숫자로 변환
#             else:
#                 details = None  # 유효하지 않은 경우 None

#             # 유효한 조건만 추가
#             if condition and (details is not None or condition):
#                 conditions.append({
#                     "condition": condition,
#                     "details": details
#                 })

#         # 조건 없는 항목 또는 details가 None인 항목 제거
#         fields['spcl_cnd_details'] = [
#             condition for condition in conditions
#             if condition['condition'] and condition['details'] is not None
#         ]

# # JSON 데이터에 전처리 적용
# preprocess_spcl_cnd(data)

# # 결과 저장
# with open('processed_products.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)

# print("spcl_cnd 필드가 전처리된 JSON 파일이 생성되었습니다.")