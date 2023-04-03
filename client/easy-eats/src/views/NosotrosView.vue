
<template>
    <div class="nosotros">
        <Navbar />
        <FondoFrutas />
     <!-- Contenido -->
      <div class="container__nosotros">
      <div class="title">
        <h1>Hacerca de nosotros</h1>
      </div>
      <div class="cajauno">
      <div class="vision">
        <h3>Vision</h3>
        <p>Ser la herramienta ideal para que cualquier persona mayor de 18 años pueda descubrir, crear y compartir deliciosas recetas con una amplia comunidad de aficionados a la cocina en todo el mundo hispanoablante. La plataforma será fácil de usar y estar disponible en múltiples dispositivos, desde computadoras de escritorio hasta dispositivos móviles.</p>
       </div>
       <div class="mision">
        <h3>Misiòn</h3>
      <p>Fomentar la creatividad y la experimentación en la cocina, brindando una variedad de recetas para satisfacer las necesidades y gustos de nuestros usuarios. Crear una comunidad participativa y colaborativa de amantes de la cocina, donde los usuarios puedan compartir sus conocimientos culinarios y aprender de otros miembros de la comunidad. </p>
       </div>
      </div>
      <div class="title">
        <h1>Contacto</h1>
      </div>
      <div class="datos">
        <p>Team Wizard Of Code</p>
        <a href="https://wa.me/qr/PUD62BLERMXSA1">55-74-18-15-29</a>
        <a href="http://mail.google.com/mail?hl=es-419">Wizard.Of.CodeOficial@gmail.com</a>
      </div>
      </div>
      <Footer />
    </div>

    <!-- </div> -->
</template>

<script>
import { useRouter } from 'vue-router';
import FondoFrutas from '../components/layout/FondoFrutas';
import Header from '../components/home/Header';
// import Carrusel from '../components/home/Carrusel';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';


export default {
  name: "Nosotros",
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
</script>
