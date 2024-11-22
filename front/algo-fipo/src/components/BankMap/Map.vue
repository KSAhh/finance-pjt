<template>
  <h1>주변 은행 찾기<hr></h1>
<!-- 지도 컨테이너 -->
 <div id="page-container">
   <div ref="mapContainer" class="map-container"></div>
   <!-- 검색 입력 및 결과 -->
   
   <div class="search-list">
    <div class="search-container">
     <input
     v-model="keyword"
     type="text"
     placeholder="검색할 지역을 입력하세요"
     @keyup.enter="searchPlaces"
     />
     <button @click="searchPlaces">검색</button>
    </div>
    <div class="alert-content">{{ alertContent }}</div>
  </div>
 </div>


  
</template>
  
  <script setup>
  import { ref, onMounted, nextTick } from "vue";
  
  const { VITE_KAKAO_JS_KEY } = import.meta.env;
  const mapContainer = ref(null); // 지도 DOM 요소
  const keyword = ref(""); // 검색어
  let mapInstance = null; // 지도 객체
  let ps = null; // 장소 검색 객체
  const markers = []; // 마커 배열
  const alertContent = ref("")

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
  
  const displayMarker = (place) => {
    const marker = new kakao.maps.Marker({
      map: mapInstance,
      position: new kakao.maps.LatLng(place.y, place.x),
    });
    markers.push(marker);

    const infoWindow = new kakao.maps.InfoWindow({
      content: `
        <p style="width: 100%; padding:5px 25px 5px 5px; font-size:12px; white-space: nowrap; display:inline-block; ">
          ${place.place_name}
        </p>
      `,
      zIndex: 1,
      removable : true
    });

    kakao.maps.event.addListener(marker, "click", () => {
      infoWindow.open(mapInstance, marker);
    });

    kakao.maps.event.addListener(infoWindow, "click", () => {
      infoWindow.close()
    })
  };


  // 은행 검색 (마커표시)
  const searchBanksInBounds = () => {
    if (!ps) return;
  
    ps.categorySearch(
      "BK9",
      (data, status, pagination) => {
        if (status === kakao.maps.services.Status.OK) {
          removeAllMarkers();
  
          const bounds = mapInstance.getBounds();
          data.forEach((place) => {
            const position = new kakao.maps.LatLng(place.y, place.x);
            displayMarker(place);
          });

        // } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        //   alert("현재 위치에 은행이 없습니다.");
        } else {
          console.log(status)
          // alert("은행 검색 중 오류가 발생했습니다.");
        }
      },
      { useMapBounds: true }
    );
  };
  
  // 키워드 검색
  const searchPlaces = () => {
    if (!keyword.value.trim()) {
      alertContent.value = ""
      return;
    }
  
    ps.keywordSearch(keyword.value, placesSearchCB);
  }

  const placesSearchCB = (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
        displayPlaces(data) // 검색 목록, 마커 표시
        alertContent.value = `"${keyword.value}" 에 대한 은행 검색 결과 총 ${data.length}건`
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alertContent.value = `"${keyword.value}" 에 대한 은행 검색 결과 총 0건`
      } else {
        alert("검색 중 오류가 발생했습니다.");
      }
  }


const displayPlaces = (places) => {
    const firstResult = places[0];
    const center = new kakao.maps.LatLng(firstResult.y, firstResult.x);
    mapInstance.setCenter(center);
    searchBanksInBounds();
  }

  
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
  
  // 컴포넌트 마운트 시 지도 초기화
  onMounted(() => {
    initializeMap();
  });
  </script>
  
  <style scoped>

  h1 {
    margin: 20px auto;
    max-width: 1200px;
    font-size: 2rem;
  }

  #page-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    max-width: 1200px; /* 전체 영역 크기 확대 */
    margin: auto;
    gap: 20px;
  }


  .map-container {
    flex: 3; /* 지도 영역을 더 크게 설정 */
    height: 70vh;
    border: 1px solid #ccc;
    position: relative;
    margin-bottom: 100px;
    min-width: 700px; /* 최소 너비 설정 */
  }

  .search-list {
    display: flex;
    flex-direction: column;
  }

  .search-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2px;
  }

  .search-container input[type="text"] {
    width: 300px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px 0 0 5px; 
  }
  input:focus{
    outline: none;
  }
  .search-container button {
    padding: 10px 20px;
    background-color: #a1d0ec;
    color: white;
    border: none;
    border-radius: 0 5px 5px 0;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .search-container button:focus {
    outline: none;
  }

  .search-container button:hover {
    background-color: #3174f2;
  }

  .alert-content{
    margin-top: 10px;
    text-align: center;
  }
</style>
  