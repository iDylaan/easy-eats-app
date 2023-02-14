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

            <div class="inputs__container">
                <div class="input__form-container">
                    <label for="username">Nombre de Usuario <span class="required__text">*</span></label>
                    <div class="inputs_username-container">
                        <input v-model="username" @input="validarUsername" type="text" name="username" id="username"
                            placeholder="Username"> #
                        <input v-model="tagline" @input="validarTagline" type="text" name="tagline" id="tagline"
                            placeholder="Tag">
                    </div>
                </div>

                <div class="input__form-container">
                    <label for="name">Nombre</label>
                    <input v-model="name" @input="validarName" type="text" name="nombre" id="nombre"
                        placeholder="Nombre Completo">
                </div>

                <div class="input__form-container">
                    <label for="date_of_birth">Fecha de nacimiento <span class="required__text">*</span></label>
                    <input v-model="date_of_birth" @input="validarDate_of_birth" type="date" name="date_of_birth"
                        id="date_of_birth">
                </div>

                <div class="input__form-container">
                    <label for="username">Correo electronico <span class="required__text">*</span></label>
                    <input v-model="email" @input="validarEmail" type="email" name="email" id="email" autocomplete="off"
                        placeholder="exampe@example.com">
                </div>

                <div class="input__form-container">
                    <label for="username">Contraseña <span class="required__text">*</span></label>
                    <input v-model="password" @input="validarPassword" type="password" name="password" id="password"
                        autocomplete="off" placeholder="Contraseña">
                </div>
                <div class="input__form-container">
                    <label for="username">Confirmar Contraseña <span class="required__text">*</span></label>
                    <input v-model="password_confirm" @input="validarPassword_confirm" type="password"
                        name="password_confirm" id="password-confirm" autocomplete="off"
                        placeholder="Confirmar contraseña">
                </div>

                <input v-model="id_rol" @input="validarId_rol" type="hidden" name="id_rol" id="id_rol">
            </div>


            <div class="form__terminos">
                <input type="checkbox" id="cbx" style="display: none;">
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
                <button @click.prevent="submitForm" @click="signin" :disable="!validForm">Registrarse</button>
            </div>
        </form>
    </div>
</template>
<script>
import { ref } from 'vue';

export default {
    name: 'FormSignin',
    setup() {
        let emailValid = ref(false);
        let id_rol = ref(2);
        let username = ref('');
        let tagline = ref('');
        let name = ref('');
        let email = ref('');
        let password = ref('');
        let password_confirm = ref('');
        let date_of_birth = ref('');
        let validForm = ref(false);

        const validarUsername = () => {
            username.value = username.value.trim();
            if (username.value.length < 2 || username.value.length > 15) {
                console.log("Username no valido");
            }

            if (username.value.length > 15) {
                username.value = username.value.slice(0, -1);
            }
        }

        const validarTagline = () => {
            tagline.value = tagline.value.trim().toUpperCase();
            if(tagline.value.length < 4 || tagline.value.length > 5) {
                console.log("Tagline no valido");
            }
            
            if(tagline.value.length > 15) {
                tagline.value = tagline.value.slice(0, -1);
            }
        }

        const validarName = () => {
            name.value = name.value;
        }

        const validarEmail = () => {
            const regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            email.value = email.value.trim();
            emailValid.value = regex.test(String(email.value).toLowerCase());
            console.log(email.value);
            console.log(emailValid.value);
        }
        const validarPassword = () => {
            password.value = password.value.trim();
            if(password.value < 8 ){
                console.log("Contraseña no valida");
            }
        }
        const validarPassword_confirm = () => {
            password_confirm.value = password_confirm.value.trim();

            if(password.value < 8 ){
                console.log("Contraseña no valida");
            }

            if(password_confirm.value!== password.value) {
                console.log("Las contraseñas no coinciden");
            }
        }
        const validarDate_of_birth = () => {
            date_of_birth.value = date_of_birth.value.trim().toUpperCase();
            console.log(date_of_birth.value);
        }

        const validarFormulario = () => {

        }

        return {
            id_rol,
            username,
            tagline,
            name,
            email,
            password,
            password_confirm,
            date_of_birth,
            validarUsername,
            validarTagline,
            validarName,
            validarEmail,
            validarPassword,
            validarPassword_confirm,
            validarDate_of_birth,
            validForm,
            emailValid
        }
    }
}
</script>