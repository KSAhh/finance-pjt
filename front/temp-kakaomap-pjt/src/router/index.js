import KakaomapView from '@/views/KakaomapView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: KakaomapView,
    },
  ],
})

export default router
