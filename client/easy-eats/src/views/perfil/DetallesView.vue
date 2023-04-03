<template>
    <div class="detallesPerfil">
       <navbar />
       <!-- <FondoFrutas /> -->
       <section class="seccion-perfil-usuario">
        <div class="perfil-usuario-header">
            <div class="perfil-usuario-portada">
                <div class="perfil-usuario-avatar">
                    <img src="../../assets/imgs/yo.jpg" alt="img-avatar">
                    <button type="button" class="boton-avatar">
                        <i class="far fa-image"></i>
                    </button>
                </div>
                <!-- <button type="button" class="boton-portada">
                    <i class="far fa-image"></i> Cambiar fondo
                </button> -->
            </div>
        </div>
        <div class="perfil-usuario-body">
            <div class="perfil-usuario-bio">
                <h3 class="titulo">Campos Figueroa Brandon</h3>
                <p class="texto">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                    tempor incididunt ut labore et dolore magna aliqua.</p>
            </div>
            <div class="perfil-usuario-footer">
                <ul class="lista-datos">
                    <li><i class="icono fas fa-map-signs"></i> Nombre de Usuario:</li>
                    <li><i class="icono fas fa-phone-alt"></i> TagLine:</li>
                    <li><i class="icono fas fa-briefcase"></i> Fecha de nacimiento:</li>
                    <li><i class="icono fas fa-building"></i> Corre electronico:</li>
                </ul>
            </div>
            <div class="redes-sociales">
                <a href="" class="boton-redes facebook fab fa-facebook-f"><i class="icon-facebook"></i></a>
            </div>
        </div>
    </section>

    <div class="mis-redes" style="display: block;position: fixed;bottom: 1rem;left: 1rem; opacity: 0.5; z-index: 1000;">
    <p style="font-size: .75rem;">Apock graficos</p>
    <div>
        <a target="_blank" href="#"><i class="fab fa-facebook-square"></i></a>
       
    </div>
</div>



    </div>
</template>
<!-- 

<script>
import { useRouter } from 'vue-router';
import FondoFrutas from '../components/layout/FondoFrutas';
import Header from '../components/home/Header';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';


export default {
  name: "Detalles",
  setup() {
    const router = useRouter();
  },
  components: {
    Navbar,
    Header,
    FondoFrutas,
    Footer
  }
}
</script> -->
