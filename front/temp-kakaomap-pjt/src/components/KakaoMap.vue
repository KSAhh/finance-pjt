<template>
  <!-- 지도 지정(mapContainer참조하여 동적으로 제어) & 크기설정 -->
  <div ref="mapContainer" style="width: 100%; height:70vh"></div>

  <!-- 검색 입력 창 -->
  <input 
      v-model="keyword" 
      type="text" 
      placeholder="검색할 지역을 입력하세요" 
      @keyup.enter="searchPlaces()"
      style="width: 300px; padding: 10px; margin-bottom: 10px;"
  />
    <button @click="searchPlaces" style="padding: 10px;">허덤바보</button>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const { VITE_KAKAO_JS_KEY } = import.meta.env;
const mapContainer = ref(null); // 지도 표시 객체


// const keyword = ref(''); // 검색어 입력 값
// const ps = ref(null); // 장소 검색 객체
// const markers = ref([]); // 마커 배열


// 컴포넌트 마운트 시 지도 로드
onMounted(() => {
  loadKakaoMap(mapContainer.value)
})

// onMounted Lifehook - 지도 생성
const loadKakaoMap = (container) => {
    const script = document.createElement('script') // script 태그 생성
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${VITE_KAKAO_JS_KEY}&autoload=false&libraries=services,clusterer,drawing` // 카카오지도 API URL
    // autoload : API가 자동으로 지도를 로드할 지 여부
    // libraries : 카카오제공 라이브러리 사용 (services - 검색 기능)
    document.head.appendChild(script); // <head>태그에 지도 추가

    // <script> 로드된 후 (콜백함수)
    script.onload = () => {
        // 지도 출력
        window.kakao.maps.load(() => { // 지도초기화
            const options = {
                center: new window.kakao.maps.LatLng(37.503188, 127.044811), // 지도 중심 좌표 (위도, 경도) (초기값: 멀티캠퍼스)
                level: 3,                                                    // 지도 확대 정도 (작을수록 확대됨)
                maxLevel: 5,                                                 // 사용자가 최대 확대 정도 (사용할 레벨 제한)
            }
            const mapInstance = new window.kakao.maps.Map(container, options); // 지도 객체 생성 (container에 렌더링 된 후 반환)

            
            // 2. 마커 표시 (초기위치 한 곳)
            const markerPosition = new kakao.maps.LatLng(37.503188, 127.044811) // 좌표 객체 생성 (초기값 지정)
            const marker = new kakao.maps.Marker({ position: markerPosition, }) // 마커 객체 생성 (초기값 지정)
            marker.setMap(mapInstance)                                          // 지도객체(mapInstance)에 마커 표시 
            // 마커 클릭 시 인포윈도우 표시
            kakao.maps.event.addListener(marker, 'click', function () {
                infoWindow.setContent(`<div style="padding:5px;font-size:12px;">현재 위치</div>`)
                infoWindow.open(mapInstance, marker) // 현재 마커에 인포윈도우 열기
            })
                 

            // 3. 마커 표시 (은행위치 여러 곳)
            const markers = []                                      // 마커 배열
            const ps = new kakao.maps.services.Places(mapInstance)  // 장소 검색 객체 생성
            const searchBanksInBounds = () => { ps.categorySearch('BK9', placesSearchCB, { useMapBounds: true })} // 카테고리기반 검색 완료 후, placeSearchCB 함수 호출 / useMapBounds: 현재 지도 범위를 기준으로 검색을 제한
            
            // - 은행 카테고리 검색 결과 (콜백 함수)
            const placesSearchCB = (data, status, pagination) => {
                if (status === kakao.maps.services.Status.OK) {
                  removeAllMarkers() // 기존 마커 제거 (중복 방지)
                  for (let i = 0; i < data.length; i++) {
                    displayMarker(data[i]) // 새로운 검색 결과 표시
                  }
                } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
                  alert('검색 결과가 없습니다.')
                } else {
                  alert('검색 중 오류가 발생했습니다.')
                }
            }

            // - 기존 마커 삭제
            function removeAllMarkers() {
                for (let i = 0; i < markers.length; i++) {
                    markers[i].setMap(null) // 지도에서 마커 제거
                }
                markers.length = 0 // 배열 초기화
            }

            

            const infoWindow = new kakao.maps.InfoWindow({ zIndex: 1 }); // 전역 인포윈도우 객체 생성

            // - 지도에 마커 표시
            function displayMarker(place) {
              const marker = new kakao.maps.Marker({
                map: mapInstance, // 지도 객체
                position: new kakao.maps.LatLng(place.y, place.x), // 장소의 위도, 경도를 기반으로 마커 생성
              })
              markers.push(marker); // 마커를 배열에 저장

              // 마커 클릭 시 인포윈도우 표시
              kakao.maps.event.addListener(marker, 'click', function () {
                infoWindow.setContent(
                  `<div style="padding:5px;font-size:12px;">${place.place_name}</div>` // 장소명 표시
                );
                infoWindow.open(mapInstance, marker); // 현재 마커에 인포윈도우 열기
              });
            }
            
            // 4. 장소 검색 기능
            // - 키워드 검색 함수
            const searchPlaces = () => {
                if (!keyword.value.trim()) {
                    alert('검색어를 입력하세요.')
                    return
                }
                ps.keywordSearch(keyword.value, placesSearchCB) // 키워드 검색 실행
            }
            searchBanksInBounds(); // 초기 은행 검색
        });
    };
};


</script>

<style scoped>
/* 부모 컨테이너 스타일 */
div {
  display: flex;
  flex-direction: column;
  align-items: center; /* 가로 정렬 */
  justify-content: center; /* 세로 정렬 */
  height: 100vh; /* 화면 높이 전체 */
  background-color: #f9f9f9; /* 배경색 */
}

/* 공통 스타일 */
input,
button {
  font-family: Arial, sans-serif;
  font-size: 16px;
  border-radius: 5px;
  outline: none;
  transition: all 0.3s ease;
}

/* 입력창 스타일 */
input[type="text"] {
  width: 300px;
  padding: 10px 15px;
  border: 1px solid #ccc;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  margin-bottom: 15px;
}

input[type="text"]:focus {
  border-color: #4caf50;
  box-shadow: 0px 2px 5px rgba(76, 175, 80, 0.5);
}

/* 버튼 스타일 */
button {
  padding: 10px 20px;
  border: none;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}

button:hover {
  background-color: #45a049;
}

button:active {
  transform: scale(0.98);
  background-color: #3e8e41;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
