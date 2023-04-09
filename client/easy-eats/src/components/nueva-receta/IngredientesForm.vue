<template>
    <div class="registrar-ingredientes">
        <form>

            <div class="ingredientes__container">
                <p>Registra los ingredientes que hay en tu receta</p>
            </div>

            <div class="ingredientes__container">

                <div v-for="(ingrediente, index) in ingredientes" :key="index" class="inputs-ingredientes__container">
                    <InputIngrediente :data="ingrediente" @eliminar="eliminarIngrediente(index)" />
                </div>


                <div class="nuevo-ingrediente-button__container">
                    <button class="nuevo-ingrediente-button btn btn-naranja" @click="agregarIngrediente"
                        @click.prevent="handleClick">
                        <font-awesome-icon icon="fa-solid fa-plus" />
                        Nuevo ingrediente
                    </button>
                </div>
            </div>

            <div class="buttons-section__container">
                <button class="btn btn-cancelar" @click="goHome">Cancelar</button>
                <input class="btn btn-siguiente" type="sumbit" value="Siguiente">
            </div>
        </form>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';
import { onMounted, ref, defineAsyncComponent, defineComponent } from 'vue';


export default defineComponent({
    name: 'IngredientesForm',
    setup() {
        const router = useRouter();
        const ingredientes = ref([]);


        onMounted(() => {
            agregarIngrediente();
        })


        const agregarIngrediente = () => {
            ingredientes.value.push(ingredientes.value.length + 1);
        }
        const eliminarIngrediente = (index) => {
            ingredientes.value.splice(index, 1);
        }


        const handleClick = (event) => {
            event.preventDefault();
        }

        const goHome = () => {
            router.push('/');
        }

        return {
            goHome,
            ingredientes,
            agregarIngrediente,
            eliminarIngrediente,
            handleClick
        }
    },
    components: {
        InputIngrediente: defineAsyncComponent(() => import('@/components/nueva-receta/InputIngrediente'))
    }
})
</script>