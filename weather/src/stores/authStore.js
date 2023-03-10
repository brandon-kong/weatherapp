import { defineStore } from 'pinia'
import { useLocalStorage } from '@vueuse/core'
import axios from 'axios'

export const useAuthStore = defineStore('auth',{
    state: () => ({
        session: useLocalStorage('session', {
            token: null,
            isAuthenticated: false,
        }),
    }),

    actions: {
        async getSession() {
            // Check if token is set in local storage
            // Check if token is valid
            axios.get('http://127.0.0.1:8000/api/session')
            .then(response => {
                const data = response.data
                console.log(data)
            })
            .catch(error => {
                console.log(error)
            })
        },

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
                console.log(data.token)
                this.session.token = data.token
                this.session.isAuthenticated = true

                // Set token in local storage
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
                console.log(data.token)
                this.session.token = data.token
                this.session.isAuthenticated = true

                // Set token in local storage
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
})