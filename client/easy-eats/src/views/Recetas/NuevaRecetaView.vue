<template>
    <div class="nueva-receta">
        <!-- Fixeds -->
        <Navbar />
        <FondoFrutas />


        <div class="nueva-receta__container">

            <div class="step-titles__container">

                <div class="step-title__container">
                    <h3>Registrar Receta</h3>
                </div>

                <div class="step-title__container">
                    <h3>Imagen</h3>
                </div>

                <div class="step-title__container">
                    <h3>Pasos</h3>
                </div>

                <div class="step-title__container">
                    <h3>Ingredientes</h3>
                </div>

                <div class="step-title__container">
                    <h3>Utensilios</h3>
                </div>

                <div class="step-title__container">
                    <h3>Categorias</h3>
                </div>

            </div>

            <div class="forms__container">

                <div class="form__container" id="registrar-receta__container">
                    <!-- <RegistrarReceta /> -->
                    <!-- <RegistrarImagen /> -->
                    <!-- <RegistrarPasos /> -->
                    <RegistrarIngredientes />
                </div>

            </div>

        </div>

        <!-- Termina Contenido -->
        <Footer />
    </div>
</template>
<script>
// Layout
import FondoFrutas from '@/components/layout/FondoFrutas';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';

// Formularios
import RegistrarReceta from '@/components/nueva-receta/RegistrarRecetaForm';
import RegistrarImagen from '@/components/nueva-receta/ImagenForm';
import RegistrarPasos from '@/components/nueva-receta/PasosForm';
import RegistrarIngredientes from '@/components/nueva-receta/IngredientesForm';

// Elementos de Vue
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';

export default {
    name: 'NuevaReceta',
    setup() {
        const router = useRouter();
        const isLoged = ref(false);


        onMounted(() => {
            isLoged.value = localStorage.getItem('token') ? true : false;

            if (!isLoged.value) {
                router.push('/login');
            }
        })


        return {
        }
    },
    components: {
        // Layout
        FondoFrutas,
        Navbar,
        Footer,
        // Formularios
        RegistrarReceta,
        RegistrarImagen,
        RegistrarPasos,
        RegistrarIngredientes
    }
}
</script>