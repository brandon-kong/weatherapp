<template>
    <div class="weather-container">
        {{ $route.params.lon }} {{ $route.params.lat }}
        {{ data }}
        {{ error }}
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

import { GetWeatherQuery } from '@/libraries/weather'

export default {
    name: 'WeatherView',

    data() {
        return {
            data: {},
            error: null
        }
    },

    mounted() {
        this.getWeather()
    },

    watch: {
        '$route.params.lat': function () {
            this.getWeather()
        },

        '$route.params.lon': function () {
            this.getWeather()
        }
    },

    methods: {
        getWeather() {
            const { lon, lat } = this.$route.params
            GetWeatherQuery({ lon, lat }, this.weatherCallback)
        },

        weatherCallback (data) {
           this.data = data
        }
    }
}

</script>
