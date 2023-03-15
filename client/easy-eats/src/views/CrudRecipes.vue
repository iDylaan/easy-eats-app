<template>
  <div class="">
    <h1>Recetas</h1>
    <button @click="Insertar receta">Insertar_receta</button>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: "Home",
  setup() {
    const router = useRouter();

    const iniciarSesion = () => {
      router.push("/login");
    }

    return {
      iniciarSesion
    }
  }
}
</script>