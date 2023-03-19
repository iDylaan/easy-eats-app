<template>
    <div class="form-login__container">

        <div class="hoja1__container">
            <img src="@/assets/imgs/Hoja1.png" alt="Hoja flotante" class="floating-image1">
        </div>

        <div class="card">
            <form novalidate>
                <div v-if="error" class="alert-error">{{ error }}</div>
                <div v-if="message" class="alert-success">{{ message }}</div>
                <div :class="emailClasses">
                    <svg class="input-icon" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M207.8 20.73c-93.45 18.32-168.7 93.66-187 187.1c-27.64 140.9 68.65 266.2 199.1 285.1c19.01 2.888 36.17-12.26 36.17-31.49l.0001-.6631c0-15.74-11.44-28.88-26.84-31.24c-84.35-12.98-149.2-86.13-149.2-174.2c0-102.9 88.61-185.5 193.4-175.4c91.54 8.869 158.6 91.25 158.6 183.2l0 16.16c0 22.09-17.94 40.05-40 40.05s-40.01-17.96-40.01-40.05v-120.1c0-8.847-7.161-16.02-16.01-16.02l-31.98 .0036c-7.299 0-13.2 4.992-15.12 11.68c-24.85-12.15-54.24-16.38-86.06-5.106c-38.75 13.73-68.12 48.91-73.72 89.64c-9.483 69.01 43.81 128 110.9 128c26.44 0 50.43-9.544 69.59-24.88c24 31.3 65.23 48.69 109.4 37.49C465.2 369.3 496 324.1 495.1 277.2V256.3C495.1 107.1 361.2-9.332 207.8 20.73zM239.1 304.3c-26.47 0-48-21.56-48-48.05s21.53-48.05 48-48.05s48 21.56 48 48.05S266.5 304.3 239.1 304.3z">
                        </path>
                    </svg>
                    <input v-model="email" @input="validarEmail" autocomplete="off" id="email" placeholder="Correo"
                        class="input-field" name="email" type="email" />
                </div>
                <div :class="passwordClasses">
                    <svg class="input-icon" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                        </path>
                    </svg>
                    <input v-model="password" @input="validarPassword" autocomplete="off" id="password"
                        placeholder="Contraseña" class="input-field" name="password" type="password" />
                </div>
                <button @click.prevent="submitForm" @click="login" :disabled="!formValid" class="btn" type="submit">Iniciar
                    Sesión</button>
                <a href="#" class="btn-link">¿Olvidaste tu contraseña?</a>
            </form>
            <div v-if="showSinginResponsive" class="register__message-container">
                <p>¿No tienes cuenta? <span @click="signinRedirect">regístrate en Easy Eats!</span></p>
            </div>
        </div>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';
import axios from 'axios';
import { ref, computed, onMounted, onUnmounted } from 'vue';

export default {
    setup() {
        const URL = 'https://easy-eats-back.fly.dev';
        const router = useRouter();
        let showSinginResponsive = ref(false);
        let emailCnt = 0;
        let passwordCnt = 0;
        let email = ref('');
        let password = ref('');
        let emailValid = ref(true);
        let passwordValid = ref(true);
        let formValid = ref(false);
        let error = ref('');
        let message = ref('');

        onMounted(() => {
            login().catch(error => {
                console.error(error)
            })

            window.addEventListener('change', () => handleResize);
            handleResize();
            console.log(window.innerWidth);
            console.log(handleResize());
        })
        
        onUnmounted(() => {
            window.addEventListener('resize', () => handleResize);
        })

        const handleResize  = () => showSinginResponsive.value = window.innerWidth <= 1200;

        const signinRedirect = () => router.push('/signin');

        const validateInputs = () => formValid.value = emailValid.value && passwordValid.value && emailCnt > 0 && passwordCnt > 0;

        const validarEmail = () => {
            const regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            emailValid.value = regex.test(String(email.value).toLowerCase());
            emailCnt++;
            validateInputs();
        }
        const validarPassword = () => {
            passwordValid.value = password.value.length >= 8;
            passwordCnt++;
            validateInputs();
        }

        const login = async () => {
            if (!validateInputs()) { return; }
            const ROUTE = '/login';
            error.value = '';
            message.value = '';

            try {
                let data = {
                    'email': email.value,
                    'password': password.value
                }

                const response = await axios({
                    method: 'POST',
                    url: URL + ROUTE,
                    data: data
                });

                if (response.data.status !== 'OK') {
                    error.value = "Error inesperado en la petición";
                }

                if (response.data.status === 401) {
                    error.value = 'Correo o contraseña incorrectos';
                }

                if (!response.data.status) {
                    error.value = '';
                    message.value = '! Bienvenido ' + response.data.username + ' !';
                    localStorage.setItem("token", response.data.token);
                    localStorage.setItem("username", response.data.username);
                    localStorage.setItem("tagline", response.data.tagline);

                    setTimeout(() => {
                        router.push('/')
                            .catch(err => {
                                console.error('Error al redirigir a la ruta', err);
                            });
                    }, 900);
                }

            } catch (error) {
                console.log(error);
            }
        }

        return {
            email,
            password,
            validateInputs,
            validarEmail,
            validarPassword,
            login,
            error,
            message, 
            signinRedirect,
            showSinginResponsive: computed(() => showSinginResponsive.value),
            emailValid: computed(() => emailValid.value),
            passwordValid: computed(() => passwordValid.value),
            formValid: computed(() => formValid.value),
        };
    },
    computed: {
        emailClasses() {
            return {
                'input-invalid': !this.emailValid,
                'field': true
            }
        },
        passwordClasses() {
            return {
                'input-invalid': !this.passwordValid,
                'field': true
            }
        },
        formValid() {
            return this.formValid;
        }
    },
};
</script>
