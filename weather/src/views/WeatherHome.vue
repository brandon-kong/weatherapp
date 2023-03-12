<template>
    <div class="weather-container">
       welcome home bro
    </div>
</template>

<style>

.weather-container {
    display: flex;
    min-height: 100vh;
    width: 100%;
    height: fit-content;
    box-sizing: border-box;
    padding: var(--outer-padding);

    text-align: center;
    grid-column-gap: calc(var(--outer-padding) * 2);
    flex-grow: 1;
}


</style>
<script>

export default {
    name: 'WeatherView',
}

</script>
