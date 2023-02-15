<template>
    <div class="singin-form">

        <div class="tomato__container">
            <img src="@/assets/imgs/Tomato1.png" alt="Tomate Flotante">
        </div>

        <h1>
            Registrarse
            <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
        </h1>

        <form novalidate>

            <div v-if="error" class="alert-error">{{ error }}</div>

            <div class="inputs__container">
                <div class="input__form-container">
                    <label for="username">Nombre de Usuario <span class="required__text">*</span></label>
                    <div class="inputs_username-container">
                        <input v-model="username" autocomplete="off" @input="validateInput('username')"
                            :style="{ borderBottom: borderBottomColorUsername }" type="text" name="username"
                            id="username" placeholder="Username"> #

                        <input v-model="tagline" autocomplete="off" @input="validateInput('tagline')"
                            :style="{ borderBottom: borderBottomColorTagline }" type="text" name="tagline" id="tagline"
                            placeholder="Ej.- HGD75">
                    </div>
                </div>

                <div class="input__form-container">
                    <label for="name">Nombre</label>
                    <input v-model="name" @input="validateInput('name')"
                        :style="{ borderBottom: borderBottomColorName }" autocomplete="off" type="text" name="nombre"
                        id="nombre" placeholder="Nombre Completo">
                </div>

                <div class="input__form-container">
                    <label for="date_of_birth">Fecha de nacimiento <span class="required__text">*</span></label>
                    <input v-model="date_of_birth" @input="validateInput('date_of_birth')"
                        :style="{ borderBottom: borderBottomColorDate_of_birth }" :max="maxDate" type="date"
                        name="date_of_birth" id="date_of_birth">
                </div>

                <div class="input__form-container">
                    <label for="email">Correo electronico <span class="required__text">*</span></label>
                    <input v-model="email" @input="validateInput('email')"
                        :style="{ borderBottom: borderBottomColorEmail }" type="email" name="email" id="email"
                        autocomplete="off" placeholder="ejemplo@correo.com">
                </div>

                <div class="input__form-container">
                    <label for="password">Contraseña <span class="required__text">*</span></label>
                    <input v-model="password" @input="validateInput('password')"
                        :style="{ borderBottom: borderBottomColorPassword }" type="password" name="password"
                        id="password" autocomplete="off" placeholder="Contraseña">
                </div>
                <div class="input__form-container">
                    <label for="password_confirm">Confirmar Contraseña <span class="required__text">*</span></label>
                    <input v-model="password_confirm" @input="validateInput('password_confirm')"
                        :style="{ borderBottom: borderBottomColorPassword_confirm }" type="password"
                        name="password_confirm" id="password-confirm" autocomplete="off"
                        placeholder="Confirmar contraseña">
                </div>
            </div>

            <div class="form__terminos">
                <input v-model="checkbox" type="checkbox" @change="validateInput('checkbox')" id="cbx"
                    style="display: none;">
                <label for="cbx" class="check">
                    <svg width="18px" height="18px" viewBox="0 0 18 18">
                        <path
                            d="M1,9 L1,3.5 C1,2 2,1 3.5,1 L14.5,1 C16,1 17,2 17,3.5 L17,14.5 C17,16 16,17 14.5,17 L3.5,17 C2,17 1,16 1,14.5 L1,9 Z">
                        </path>
                        <polyline points="1 9 7 14 15 4"></polyline>
                    </svg>
                </label>
                <a href="#">Acepto terminos y condiciones</a>
            </div>

            <div class="form__button">
                <button @click.prevent="submitForm" @click="signin" :disabled="!validForm">Registrarse</button>
            </div>
        </form>
    </div>
</template>
<script>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

export default {
    name: 'FormSignin',
    setup() {
        const URL = 'http://localhost:4000';
        const router = useRouter();
        const id_rol = 2;
        // Variables del form
        let error = ref('');
        let username = ref('');
        let tagline = ref('');
        let name = ref('');
        let email = ref('');
        let password = ref('');
        let password_confirm = ref('');
        let date_of_birth = ref('');
        let date = '';
        // Validators
        let checkbox = ref(false);
        let usernameValid = ref(false);
        let taglineValid = ref(false);
        let date_of_birthValid = ref(false);
        let emailValid = ref(false);
        let passwordsValid = ref(false);
        let validForm = ref(false);
        // Contadores
        let cntCheckbox = 0;
        // Variables de decoradores
        let borderBottomColorUsername = ref(''); // grey red #14be14
        let borderBottomColorTagline = ref('');
        let borderBottomColorName = ref('');
        let borderBottomColorEmail = ref('');
        let borderBottomColorPassword = ref('');
        let borderBottomColorPassword_confirm = ref('');
        let borderBottomColorDate_of_birth = ref('');

        let maxDate = computed(() => {
            let today = new Date();
            let max_date = new Date(today.setFullYear(
                today.getFullYear() - 18,
                today.getMonth(),
                today.getDate()
            ));
            return max_date.toISOString().slice(0, 10);
        });

        const validateInput = input => {
            switch (input) {
                case 'username': validarUsername(); break;
                case 'tagline': validarTagline(); break;
                case 'name': validarName(); break;
                case 'email': validarEmail(); break;
                case 'password': validarPasswords(); break;
                case 'password_confirm': validarPasswords(); break;
                case 'date_of_birth': validarDate_of_birth(); break;
                case 'checkbox': checkbox.value = checkbox.value === true ? true : false; break;
                default: break;
            }
            if (!checkbox.value) { validForm.value = false; }

            const valid = (
                usernameValid.value &&
                taglineValid.value &&
                emailValid.value &&
                passwordsValid.value &&
                date_of_birthValid.value &&
                checkbox.value
            )
            validForm.value = valid;
            return valid;
        }

        const validarUsername = () => {
            username.value = username.value.trim();
            if (username.value.length > 15) { username.value = username.value.slice(0, -1); }
            if (username.value.length < 2 || username.value.length > 15) {
                borderBottomColorUsername.value = '3px solid red';
                usernameValid.value = false;
            } else {
                borderBottomColorUsername.value = '3px solid #14be14';
                usernameValid.value = true;
            }
        }
        const validarTagline = () => {
            tagline.value = tagline.value.trim().toUpperCase();
            if (tagline.value.length > 5) { tagline.value = tagline.value.slice(0, -1); }
            if (tagline.value.length < 4 || tagline.value.length > 5) {
                borderBottomColorTagline.value = '3px solid red';
                taglineValid.value = false;
            } else {
                borderBottomColorTagline.value = '3px solid #14be14';
                taglineValid.value = true;
            }
        }
        const validarName = () => {
            if (name.value.length > 60) { name.value = name.value.slice(0, -1); }
            if (name.value.length >= 3 && name.value.length <= 60) {
                borderBottomColorName.value = '3px solid #14be14';
            } else if (name.value.length === 0) {
                borderBottomColorName.value = '3px solid grey';
            } else {
                borderBottomColorName.value = '3px solid red';
            }
        }
        const validarEmail = () => {
            if (email.value.length > 60) { email.value = email.value.slice(0, -1); }
            const regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            email.value = email.value.trim();
            if (!regex.test(String(email.value).toLowerCase())) {
                borderBottomColorEmail.value = '3px solid red';
                emailValid.value = false;
            } else {
                borderBottomColorEmail.value = '3px solid #14be14';
                emailValid.value = true;
            }
        }

        const validarPasswords = () => {
            validarPassword();
            validarPassword_confirm();

            passwordsValid.value = validarPassword() && validarPassword_confirm();
        }
        const validarPassword = () => {
            password.value = password.value.trim();
            if (password.value.length > 40) { password.value = password.value.slice(0, -1); }
            if (password.value.length < 8 || password.value.length > 40) {
                borderBottomColorPassword.value = '3px solid red';
                return false;
            } else {
                borderBottomColorPassword.value = '3px solid #14be14';
                return true;
            }
        }
        const validarPassword_confirm = () => {
            password_confirm.value = password_confirm.value.trim();
            if (password_confirm.value.length > 40) { password_confirm.value = password_confirm.value.slice(0, -1); }
            borderBottomColorPassword_confirm.value =
                password_confirm.value.length >= 8 && password_confirm.value.length <= 40 &&
                    password_confirm.value === password.value
                    ? '3px solid #14be14'
                    : '3px solid red';
            if (password.value.length === 0) {
                borderBottomColorPassword_confirm.value =
                    password_confirm.value.length >= 8 && password_confirm.value.length <= 40
                        ? '3px solid #14be14'
                        : '3px solid red';
            }
            return (
                password_confirm.value.length >= 8 &&
                password_confirm.value.length <= 40 &&
                password_confirm.value === password.value
            )

        }
        const validarDate_of_birth = () => {
            // Cambiando formato YYYY-MM-DD a DD-MM-YYYY
            if (date_of_birth.value.length !== 10 || date_of_birth.value > maxDate.value) {
                borderBottomColorDate_of_birth.value = '3px solid red';
                date_of_birthValid.value = false;
            } else {
                borderBottomColorDate_of_birth.value = '3px solid #14be14';
                date_of_birthValid.value = true;
            }
            let dateParts = date_of_birth.value.split('-');
            date = dateParts[2] + '-' + dateParts[1] + '-' + dateParts[0];
        }

        const signin = async () => {
            if (!validateInput()) {
                error.value = "Formulario no válido";
                return;
            }
            error.value = '';
            const ROUTE = '/users';
            const user = {
                username: username.value,
                tagline: tagline.value,
                name: name.value,
                date_of_birth: date,
                email: email.value,
                password: password.value,
                id_rol: id_rol
            }

            const response = await axios({
                method: "POST",
                url: URL + ROUTE,
                data: user
            })

            if (response.data.status === 400) {
                if (response.data.campo === "tagline") {
                    borderBottomColorTagline.value = "3px solid red";
                    taglineValid.value = false;
                    validateInput();
                }
                if (response.data.campo === "email") {
                    borderBottomColorEmail.value = "3px solid red";
                    emailValid.value = false;
                    validateInput();
                }

                error.value = response.data.message;
                return;
            }

            router.push('/login')
                .catch(err => {
                    console.error('Error al redirigir a la ruta', err);
                });
        }

        return {
            signin,
            error,
            id_rol,
            username,
            tagline,
            name,
            email,
            password,
            password_confirm,
            date_of_birth,
            checkbox,
            validarUsername,
            validarTagline,
            validarName,
            validarEmail,
            validarPassword,
            validarPassword_confirm,
            validarPasswords,
            validarDate_of_birth,
            emailValid,
            usernameValid,
            taglineValid,
            date_of_birthValid,
            passwordsValid,
            validForm,
            borderBottomColorUsername,
            borderBottomColorTagline,
            borderBottomColorName,
            borderBottomColorEmail,
            borderBottomColorPassword,
            borderBottomColorPassword_confirm,
            borderBottomColorDate_of_birth,
            validateInput,
            maxDate
        }
    }
}
</script>