<template>
    <router-link class="a-hovered" :to="to">
        <slot></slot>
    </router-link>
</template>

<style scoped>
.a-hovered {
    color: var(--primary-color);
    border-radius: 3px;
    padding: var(--a-hovered-padding);
    transition: color .2s ease-in-out;
}
.a-hovered:focus {
    background-color: var(--primary-color-background);
}

</style>
<script>

export default {
    name: 'LinkComponent',
    props: {
        to: {
            type: String,
            required: true
        }
    }
}
</script>