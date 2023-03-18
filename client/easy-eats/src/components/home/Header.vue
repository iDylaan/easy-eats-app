<title>Header</title>
<template>
    <header :class="headerClass">






        <div class="bg-imagen_container">
            <img src="../../assets/imgs/easyeatsbackground.png" alt="">
        </div>

    </header>

    <section class="zona1"></section>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: 'Header',
    setup() {
        const scrollPosition = ref(0);
        const headerClass = ref('');
        const router = useRouter();
        let isLoged = ref(false);


        // windowaddEventListener("scroll", function () {
        //     var header = document.querySelector('header');
        //     header.classList.toggle("abajo", window.scrollY > 0);

        // })

        const handleScroll = () => {
            scrollPosition.value = window.scrollY;
            if (scrollPosition.value > 0) {
                headerClass.value = 'fixed';
            } else {
                headerClass.value = '';
            }
        }

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