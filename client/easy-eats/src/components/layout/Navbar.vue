<template lang="">
 
 <nav class="navbar">

<div class="logo_containes">
   
        <img src="../../assets/imgs//icono_fondos_pscuros.png">
    
</div>
<div class="options_container">
<ul>
    <li><a href="#">Inicio</a></li>
    <li><a href="#">Recetas</a></li>
    <li><a href="#">Nutrición</a></li>
    <li><a href="#">Nosotros</a></li>
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

</div>

<!-- menu de hamburguesa -->
<!-- <div class="btn">
    <font-awesome-icon icon="fa-solid fa-bars" />
</div> -->
</nav>

</template>
<script>
export default {
    
}
</script>