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
  
    <div class="box__recipes">
       <div class="logo">
            <img src="../assets/imgs/receta1.jpg" alt="">
        </div>
        <h2>Ensalada de quinoa  y verduras</h2>
        <div class="parrafo">
        <p>La ensalada de quinoa y verduras es una ensalada saludable y nutritiva que se prepara con quinoa cocida y verduras frescas como pepino, tomate, cebolla, pimiento y lechuga.</p>
        </div>
        <br>
        <div class="receta-detalles__container">
        <div class="receta-tiempo__container">
          <span>30</span> minutos 🕐
           </div>
          <br>
          <div class="receta-personas__container">
          <span>6</span> personas 👥
          </div>
      </div>

    </div>

    <div class="box__recipes">
      <div class="logo">
            <img src="../assets/imgs/ensa_verduras.png" alt="">
        </div>
        <h2>Ensalada de verduras</h2>
        <div class="parrafo">
        <p>La ensalada de quinoa y verduras es una ensalada saludable y nutritiva que se prepara con quinoa cocida y verduras frescas como pepino, tomate, cebolla, pimiento y lechuga.</p>
        </div>
        <br>
        <div class="receta-detalles__container">
        <div class="receta-tiempo__container">
          <span>30</span> minutos 🕐
           </div>
          <br>
          <div class="receta-personas__container">
          <span>6</span> personas 👥
          </div>
      </div>         
    </div>
    <div class="box__recipes">
       <div class="logo">
            <img src="../assets/imgs/higado.jpg" alt="">
        </div>
        <h2>Higado de res</h2>
        <div class="parrafo">
        <p>Los tacos de hígado son un platillo mexicano que se prepara con hígado de res encebollado y se sirve en tortillas de maíz. La receta varía dependiendo del lugar donde se prepare, pero generalmente se corta el hígado en trozos y se cocina con cebolla y especias como sal, pimienta y comino</p>
        </div>
        <br>
        <div class="receta-detalles__container">
        <div class="receta-tiempo__container">
          <span>30</span> minutos 🕐
           </div>
          <br>
          <div class="receta-personas__container">
          <span>8</span> personas 👥
          </div>
      </div>
    </div>

    <div class="box__recipes">
      <div class="logo">
            <img src="../assets/imgs/cal_res.jpg" alt="">
        </div>
        <h2>Caldo de res</h2>
       
        <div class="parrafo">
        <p>El caldo de res es un platillo mexicano que se prepara con carne de res y verduras. Es un platillo muy popular en México y se consume en épocas de frío. La receta varía según la región y el gusto personal. Por ejemplo, una receta sugiere cocinar la carne de res con ajo, hojas de laurel y sal</p>
        </div>
        <br>
        <div class="receta-detalles__container">
        <div class="receta-tiempo__container">
          <span>1</span> hora 🕐
           </div>
          <br>
          <div class="receta-personas__container">
          <span>9</span> personas 👥
          </div>
      </div>         
    
        
    </div>
    <div class="box__recipes">
      <div class="logo">
            <img src="../assets/imgs/fresas.jpg" alt="">
        </div>
        <h2>Fresas con crema </h2>
               
        <div class="parrafo">
        <p>Las fresas con crema es un postre mexicano que se prepara con fresas frescas cortadas en pedazos y mezcladas con crema mexicana y leche condensada o azúcar. La receta varía según la región y el gusto personal. Por ejemplo, una receta sugiere mezclar la crema mexicana con la leche condensada y las fresas</p>
        </div>
        <br>
        <div class="receta-detalles__container">
        <div class="receta-tiempo__container">
          <span>1</span> hora 🕐
           </div>
          <br>
          <div class="receta-personas__container">
          <span>9</span> personas 👥
          </div>
      </div>         
    </div>
    <div class="box__recipes">
      <div class="logo">
            <img src="../assets/imgs/frutos_rojos.jpg" alt="">
        </div>
        <h2>Ensalada de frutos rojos</h2>
        <div class="parrafo">
        <p>La ensalada de frutos rojos es una ensalada que se prepara con frutas rojas como fresas, frambuesas, zarzamoras y moras. La receta varía según la región y el gusto personal. Por ejemplo, una receta sugiere mezclar el mix de hojas verdes como base del plato con los frutos rojos y el queso</p>
        </div>
        <br>
        <div class="receta-detalles__container">
        <div class="receta-tiempo__container">
          <span>40</span> minutos 🕐
           </div>
          <br>
          <div class="receta-personas__container">
          <span>9</span> personas 👥
          </div>
      </div>       
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
