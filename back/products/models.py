from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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
    join_member = models.TextField(default="실명의 개인")                            # 가입대상
    etc_note = models.TextField(default="Unknown")                                  # 기타 유의사항
    fin_co_subm_day = models.CharField(max_length=12, default="000000000000")       # 금융회사 제출일 (YYYYMMDDHH24MI 형식)
    max_limit = models.DecimalField(max_digits=15, decimal_places=2, default=-1.00) # 최고한도

    class Meta:
        abstract = True  # 부모 클래스는 테이블 생성 안 함
    
# 금융상품 - 예금
class DepositProduct(AbstractProduct):
    pass # 전용필드
    
# 금융상품 - 적금
class SavingProduct(AbstractProduct):
    pass # 전용필드


# 금융상품 옵션
class ProductOption(models.Model):
    # GenericForeignKey를 위한 필드
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')

    # 옵션 데이터 - 공통
    intr_rate_type_nm = models.CharField(max_length=100, default="Unknown")                 # 저축금리 유형명 / ex) 단리, 복리 
    save_trm = models.IntegerField(default=-1)                                              # 저축 기간 [단위: 개월]
    intr_rate = models.DecimalField(max_digits=5, decimal_places=2, default=-1.00)          # 저축 금리 [소수점 2자리]
    intr_rate2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)          # 최고 우대금리 [소수점 2자리]
    
    # 옵션 데이터 - 적금
    rsrv_type_nm = models.CharField(max_length=100, default="Unknown")                      # 적립 유형명 / ex) "정액적립식"


# 유저가 가입한 금융상품
# class UserProduct(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자를 참조
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 상품을 참조
#     product_type = models.CharField(max_length=50)  # 상품 유형 (예: 예금, 적금)
#     balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)  # 상품에 남은 잔액
#     start_date = models.DateField()  # 상품 가입 날짜
#     end_date = models.DateField(null=True, blank=True)  # 상품 만기 날짜
#     status = models.CharField(max_length=20, default="active")  # 상태 (예: active, completed)
#     created_at = models.DateTimeField(auto_now_add=True)  # 레코드 생성 시간

#     def __str__(self):
#         return f"{self.user.username} - {self.product.fin_prdt_nm}"