
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
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Assumenda rerum et voluptas maxime quod magni laboriosam ullam suscipit tenetur, ducimus exercitationem architecto obcaecati quam similique inventore rem amet illo fugit fuga itaque. Ad dolores eum, iste deleniti ratione, enim quis doloremque soluta veritatis culpa quos ducimus recusandae qui dolorem blanditiis, iure nulla sapiente ut voluptatibus hic maxime quas corporis eligendi tempore. In debitis saepe eligendi! Totam placeat exercitationem corrupti reprehenderit voluptates odit, delectus officiis voluptas itaque ab quibusdam eos fuga quasi! Eius maxime amet nisi enim assumenda quidem, rem, iusto reprehenderit veritatis corrupti cum aliquam unde officiis et, adipisci in.</p>
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
