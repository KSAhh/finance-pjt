<template>
  <div>
    <h1>1차</h1>
    <!-- 지도 컨테이너 -->
    <div ref="mapContainer" class="map-container"></div>

    <!-- 검색 입력 -->
    <div class="search-container">
      <input
        v-model="keyword"
        type="text"
        placeholder="검색할 지역을 입력하세요"
        @keyup.enter="searchPlaces"
      />
      <button @click="searchPlaces">검색</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const { VITE_KAKAO_JS_KEY } = import.meta.env;
const mapContainer = ref(null); // 지도 DOM 요소
const keyword = ref(""); // 검색어
let mapInstance = null; // 지도 객체
let ps = null; // 장소 검색 객체
const markers = []; // 마커 배열

// 지도 로드 함수
const loadKakaoMap = async () => {
  return new Promise((resolve) => {
    const script = document.createElement("script");
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${VITE_KAKAO_JS_KEY}&autoload=false&libraries=services,clusterer,drawing`;
    document.head.appendChild(script);

    script.onload = () => {
      window.kakao.maps.load(() => {
        resolve(window.kakao);
      });
    };
  });
};

// 마커 관리 함수
const removeAllMarkers = () => {
  markers.forEach((marker) => marker.setMap(null));
  markers.length = 0;
};

const displayMarker = (place) => {
  const marker = new kakao.maps.Marker({
    map: mapInstance,
    position: new kakao.maps.LatLng(place.y, place.x),
  });
  markers.push(marker);

  const infoWindow = new kakao.maps.InfoWindow({ zIndex: 1 });
  kakao.maps.event.addListener(marker, "click", () => {
    infoWindow.setContent(
      `<div style="padding:5px;font-size:12px;">${place.place_name}</div>`
    );
    infoWindow.open(mapInstance, marker);
  });
};

// 검색 함수
const searchBanksInBounds = () => {
  if (!ps) return;
  ps.categorySearch("BK9", placesSearchCB, { useMapBounds: true });
};

const placesSearchCB = (data, status) => {
  if (status === kakao.maps.services.Status.OK) {
    removeAllMarkers();
    data.forEach((place) => displayMarker(place));
  } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
    alert("검색 결과가 없습니다.");
  } else {
    alert("검색 중 오류가 발생했습니다.");
  }
};

const searchPlaces = () => {
  if (!keyword.value.trim()) {
    alert("검색어를 입력하세요.");
    return;
  }

  ps.keywordSearch(keyword.value, (data, status) => {
    if (status === kakao.maps.services.Status.OK) {
      const firstResult = data[0];
      const center = new kakao.maps.LatLng(firstResult.y, firstResult.x);
      mapInstance.setCenter(center);
      searchBanksInBounds();
    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
      alert("키워드 검색 결과가 없습니다.");
    } else {
      alert("검색 중 오류가 발생했습니다.");
    }
  });
};

// 지도 초기화
const initializeMap = async () => {
  const kakao = await loadKakaoMap();

  const options = {
    center: new kakao.maps.LatLng(37.503188, 127.044811),
    level: 3,
  };
  mapInstance = new kakao.maps.Map(mapContainer.value, options);
  ps = new kakao.maps.services.Places(mapInstance);

  // 초기 은행 검색
  searchBanksInBounds();
};

// 마운트 시 지도 로드
onMounted(() => {
  initializeMap();
});
</script>

<style scoped>
/* 지도 컨테이너 스타일 */
.map-container {
  width: 100%;
  height: 70vh;
  border: 1px solid #ccc;
}

/* 검색 입력 및 버튼 스타일 */
.search-container {
  margin: 10px 0;
  display: flex;
  align-items: center;
  gap: 10px;
}

input[type="text"] {
  width: 300px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}
</style>
