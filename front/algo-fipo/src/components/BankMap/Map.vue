<template>
  <h1 class="text-2xl font-bold text-center my-5">주변 은행 찾기<hr class="my-2"></h1>
  <!-- 지도 컨테이너 -->
  <div id="page-container" class="flex flex-col md:flex-row justify-between items-start max-w-7xl mx-auto gap-8">
  <div ref="mapContainer" class="map-container w-full md:w-3/4 h-[70vh] border border-gray-300 relative mb-6 md:mb-24"></div>
  <!-- 검색 입력 및 결과 -->
  <div class="flex flex-col gap-4 md:w-1/3">
    <div class="flex flex-col justify-start gap-2">
      <select v-model="selectedBank" class="p-2 border border-gray-300 rounded-md">
          <option value="">전체 은행</option>
          <option value="국민은행">국민은행</option>
          <option value="농협은행">농협은행</option>
          <option value="신한은행">신한은행</option>
          <option value="우리은행">우리은행</option>
          <option value="하나은행">하나은행</option>
          <!-- 필요한 은행들을 추가하세요 -->
        </select>
        <input
          v-model="keyword"
          type="text"
          class="w-[300px] p-2 border border-gray-300 rounded-md focus:outline-none"
          placeholder="검색할 지역을 입력하세요"
          @keyup.enter="searchPlaces"
        />
        <button @click="searchPlaces" class="px-4 py-2 bg-blue-400 text-white rounded-md hover:bg-blue-500 transition-colors whitespace-nowrap">검색</button>
      </div>
      <div class="text-center text-sm text-gray-600">{{ alertContent }}</div>

      <div id="menu_wrap" class="bg_white">
        <ul class="list-none p-0 m-0">
          <li v-for="place in paginatedList" :key="place.index" class="flex items-center p-3 border-b border-gray-200 hover:bg-gray-100">
            <div class="mr-2">
              <span class="inline-block w-8 h-8 bg-blue-500 text-white text-center leading-8 font-bold rounded-full" :class="'marker_' + (place.index + 1)">{{ place.index + 1 }}</span>
            </div>
            <div class="flex-1">
              <h5 class="text-lg font-semibold text-gray-800">{{ place.name }}</h5>
              <span v-if="place.roadAddress" class="block text-sm text-gray-600 mt-1">{{ place.roadAddress }}</span>
              <span v-else class="block text-sm text-gray-500 mt-1">{{ place.jibunAddress }}</span>
              <span class="block text-xs text-gray-400 mt-1" v-if="place.phone">{{ place.phone }}</span>
            </div>
          </li>
        </ul>
        <div class="flex justify-center items-center gap-3 mt-5">
          <button
            @click="currentPage > 1 && (currentPage -= 1)"
            :disabled="currentPage === 1"
            class="px-4 py-2 border border-gray-300 bg-gray-100 rounded hover:bg-gray-200 disabled:cursor-not-allowed disabled:bg-gray-50 whitespace-nowrap"
          >
            이전
          </button>
          <span class="text-gray-600 text-sm whitespace-nowrap">페이지 {{ currentPage }} / {{ totalPages }}</span>
          <button
            @click="currentPage < totalPages && (currentPage += 1)"
            :disabled="currentPage === totalPages"
            class="px-4 py-2 border border-gray-300 bg-gray-100 rounded hover:bg-gray-200 disabled:cursor-not-allowed disabled:bg-gray-50 whitespace-nowrap"
          >
            다음
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from "vue";
import customMapMarker from '@/assets/customMapMarker.png';

const { VITE_KAKAO_JS_KEY } = import.meta.env;
const mapContainer = ref(null); // 지도 DOM 요소
const keyword = ref(""); // 검색어
let mapInstance = null; // 지도 객체
let ps = null; // 장소 검색 객체
const markers = []; // 마커 배열
const alertContent = ref("");
const selectedBank = ref(""); // 선택된 은행

// Kakao 지도 API 로드 함수
const loadKakaoMap = async () => {
  return new Promise((resolve) => {
    const script = document.createElement("script");
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${VITE_KAKAO_JS_KEY}&autoload=false&libraries=services`;
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
  markers.forEach((marker) => marker.setMap(null)); // 모든 마커를 지도에서 제거
  markers.length = 0; // 배열 초기화
};

const displayMarker = (place, index) => {
  const imageSrc = customMapMarker;
  const imageSize = new kakao.maps.Size(40, 55); // 마커이미지의 크기
  const imageOption = { offset: new kakao.maps.Point(22, 69) }; // 마커의 좌표와 일치시킬 이미지 안에서의 좌표
  const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);

  const marker = new kakao.maps.Marker({
    map: mapInstance,
    position: new kakao.maps.LatLng(place.y, place.x),
    image: markerImage,
  });

  const infoWindow = new kakao.maps.InfoWindow({
    content: `
      <p style="width: 100%; padding:5px 25px 5px 5px; font-size:12px; white-space: nowrap; display:inline-block; ">
        ${index + 1}. ${place.place_name}
      </p>
    `,
    zIndex: 1,
    removable: true,
  });
  markers.push(marker);

  kakao.maps.event.addListener(marker, "click", () => {
    infoWindow.open(mapInstance, marker);
  });
};

// 은행 검색 (마커 표시)
const searchBanksInBounds = () => {
  if (!ps) return;

  ps.categorySearch(
    "BK9",
    (data, status, pagination) => {
      if (status === kakao.maps.services.Status.OK) {
        removeAllMarkers();

        // 선택된 은행으로 데이터 필터링
        if (selectedBank.value) {
          data = data.filter(place => place.place_name.includes(selectedBank.value));
        }

        data.forEach((place, index) => {
          displayMarker(place, index);
        });

        listEl.value = data.map((place, index) => ({
          index,
          name: place.place_name,
          roadAddress: place.road_address_name || null,
          jibunAddress: place.address_name,
          phone: place.phone || null,
        }));

        const bankName = selectedBank.value || "전체";
        alertContent.value = `현재 지도 영역 내 ${bankName} 은행 검색 결과 총 ${data.length}건`;
      } else {
        console.log(status);
        // 기타 상태 처리
      }
    },
    { useMapBounds: true }
  );
};

// 키워드 검색
const searchPlaces = () => {
  if (!keyword.value.trim()) {
    alertContent.value = "";
    return;
  }

  ps.keywordSearch(keyword.value, placesSearchCB);
};

const placesSearchCB = (data, status, pagination) => {
  if (status === kakao.maps.services.Status.OK) {
    displayPlaces(data); // 검색 목록, 마커 표시
    alertContent.value = `"${keyword.value}" 에 대한 검색 결과 총 ${data.length}건`;
  } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
    alertContent.value = `"${keyword.value}" 에 대한 검색 결과 총 0건`;
  } else {
    alert("검색 중 오류가 발생했습니다.");
  }
};

const listEl = ref([]); // 검색결과 목록

const displayPlaces = (places) => {
  const firstResult = places[0];
  const center = new kakao.maps.LatLng(firstResult.y, firstResult.x);
  mapInstance.setCenter(center);
  searchBanksInBounds();
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

  kakao.maps.event.addListener(mapInstance, "bounds_changed", () => {
    searchBanksInBounds();
  });

  searchBanksInBounds();
};

// 검색결과 페이지네이션
const currentPage = ref(1); // 현재 페이지
const itemsPerPage = 5; // 페이지당 항목 수

// 현재 페이지에 표시될 항목
const paginatedList = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage;
  return listEl.value.slice(startIndex, startIndex + itemsPerPage);
});
const totalPages = computed(() => {
  return Math.ceil(listEl.value.length / itemsPerPage);
});

// 선택된 은행 변경 시 재검색
watch(selectedBank, () => {
  searchBanksInBounds();
});

// 컴포넌트 마운트 시 지도 초기화
onMounted(() => {
  initializeMap();
});
</script>

<style scoped>
#page-container {
  display: flex;
  flex-direction: column;
  gap: 20px; /* 두 영역 사이 간격 */
}

@media (min-width: 768px) {
  #page-container {
    flex-direction: row;
    gap: 60px; /* 큰 화면에서는 더 넓은 간격 */
  }
}

.map-container {
  flex: 1;
  min-height: 70vh; /* 지도 기본 높이 */
  border: 1px solid #ccc;
}

.flex-col {
  display: flex;
  flex-direction: column;
  justify-content: flex-start; /* 세로 정렬 상단 */
  gap: 10px;
}

ul {
  padding: 0;
  margin: 0;
  list-style: none;
}

li {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #eee;
  gap: 10px;
}

input, select {
  width: 100%;
  max-width: 300px;
  box-sizing: border-box;
}

@media (min-width: 768px) {
  input, select {
    max-width: 100%; /* 큰 화면에서는 가로 폭 조정 */
  }
}


button {
  padding: 10px 15px;
  font-size: 14px;
}

.flex {
  flex-wrap: wrap; /* 좁은 화면에서는 버튼이 여러 줄로 정렬 */
  justify-content: center;
  gap: 10px;
}

@media (min-width: 768px) {
  .flex {
    flex-wrap: nowrap; /* 큰 화면에서는 한 줄로 정렬 */
  }
}

</style>
