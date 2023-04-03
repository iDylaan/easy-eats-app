<template lang="">
 
 <nav class="navbar">

<div class="logo_containes" @click="goHome">
   
        <img src="../../assets/imgs//icono_fondos_pscuros.png">
    
</div>
<div class="options_container">
<ul>
    <li><a @click="goHome">Inicio</a></li>
    <li><a href="#">Recetas</a></li>
    <li><a href="#">Nutrición</a></li>
    <li><a @click="goNosotros">Nosotros</a></li>
</ul>
</div>

<div class="profile-options">
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

    <button @click="nuevaReceta">
        Nueva Receta
    </button>

</div>

<!-- menu de hamburguesa -->
<!-- <div class="btn">
    <font-awesome-icon icon="fa-solid fa-bars" />
</div> -->
</nav>

</template>
<script>
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';

export default {
    setup() {
        const router = useRouter();
        const isLoged = ref(false);

        const goHome = () => router.push('/');
        const nuevaReceta = () => router.push("/subir-receta");
        const goNosotros = () => router.push("/nosotros");

        const iniciarSesion = () => router.push("/login");

        const cerrarSesion = () => {
            localStorage.removeItem('token');
            localStorage.removeItem('username');
            localStorage.removeItem('tagline');
            window.location.reload();
        }


        onMounted(() => {
            isLoged.value = localStorage.getItem('token') ? true : false;
        })

        return {
            router,
            iniciarSesion,
            cerrarSesion,
            nuevaReceta,
            goHome,
            isLoged,
            goNosotros,
        }
    }
}
</script>