<template>
  <div class="max-w-8xl mx-auto bg-white rounded-lg shadow-lg p-8 mt-10 mb-20">
    <Map/>
  </div>
</template>
  
<script setup>
import Map from '@/components/BankMap/Map.vue';  


</script>
  
  <style scoped>
  
  </style>

<!-- 현재 위치 기능 통합:
현재 위치를 가져와 지도 중심을 설정하고, 현재 위치에 마커를 추가.

검색 기능 통합:
키워드 검색 및 은행 정보 표시 기능 포함.

마커 관리:
기존 마커 제거 및 새 마커 추가를 간단한 함수로 관리.

Kakao 지도 API 비동기 로드:
loadKakaoMap 함수로 API 로드 처리.

사용자 입력 처리:
검색 입력과 버튼 클릭 이벤트 처리. -->