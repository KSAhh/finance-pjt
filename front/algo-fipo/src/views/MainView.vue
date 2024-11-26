<template>
  <div class="w-full max-w-screen-2xl mx-auto p-6">
    <!-- Intro Section -->
    <section class="mb-12">
      <div class="flex flex-col space-y-12 sm:space-y-16 md:space-y-10">
        <!-- 첫 번째 문장 -->
        <div
          class="shadow-text py-20 text-xl sm:text-2xl md:text-4xl lg:text-5xl font-thin text-left leading-loose lg:ml-12"
          :class="showFirstSentence ? 'animate-left-to-right' : 'invisible'"
        >
          <span class="highlight-effect">내게 맞는</span>
          <span class="block md:inline">금융 상품을 찾고 싶으십니까?</span>
        </div>
        <!-- 두 번째 문장 -->
        <div
          class="shadow-text py-20 text-xl sm:text-2xl md:text-4xl lg:text-5xl font-medium text-right leading-loose lg:mr-12"
          :class="showSecondSentence ? 'animate-right-to-left' : 'invisible'"
        >
          <span class="block md:inline">어떤 상품을 원하는지 </span>
          <div class="block md:inline text-black">
            <span
              :class="showSecondSentence ? 'highlight-effect-delayed' : ''"
              >몰라도</span
            >
            <span> 괜찮습니다.</span>
          </div>
        </div>
      </div>
      <!-- "algo.fipo가 찾아드리겠습니다." -->
      <div
        class="flex flex-wrap md:flex-nowrap items-center px-4 sm:px-6 md:px-8 lg:px-12 pt-15 text-left font-bold text-2xl sm:text-3xl md:text-4xl lg:text-6xl mt-12 leading-relaxed"
        :class="showThirdSentence ? 'animate-fade-in' : 'invisible'"
      >
        <span class="algo-fipo-effect">algo.fipo</span>
        <span class="text-black md:ml-2">가 찾아드리겠습니다.</span>
      </div>
    </section>

    <div class="w-full max-w-screen-2xl mx-auto p-6">
    <!-- Main Content -->
    <div class="flex flex-col md:flex-row items-stretch px-4 sm:px-6 md:px-8 lg:px-12">
      <!-- 파란 박스 -->
      <div
        class="w-full md:w-1/3 bg-[#0048e8] text-white p-6 md:rounded-l min-h-[400px]"
      >
        <div
          class="text-[clamp(1rem, 2.5vw, 1.5rem)] font-bold mb-6 border-b border-white pb-2 text-center"
        >
          금융 상품 추천 서비스
        </div>
        <ul
          class="space-y-4 sm:space-y-6 md:space-y-8 text-[clamp(0.875rem, 2vw, 1.125rem)] text-center"
        >
          <li
            v-for="(service, index) in serviceList"
            :key="index"
            @click="selectedContent = service.label"
            class="cursor-pointer hover:bg-[#003bb5] hover:text-white hover:font-extrabold transition-all duration-300 py-2 px-4 rounded-lg"
          >
            {{ service.label }}
          </li>
        </ul>
      </div>

      <!-- 노란 박스 -->
      <div class="w-full md:w-2/3 bg-[#ffd700] p-8 md:rounded-r min-h-[400px] flex flex-col justify-center items-start shadow-lg">
        <h2 class="text-2xl md:text-3xl font-semibold text-gray-800 mb-4">
          {{ selectedContent || "서비스를 선택해 주세요." }}
        </h2>
        <p v-if="selectedContent === '개인 맞춤형 추천'" class="text-gray-700 text-lg leading-relaxed">
          사용자 데이터를 기반으로 최적화된 금융 상품을 추천합니다. <br />
          AI 알고리즘을 활용해 다양한 조건을 분석하여 최적의 선택을 제공합니다.
        </p>
        <p v-else-if="selectedContent === '개인 맞춤 정보 입력형'" class="text-gray-700 text-lg leading-relaxed">
          사용자가 입력한 정보를 기반으로 적합한 금융 상품을 제안합니다. <br />
          직접 선택과 입력을 통해 보다 세밀한 필터링이 가능합니다.
        </p>
        <p v-else-if="selectedContent === '기본 필터형'" class="text-gray-700 text-lg leading-relaxed">
          단순 필터링을 통해 상품을 비교하고 선택할 수 있습니다. <br />
          금리, 기간, 최소 금액 등 기본 정보를 중심으로 결과를 확인하세요.
        </p>
        <p v-else-if="selectedContent === '환율 계산 서비스'" class="text-gray-700 text-lg leading-relaxed">
          실시간 환율 정보를 제공하며, 환율 변동 내역과 주요 통화 간 비교도 가능합니다. <br />
          해외 송금이나 외환 거래에 유용한 도구입니다.
        </p>
        <p v-else-if="selectedContent === '은행 지도 서비스'" class="text-gray-700 text-lg leading-relaxed">
          현재 위치 기반으로 가까운 은행 지점을 안내합니다. <br />
          지점별 운영 시간, ATM 위치 및 추가 서비스 정보를 확인할 수 있습니다.
        </p>
        <p v-else-if="selectedContent === '기타 서비스'" class="text-gray-700 text-lg leading-relaxed">
          더 많은 정보와 기능이 추가될 예정입니다. 기대해 주세요!
        </p>
      </div>
    </div>
  </div>


  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useUserStore } from "@/stores/user"
const userStore = useUserStore()

// 상태
const selectedContent = ref(null);
const showFirstSentence = ref(false);
const showSecondSentence = ref(false);
const showThirdSentence = ref(false);

// 서비스 목록
const serviceList = [
  { label: "개인 맞춤형 추천" },
  { label: "개인 맞춤 정보 입력형" },
  { label: "기본 필터형" },
  { label: "환율 계산 서비스" },
  { label: "은행 지도 서비스" },
  { label: "기타 서비스" },
];

onMounted(async() => {
  // 유저정보 가져오기
  await userStore.getUserInfo()
  const userInfo = userStore.userInfo
  if (userInfo.nickname) {
    localStorage.setItem("nickname", userInfo.nickname)
  }

  // 애니메이션 초기화
  showFirstSentence.value = true;
  setTimeout(() => {
    showSecondSentence.value = true;
  }, 1400);
  setTimeout(() => {
    showThirdSentence.value = true;
  }, 2800);
});
</script>

<style scoped>
/* 텍스트 박스 그림자 효과 */
.shadow-text {
  position: relative;
  text-shadow: 2px 1px 5px rgba(0, 0, 0, 0.3); /* 그림자 번짐 */
}

/* 'algo.fipo' 텍스트 효과 */
.algo-fipo-effect {
  color: #0048e8;
  font-weight: bold;
  text-shadow: 1px 1px 6px rgba(0, 72, 232, 0.7); /* 파란색 번짐 */
}

/* 형광펜 애니메이션 정의 */
@keyframes highlight {
  0% {
    width: 0;
    opacity: 0.5;
  }
  100% {
    width: 100%;
    opacity: 0.7;
  }
}

/* 형광펜 효과 */
.highlight-effect {
  position: relative;
  display: inline-block;
}

.highlight-effect::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 1.2em; /* 형광펜 높이 */
  background-color: #ffd700; /* 형광펜 색상 */
  z-index: -1; /* 텍스트 위로 올라오지 않게 설정 */
  width: 0;
  animation: highlight 0.5s ease-out forwards; /* 애니메이션 시간 조정 */
  animation-delay: 0.7s; /* 텍스트 애니메이션 후 실행 */
}

/* 두 번째 문장 형광펜 딜레이 효과 */
.highlight-effect-delayed {
  position: relative;
  display: inline-block;
}

.highlight-effect-delayed::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 1.2em; /* 형광펜 높이 */
  background-color: #ffd700; /* 형광펜 색상 */
  z-index: -1; /* 텍스트 위로 올라오지 않게 설정 */
  width: 0;
  animation: highlight 0.5s ease-out forwards; /* 애니메이션 시간 조정 */
  animation-delay: 0.8s; /* 두 번째 문장 등장 후 형광펜 실행 */
}

/* 텍스트 애니메이션 정의 */
@keyframes left-to-right {
  0% {
    transform: translateX(-10%);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes right-to-left {
  0% {
    transform: translateX(10%);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.invisible {
  opacity: 0;
}


.animate-left-to-right {
  animation: left-to-right 0.7s ease-in-out forwards;
}

.animate-right-to-left {
  animation: right-to-left 0.7s ease-in-out forwards;
}

.animate-fade-in {
  animation: fade-in 2s ease-in-out forwards;
}

/* 파란 박스 호버 효과 */
ul li {
  font-family: 'Inter', sans-serif;
}

ul li:hover {
  background-color: #003bb5;
  color: #ffffff;
  font-weight: 800;
  transition: all 0.3s ease-in-out;
  border-radius: 8px;
}
</style>
