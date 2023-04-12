<template lang="">

    <div class="RecetaCard">
        <div class="recetas" @click="detallesRecetas">
        <div class="card">
        <div class="card-image"></div>
        <div class="category"> Pizza </div>
        <div class="heading">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam laborum neque expedita est dolor aliquid modi veritatis temporibus nulla totam, consequuntur laudantium odio ut natus eaque tenetur delectus ipsum in quidem perferendis quis laboriosam dolores at. Repudiandae, sed id. Similique ea consequatur officia, laborum saepe voluptatibus facilis numquam itaque temporibus?
      </div>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';


export default {
  name: "RecetaCard",
  setup() {
    const router = useRouter();
    const detallesRecetas = () => router.push("/detallesRecetas");

    return{
      router,
      detallesRecetas
    }
  },
  components: {
  }
}
</script>