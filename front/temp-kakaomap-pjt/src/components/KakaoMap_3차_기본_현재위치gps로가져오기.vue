<template>
  <h1>3차</h1>
  <div>
    <h1>현재 위치</h1>
    <div ref="map" style="width: 100%; height: 400px;"></div>
    <p>위도: {{ currentLocation.lat }}</p>
    <p>경도: {{ currentLocation.lng }}</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const mapElement = ref(null);
    const currentLocation = ref({ lat: null, lng: null });

    // 현재 위치 가져오기
    const getCurrentLocation = () => {
      if (navigator.geolocation) {
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
      } else {
        console.error("이 브라우저는 Geolocation을 지원하지 않습니다.");
      }
    };

    onMounted(() => {
      getCurrentLocation();
    });

    return {
      mapElement,
      currentLocation,
    };
  },
};
</script>

<style>
/* 지도에 필요한 스타일 설정 */
#map {
  width: 100%;
  height: 100%;
}
</style>
