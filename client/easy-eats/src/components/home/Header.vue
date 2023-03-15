<title>Header</title>
<template>
    <header :class="headerClass">
        <!-- <div class="logo">LOGO</div> -->





        <nav class="navbar">

            <div class="logo_containes">
                <a href="#" class="brand">
                    <img src="../../assets/imgs/icono_fondos_pscuros.png">
                </a>
            </div>

            <div class="btn">
                <i class="fas fa-times close-btn"></i>
            </div>

            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Recetas</a></li>
                <li><a href="#">Saludable</a></li>
                <li><a href="#">Nosotros</a></li>
                <li><a href="#">Contacto</a></li>
            </ul>
            
            <div class="profile-options">
                <button v-if="!isLoged" @click="iniciarSesion">
                    Iniciar Sesion
                    <div class="arrow-wrapper">
                        <div class="arrow"></div>
    
                    </div>
                </button>
    
                <button v-if="isLoged" @click="cerrarSesion">
                    Cerrar Sesión
                    <div class="arrow-wrapper">
                        <div class="arrow"></div>
    
                    </div>
                </button>
    
            </div>

            <div class="btn">
                <font-awesome-icon icon="fa-solid fa-bars" />
            </div>
        </nav>

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