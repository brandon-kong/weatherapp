<template>
    <nav class="nav-container">
        <div class="logo">
            <router-link to="/">
                <img class="" src="@/assets/imgs/logo-64.png" alt="logo">
            </router-link>
        </div>
    </nav>
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
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logo {
    display: flex;
    align-items: center;
    height: 100%;
}
</style>

<script>

export default {
    name: 'NavbarComponent',
    data() {
        return {
            isMenuOpen: false
        }
    },
    methods: {
        toggleMenu() {
            this.isMenuOpen = !this.isMenuOpen
        }
    }
}

</script>