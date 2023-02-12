<template>
  <router-view/>
</template>
<script>
import { onMounted, computed } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'App',
  setup() {
    const store = useStore();
    const user = computed(() => store.state.user);

    onMounted(() => {
      console.log(user.value);
    });

    return {
      user,
    }
  }
}
</script>