<template>
    <div class="search-universe">
        <form class="searchbar-container" v-on:submit.stop.prevent="forceSearchResult">
            <input class="searchbar autocomplete geoapify-autocomplete-input" type="text" placeholder="Search Locations"
            v-model="search"
            :class="boxClass"
            @input="onInputChange"
            @focus="focusIn"
            @keydown.down="arrowDown"
            @keydown.up="arrowUp"
            @keydown.enter="onEnter"
            name="search"
            autocomplete="off"
            />
        </form>
        <div class="search-container">
            <ul v-show="query.length > 0" class="search-list">
                <li v-for="(result, i) in query" :key="i"
                    :class="{ 'is-active': i === arrowIndex }"
                    class="search-suggestion"
                    @click="setResult(result.properties.formatted)"
                    @mouseover="setArrowIndex(i)"
                    >
                    {{ result.properties.formatted }}
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>

.search-universe {
    z-index: 10;
}
.searchbar-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.searchbar {
    width: 300px;
    height: 1rem;
    border: 1px solid #bbb;
    border-radius: 3px;
    padding: 1rem 2rem;
    font-size: 1rem;
    outline: none;
    opacity: 0.6;
    text-align: center;
    transition: all 0.3s ease;
}

.searchbar:focus {
    outline: none;
    opacity: 1;
}

.search-container {
    color: black;
    margin: auto;
    width: 300px;
    position: absolute;
    background-color: #fff;
}

.search-list {
    list-style: none;
    border: 1px solid #ccc;
    border-radius: 0px 0px 3px 3px;
    border-top: none;
}

.search-suggestion {
    height: 4rem;
    width: 100%;
    padding: 1.4rem 2rem;
    font-size: .8rem;
    
    display: flex;
    align-items: center;
    transition: all 0.1s ease;
}

.search-suggestion:hover {
    background-color: var(--primary-color);
    color: #fff;
    cursor: pointer;
}

.is-active {
    background-color: var(--primary-color);
    color: #fff;
}

.search-open {
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    border-bottom: none;
}

.search-hidden {
    border-bottom-left-radius: var(--input-border-radius);
    border-bottom-right-radius: var(--input-border-radius);
}

</style>
<script>

import { GetAutocompleteQuery } from '@/libraries/geocoder'

export default {
    name: "SearchbarComponent",
    data() {
        return {
            search: "",
            query: [],
            arrowIndex: 0,
            debounce: false,
            boxClass: "search-hidden"
        }
    },

    methods: {
        arrowUp() {
            if (this.arrowIndex == 0) {
                this.arrowIndex = this.query.length - 1;
            }
            else {
                this.arrowIndex--;
            }
        },

        arrowDown() {
            if (this.arrowIndex == this.query.length - 1) {
                this.arrowIndex = 0;
            }
            else {
                this.arrowIndex++;
            }
        },

        setArrowIndex (index) {
            this.arrowIndex = index;
        },

        setResult (result) {
            this.search = result;
            this.query = [];
        },

        onEnter () {
            this.setResult(this.query[this.arrowIndex].properties.formatted);
        },

        onInputChange () {
            GetAutocompleteQuery(this.search, this.weatherAutocompleteCallback)
        },

        focusOut () {
            console.log('hi')
            this.query = []
            this.updateBoxClass()
        },

        weatherAutocompleteCallback (data) {
            if (this.debounce == true) {
                return
            }
            this.query = data.features
            this.updateBoxClass()

            return this.data
        },

        updateBoxClass () {
            console.log(this.query.length)
            if (this.query.length > 0) {
                this.boxClass = "search-open"
            }
            else {
                this.boxClass = "search-hidden"
            }

            setTimeout(() => {
                this.debounce = false
            }, 100)
        }
    }
}

</script>