<template lang="">
    <div class="detallesRecetas">
        <Navbar />
       <FondoFrutas />

       <div class="nombre-receta">
        <h1>Pizza</h1>
       </div>

       <div class="img">
        <img src="../../assets/imgs/pizza.jpg" alt="">
       </div>

       <div class="descripcion">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias obcaecati fuga deleniti aperiam dolore cumque, unde odit iste asperiores amet error molestias quae, aut laboriosam ad? Sit sequi voluptates ullam error. Quae repellendus eius, dolores alias rerum quasi, nostrum quo consectetur adipisci quas molestiae cumque nam architecto deserunt iure ratione similique tempore blanditiis mollitia dolorum voluptate a pariatur. Ullam at esse quibusdam! Maiores dolor saepe delectus autem repellat, perspiciatis maxime odio, corporis vitae ipsum non dignissimos officia culpa a tempore commodi magni vero numquam magnam! Ea quod explicabo reiciendis dolores, tenetur quo culpa earum optio harum asperiores facere dicta officia quia iure molestias adipisci nesciunt ab non. Odio, similique! Perferendis esse libero ipsum temporibus ipsam? Architecto aperiam explicabo quae cumque veritatis fuga, accusamus voluptatibus doloribus expedita aliquid, praesentium molestiae asperiores amet dolorum adipisci placeat. Fuga velit, quas voluptate voluptatum magnam ab tempora earum libero dolores debitis temporibus ducimus eaque. Dignissimos!</p>
       </div>

        
    </div>
</template>

<script>

import FondoFrutas from '@/components/layout/FondoFrutas';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';

// import { useRouter } from 'vue-router';

export default {
  name: "detallesRecetas",
  setup() {

    return{

    }
  },
  components: {
    Navbar,
    FondoFrutas,
    Footer,
  },

}
</script>
