import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth',{
    state: () => ({
        token: null,
        user: null,
        isAuthenticated: false
    }),

    actions: {
        async register({email, password}) {
            if (this.isAuthenticated) {
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
                this.token = data.token
                this.user = data.email
                this.isAuthenticated = true

                // Set token in local storage
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
})