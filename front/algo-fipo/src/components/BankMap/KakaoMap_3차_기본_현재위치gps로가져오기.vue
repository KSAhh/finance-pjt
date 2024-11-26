<template>
  <div>
    <h1>3차</h1>
    <div>
      <h1>현재 위치</h1>
      <div ref="mapElement" class="map-container"></div>
      <p>위도: {{ currentLocation.lat }}</p>
      <p>경도: {{ currentLocation.lng }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const mapElement = ref(null); // 지도 엘리먼트
const currentLocation = ref({ lat: null, lng: null }); // 현재 위치

// 현재 위치 가져오기
const getCurrentLocation = () => {
  if (!navigator.geolocation) {
    console.error("이 브라우저는 Geolocation을 지원하지 않습니다.");
    return;
  }

  navigator.geolocation.getCurrentPosition(
    (position) => {
      const { latitude, longitude } = position.coords;
      currentLocation.value = { lat: latitude, lng: longitude };

      // 지도 생성
      const map = new kakao.maps.Map(mapElement.value, {
        center: new kakao.maps.LatLng(latitude, longitude),
        level: 3,
      });

      // 마커 표시
      const marker = new kakao.maps.Marker({
        position: new kakao.maps.LatLng(latitude, longitude),
      });
      marker.setMap(map);
    },
    (error) => {
      console.error("위치 정보를 가져오는데 실패했습니다.", error);
    }
  );
};

// 컴포넌트가 마운트된 후 지도와 위치 초기화
onMounted(() => {
  getCurrentLocation();
});
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 400px;
  border: 1px solid #ccc;
}
</style>
