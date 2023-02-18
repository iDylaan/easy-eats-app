<template>
    <header :class="headerClass">
        <div class="logo">LOGO</div>
        <nav class="navbar">
            <a href="">Inicio</a> <span class="navpipe">|</span>
            <a href="">Recetas</a> <span class="navpipe">|</span>
            <a href="">Salud y Nutrición</a>
        </nav>
        <div class="profile-options">
            <!-- <button v-if="isLoged" @click="cerrarSesion">Cerrar Sesión</button>
            <button v-if="!isLoged" @click="iniciarSesion">Iniciar Sesión</button> -->

            <button v-if="!isLoged" @click="iniciarSesion">
                Iniciar Sesion
                <div class="arrow-wrapper">
                    <div class="arrow"></div>

                </div>
            </button>

            <button v-if="isLoged" @click="cerrarSesion">
                Cerrar Sesión
                <div class="arrow-wrapper">
                    <div class="arrow"></div>

                </div>
            </button>

        </div>
    </header>
</template>
<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: 'Header',
    setup() {
        const scrollPosition = ref(0);
        const headerClass = ref('');

        const handleScroll = () => {
            scrollPosition.value = window.scrollY;
            if (scrollPosition.value > 0) { 
                headerClass.value = 'fixed';
            } else {
                headerClass.value = '';
            }
        }

        onMounted(() => {
            window.addEventListener('scroll', headerClass);
        })

        onBeforeUnmount(() => {
            window.removeEventListener('scroll', headerClass);
        });

        const router = useRouter();
        let isLoged = ref(false);

        const iniciarSesion = () => {
            router.push("/login");
        }
        const cerrarSesion = () => {
            localStorage.removeItem('token');
            localStorage.removeItem('username');
            localStorage.removeItem('tagline');
            router.push('/');
        }

        return {
            isLoged,
            headerClass,
            iniciarSesion,
            cerrarSesion
        }
    }
}
</script>