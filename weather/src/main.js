import { createApp } from 'vue'
import App from './App.vue'

import { createPinia } from 'pinia'

import router from '@/router'

const vueApp = createApp(App)
vueApp.use(router)
vueApp.use(createPinia())
vueApp.mount('#app')
