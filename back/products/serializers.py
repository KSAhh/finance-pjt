from rest_framework import serializers
from .models import Product, ProductOption, JoinWay
import json

# 상품
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# 옵션
class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'
        read_only_fields = ['product']


# 가입방법
class JoinWaySerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinWay
        fields = ['way']