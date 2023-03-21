<template>
  <div class="home">
    <!-- Fixeds -->
    <FondoFrutas />
    <Navbar />

    <!-- Contenido -->
    <Header />

    <div class="pollo">
      <div class="img"><img src="../assets/imgs/polllo_hor.jpg" alt=""></div>
      <p>El pollo al horno con hierbas es un plato delicioso y fácil de preparar que consiste 
         en muslos de pollo sazonados con una mezcla de hierbas frescas como el tomillo, el romero 
         y la salvia. Se hornea en el horno a una temperatura alta hasta que esté crujiente por fuera 
         y tierno por dentro.
      </p> 

      <div class="receta-detalles__container">
        <div class="receta-tiempo__container">
          <span>2</span> Horas 🕐
           </div>
            |
          <div class="receta-personas__container">
          <span>8</span> personas 👥
          </div>
      </div>

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
