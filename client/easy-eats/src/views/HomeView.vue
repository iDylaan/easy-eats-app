<template>
  <div class="">
    <h1>Desde home</h1>
    <button @click="iniciarSesion">Iniciar Sesion</button>
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
