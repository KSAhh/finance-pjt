// src/components/loan/loanpage/filterOptions.js

// 직군 옵션
export const jobOptions = [
    { id: 'employee', name: '직장인' },
    { id: 'business_owner', name: '사업자' },
    { id: 'unemployed', name: '무직·주부' },
    { id: 'others', name: '기타' },
  ];
  
  // 대출종류 옵션
  export const loanTypes = [
    { id: '신용', name: '신용' },
    { id: '사업자금', name: '사업자금' },
    { id: '정책자금', name: '정책자금' },
    { id: '자동차담보', name: '자동차담보' },
    { id: '카드론', name: '카드론' },
    { id: '약관', name: '약관' },
    { id: '비상금', name: '비상금' },
  ];
  
  // 특징 옵션
  export const features = [
    { id: '당일입금', name: '당일입금' },
    { id: '만기일시상환', name: '만기일시상환' },
    { id: '마이너스통장', name: '마이너스통장' },
    { id: '앱설치없음', name: '앱설치 없음' },
    { id: '고정금리', name: '고정금리' },
    { id: '1금융', name: '1금융' },
    { id: '중도상환무료', name: '중도상환무료' },
    { id: '대환가능', name: '대환가능' },
    { id: '휴일입금', name: '휴일입금' },
    { id: '비대면', name: '비대면' },
    { id: '금리10%이하', name: '금리 10% 이하' },
    { id: '한도5천만원이상', name: '한도 5천만원 이상' },
    { id: 'DSR제외', name: 'DSR제외' },
  ];
  
  // 금융권 옵션
  export const financialGroups = [
    { id: '은행', name: '은행' },
    { id: '저축은행', name: '저축은행' },
    { id: '카드사', name: '카드사' },
    { id: '캐피탈', name: '캐피탈' },
    { id: '보험사', name: '보험사' },
    { id: 'P2P', name: 'P2P' },
  ];
  
  // 금융사 옵션 섹션별 구성
  export const financialCompanySections = [
    {
      name: '은행',
      companies: [
        { id: 'BNK경남은행', name: 'BNK경남은행' , logo: () => import('@/assets/BankLogo/bankName=경남.svg')},
        { id: 'BNK부산은행', name: 'BNK부산은행' },
        { id: 'IBK기업은행', name: 'IBK기업은행' },
        { id: 'KB국민은행', name: 'KB국민은행' },
        { id: 'NH농협은행', name: 'NH농협은행' },
        { id: 'SC제일은행', name: 'SC제일은행' },
        { id: 'SH수협은행', name: 'SH수협은행' },
        { id: 'iM뱅크(DGB대구은행)', name: 'iM뱅크(DGB대구은행)' },
        { id: '광주은행', name: '광주은행' },
        { id: '신한은행', name: '신한은행' },
        { id: '우리은행', name: '우리은행' },
        { id: '전북은행', name: '전북은행' },
        { id: '케이뱅크', name: '케이뱅크' },
        { id: '하나은행', name: '하나은행' },
      ],
    },
    {
      name: '저축은행',
      companies: [
        { id: 'BNK저축은행', name: 'BNK저축은행' },
        { id: 'DB저축은행', name: 'DB저축은행' },
        { id: 'IBK저축은행', name: 'IBK저축은행' },
        // ... 기타 저축은행 목록
      ],
    },
    {
      name: '카드사',
      companies: [
        { id: 'BC카드', name: 'BC카드' },
        { id: 'KB국민카드', name: 'KB국민카드' },
        { id: '신한카드', name: '신한카드' },
        { id: '우리카드', name: '우리카드' },
        { id: '현대카드', name: '현대카드' },
      ],
    },
    // ... 기타 금융권 섹션과 금융사 목록
  ];
  
  // 은행 목록 (for selectedFilterLabels)
  export const banks = financialCompanySections.find(
    (section) => section.name === '은행'
  )?.companies || []; // 안전하게 빈 배열로 초기화
  
  // 금융사 목록 (for selectedFilterLabels)
  export const financialCompanies = financialCompanySections.flatMap(
    (section) => section.companies || [] // 안전하게 companies를 펼침
  );
  