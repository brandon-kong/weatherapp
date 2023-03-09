<template>
    <main class="login-container">
        <section class="login-widget">
            <div>
                <header class="login-title">
                    <h1 class="welcome-back">Create account</h1>
                </header>
            </div>
            <div class="form-section">
                <div class="form-field">
                    <form @submit.stop.prevent="register" novalidate class="form-login">
                        <InputBox @inputChange="updateEmail" type="text" class="email-field" placeholder="Email address" autocomplete="off" />
                        <InputBox @inputChange="updatePassword" type="password" class="password-field" placeholder="Password" autocomplete="off" />
                        <button class="submit-field input-field" type="submit">Continue</button>
                    </form>
                </div>
                <div class="sign-up-redirect">
                    <p>Already have an account? <Link to="/login">Sign in</Link></p>
                </div>
                <div class="or-separator">
                    <p>or</p>
                </div>
                <div class="social-login">
                    <button class="oauth-box google-field input-field" type="submit">
                        <span class="brand-img google-img"></span>
                        <span>Continue with Google</span>
                    </button>
                    <button class="oauth-box microsoft-field input-field" type="submit">
                        <span class="brand-img microsoft-img"></span>
                        <span>Continue with Microsoft Account</span>
                    </button>
                </div>
                <p class="tas-disclaimer">By creating an account, you are agreeing to our<Link to="/terms-and-conditions">terms and conditions</Link></p>
            </div>
        </section>
    </main>
</template>

<style scoped>

.login-container {
    display: flex;
    min-height: 100vh;
    width: 100%;
    height: fit-content;
    box-sizing: border-box;
    padding: var(--outer-padding);

    text-align: center;
    align-items: center;
    justify-content: center;
    grid-column-gap: calc(var(--outer-padding) * 2);
    flex-grow: 1;
}

.login-widget {
    display: flex;
    flex-direction: column;
    justify-content: center;
    grid-area: center;
    background-color: white;
    width: var(--login-widget-width);
    border-radius: var(--spacing-2);
    overflow: hidden;
}

.login-title {
    padding: var(--spacing-1) var(--spacing-5) var(--spacing-3);
    text-align: center;
    flex-shrink: 0;
}

.welcome-back {
    font-size: var(--title-font-size);
    margin: var(--header-title-spacing,var(--spacing-3)) 0 var(--spacing-2);
}

.form-section {
    padding: 0 var(--spacing-5) var(--spacing-5);
}
.form-login {
    display: flex;
    flex-direction: column;
}

.input-field {
    height: var(--input-height);
    border-radius: var(--input-border-radius);
    padding: var(--input-padding);
    font-size: var(--input-font-size);
    transition: border .2s ease-in-out;
}

.email-field {
    margin-bottom: var(--spacing-2);
}

.password-field {
    margin-bottom: var(--spacing-3);
}

.submit-field {
    background-color: var(--primary-color);
    color: white;
    outline: 0px solid;
    transition: background-color .2s ease-in-out, outline .1s ease-in-out;
}

.submit-field:hover {
    background-color: var(--primary-color-hover);
}

.submit-field:focus {
    outline: 3px solid var(--primary-color-light);
}

.sign-up-redirect {
    margin: var(--spacing-3) 0 0 0;
}

.or-separator {
    display: flex;
    justify-content: space-around;
    margin: var(--spacing-3) 0 var(--spacing-3) 0;
}

.or-separator p {
    flex: .2 0 auto;
    text-transform: uppercase;
    font-size: .8rem;
}
.or-separator::before {
    content: '';
    flex: 1;
    border-bottom: 1px solid #ccc;
    height: .5rem;
}

.or-separator::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #ccc;
    height: .5rem;
}

.social-login {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-1);
    margin-bottom: var(--spacing-3);
}

.oauth-box {
    display: flex;
    align-items: center;
    background-color: white;
    border: 1px solid #ccc;
    color: var(--font-default-color);
    transition: background-color .2s ease-in-out;
}

.oauth-box:hover {
    background-color: #f1f1f1;
}

.oauth-box:focus {
    background-color: var(--primary-color-background);
}

.brand-img {
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    width: 1.5rem;
    height: 1.5rem;
    margin-right: var(--spacing-2);
}

.google-img {
    background-image: url('~@/assets/imgs/google.svg');
}

.microsoft-img {
    background-image: url('~@/assets/imgs/microsoft.svg');
}

@media screen and (max-width: 600px) {
    .login-container {
        padding: var(--outer-padding-minimized);
    }

    .login-widget {
        width: 100%;
    }
}

</style>

<script>

import { useAuthStore } from '@/stores/authStore'

import Link from '@/components/Link'
import InputBox from '@/components/Form/InputBox'

export default {
    name: 'RegisterView',

    data() {
        return {
            email: '',
            password: ''
        }
    },

    components: {
        Link,
        InputBox
    },

    methods: {
        updateEmail(value) {
            this.email = value
        },

        updatePassword(value) {
            this.password = value
        },

        async register() {
            const authStore = useAuthStore()
            await authStore.register({
                email: this.email, 
                password:this.password
            })
        }
    }
}

</script>
