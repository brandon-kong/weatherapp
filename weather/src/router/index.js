import { createRouter, createWebHistory} from 'vue-router'

// View components
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },

    {
        path: '/login',
        name: 'Login',
        component: Login
    },

    {
        path: '/register',
        name: 'Register',
        component: Register
    },

    {
        path: '/terms-and-conditions',
        name: 'TermsAndConditions',
        component: () => import('@/views/TOS.vue')
    },

    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: () => import('@/views/404.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router