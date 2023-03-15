<template lang="">
 
 <nav class="navbar">

<div class="logo_containes">
    <a href="#" class="brand">
        <img src="../../assets/imgs/icono_fondos_pscuros.png">
    </a>
</div>

<div class="btn">
    <i class="fas fa-times close-btn"></i>
</div>

<ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">Recetas</a></li>
    <li><a href="#">Saludable</a></li>
    <li><a href="#">Nosotros</a></li>
    <li><a href="#">Contacto</a></li>
</ul>

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

</div>

<div class="btn">
    <font-awesome-icon icon="fa-solid fa-bars" />
</div>
</nav>

</template>
<script>
export default {
    
}
</script>