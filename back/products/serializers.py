from rest_framework import serializers
from .models import DepositProducts, DepositOptions

# 상품 정보
class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

        
# 옵션 정보
class DepositOptionsSerializer(serializers.ModelSerializer):
    # 기본 값 지정
    intr_rate_type_nm=serializers.CharField(default='미제공') # 저축 금리 유형명
    intr_rate=serializers.FloatField(default=0.0)             # 저축 금리 [소수점 2자리]
    intr_rate2=serializers.FloatField(default=0.0)            # 최고 우대금리 [소수점 2자리]
    save_trm=serializers.IntegerField(default=0)              # 저축 기간 [단위: 개월]

    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ['product']