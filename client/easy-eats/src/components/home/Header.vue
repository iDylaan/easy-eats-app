<title>Header</title>
<template>
    <header :class="headerClass">

        <div class="bg-imagen_container">
            <div class="card-receta__container">

                <div class="imag-container">
                    <img src="../../assets/imgs/ensala_rusa.jpg" alt="">
                </div>

                <div class="detalles__container">
                    <div class="receta-nombre__container">
                        <h2>Ensalada Rusa</h2>
                    </div>
                    <div class="receta-descripcion__container">
                        <p>Es una ensalada típica de diversos países de Europa, Asia y América. Dependiendo de la tradición culinaria de cada región ha evolucionado de manera diferente, pudiendo llevar ingredientes distintos, pero incluyendo habitualmente patatas y otras hortalizas cocidas amalgamadas con mayonesa.</p>
                    </div>
                    <div class="receta-detalles__container">
                        <div class="receta-puntaje__container">
                            ⭐⭐⭐⭐⭐
                        </div>
                        |
                        <div class="receta-tiempo__container">
                            <span>3</span> minutos 🕐
                        </div>
                        |
                        <div class="receta-personas__container">
                            <span>4</span> personas 👥
                        </div>
                    </div>
                </div>

            </div>
        </div>

    </header>

    <!-- <section class="zona1"></section> -->
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: 'Header',
    setup() {
        const headerClass = ref('');
        const router = useRouter();
        let isLoged = ref(false);


        // windowaddEventListener("scroll", function () {
        //     var header = document.querySelector("header");
        //     header.classList.toggle("abajo", window.scrollY > 0);

        // })

        // const handleScroll = () => {
        //     scrollPosition.value = window.scrollY;
        //     if (scrollPosition.value > 0) {
        //         headerClass.value = 'fixed';
        //     } else {
        //         headerClass.value = '';
        //     }
        // }

        // export default {
        //     methods: {
        //         handleScroll() {
        //             scrollPosition.value = window.scrollY;
        //     if (scrollPosition.value > 0) {
        //         headerClass.value = 'fixed';
        //     } else {
        //         headerClass.value = '';
        //     }
        //         }
        //     }
        // }

        onMounted(() => {
            window.addEventListener('scroll', headerClass);
            isLoged.value = localStorage.getItem('token') ? true : false;
        })

        onBeforeUnmount(() => {
            window.removeEventListener('scroll', headerClass);
        });

        const iniciarSesion = () => {
            router.push("/login");
        }
        const cerrarSesion = () => {
            localStorage.removeItem('token');
            localStorage.removeItem('username');
            localStorage.removeItem('tagline');
            window.location.reload();
        }



        return {
            isLoged,
            headerClass,
            iniciarSesion,
            cerrarSesion
        }



    }
}




</script>