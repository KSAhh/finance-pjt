<template>
  <li class="px-4 lg:px-6 xl:px-8 relative group">
    <!-- 메뉴 이름 -->
    <a href="#" @click.prevent="onMenuClick" class="hover:underline">
      {{ label }}
    </a>

    <!-- 드롭다운 메뉴 -->
    <div
      v-if="isVisible"
      class="dropdown-menu fixed top-[64px] left-0 w-screen bg-white border border-gray-300 rounded opacity-0 h-0 overflow-hidden transition-all duration-500 ease-in-out group-hover:h-64 group-hover:opacity-100 z-50"
    >
      <div class="flex h-full">
        <!-- 첫 번째 영역 -->
        <div class="w-1/3 bg-gray-100 p-6 shadow-sm animate-slide-in-left text-container">
          <h3 class="text-lg font-semibold border-b pb-2 mb-4 border-gray-300 animate-slide-in-left">
            {{ label }} 정보
          </h3>
          <p class="mt-2 text-sm text-gray-600 leading-relaxed">

            <p v-if="label === '예적금'">
              예적금 상품에 대한 정보를 확인하실 수 있습니다.<br />
              은행별로 제공되는 예금 및 적금 상품의 조건, 금리, 혜택 등을 한눈에 비교해 보세요.
            </p>
            <p v-else-if="label === '대출'">
              대출 상품에 대한 정보를 제공합니다.<br />
              대출 가능 금액, 금리 조건, 상환 방식 등 주요 정보를 확인하고<br />
              자신에게 맞는 대출 상품을 찾아볼 수 있습니다.
            </p>
            <p v-else-if="label === '은행 지도'">
              주변 은행의 위치를 손쉽게 확인하실 수 있습니다.<br />
              가까운 은행 지점을 찾아 편리하게 방문 계획을 세워보세요.
            </p>
            <p v-else-if="label === '환율'">
              환율 정보를 실시간으로 확인하실 수 있습니다.<br />
              주요 통화의 현재 환율과 변동 사항을 확인하고 외환 거래에 필요한 정보를 받아보세요.
            </p>
            <p v-else>
              관련된 정보가 없습니다.<br />
              더 많은 정보를 원하시면 고객센터로 문의해 주세요.
            </p>
          </p>
        </div>

        <!-- 두 번째 영역 -->
        <div class="w-1/3 bg-white p-6 border-l border-r border-gray-200 shadow-sm animate-fade-in">
          <ul class="space-y-4">
            <li style="font-weight: 300;"
              v-for="(item, index) in dropdownContent"
              :key="index"
              class="cursor-pointer font-medium "
              @click="onItemClick(item)"
            >
              {{ item.label || item }}
            </li>
          </ul>
        </div>

        <!-- 세 번째 영역 -->
        <div class="w-1/3 bg-gray-100 p-6 rounded-lg shadow-sm animate-slide-in-right text-container">
            <h3 class="text-lg pb-2 mb-4 border-gray-300 border-b">추가 정보</h3>
            <p class="mt-2 text-sm text-gray-600 leading-relaxed">
              <template v-if="label === '예적금'">
                예적금 상품과 관련된 유용한 팁을 확인해 보세요.<br />
                - 자동이체를 활용하면 추가 금리 혜택을 받을 수 있습니다.<br />
                - 적금 만기일을 잊지 말고 확인하세요.<br />
                - 만기 후 방치된 금액은 일반 금리로 전환될 수 있습니다.<br />
                - 정기 예금보다 자유 예금이 필요한 경우도 고려해 보세요.
              </template>
              <template v-else-if="label === '대출'">
                대출 신청 전 꼭 확인해야 할 사항:<br />
                - 금리 외에 연체 이자율, 상환 수수료 등 추가 비용을 비교하세요.<br />
                - 신용 점수에 따라 대출 한도와 금리가 달라질 수 있습니다.<br />
                - 소득 증빙 자료를 준비하면 대출 승인 속도를 높일 수 있습니다.
              </template>
              <template v-else-if="label === '은행 지도'">
                은행 방문 시 참고할 팁:<br />
                - 특정 업무는 예약제를 통해 빠르게 처리할 수 있습니다.<br />
                - ATM 위치와 운영 시간을 사전에 확인하세요.<br />
                - 은행 지점별로 제공하는 특화 서비스가 있을 수 있으니 확인해 보세요.
              </template>
              <template v-else-if="label === '환율'">
                환율 거래를 위한 추가 정보:<br />
                - 환율은 하루에도 여러 번 변동될 수 있으니 실시간으로 확인하세요.<br />
                - 주요 은행의 환율 우대율을 비교해 더 유리한 조건으로 거래하세요.<br />
                - 해외 결제 시 적용되는 환율과 수수료도 확인하세요.
              </template>
              <template v-else>
                추가 정보가 없습니다.<br />
                관련 정보는 고객센터로 문의해 주세요.
              </template>
            </p>
          </div>

      </div>
    </div>
  </li>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  label: {
    type: String,
    required: true,
  },
  dropdownContent: {
    type: Array,
    default: () => [],
  },
  isVisible: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(['click-menu', 'click-item']);

function onMenuClick() {
  emit('click-menu', props.label);
}

function onItemClick(item) {
  emit('click-item', item);
}
</script>

<style scoped>
a {
  text-decoration: none; /* 밑줄 제거 */
  color: inherit; /* 기본 텍스트 색상 유지 */
}

a:hover {
  text-decoration: none; /* 호버 시에도 밑줄 제거 */
}

/* 애니메이션 정의 */
@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slide-in-left {
  from {
    transform: translateX(-20px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slide-in-right {
  from {
    transform: translateX(20px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.text-container {
  white-space: normal; /* 줄바꿈 허용 */
  word-break: break-word; /* 긴 단어 줄바꿈 */
  overflow-wrap: break-word; /* 단어가 영역을 넘지 않도록 */
}
/* 애니메이션 클래스 */
.animate-fade-in {
  animation: fade-in 0.5s ease-in-out;
}

.animate-slide-in-left {
  animation: slide-in-left 0.5s ease-in-out;
}

.animate-slide-in-right {
  animation: slide-in-right 0.5s ease-in-out;
}



</style>
