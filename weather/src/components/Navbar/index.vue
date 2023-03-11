<template>
    <div class="univ-nav">
        <nav class="nav-container">
            <div class="logo">
                <router-link to="/">
                    <img draggable="false" class="logo-img" src="@/assets/imgs/logo-64.png" alt="logo">
                </router-link>
            </div>
            <Searchbar />
            <button v-show="isAuthenticated" @click="logout">Logout</button>
            <button v-show="!isAuthenticated">Log in</button>
        </nav>
    </div>
</template>

<style scoped>

.nav-container {
    position: absolute;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
    height: var(--navbar-height);
    background-color: #fff;
    border-bottom: 1px solid #ccc;
}

.logo {
    display: flex;
    align-items: center;
    height: 100%;
}

.logo-img {
    height: 40px;
}
</style>

<script>

import Searchbar from '@/components/Searchbar'
import { useAuthStore } from '@/stores/authStore'

export default {
    name: 'NavbarComponent',
    data() {
        return {
            isMenuOpen: false
        }
    },

    components: {
        Searchbar
    },
    methods: {
        logout() {
            const authStore = useAuthStore()
            authStore.logout()
        }
    },

    computed: {
        isAuthenticated () {
            const authStore = useAuthStore()
            return authStore.isAuthenticated
        }
    }
}

</script>