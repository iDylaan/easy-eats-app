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
                        <input @input="validarUsername" type="text" name="username" id="username" placeholder="Username"> #
                        <input @input="validarTagline" type="text" name="tagline" id="tagline" placeholder="Tag">
                    </div>
                </div>

                <div class="input__form-container">
                    <label for="name">Nombre</label>
                    <input type="text" name="nombre" id="nombre" placeholder="Nombre Completo">
                </div>

                <div class="input__form-container">
                    <label for="date_of_birth">Fecha de nacimiento <span class="required__text">*</span></label>
                    <input type="date" name="date" id="date">
                </div>

                <div class="input__form-container">
                    <label for="username">Correo electronico <span class="required__text">*</span></label>
                    <input type="email" name="email" id="email" autocomplete="off" placeholder="exampe@example.com">
                </div>

                <div class="input__form-container">
                    <label for="username">Contraseña <span class="required__text">*</span></label>
                    <input type="password" name="password" id="password" autocomplete="off" placeholder="Contraseña">
                </div>
                <div class="input__form-container">
                    <label for="username">Confirmar Contraseña <span class="required__text">*</span></label>
                    <input type="password" name="password-confirm" id="password-confirm" autocomplete="off" placeholder="Confirmar contraseña">
                </div>

                <input type="hidden" name="id_rol" id="id_rol">
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
                <button @click="signin">Registrarse</button>
            </div>
        </form>
    </div>
</template>
<script>
import { ref } from 'vue';

export default {
    name: 'FormSignin',
    setup() {
        let id_rol = ref(2);
        let username = ref('');
        let tagline = ref('');

        const signin = async () => {
        }

        const validarUsername = () => {
            username.value = username.value.trim();
            console.log(username.value);
        }

        const validarTagline = () => {
            tagline.value = tagline.value.trim().toUpperCase();
            console.log(tagline.value);
        }

        return {
            id_rol,
            username,
            tagline,
            validarUsername,
            validarTagline
        }
    }
}
</script>