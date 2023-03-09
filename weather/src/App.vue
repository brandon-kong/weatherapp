<template>
    <Navbar />
    <div class="app-container">
        <router-view></router-view>
    </div>
</template>

<script>

import Navbar from '@/components/Navbar'
export default {
    name: 'App',
    components: {
        Navbar
    }
}

</script>

<style>

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
}

:root {
    --primary-color: #3f51b5;
    --primary-color-hover: #364499;
    --primary-color-background: #e6e9ffd7;
    --primary-color-light: #a6b3ff;
    --dark-gray: #2d333a;
    --spacing: 8px;
    --outer-padding: calc(var(--spacing) * 10);
    --outer-padding-mobile: calc(var(--spacing) * 5);
    --outer-padding-minimized: calc(var(--spacing) * 2) calc(var(--spacing) * 2);
    --login-widget-width: calc(var(--spacing) * 50);
    --spacing-1: var(--spacing);
    --spacing-2: calc(var(--spacing) * 2);
    --spacing-3: calc(var(--spacing) * 3);
    --spacing-4: calc(var(--spacing) * 4);
    --spacing-5: calc(var(--spacing) * 5);
    --a-hovered-padding: 3px 5px;
    --font-default-color: var(--dark-gray);
    --title-font-size: 1.7rem;
    --input-height: 54px;
    --input-border-radius: 3px;
    --input-padding: 0 16px;
    --input-font-size: 1rem;

    --navbar-height: 60px;

    --box-shadow: 0 12px 40px rgba(0,0,0,0.12);
    --mobile-breakpoint: 600px;
}

*, :after, :before {
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
}


html, body, p, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dt, dd, blockquote, figure, fieldset, legend, textarea, pre, iframe, hr, th, td, input, button, select, menu {
    margin: 0;
    padding: 0;
}

body {
    overflow: auto;
}

main, div {
    box-sizing: border-box;
}

input:focus {
    outline: none;
}

button {
    cursor: pointer;
    border: none;
    transition: border 0.2s ease-in-out;
}

button:focus {
    outline: none;
}

a:focus {
    outline: none;
}

a {
    text-decoration: none;
    color: var(--primary-color);
}

a:hover {
    text-decoration: none;
}

.noselect {
    -ms-user-select: none;
    user-select: none;
    -moz-user-select: none;
    -khtml-user-select: none;
    -webkit-user-select: none;
}

</style>
