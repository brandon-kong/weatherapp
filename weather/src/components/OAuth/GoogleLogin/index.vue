<template>
    <button @click="loginWithGoogle" class="oauth-box google-field input-field" type="submit">
        <span class="brand-img google-img"></span>
        <span>Continue with Google</span>
    </button>
</template>

<style scoped>

.oauth-box {
    display: flex;
    align-items: center;
    background-color: white;
    border: 1px solid #ccc;
    color: var(--font-default-color);
    width: 100%;
    transition: all .2s ease-in-out;
}

.oauth-box:hover {
    background-color: #f1f1f1;
}

.oauth-box:focus {
    background-color: var(--primary-color-background);
    border-color: var(--primary-color);
}

.brand-img {
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    width: 1.5rem;
    height: 1.5rem;
    margin-right: var(--spacing-2);
}

.google-img {
    background-image: url('~@/assets/imgs/google.svg');
}

</style>

<script>

import { googleAuthCodeLogin } from 'vue3-google-login'
import axios from 'axios'

export default {
    name: 'GoogleLogin',
    methods: {
        loginWithGoogle() {
            googleAuthCodeLogin().then((response) => {
                axios.post('http://localhost:8000/api/google-auth', {
                    code: response.code
                }).then((response) => {
                    console.log(response)
                })
                .catch((error) => {
                    console.log(error)
                })
            })
        }
    }
}   
</script>