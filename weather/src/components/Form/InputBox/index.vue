<template>
    <div class="field-holder">
        <input 
            :type="type"
            :disabled="disabled"
            :name="name"
            :autocomplete="autocomplete"

            @input="onInput"
            class="input-box input-field"
            required
        >
        <label :for="name" class="input-label noselect">{{ placeholder }}</label>
    </div>
</template>

<style scoped>

.field-holder {
    position: relative;
}

.input-box {
    width: 100%;
    background-color: white;
    border: 1px solid #ccc;
}

.input-field {
    height: var(--input-height);
    border-radius: var(--input-border-radius);
    padding: var(--input-padding);
    font-size: var(--input-font-size);
    transition: border .2s ease-in-out;
}

.input-box:focus {
    outline: none;
    border-color: var(--primary-color);
}

.input-box:focus ~ .input-label {
    color: var(--primary-color);
}

.input-box:focus ~ .input-label, .input-box:not(:focus):valid ~ .input-label {
    outline: none;
    pointer-events: none;
    top: 0;
    left: 10px;
    font-size: .8rem;
}

.input-label {
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    left: 15px;
    font-size: 1rem;
    color: #999999;
    background-color: white;
    padding: 0 5px;
    transition: all 0.15s ease;
}

</style>

<script>

export default {
    name: 'InputBoxComponent',

    props: {
        type: {
            type: String,
            default: 'text'
        },
        placeholder: {
            type: String,
            default: ''
        },
        disabled: {
            type: Boolean,
            default: false
        },
        required: {
            type: Boolean,
            default: false
        },
        name: {
            type: String,
            default: ''
        },
        autocomplete: {
            type: String,
            default: ''
        },
        value: {
            type: String,
            default: '',
        }
    },

    methods: {
        onInput(event) {
            this.$emit('inputChange', event.target.value);
        }
    }
}

</script>