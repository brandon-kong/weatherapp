<template>
    <main class="login-container">
        <section class="login-widget">
            <div>
                <header class="login-title">
                    <h1 class="welcome-back">Welcome back</h1>
                </header>
            </div>
            <div class="form-section">
                <div class="form-field">
                    <form class="form-login">
                        <input class="input-box email-field input-field" type="text" autocomplete="off" placeholder="Email address" />
                        <input class="input-box password-field input-field" type="password" autocomplete="off" placeholder="Password" />
                        <button class="submit-field input-field" type="submit">Continue</button>
                    </form>
                </div>
                <div class="sign-up-redirect">
                    <p>Don't have an account? <router-link to="/">Sign up</router-link></p>
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
}

.login-widget {
    grid-area: center;
    background-color: white;
    width: var(--login-widget-width);
    border-radius: var(--spacing-2);
}

.login-title {
    padding: var(--spacing-5) var(--spacing-5) var(--spacing-3);
    text-align: center;
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

.input-box {
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

.floating-label {
  position: absolute;
  pointer-events: none;
  left: 20px;
  top: 18px;
  transition: 0.2s ease all;
}

.input-field:focus{
    border: 1px solid var(--primary-color);
}

.input-field:focus ~ .floating-label,
.input-field:not(:focus):valid ~ .floating-label{
  top: 0px;
  left: 10px;
  font-size: 14px;
  opacity: 1;
  color: var(--primary-color);
}

.email-field {
    margin-bottom: var(--spacing-1);
}

.password-field {
    margin-bottom: var(--spacing-3);
}

.submit-field {
    background-color: var(--primary-color);
    color: white;
    transition: background-color .2s ease-in-out;
}

.submit-field:hover {
    background-color: var(--primary-color-hover);
}

.sign-up-redirect {
    margin: var(--spacing-3) 0 0 0;
}

.or-separator {
    display: flex;
    justify-content: space-around;
    margin: var(--spacing-3) 0 0 0;
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
    margin: var(--spacing-3) 0 0 0;
    display: flex;
    flex-direction: column;
    gap: var(--spacing-1);
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

</style>

<script>

export default {
    name: 'HomeView',

    data() {
        return {
            email: '',
            password: ''
        }
    },
}

</script>
