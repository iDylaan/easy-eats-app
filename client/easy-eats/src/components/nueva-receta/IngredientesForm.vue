<template>
    <div class="registrar-receta">
        <form>

            <div class="ingredientes__container">
                
            </div>


            <div class="buttons-section__container">
                <button class="btn btn-cancelar" @click="goHome">Cancelar</button>
                <input  class="btn btn-siguiente" type="sumbit" value="Siguiente">
            </div>
        </form>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';

export default {
    name: 'IngredientesForm',
    setup () {
        const router = useRouter();

        const goHome = () => {
            router.push('/');
        }

        return {
            goHome
        }
    }
}
</script>