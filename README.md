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

https://github.com/user-attachments/assets/95aa4d90-ef9d-4697-8bc1-d3d993a8ed63

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
