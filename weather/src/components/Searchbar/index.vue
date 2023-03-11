<template>
    <div class="">
        <form class="searchbar-container" v-on:submit.stop.prevent="forceSearchResult">
            <input class="searchbar autocomplete geoapify-autocomplete-input" type="text" placeholder="Search Locations"
            v-model="search" @input="searchLocations"
            @focus="focusIn"
            @keydown.down="arrowDown"
            @keydown.up="arrowUp"
            @keydown.enter="onEnter"
            name="search"
            autocomplete="off"
            />
        </form>
        <div class="search-container">
            <ul class="search-list">
                <li v-for="(result, i) in query" :key="i"
                    :class="{ 'is-active': i === arrowIndex }"
                    class="search-suggestion"
                    @click="setResult(result)"
                    @mouseover="setArrowIndex(i)"
                    >
                    {{ result }}
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>

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

    box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
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
    height: 2rem;
    width: 100%;
    padding: 1.4rem 2rem;

    display: flex;
    align-items: center;
    transition: all 0.2s ease;
}

.search-suggestion:hover {
    background-color: #eee;
    cursor: pointer;
}

.is-active {
    background-color: var(--primary-color-background);
}
</style>
<script>

export default {
    name: "SearchbarComponent",
    data() {
        return {
            search: "",
            query: [
                'hello', 'world', 'this', 'is', 'a', 'test'
            ],
            arrowIndex: 0,
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
    }
}

</script>