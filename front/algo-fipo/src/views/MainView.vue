<template>
  <div class="w-full max-w-screen-2xl mx-auto p-6">
    <!-- Intro Section -->
    <section class="mb-12">
      <div class="flex flex-col space-y-12 sm:space-y-16 md:space-y-20">
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
              >몰라도, </span
            >
            <span>괜찮습니다.</span>
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

    <!-- Main Content -->
    <div
      class="flex flex-col md:flex-row items-stretch px-4 sm:px-6 md:px-8 lg:px-12"
    >
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
            @click="selectedContent = '개인 맞춤형 어드밴스드'"
            class="cursor-pointer hover:underline"
          >
            개인 맞춤형 어드밴스드
          </li>
          <li
            @click="selectedContent = '개인 맞춤형 정보 입력형'"
            class="cursor-pointer hover:underline"
          >
            개인 맞춤형 정보 입력형
          </li>
          <li
            @click="selectedContent = '기본 필터형'"
            class="cursor-pointer hover:underline"
          >
            기본 필터형
          </li>
        </ul>
        <div
          class="text-[clamp(1rem, 2.5vw, 1.5rem)] font-bold mt-8 border-b border-white pb-2 text-center"
        >
          기타 서비스 소개
        </div>
        <ul
          class="space-y-4 sm:space-y-6 md:space-y-8 text-[clamp(0.875rem, 2vw, 1.125rem)] text-center"
        >
          <li
            @click="selectedContent = '환율 계산 서비스'"
            class="cursor-pointer hover:underline"
          >
            환율 계산 서비스
          </li>
          <li
            @click="selectedContent = '은행 지도 서비스'"
            class="cursor-pointer hover:underline"
          >
            은행 지도 서비스
          </li>
          <li
            @click="selectedContent = '?'"
            class="cursor-pointer hover:underline"
          >
            ?
          </li>
        </ul>
      </div>

      <!-- 노란 박스 -->
      <div
        class="w-full md:w-2/3 bg-[#ffd700] p-6 md:rounded-r min-h-[400px]"
      >
        <p
          v-if="selectedContent"
          class="text-[clamp(0.875rem, 2vw, 1.25rem)]"
        >
          {{ selectedContent }} 서비스 내용입니다.
        </p>
        <p
          v-else
          class="text-[clamp(0.875rem, 2vw, 1.25rem)]"
        >
          서비스를 선택해 주세요.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainView",
  data() {
    return {
      selectedContent: null,
      showFirstSentence: false,
      showSecondSentence: false,
      showThirdSentence: false,
    };
  },
  mounted() {
    this.showFirstSentence = true;
    setTimeout(() => {
      this.showSecondSentence = true;
    }, 1400);
    setTimeout(() => {
      this.showThirdSentence = true;
    }, 2800);
  },
};
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
  visibility: hidden;
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
</style>
