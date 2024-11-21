from rest_framework import serializers
from .models import DepositProduct, SavingProduct, ProductOption
import json

# 상품 - 예금
class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'

# 상품 - 적금
class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'


# 옵션
class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'
        read_only_fields = ['product']
