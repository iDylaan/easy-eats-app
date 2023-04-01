
<template>
    <div class="nosotros">
        <Navbar />
     <!-- Contenido -->
      <div class="container__nosotros">
      <div class="title">
        <h1>Hacerca de nosotros</h1>
      </div>
      <div class="vision">
        <h3>Vision</h3>
      </div>
      </div>
    </div>

    <!-- <Footer /> -->
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
  name: "Home",
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
