<template>
  <div class="app">
    <router-view/>
  </div>
</template>
<script>
import { onMounted, ref } from 'vue'
// import validateJwt from './utils/misc';
// import store from './store/store'

export default {
  name: 'App',
  setup() {
    const user = ref( null );

    onMounted(() => {
      if (!user) {
        this.$router.push('/login');
      }
    });

    return {
      user,
    }
  }
}
</script>


<style lang="scss">
@import './assets/styles/main.scss';
</style>

<meta>