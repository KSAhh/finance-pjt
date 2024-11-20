from django.db import models

# 금융상품
class Product(models.Model):
    # 예/적금 공통
    kor_co_nm = models.CharField(max_length=255, default="Unknown")                 # 금융회사명
    fin_prdt_cd = models.CharField(max_length=255, default="Unknown")               # 금융 상품 코드
    fin_prdt_nm = models.CharField(max_length=255, default="Unknown")               # 금융 상품명
    join_way = models.CharField(max_length=255, default="Unknown")                  # 가입 방법
    mtrt_int = models.TextField(default="Unknown")                                  # 만기 후 이자율 조건 설명
    spcl_cnd = models.TextField(default="Unknown")                                  # 우대 조건
    join_deny = models.IntegerField(default=1)                                      # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField(default="실명의 개인")                            # 가입대상
    etc_note = models.TextField(default="Unknown")                                  # 기타 유의사항
    fin_co_subm_day = models.CharField(max_length=12, default="000000000000")       # 금융회사 제출일 (YYYYMMDDHH24MI 형식)

    # 적금
    max_limit = models.DecimalField(max_digits=15, decimal_places=2, default=-1.00)    # 최고한도


# 금융상품 옵션
class ProductOption(models.Model):
    # 예/적금 공통
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="options")  # 외래 키(Product 클래스 참조)
    intr_rate_type_nm = models.CharField(max_length=100, default="Unknown")                 # 저축금리 유형명 / ex) 단리, 복리 
    save_trm = models.IntegerField(default=-1)                                              # 저축 기간 [단위: 개월]
    intr_rate = models.DecimalField(max_digits=5, decimal_places=2, default=-1.00)          # 저축 금리 [소수점 2자리]
    intr_rate2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)          # 최고 우대금리 [소수점 2자리]
    
    # 적금
    rsrv_type_nm = models.CharField(max_length=100, default="Unknown")                      # 적립 유형명 / ex) "정액적립식"


# 은행
class Bank(models.Model):
    bank_name = models.CharField(max_length=255, default="Unknown")                     # 은행명
    address = models.CharField(max_length=500, default="Unknown")                       # 지점 주소
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0000)      # 위도 (기본값: 바다 위 좌표) (총 9자리 중 소수점 이하에 6자리를 사용)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=-160.0000)  # 경도 (기본값: 바다 위 좌표)
    created_at = models.DateTimeField(auto_now_add=True)                                # 생성 시간


# 은행지점별 예적금 정보(M:N)
class BankProduct(models.Model):
    bank_location = models.ForeignKey(Bank, on_delete=models.CASCADE)   # 은행 위치 참조
    product = models.ForeignKey(Product, on_delete=models.CASCADE)      # 예적금 상품 참조