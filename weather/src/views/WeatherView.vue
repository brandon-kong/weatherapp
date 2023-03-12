<template>
    <div v-if="data" class="weather-container">
        <h1 v-if="data" class="location-title">{{ location && location.properties && location.properties.formatted }}</h1>
        <div class="currentTempData">
            <h1 class="currentTemp">{{ data.currentConditions.temp }}°</h1>
            <p class="tempDescription">{{ data.days[0].description }}</p>
            <div class="hi-lo">
                <span class="hi range-ind">H: {{ data.days[0].tempmax }}°</span>
                <span class="lo range-ind">L: {{ data.days[0].tempmin }}°</span>
            </div>
            <div class="addToList">
                <button class="addToListButton" @click="addToList(location)">Add to List</button>
            </div>
        </div>
        <div class="iframe-container">
            <iframe
                width="600"
                height="450"
                style="border:0"
                loading="lazy"
                allowfullscreen
                referrerpolicy="no-referrer-when-downgrade"
                :src="`https://www.google.com/maps/embed/v1/place?key=AIzaSyBNoZzwnXN9RC9KfjtX0dDTdh7u1RBu0Fo
                    &q=${location && location.properties.formatted}`">
            </iframe>
            <div v-if="location" class="">
                <p>Latitude: {{ location.geometry.coordinates[1] }}</p>
                <p>Longitude: {{ location.geometry.coordinates[0] }}</p>
            </div>
        </div>
        {{ data.currentConditions }}
        <hr />
        {{ data.days[0] }}
        {{ error }}
    </div>
</template>

<style>

.weather-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    width: 100%;
    height: fit-content;
    box-sizing: border-box;
    padding: var(--outer-padding);
    

    text-align: center;
    grid-column-gap: calc(var(--outer-padding) * 2);
    flex-grow: 1;
}

.location-title {
    font-size: 2rem;
    font-weight: 700;
    margin: 0;
    padding: 0;
    margin-bottom: 30px;
}

.currentTempData {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 30px;
    background-color: #f1f1f1;
    border-radius: 10px;
    padding: 20px 0;
}

.currentTemp {
    font-size: 6rem;
    font-weight: 200;
    margin: 0;
    padding: 0;
}

.tempDescription {
    font-size: 1.3rem;
    font-weight: 200;
    color: #777;
    margin: 0;
    padding: 0;
}

.hi-lo {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    margin-top: 10px;
    gap: 20px;
}

.range-ind {
    font-size: 1.3rem;
    font-weight: 200;
    margin: 0;
    padding: 0;
}

.addToList {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    margin-top: 10px;
    gap: 20px;
}
.addToListButton {
    background-color: #fff;
    border: none;
    border-radius: 10px;
    padding: 5px 30px;
    font-size: 1.3rem;
    font-weight: 200;
    margin: 0;
    margin-top: 10px;
    cursor: pointer;
}

.iframe-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 20px;
}

</style>

<script>

import { GetWeatherQuery } from '@/libraries/weather'
import { reverseGeocode } from '@/libraries/geocoder'

import { useAuthStore } from '@/stores/authStore'

// Components
//Library Components

export default {
    name: 'WeatherView',

    data() {
        return {
            data: null,
            location: null,
            error: null,

            currentTemp: 0,
            maxTemp: 0
        }
    },

    components: {
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
            reverseGeocode({ lon, lat }, this.reverseGeocodeCallback)
            GetWeatherQuery({ lon, lat }, this.weatherCallback)
        },

        weatherCallback (data) {
           this.data = data.data
            this.currentTemp = this.data.currentConditions.temp
            this.maxTemp = this.data.days[0].maxTemp
        },

        reverseGeocodeCallback (data) {
            this.location = data
        },

        addToList (request) {
            const authStore = useAuthStore()
            if (authStore.session.isAuthenticated === false) {
                this.$router.push('/login')
            } else {
                console.log(request)
            }
        }
    }
}

</script>
