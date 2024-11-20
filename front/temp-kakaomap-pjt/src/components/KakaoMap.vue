<template>
  <div ref="mapContainer" style="width: 100%; height:70vh">
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
const { VITE_KAKAO_JS_KEY } = import.meta.env

const mapContainer = ref(null)

onMounted(() => {
  loadKakaoMap(mapContainer.value)
})

const loadKakaoMap = (container) => {
  const script = document.createElement('script')
  script.src = `https://dqpi.kakao.com/v2/maps/sdk.js?appkey=${VITE_KAKAO_JS_KEY}&autoload=false`
  document.head.appendChild(script)

  script.onload = () => {
    window.kakao.maps.load(() => {
      const options = {
        center: new window.kakao.maps.LatLng(33.450701, 126.570667),
        level: 3,
        maxLevel: 5,
      }
      const mapInstance = new window.kakao.maps.Map(container, options)
    })
  }
}

</script>

<style scoped>

</style>