<template>
    <div class="logo-login-signin__container">
        <div class="content__contianer" @click="goHome">
            <div class="logo__container">
                <img src="../../assets/imgs/icono_fondos_pscuros.png" alt="Logo Easy Eats">
            </div>
            <div class="title__container">
                <p>Easy Eats</p>
            </div>
        </div>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';

export default {
    name: 'LogoFixed',
    setup () {
        const router = useRouter();

        const goHome = () => {
            router.push('/');
        }

        return {
            goHome
        }
    }
}
</script>