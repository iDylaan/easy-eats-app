<template>
  <div class="home">
    <!-- Fixeds -->
    <FondoFrutas />
    <Navbar />

    <!-- Contenido -->
    <Header />

    <div class="prueba">
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis hic aliquid eaque eos voluptatem maiores, possimus, illum consequatur laudantium itaque iure nemo. Aut expedita quia quasi, neque libero ex, nam eaque eveniet doloremque cum at corrupti officiis quod quisquam velit maxime. Accusamus doloribus excepturi, alias odit nihil officia ea quam exercitationem! Accusantium nihil harum ratione, sit eligendi, rem veniam dolorem ex reprehenderit earum esse. Amet quas, quae quibusdam inventore vel velit iure deleniti fuga qui, at dicta pariatur exercitationem nobis fugit accusantium error, ex blanditiis eos eligendi perspiciatis facilis. Vero impedit molestias quaerat accusamus soluta rem debitis alias dolore nesciunt?</p>
    </div>

    <!-- Termina Contenido -->
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import FondoFrutas from '../components/layout/FondoFrutas';
import Header from '../components/home/Header';
// import Carrusel from '../components/home/Carrusel';
import Navbar from '../components/layout/Navbar';


export default {
  name: "Home",
  setup() {
    const router = useRouter();
  },
  components: {
    Navbar,
    Header,
    FondoFrutas
  }
}
</script>
