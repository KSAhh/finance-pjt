from django.db import connection
import pandas as pd

import os
import django
# Django 설정 모듈 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'algofipo_pjt.settings')

# Django 설정 로드
django.setup()

# 이제 Django ORM을 사용할 수 있습니다.
from products.models import SavingProduct

# 데이터 가져오기
query = DepositProduct.objects.all().values()
df = pd.DataFrame.from_records(query)

# 엑셀로 내보내기
df.to_excel('DepositProduct.xlsx', index=False)
print("데이터가 'output.xlsx' 파일로 저장되었습니다.")