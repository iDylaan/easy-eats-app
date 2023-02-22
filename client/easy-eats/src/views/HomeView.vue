<template>
  <!-- <div class="home">
    <Header />
    <img src="@/assets/imgs/Banner-Food1.png" alt="">
    <Carrusel />
  </div> -->

  <PagePreloader />
</template>

<script>
import { useRouter } from 'vue-router';
import Header from '../components/home/Header';
import Carrusel from '../components/home/Carrusel';
import PagePreloader from '@/components/page-wrapper/PagePreloader';


export default {
  name: "Home",
  setup() {
    const router = useRouter();
  },
  components: {
    Header,
    Carrusel,
    PagePreloader
  }
}
</script>
