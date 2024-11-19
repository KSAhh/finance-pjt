from rest_framework import serializers
from .models import Product, ProductOption
import json

# 상품
class ProductSerializer(serializers.ModelSerializer):
    max_limit = serializers.DecimalField(max_digits=15, decimal_places=2, default=-1, allow_null=True) # null 값을 허용

    class Meta:
        model = Product
        fields = '__all__'

    # max_limit 필드는 존재하나, 값이 null인 경우 -> 기본값 적용
    def validate_max_limit(self, value):
        if value is None:
            return -1
        return value

    def validate_intr_rate(self, value):
        if value is None:
            return -1.00
        return value

    def validate_join_way(self, value):
        # join_way가 문자열로 전달된 경우, 리스트로 변환
        if isinstance(value, str):
            value = value.split(",")  # 콤마로 구분된 문자열을 리스트로 변환
            value = [item.strip() for item in value]  # 공백 제거
        if not isinstance(value, list):
            raise serializers.ValidationError("join_way must be a valid list.")
        return value
    

# 옵션
class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'
        read_only_fields = ['product']