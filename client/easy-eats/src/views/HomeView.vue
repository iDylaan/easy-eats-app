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




    <div class="container__recipes">
    <!-- <div class="box__recipes">
        <div class="logo">
            <img src="../../assets/imgs/icono_fondos_pscuros.png" alt="">
         
        </div>
        
        <div class="terms">
            <p>En nuestro sitio web, respetamos su privacidad y nos comprometemos a proteger sus datos personales. </p>
        </div>
    </div> -->
    <div class="box__recipes">
       <div class="logo">
            <img src="../assets/imgs/receta1.jpg" alt="">
        </div>
        <h2>Ensalada de quinoa <br> y verduras</h2>
        <a href="#">Lorem, ipsum dolor.</a>
    </div>

    <div class="box__recipes">
      <div class="logo">
            <img src="../assets/imgs/receta2.jpg" alt="">
        </div>
        <h2>Sopa de calabaza</h2>
        <a href="#">Lorem, ipsum dolor.</a>           
    </div>
    <div class="box__recipes">
      <div class="logo">
            <img src="../assets/imgs/receta3.jpg" alt="">
        </div>
        <h2>Chili con carne </h2>
        <a href="#">Lorem, ipsum dolor.</a>        
    </div>
    <div class="box__recipes">
      <div class="logo">
            <img src="../assets/imgs/receta4.jpg" alt="">
        </div>
        <h2>Pasta con salsa de <br> tomate casera </h2>
        <a href="#">Lorem, ipsum dolor.</a>        
    </div>
</div>

    

    <!-- Termina Contenido -->
    <Footer />
  </div>

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
