<template>
  <div class="login">
    <span class="bg-darken"></span>

    <div class="legend__container">
      <LegendLogin />
    </div>

    <div class="login__container">
      <h1 class="login__title">
        <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
        Iniciar Sesión
      </h1>
      <FormLogin />
    </div>
  </div>
</template>
<script>
import FormLogin from '../components/login-signin/FormLogin';
import LegendLogin from '../components/login-signin/LegendLogin';

export default {
  name: "Login",
  components: {
    FormLogin,
    LegendLogin,
  },
}
</script>
<style>
    
</style>