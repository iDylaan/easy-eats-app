<template>
  <div class="login">
    <Logo />
    <span class="bg-darken"></span>


    <div class="legend__container">
      <LegendLogin />
    </div>

    <div class="login__container">
      <h1 class="login__title">
        <font-awesome-icon icon="fa-solid fa-user" />
        Iniciar Sesión
      </h1>
      <FormLogin />
    </div>
  </div>
</template>
<script>
import FormLogin from '../../components/login-signin/FormLogin';
import LegendLogin from '../../components/login-signin/LegendLogin';
import Logo from '../../components/login-signin/LogoFixed';

export default {
  name: "Login",
  components: {
    FormLogin,
    LegendLogin,
    Logo
  },
}
</script>
<style>
    
</style>