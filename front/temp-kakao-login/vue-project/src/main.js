import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const KAKAO_LOGIN_JS_KEY = import.meta.env.VITE_KAKAOLOGIN_JS_KEY
Kakao.init(KAKAO_LOGIN_JS_KEY);
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.mount('#app')
