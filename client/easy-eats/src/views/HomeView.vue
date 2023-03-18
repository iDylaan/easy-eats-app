<template>
  <div class="home">
    <Header />
    <Navbar />
    <Carrusel />  
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
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
    // Carrusel,
  }
}
</script>
