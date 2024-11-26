import sqlite3
import pandas as pd

def export_sqlite_to_excel_and_csv(db_path, excel_file_path, csv_directory_path):
    """
    SQLite3 파일을 엑셀 및 CSV 파일로 저장
    
    Args:
        db_path (str): SQLite3 데이터베이스 파일 경로
        excel_file_path (str): 저장할 엑셀 파일 경로
        csv_directory_path (str): 저장할 CSV 파일 디렉토리 경로
    """
    # SQLite3 데이터베이스 연결
    conn = sqlite3.connect(db_path)
    
    try:
        # 테이블 목록 가져오기
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [table[0] for table in cursor.fetchall()]

        if not tables:
            raise ValueError("데이터베이스에 테이블이 없습니다.")
        
        with pd.ExcelWriter(excel_file_path) as writer:
            for table in tables:
                if table in ["products_depositproduct", "products_productoption", "products_savingproduct", "products_userproduct"]:
                    print(table, "저장 완료")
                    df = pd.read_sql_query(f"SELECT * FROM {table};", conn)
                    df.to_excel(writer, sheet_name=table, index=False)
                    csv_file_path = f"{csv_directory_path}/{table}.csv"
                    df.to_csv(csv_file_path, index=False)
            print(f"데이터베이스가 성공적으로 {excel_file_path} 및 {csv_directory_path}에 저장되었습니다.")
    except Exception as e:
        print(f"에러 발생: {e}")
    finally:
        # 데이터베이스 연결 닫기
        conn.close()

if __name__ == "__main__":
    db_file = "./db.sqlite3"  # SQLite3 파일 경로
    excel_output = "./raw_data/db_to_csv_file/output.xlsx"  # 생성할 엑셀 파일 경로
    csv_output_dir = "./raw_data/db_to_csv_file"  # CSV 파일 저장 디렉토리 경로
    
    # CSV 디렉토리가 없는 경우 생성
    import os
    if not os.path.exists(csv_output_dir):
        os.makedirs(csv_output_dir)
    
    # 변환 함수 실행
    export_sqlite_to_excel_and_csv(db_file, excel_output, csv_output_dir)

####################
# Django 모델을 직접 저장

# from django.db import connection
# import pandas as pd
# import os, django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'algofipo_pjt.settings')
# django.setup()

# from products.models import DepositProduct, SavingProduct, ProductOption

# for m in [DepositProduct, SavingProduct, ProductOption]:
#     query = m.objects.all().values()
#     df = pd.DataFrame.from_records(query)
#     df.to_excel(f"{m}.xlsx", index=False)
#     print(f"데이터가 '{m}.xlsx' 파일로 저장되었습니다.")
