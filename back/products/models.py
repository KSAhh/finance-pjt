from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from datetime import date

from django.contrib.auth import get_user_model
User = get_user_model()

# 금융상품 - 공통
class AbstractProduct(models.Model):
    kor_co_nm = models.CharField(max_length=255, default="Unknown")                 # 금융회사명
    fin_prdt_cd = models.CharField(max_length=255, default="Unknown")               # 금융 상품 코드
    fin_prdt_nm = models.CharField(max_length=255, default="Unknown")               # 금융 상품명
    join_way = models.CharField(max_length=255, default="Unknown")                  # 가입방법
    mtrt_int = models.TextField(default="Unknown")                                  # 만기 후 이자율 조건 설명
    spcl_cnd = models.TextField(default="Unknown")                                  # 우대 조건
    join_deny = models.IntegerField(default=1)                                      # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField(default="실명의 개인")                              # 가입대상
    etc_note = models.TextField(default="Unknown")                                  # 기타 유의사항
    fin_co_subm_day = models.CharField(max_length=12, default="000000000000")       # 금융회사 제출일 (YYYYMMDDHH24MI 형식)
    max_limit = models.DecimalField(max_digits=15, decimal_places=2, default=-1.00) # 최고한도

    class Meta:
        abstract = True  # 부모 클래스는 테이블 생성 안 함
    
# 금융상품 - 예금 전용필드
class DepositProduct(AbstractProduct):
    options = GenericRelation('ProductOption')  # GenericRelation 추가 (역참조 위함)
    
# 금융상품 - 적금 전용필드
class SavingProduct(AbstractProduct):
    options = GenericRelation('ProductOption')  # GenericRelation 추가 (역참조 위함)


# 금융상품 옵션
class ProductOption(models.Model):
    # GenericForeignKey를 위한 필드
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # 객체를 참조하려는 모델
    object_id = models.PositiveIntegerField() # 특정 모델 객체의 pk 값
    product = GenericForeignKey('content_type', 'object_id')

    # 옵션 데이터 - 공통
    intr_rate_type_nm = models.CharField(max_length=100, default="Unknown")                 # 저축금리 유형명 / ex) 단리, 복리 
    save_trm = models.IntegerField(default=-1)                                              # 저축 기간 [단위: 개월]
    intr_rate = models.DecimalField(max_digits=5, decimal_places=2, default=-1.00)          # 저축 금리 [소수점 2자리]
    intr_rate2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)          # 최고 우대금리 [소수점 2자리]
    
    # 옵션 데이터 - 적금
    rsrv_type_nm = models.CharField(max_length=100, default="Unknown")                      # 적립 유형명 / ex) "정액적립식"


# 유저가 가입한 금융상품
class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 참조
    product_type = models.CharField(max_length=50)  # 상품 유형

    # 예금/적금/기타 상품 중 택1
    deposit_product = models.ForeignKey(DepositProduct, null=True, blank=True, on_delete=models.SET_NULL, related_name="user_products")  # 예금 상품
    saving_product = models.ForeignKey(SavingProduct, null=True, blank=True, on_delete=models.SET_NULL, related_name="user_products")  # 적금 상품

    kor_co_nm = models.CharField(max_length=255)                 # 금융회사명
    fin_prdt_nm = models.CharField(max_length=255)               # 금융 상품명
    balance = models.DecimalField(max_digits=20, decimal_places=0)  # 상품에 남은 잔액
    start_date = models.DateField(blank=True, default=date(1, 1, 1))    # 상품 가입일 (기본값 : 서기 1년 1월 1일)
    end_date = models.DateField(blank=True, default=date(9999, 12, 31))      # 상품 만기일 (기본값 : 서기 9999년 12월 31일)

    def __str__(self):
        product_name = (
            self.deposit_product.fin_prdt_nm if self.product_type == "deposit" else self.saving_product.fin_prdt_nm)
        return f"{self.user.username} - {product_name}"
