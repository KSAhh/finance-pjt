# 💰 AlgoFiPo Project

> **재테크를 효율적으로 관리할 수 있는 서비스**  
> 결혼 후 자가 마련과 신혼여행을 준비하는 사용자들을 대상으로 예적금 금리비교, 환율 계산기, 근처 은행 검색, 그리고 사용자 맞춤형 금융 상품 추천 서비스를 제공합니다.

---

## 🚀 프로젝트 목표
- 금융상품 데이터 기반 예금 및 적금 금리 비교 서비스 구성
- 환율 정보 API를 활용한 환율 계산 서비스 구성
- 지도 API를 활용한 은행 검색 서비스 구성
- 일반상품시세(금, 석유)와 주가지수 시세(KOSPI, KOSDAQ 등) API를 활용한 차트 서비스 구성
- 시세 데이터 추세 분석을 통한 투자 추천 알고리즘 구성
- 커뮤니티 서비스 추가로 사용자 소통 강화

---

## 📅 개발기간
**2024년 11월 18일 ~ 2024년 11월 26일**

---

## 👥 Collaborators
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/KSAhh">
        <img src="https://avatars.githubusercontent.com/KSAhh" width="150px;" alt="KSAhh"/>
        <br/><sub><b>KSAhh</b><br></sub>
        <p>김수아 / Backend(Django), Frontend(Vue), Git 규칙 지정</p>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/sadtearcat">
        <img src="https://avatars.githubusercontent.com/sadtearcat" width="150px;" alt="sadtearcat"/>
        <br/><sub><b>sadtearcat</b><br></sub>
        <p>백지원 / Frontend(Vue), 상품 추천 알고리즘 개발</p>
      </a>
    </td>
  </tr>
</table>

---

## 🛠 주요 기능
1. **예적금 금리 비교**  
   - 사용자가 선택한 금융사, 상품옵션에 맞는 상품을 조회합니다.

2. **환율 계산기**  
   - 출국을 위해 필요한 환전 금액을 계산합니다.

3. **근처 은행 검색**  
   - 검색 키워드 근처의 은행 지점을 검색합니다.

4. **맞춤형 금융 상품 추천**  
   - 금융상품 및 사용자 데이터를 기반으로 개인의 재정 상태에 맞는 금융 상품을 추천합니다.

5. **고객센터**  
   - 사용자 간의 질문, 리뷰 등을 공유할 수 있으며, 관리자의 답변을 제공받을 수 있습니다.

6. **프로필 관리**  
   - 사용자 정보를 관리할 수 있습니다.

---

## 🔧 기술 스택
### Backend
- **Framework**: Django REST Framework
- **Database**: SQLite
- **Language**: Python
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
- ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white)
- ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white)

<img src="https://skillicons.dev/icons?i=githubactions" width="48" height="48" alt="GitHub Actions"/>

<img src="https://skillicons.dev/icons?i=python" width="48" height="48" alt="Python"/>
<img src="https://skillicons.dev/icons?i=django" width="48" height="48" alt="Django"/>
<img src="https://skillicons.dev/icons?i=sqlite" width="48" height="48" alt="SQLite"/>

[![My Skills](https://skillicons.dev/icons?i=python,nodejs,figma,django,sqlite,&theme=light&perline=5)](https://skillicons.dev)

### Frontend
- **Framework**: Vue3
- **State Management**: Pinia
- **Styling**: Tailwind CSS
- **Visualization**: Chart.js
- **HTTP Client**: Axios
- ![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=Vue.js&logoColor=white)
- ![TailwindCSS](https://img.shields.io/badge/TailwindCSS-06B6D4?style=flat-square&logo=TailwindCSS&logoColor=white)
- ![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=Chart.js&logoColor=white)

[![My Skills](https://skillicons.dev/icons?i=html,css,js,vue,tailwind&theme=light&perline=5)](https://skillicons.dev)



<img src="https://skillicons.dev/icons?i=vue" width="48" height="48" alt="Vue.js"/>
<img src="https://skillicons.dev/icons?i=tailwind" width="48" height="48" alt="Tailwind CSS"/>
<img src="https://skillicons.dev/icons?i=css" width="48" height="48" alt="CSS"/>
<img src="https://skillicons.dev/icons?i=javascript" width="48" height="48" alt="JavaScript"/>
<img src="https://skillicons.dev/icons?i=chartjs" width="48" height="48" alt="Chart.js"/>


[![My Skills](https://skillicons.dev/icons?i=git,notion,github,githubactions&theme=light&perline=5)](https://skillicons.dev)


### External APIs
- **한국수출입은행 API**
- **카카오 API**
- **금융감독원 API**

---
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
│   └── requirements.txt   - 의존성 파일
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

--- 

## ⚙ ERD
![ERD 다이어그램](링크 또는 파일 업로드)

---

## 🧩 컴포넌트 구조
NavBar: 네비게이션 바
BankMap: 지도 기반 은행 검색
CustomerService: 고객센터
ExchangeRate: 환율 계산기
Savings: 예적금 금리 비교
LoanPage: 대출 관련 서비스
(이미지 첨부)

---

## 📈 투자 추천 알고리즘 원리
데이터 수집
금융상품 시세, 주가지수 데이터를 외부 API를 통해 수집합니다.
추세 분석
특정 기간 동안의 데이터를 분석하여 상승/하락 추세를 예측합니다.
사용자 맞춤 추천
사용자의 투자 성향(위험 선호도 등)을 기반으로 최적의 투자 상품을 추천합니다.

---

## 📝 개발일지
1주차
프로젝트 초기 세팅: Django, Vue3 환경 구축
API 연동: 금융감독원, 카카오 맵 API 테스트
2주차
주요 기능 개발
예적금 금리 비교, 환율 계산기
알고리즘 로직 설계

---

## 🛠 이슈 관리
초기 설정 문제: Vue3와 Tailwind CSS 연동 시 스타일 적용 문제 해결
API 호출 최적화: 다중 호출 문제를 Axios 인터셉터로 해결

---

## 🎓 배운점 및 느낀점
김수아: Django REST Framework를 활용하여 데이터 API 설계 및 효율적인 상태 관리를 배웠습니다.
백지원: Vue3와 Chart.js를 사용한 데이터 시각화 경험을 쌓을 수 있었습니다

---

## 📦 설치 및 실행 방법
- Frontend

```bash
# Frontend
$ cd front/algo-fipo
$ npm install
$ npm run dev
# $ npm install
# $ npm insatll axios
# $ npm install 테일윈드????
# $ npm i vue3-kakao-maps (해당 라이브러리 사용하는지 최종 확인 필)

# Backend
$ cd back
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata data.json
$ python manage.py runserver

```

## 📅 개발 일정
**Branch History 기반 정리**
### 1주차
- 프로젝트 구조 설계 및 초기 세팅
  - Django REST Framework와 Vue3를 기반으로 백엔드와 프론트엔드 분리
  - 초기 디렉터리 구조 구성

### 2주차
- 주요 기능 구현 착수
  - 예적금 금리 비교 기능
  - 사용자 프로필 관리 기능

### 3주차
- 신혼여행 환율 계산기 개발
  - 한국수출입은행 환율 정보 API 연동
  - 환율 계산 로직 구현

### 4주차
- 근처 은행 검색 및 금융 상품 추천 기능 추가
  - 카카오 맵 API를 활용하여 사용자 위치 기반 은행 검색
  - 알고리즘 기반 금융 상품 추천 로직 개발

---
