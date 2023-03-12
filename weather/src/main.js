import { createApp } from 'vue'
import App from './App.vue'

import { createPinia } from 'pinia'
import vue3GoogleLogin from 'vue3-google-login'
import veProgress from 'vue-ellipse-progress'

import router from '@/router'

const vueApp = createApp(App)

vueApp.use(veProgress)
vueApp.use(router)
vueApp.use(createPinia())
vueApp.use(vue3GoogleLogin, {
    clientId: '396604274247-2gs6m177f9ajj2km4qhjplcmrgmkkp5l.apps.googleusercontent.com'
})
vueApp.mount('#app')
