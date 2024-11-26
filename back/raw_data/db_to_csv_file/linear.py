import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 프로젝트 루트 경로

# user_data = pd.read_csv('./back/raw_data/db_to/csv_file/products_userproduct.csv')
saving_data = pd.read_csv('./back/raw_data/db_to_csv_file/products_savingproduct.csv')
deposit_data = pd.read_csv('./back/raw_data/db_to_csv_file/products_depositproduct.csv')
print(saving_data.head())
# 데이터 병합 및 결합
financial_data = pd.concat([saving_data, deposit_data], ignore_index=True)

# 유저-금융 데이터 매핑
# user_financial_data = user_data.merge(financial_data, how='left', on='fin_prdt_cd')
user_financial_data = financial_data

# 모델 학습 데이터 구성
X = user_financial_data[['age', 'income', 'job_type']]  # 예시 변수
y = user_financial_data['preference_score']  # 임시 타겟 값
