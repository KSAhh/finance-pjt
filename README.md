# 💰 AlgoFiPo Project

> **재테크를 효율적으로 관리할 수 있는 서비스**  
> 결혼 후 **자가 마련**과 **신혼여행**을 준비하는 사용자들을 대상으로  
> 예적금 금리비교, 환율 계산기, 근처 은행 검색, 그리고 사용자 맞춤형 금융 상품 추천 서비스를 제공합니다.

---

## 🚀 프로젝트 목표
- 금융상품 데이터 기반 예금 및 적금 금리 비교 서비스 구성  
- 유저의 마이데이터 기반 금융 추천 알고리즘 구성   
- 환율 정보 API를 활용한 환율 계산 서비스 및 차트 구성  
- 지도 API를 활용한 은행 검색 서비스 구성  
- 고객센터 서비스로 사용성 개선  

---

## 🛠 주요 기능


### 1. 메인페이지 및 회원기능
- 사용자 정보 및 마이데이터 동의여부를 관리할 수 있습니다.

![image](https://github.com/user-attachments/assets/607b46cb-937f-4cea-8383-f5d90a5cf9b1)

### 2.상품가입 및 가입상품 조회
- 예적금 금리 비교
- 사용자가 선택한 금융사, 상품옵션에 맞는 상품을 조회합니다.

https://github.com/user-attachments/assets/501fc567-ab5c-4688-8932-1a557ad0df97

### 3-1.맞춤형 금융 상품 추천 [마이데이터 미동의자]
- 금융상품 및 사용자 데이터를 기반으로 개인의 재정 상태에 맞는 금융 상품을 추천합니다.
- 기본금리 기준 상위 10가지 상품

![image](https://github.com/user-attachments/assets/e93c23fb-e539-476d-b613-b367b65376e0)

![image](https://github.com/user-attachments/assets/38065152-b24f-40de-9328-d79f2d9e4349)

### 3-2. 맞춤형 금융 상품 추천 [마이데이터 동의자]
- 알고리즘 구현 완료

### 4. 환율계산기
- 출국을 위해 필요한 환전 금액을 계산합니다.

![image](https://github.com/user-attachments/assets/002f59f6-383f-4ec4-846c-bd0a79612342)

### 5. 근처 은행 지도
- 검색 키워드 근처의 은행 지점을 검색합니다.

https://github.com/user-attachments/assets/9b1a28f8-d9b1-49f6-8494-11e338fba79b

### 6. 고객센터
   - 사용자 간의 질문, 리뷰 등을 공유할 수 있으며, 관리자의 답변을 제공받을 수 있습니다.

### 6-1. 고객센터 글 작성

https://github.com/user-attachments/assets/69ba0383-3f3a-47eb-afb1-c51a1c3c3433

### 6-1. 고객객센터 글 수정

https://github.com/user-attachments/assets/9d203b0e-8913-4f34-9ff8-bd55129ecc9d

### 6-2. 고객센터 댓글작성

https://github.com/user-attachments/assets/57ca6a89-642a-4c86-91a4-0b8f93efd3fe

---

## 📅 개발기간
**2024년 11월 18일 ~ 2024년 11월 27일**

---

## 👥 Collaborators
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/KSAhh">
        <img src="https://avatars.githubusercontent.com/KSAhh" width="150px;" alt="KSAhh"/>
        <br/><sub><b>KSAhh / 김수아</b><br></sub>
      </a>
      <p>Backend(Django), Frontend(Vue), Git 규칙 지정, API 설계, ERD 설계</p>
    </td>
    <td align="center">
      <a href="https://github.com/sadtearcat">
        <img src="https://avatars.githubusercontent.com/sadtearcat" width="150px;" alt="sadtearcat"/>
        <br/><sub><b>sadtearcat / 백지원</b><br></sub>
      </a>
      <p>Frontend(Vue), UI 디자인, 상품 추천 알고리즘 개발</p>
    </td>
  </tr>
</table>

---

## 🔧 기술 스택
### Backend & Database
[![My Skills](https://skillicons.dev/icons?i=python,nodejs,django,sqlite,&theme=light&perline=5)](https://skillicons.dev)

### Frontend
[![My Skills](https://skillicons.dev/icons?i=html,css,js,vue,figma,tailwind&theme=light&perline=6)](https://skillicons.dev)


- **Visualization**: Chart.js
- **HTTP Client**: Axios

### 협업 Tools
[![My Skills](https://skillicons.dev/icons?i=git,notion,github,githubactions&theme=light&perline=5)](https://skillicons.dev)

### External APIs
- **한국수출입은행 API**
- **카카오 API**
- **금융감독원 API**

--- 

## ⚙ ERD

![image](https://github.com/user-attachments/assets/c8024d12-9090-4aa5-9312-27ab66da0408)


---

## 📂 디렉터리 구조
```plaintext
finance-pjt/
├── back/
│   ├── accounts/          - 회원관리
│   ├── algofipo_pjt/      - 프로젝트 설정
│   ├── articles/          - 고객센터
│   ├── exchange/          - 환율 계산기
│   ├── products/          - 금융상품
│   ├── raw_data/          - 금융상품 데이터
│   ├── requirements.txt   - 의존성 파일
│   └── 추천알고리즘        - 추천 알고리즘 전처리 (+ 생성형 AI)
├── front/
│   ├── algo-fipo/
│   │   ├── src/
│   │   │   ├── assets/    - 정적 파일
│   │   │   ├── components/- Vue 컴포넌트
│   │   │   ├── data/      - 데이터 관리
│   │   │   ├── router/    - Vue 라우터
│   │   │   ├── stores/    - 상태 관리
│   │   │   └── views/     - 페이지 컴포넌트
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── package.json
└── README.md
```

## 🧩 컴포넌트 구조

- NavBar: 네비게이션 바
- BankMap: 지도 기반 은행 검색
- CustomerService: 고객센터
- ExchangeRate: 환율 계산기
- Savings: 예적금 금리 비교
- LoanPage: 대출 관련 서비스

---


## 📈 투자 추천 알고리즘 원리
1. 예적금 데이터 수집 (금융상품정보공시API)
2. 각 상품별 spcl_intr 필드 전처리
3. 마이데이터 기반 사용자 그룹화 (더미데이터 생성)
  - 나이
  - 직업
  - 월 평균 소득
  - 월 평균 소비
  - 총 자산
  - 마이데이터 동의 여부
4. 금융 상품 추천
  - 마이데이터 활용 동의 → 개인정보 그룹화하여 추천
  - 마이데이터 활용 비동의 → 기본금리 기반 상위 항목 추천

---
### 추천 알고리즘 설계구조
핵심목표 : 신뢰성 있는 과정을 거친 더미데이터 생성으로 초기 추천 또한 논리적인 흐름을 따를 수 있도록 한다.
가정 : 
본 사이트 가입유저 상호간의 유저는 마이데이터 공유 여부를 선택할 수 있다,
더미데이터 유저들은 모두 합리적인 선택으로 상품을 선택한다.
본 사이트는 직장인이 가입할 확률이 높다고 가정한다.

더미데이터 생성 가정 : 

1. 연령별 가입 유저 비율
본 사이트는 사회초년생을 타게팅한 사이트이므로 가입 유저 비율 중 20대가 가장 많은 것이라 가정하며 연령별 비율은 다음과 같다.
랜덤함수로 설정해 전체 총합에 대한 키 값의 비율로 연령이  확률적으로 생성된다.
[20대 : 10, 30대 : 5, 40대 : 2, 50대 : 2, 60대 : 1]
각 값은 임의로 설정한 값이다.

2. 성별 비율 :
5:5로 설정해 남녀간의 균형이 있도록 했다. 이는 신규 가입자가 성별에 따라 추천 시스템의 기능을 부족하게 이용하지 않게 하기 위함이다.

```python
# 나이, 성별 함수
def generate_user_age_gender():
    age_group_weights = [10, 5, 2, 2, 1]
    age_group = random.choices([20, 30, 40, 50, 60], weights=age_group_weights, k=1)[0]
    user_age = random.randint(age_group, age_group + 9)
    user_gender = random.choice(["male", "female"])
    return user_age, user_gender
```
3. 마이데이터 허용 여부
마이데이터 허용 여부는 [1, 2, 3] 으로 나뉜다.
각 값에 대한 설명:
   ```1 = 마이데이터를 제공하고, 본 사이트 가입유저 중 1을 선택한 유저와의 가입상품 및 기타 금융정보를 공유한다.
   2 = 마이데이터를 제공하고, 오직 본인의 마이데이터를 이용하며 금융정보를 공유하지 않는다.
   3 = 마이데이터를 제공하지 않으며 기본 금융 상품 추천서비스 로직을 따른다.```

```python
# 마이데이터 허용여부 생성 함수
def generate_data_consent():
    return random.choices([1, 2, 3], weights=[6, 3, 1], k=1)[0]
```

4. 소득 및 지출 데이터 설정(최신데이터가 경향성을 증거할 수 없으리란 판단에 최근 1년간 데이터의 평균을 월평균 소득액으로 판단)
가구주_연령별_가구당_월평균_가계수지__전국_1인이상__2023_4.2~2024_4.2을 참고해 연령대별 12개월 평균 소득을 설정,
중간값과 평균값을 이용해 식을 설정해 표준편차를 설정, 
동일한 기간의
통계청 자료인 가구특성별_비목별_소비지출과 가구특성별_비목별_비소비지출값을 합산하여 지출 데이터로 활용

5. 2023 가계금융복지조사 데이터를 참고해 연령대별 자산 데이터 설정. 해당 데이터에서 부채`여부`에 따라 순자산의 범위가 크게 줄어드는 것을 고려해서 설정.

6. 소득의 극단값 고려
소득 극단값이 존재할 것이고 이것은 매우 큰 편차로 있을 것이라고 가정해 로그 정규분포로 평균 소득을 생성하는 로직을 추가.
또한 첫 달의 소득이 정해지면 나머지 11개월에 대한 표준편차가 줄어들도록 하여 현실성을 고려하도록 함.

7. 잉여자본이 있는 사람들이 사이트를 이용할 것이라는 가정.
지출은 소득의 90%를 초과할 수 없도록 설정하여 `재태크`를 목적으로 하는 사용자가 합리적인 선택을 위해 가입을 한다고 전제.

8. 금융감독원 api 관련 가정
`join_deny`가 1이 아니면 가입 조건이 있다. 이에 따라 `가입 제한`에 대해 설명하는 `join_member` 와 연관이 있을 것이라 가정


### 더미데이터 생성 과정

더미데이터 초기 생성 양식
```python
[
    {
        "age": 34,
        "gender": "여성",
        "monthly_income": 3168874,
        "monthly_expense": 2752901,
        "total_assets": 430956,
        "가입상품": {
            "가입예금": "",
            "가입정기예금": "",
            "가입적금": ""
        },
        "마이데이터허용여부": 1
    },...{더 많은 유저들}]
```
**더미유저가 자신에게 최적의 상품을 골라 빈 문자열로 설정된 가입 상품을 추가한다**
---이하 가입 과정---
1. join_deny와 join_member를 통해 user가 가입 가능한 조건인지 파악.
1-1. join_deny가 1이 아니면 join_member를 통해 그 조건이 각 유저에 해당하는지 파악한다.
2. 데이터 구조 파악으로 정규표현식으로 및 반복문장 혹은 의미없는 값 1차 전처리.
2-1. 전처리 과정에서 `토큰화`를 사용해 동일한 단어의 반복 횟수를 파악하여 전처리 진행
2-2. 처리된 데이터에서 3가지 큰 영역으로 조건을 반환
   1 - 연령 제한
   2 - 직장인 여부
   3 - 제한없음
`해당 과정은 적절한 자동화 규칙을 찾을 수 없어 수동으로 진행.`
3. 직장인이 가입했을거라는 가정으로 2는 무조건 가입 가능한 값으로 반환.
4. 더미 유저의 age가 연령 제한을 통과하는지 확인하고, 통과하지 못한다면 해당 상품에 denyed_user 필드를 생성하고, 필드 값에 더미유저의 id 값을 추가.
5.`ect_note`값으로 더미유저가 가입 가능한 상품인지 판단.
5-1. 랜덤 생성된 월평균 소득을 균등화평균소득으로 변경(가구원 수를 고려한 변경)하고 지출을 뺄셈.
5-2. 해당 규칙을 대해 groq API를 활용해 프롬프트를 작성해 `금액`관련 값만 남기도록 함.
5-3. 금액 관련 단위 또한 맞추도록 요청.
   savings에 대해 = "최소 월 납입금액"
   deposits에 대해 = "최소 가입금액"
   `기본적인 전처리가 된 데이터를 보내 응답의 정확성을 높이도록한다.`
   json 파일을 청크단위로 groq API에 전송해 응답을 저장.
   `프롬프트`:
           당신은 금융 데이터를 분석하는 전문가입니다.
        데이터 타입: '{data_type}'
        이 메시지는 총 {total_chunks}개로 나뉜 청크 중 {current_index + 1}번째입니다.

        지침:
        1. 데이터 구조를 반드시 주어진 형식(deposits와 savings)으로 유지하세요.
        2. '{data_type}' 데이터 처리 방법:
        - 최소 납입금액은 '최소 납입금액' 키에 기록하세요.
        - 추가로 중요한 정보는 '추가 정보' 키에 요약해서 기록하세요.
        3. "금액"이라는 단어를 해석할 때 주의하세요:
        - "최소"(minimum)나 "최대"(maximum)와 같은 수식어가 없을 경우, "이상"(at least) 또는 "이하"(at most)와 같은 문맥을 사용하여 판단하세요.
        - 모든 금액은 반드시 대한민국 원(₩) 단위로 기록하세요.
        4. 결과는 아래 JSON 형식으로 반환해야 합니다:
        {{
            "{data_type}": [
                {{
                    "id": "int",
                    "최소 납입금액": "int",
                    "최대 납입금액": "int (optional)",
                    "추가 정보": "string (optional)"
                }}
            ]
        }}
        JSON 형식만 반환하세요. 추가 설명이나 주석은 포함하지 마세요.
        """
6. `5-1에서 반환된 값`을 해당 유저가 `운용가능한 자산`으로 설정.
6-1. 운용가능한 자산 값은 savings에서 활용,
   ```python
# 사용자 denied_product 업데이트
def update_user_denied_products(user_test, ect_note_file, user_denied_products):
    for user_id, user_data in enumerate(user_test, start=1):
        user_monthly_disposable_income = user_data["monthly_income"] - user_data["monthly_expense"]
        user_total_assets = int(user_data["total_assets"] * 1000 * random.uniform(0.7, 0.9))  # 총자산에 랜덤 비율 적용

        # 접근 불가 상품 업데이트
        for category in ["savings", "deposits"]:
            denied_ids = {prod_id for prod_id in user_denied_products[user_id - 1]["deny_product_id"].get(category, [])}

            for product in ect_note_file[category]:
                product_id = product["id"]

                # 이미 접근 불가 상품에 포함된 경우 스킵
                if product_id in denied_ids:
                    continue

                # "최소 월 납입금액" 조건 확인 (savings)
                if category == "savings" and "최소 월 납입금액" in product and product["최소 월 납입금액"] is not None:
                    if user_monthly_disposable_income < product["최소 월 납입금액"]:
                        denied_ids.add(product_id)

                # "최소 납입금액" 조건 확인 (deposits)
                if category == "deposits" and "최소 납입금액" in product and product["최소 납입금액"] is not None:
                    if user_total_assets < product["최소 납입금액"]:
                        denied_ids.add(product_id)

            # 업데이트된 denied_ids 저장
            user_denied_products[user_id - 1]["deny_product_id"][category] = list(denied_ids)

    return user_denied_products```
    *해당 함수에 따라 상품 데이터에 접근 불가능한 더미유저 id 추가로 업데이트*

    

   





본 사이트 신규 가입 유저에 대한 추천 로직 : 


마이데이터 활용 동의시: 각 유저에 대해 마이데이터 허용 
여부를 저장하고, 허용 유저 간에 가입한 상품

마이데이터 활용 비동의시:

더미데이터 생성과정:



---

## 📅 개발 일지

### 1주차
- 프로젝트 구조 설계 및 초기 세팅
  - Django REST Framework와 Vue3를 기반으로 백엔드와 프론트엔드 분리
  - 초기 디렉터리 구조 구성
  - 24-11-11 일지 (https://github.com/users/KSAhh/projects/3/views/1?pane=info&statusUpdateId=63641)
  - 24-11-12 일지 (https://github.com/users/KSAhh/projects/3/views/1?pane=info&statusUpdateId=63645)
  - 24-11-13 일지 (https://github.com/users/KSAhh/projects/3/views/1?pane=info&statusUpdateId=63662)
  - 24-11-14 일지 (https://github.com/users/KSAhh/projects/3/views/1?pane=info&statusUpdateId=64087)
  - 24-11-15 일지 (https://github.com/users/KSAhh/projects/3/views/1?pane=info&statusUpdateId=64444)

### 2주차
- 주요 기능 구현 착수
  - API 연동: 금융감독원, 카카오 맵 API 테스트
  - 예적금 금리 비교 기능
  - 사용자 프로필 관리 기능
- 신혼여행 환율 계산기 개발
  - 한국수출입은행 환율 정보 API 연동
  - 환율 계산 로직 구현
  - 알고리즘 로직 설계
  - 24-11-17 일지 (https://github.com/users/KSAhh/projects/3/views/1?pane=info&statusUpdateId=64478)

### 3주차

- 근처 은행 검색 및 금융 상품 추천 기능 추가
  - 카카오 맵 API를 활용하여 사용자 위치 기반 은행 검색
  - 알고리즘 기반 금융 상품 추천 로직 개발
- 디자인 적용
- 프론트 적용

---



## 🛠 이슈 관리
초기 설정 문제: Vue3와 Tailwind CSS 연동 시 스타일 적용 문제 해결
API 호출 최적화: 다중 호출 문제를 Axios 인터셉터로 해결

---

## 🎓 배운점 및 느낀점
**김수아**
> DB 및 API 설계 후 Django REST Framework로 전달할 데이터를 결정한 이후에, 실제 프론트에서 사용할 때 필요한 데이터와 상이한 면이 있어서 수정을 반복하였습니다. 설계, 개발, 분석을 반복하며 애자일 방법론에 대해 이해하게 되었습니다. 여기서 효율적인 자원 관리를 위해 데이터베이스를 정규화하는 것의 필요성을 느낄 수 있었습니다.
> 또한 이메일 정규화, 비밀번호 해시화 등 커스텀하였습니다.
> 프론트 작업을 수행하면서 유저 로그인 시 닉네임 필드를 출력하거나, 글 삭제이후 바로 글 목록에서 없애는 기능 등 JavaScript에서 비동기적으로 상태관리하는 방법에 대해 배웠습니다.
> 팀원과 함께 진행해나가면서 위험관리 측면에서 부족한 점을 느꼈습니다. 업무에서 가장 중요한 점은 납기 및 고객에게 보여줄 수 있는 70%이상의 퀄리티라고 생각하는데 구현했던 결과물에 비해 표현이 아쉬워서 충분히 어필하지 못하였다고 생각합니다. 해서 아쉬웠던 점들은 보완할 예정입니다.


백지원
> Vue3와 Chart.js를 사용한 데이터 시각화 경험을 쌓을 수 있었습니다

---

## 📦 설치 및 실행 방법
- Frontend

```bash
# Frontend
$ cd front/algo-fipo
$ npm install
$ npm run dev

# Backend
$ cd back
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata exchange.json products.json
$ python manage.py runserver

```

---
