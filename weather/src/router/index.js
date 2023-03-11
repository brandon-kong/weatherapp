import { createRouter, createWebHistory} from 'vue-router'

// View components
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import TOS from '@/views/TOS.vue'
import NotFound from '@/views/404.vue'

// Stores
import { useAuthStore } from '@/stores/authStore'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            requiresAuth: true
        }
    },

    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: {
            requiresAuth: false,
            title: 'Welcome back'
        }
    },

    {
        path: '/register',
        name: 'Register',
        component: Register,
        meta: {
            requiresAuth: false
        }
    },

    {
        path: '/terms-and-conditions',
        name: 'TermsAndConditions',
        component: TOS,
        meta: {
            requiresAuth: false
        }
    },

    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: NotFound,
        meta: {
            requiresAuth: false
        }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach(async (to) => {
    const authStore = useAuthStore()
    if (to.meta.requiresAuth) {
        if (authStore.isAuthenticated) {
            return true
        }
        else {
            // redirect the user to the login page
            return { name: 'Login' }
        }
    } else {
        if (authStore.isAuthenticated) {
            // redirect the user to the home page
            if (to.name === 'Login' || to.name === 'Register') {
                return { name: 'Home' }
            }
        }
    }
})

export default router