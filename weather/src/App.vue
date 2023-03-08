<template>
  <router-view>
  </router-view>
</template>

<script>

export default {
    name: 'App',
    components: {
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
    --dark-gray: #2d333a;
    --spacing: 8px;
    --outer-padding: calc(var(--spacing) * 10);
    --login-widget-width: calc(var(--spacing) * 50);
    --spacing-1: var(--spacing);
    --spacing-2: calc(var(--spacing) * 2);
    --spacing-3: calc(var(--spacing) * 3);
    --spacing-4: calc(var(--spacing) * 4);
    --spacing-5: calc(var(--spacing) * 5);
    --font-default-color: var(--dark-gray);
    --title-font-size: 1.7rem;
    --input-height: 54px;
    --input-border-radius: 3px;
    --input-padding: 0 16px;
    --input-font-size: 1rem;

    --box-shadow: 0 12px 40px rgba(0,0,0,0.12)
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
}

a {
    text-decoration: none;
    color: var(--primary-color);
}

a:hover {
    text-decoration: underline;
}

</style>
