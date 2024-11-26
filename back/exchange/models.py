from django.db import models

class ExchangeRate(models.Model):
    cur_unit = models.CharField(max_length=10) # 통화코드
    cur_nm = models.CharField(max_length=50) # 국가/통화명(공백으로 구분)
    ttb = models.DecimalField(max_digits=12, decimal_places=4) # 송금 받을때 가격
    tts = models.DecimalField(max_digits=12, decimal_places=4) # 송금 보낼때 가격
    cur_to_krw = models.DecimalField(max_digits=12, decimal_places=4) # 매매기준율
    
    krw_to_cur = models.DecimalField(max_digits=12, decimal_places=4) # (한화 1000원당 해당국가 통화가격)
    updated_at = models.DateField() # 요청날짜