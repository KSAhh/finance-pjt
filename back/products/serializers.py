from rest_framework import serializers
from .models import DepositProduct, SavingProduct, ProductOption,  UserProduct
import json

# 상품 - 예금 & 적금
class DepositSavingSerializer(serializers.ModelSerializer):
    product_type = serializers.SerializerMethodField()  # 동적 필드 정의

    class Meta:
        model = DepositProduct # 예금, 적금 필드 동일하므로 Deposit 사용
        fields = '__all__' # product_type 필드 포함

    # 직렬화 과정에서 호출
    def get_product_type(self, obj): 
        # 상품 유형 반환
        if isinstance(obj, DepositProduct):
            return "deposit"
        elif isinstance(obj, SavingProduct):
            return "saving"
        return "unknown"

# 옵션
class ProductOptionSerializer(serializers.ModelSerializer):
    class DepositSavingTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositProduct
            fields = ['kor_co_nm', 'fin_prdt_nm']

    product = DepositSavingTitleSerializer(read_only=True) # # SavingProduct도 동일 구조
    class Meta:
        model = ProductOption
        fields = [
            "product",
            "intr_rate_type_nm",
            "save_trm",
            "intr_rate",
            "intr_rate2",
            "rsrv_type_nm",
        ]
        read_only_fields = fields


# 유저가입 상품
class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = "__all__"
        read_only_fields = ['id', 'user', 'deposit_product', 'saving_product', 'etc_product']