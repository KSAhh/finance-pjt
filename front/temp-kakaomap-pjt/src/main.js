import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useKakao } from 'vue3-kakao-maps/@utils';

import App from './App.vue'
import router from './router'

// 카카오API 사용 및 라이브러리 추가
useKakao(import.meta.env.VITE_KAKAO_JS_KEY, ['clusterer', 'services', 'drawing']); 

const app = createApp(App)
app.use(createPinia())
app.use(router)

app.mount('#app')
