import { defineStore } from 'pinia'
import { useLocalStorage } from '@vueuse/core'
import axios from 'axios'

import router from '@/router'

export const useAuthStore = defineStore('auth',{
    state: () => ({
        session: useLocalStorage('session', {
            token: null,
            isAuthenticated: false,
        }),
    }),

    getters: {
        isAuthenticated () {
            return this.session.isAuthenticated
        }
    },

    actions: {
        async login({email, password}) {
            if (this.session.token != null) {
                console.log('you are already logged in!')
                return
            }
            // Login user
            axios.post('http://127.0.0.1:8000/api/login', {
                email: email,
                password: password
            })
            
            .then(response => {
                const data = response.data
                this.session.token = data.token
                this.session.isAuthenticated = true

                router.push('/')
            })
            .catch(error => {
                console.log(error)
            })
        },

        async register({email, password}) {
            if (this.session.token != null) {
                console.log('you are already logged in!')
                return
            }
            // Register user
            axios.post('http://127.0.0.1:8000/api/users', {
                email: email,
                password: password
            })
            .then(response => {
                const data = response.data
                this.session.token = data.token
                this.session.isAuthenticated = true

                router.push('/')
            })
            .catch(error => {
                console.log(error)
            })
        },

        logout () {
            // Remove token from local storage
            this.session.token = null
            this.session.isAuthenticated = false
            
            // Redirect to login page
            router.push('/login')
        }
    }
})