<template>
  <h1>Pagina de bienvenida para <span class="easy-eats__title">Easy Eats</span> desde <span class="easy-eats__title">VueJs</span></h1>
  <Bienvenida />
  <Usuarios />
</template>

<script>
import Bienvenida from "./components/Bienvenida.vue";
import Usuarios from "./components/Usuarios.vue";
export default {
  components: {
    Bienvenida,
    Usuarios
  }
}
</script>

<style lang="scss">
  @import "@/assets/styles/main.scss";
</style>