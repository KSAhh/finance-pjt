from rest_framework import serializers
from .models import ExchangeRate

class ExchangeRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'
        read_only_fields = ['updated_at']