<template lang="">
    <div class="detallesRecetas">
        <Navbar />
       <FondoFrutas />
        <div class="card-detalles">
            
            <div class="nombre-receta">
                <h1>Pizza</h1>
            </div>

            <div class="img">
                <img src="../../assets/imgs/pizza.jpg" alt="">
            </div>

            <div class="descripcion">
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias obcaecati fuga deleniti aperiam dolore cumque, unde odit iste asperiores amet error molestias quae, aut laboriosam ad? Sit sequi voluptates ullam error. Quae repellendus eius, dolores alias rerum quasi, nostrum quo consectetur adipisci quas molestiae cumque nam architecto deserunt iure ratione similique tempore blanditiis mollitia dolorum voluptate a pariatur. Ullam at esse quibusdam! Maiores dolor saepe delectus autem repellat, perspiciatis maxime odio, corporis vitae ipsum non dignissimos officia culpa a tempore commodi magni vero numquam magnam! Ea quod explicabo reiciendis dolores, tenetur quo culpa earum optio harum asperiores facere dicta officia quia iure molestias adipisci nesciunt ab non. Odio, similique! Perferendis esse libero ipsum temporibus ipsam? Architecto aperiam explicabo quae cumque veritatis fuga, accusamus voluptatibus doloribus expedita aliquid, praesentium molestiae asperiores amet dolorum adipisci placeat. Fuga velit, quas voluptate voluptatum magnam ab tempora earum libero dolores debitis temporibus ducimus eaque. Dignissimos!</p>
            </div>

            <div class="ingredientes">
                <h3>Ingredientes</h3>
                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Porro, laboriosam voluptas vero recusandae quasi repudiandae enim iure excepturi nesciunt. Eius eos voluptates sequi nulla necessitatibus expedita? Assumenda officiis dolores animi.</p>
            </div>

            <div class="procedimiento">
                <h3>Procedimiento</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sed eligendi repellendus ea commodi at, non dolores accusantium sunt atque delectus natus quis quam impedit labore velit dicta odit, reiciendis porro!</p>
            </div>
            <div class="nutricion">
                <h3>Informacion Nutrimental</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sed eligendi repellendus ea commodi at, non dolores accusantium sunt atque delectus natus quis quam impedit labore velit dicta odit, reiciendis porro!</p>
            </div>
            <!-- <div>
                <button @click="generatePDF">Generar PDF</button>
            </div> -->
            <div class="boton-back">
                <button @click="recetas">
                    <svg height="16" width="16" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 1024 1024"><path d="M874.690416 495.52477c0 11.2973-9.168824 20.466124-20.466124 20.466124l-604.773963 0 188.083679 188.083679c7.992021 7.992021 7.992021 20.947078 0 28.939099-4.001127 3.990894-9.240455 5.996574-14.46955 5.996574-5.239328 0-10.478655-1.995447-14.479783-5.996574l-223.00912-223.00912c-3.837398-3.837398-5.996574-9.046027-5.996574-14.46955 0-5.433756 2.159176-10.632151 5.996574-14.46955l223.019353-223.029586c7.992021-7.992021 20.957311-7.992021 28.949332 0 7.992021 8.002254 7.992021 20.957311 0 28.949332l-188.073446 188.073446 604.753497 0C865.521592 475.058646 874.690416 484.217237 874.690416 495.52477z"></path></svg>
                    <span>Atras</span>
                </button>
            </div>
       
        </div>

        <Footer />
        
    </div>
</template>

<script>
import { useRouter } from 'vue-router';
import FondoFrutas from '@/components/layout/FondoFrutas';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';

import html2pdf from 'html2pdf.js';
import { setUncaughtExceptionCaptureCallback } from 'process';
// import { useRouter } from 'vue-router';

export default {
  name: "detallesRecetas",
  
  setup() {
    const router = useRouter();
    const recetas = () => router.push("/recetas");

    return{
      router,
      recetas
    }
  },
  components: {
    Navbar,
    FondoFrutas,
    Footer,
  },
//   Generar pedef setUncaughtExceptionCaptureCallback..
//   methods: {
//     generatePDF() {
//       const element = document.getElementById('pdf-content');
//       html2pdf().from(element).save();
//     }
//   }
  
}
</script>
