<script setup>
import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps' 
// KakaoMap : 맵 생성
// KakaoMapMaker : 마커 생성
import { ref } from 'vue'

const lat = ref(33.450701) // 위도
const lng = ref(126.570667) // 경도
const map = ref()

// 지도 출력
const onLoadKakaoMap = (mapRef) => {
  map.value = mapRef
}

// 부드러운 이동 효과
// 이동할 거리가 지도 화면보다 크면 -> 효과 없이 이동
const panTo = () => {
  if (map.value) {
    map.value.panTo(new kakao.maps.LatLng(33.45058, 126.574942))
  }
};

// 마우스 호버 이벤트
const infoWindow = ref("현재 위치")
const visibleRef = ref(false);

const mouseOverKakaoMapMarker = () => {
  visibleRef.value = true;
};

const mouseOutKakaoMapMarker = () => {
  visibleRef.value = false;
};</script>


<template>
  <h2>2차 </h2>
  <KakaoMap :lat="lat" :lng="lng" @onLoadKakaoMap="onLoadKakaoMap">
    <!-- 마커추가 -->
    <!-- infoWindow : 클릭시 나오는 설명창 -->
    <KakaoMapMarker :lat="lat" :lng="lng" 

      :infoWindow="{ content: infoWindow, visible: visibleRef }"
      @mouseOverKakaoMapMarker="mouseOverKakaoMapMarker"
      @mouseOutKakaoMapMarker="mouseOutKakaoMapMarker" 

      :image="{ // 마커이미지 변경
          imageSrc: '/src/assets/bank_marker.png',
          imageWidth: 120,
          imageHeight: 70,
          imageOption: {}
      }"
     
    />  
  </KakaoMap>
  <div>
    <button @click="panTo" class="demo-button">map 객체로 부드러운 이동</button>
  </div>

  
</template>
