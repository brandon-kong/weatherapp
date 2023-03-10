<template>
    <button @click="loginWithGoogle" class="oauth-box google-field input-field" type="submit">
        <span class="brand-img microsoft-img"></span>
        <span>Continue with Microsoft</span>
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
    transition: background-color .2s ease-in-out;
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

.microsoft-img {
    background-image: url('~@/assets/imgs/microsoft.svg');
}

</style>
<script>

import { googleAuthCodeLogin } from 'vue3-google-login'

export default {
    name: 'GoogleLogin',
    methods: {
        loginWithGoogle() {
            googleAuthCodeLogin().then((response) => {
                console.log("Handle the response", response)
            })
        }
    }
}
</script>