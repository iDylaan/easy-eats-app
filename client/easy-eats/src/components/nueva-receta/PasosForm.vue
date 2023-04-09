<template>
    <div class="registrar-ingredientes">
        <form @submit.prevent="handleSubmit">
            <div class="intrucciones__container">
                <p>Describe los pasos a seguir para preparar tu receta</p>
            </div>

            <div class="pasos__container">

                <div v-for="(paso, index) in pasos" :key="index" class="inputs-pasos__container">
                    <InputPaso :data="paso" @eliminar="eliminarPaso(index)"></InputPaso>
                </div>

                <div class="nuevo-paso-button__container">
                    <button class="nuevo-paso-button btn btn-naranja" @click="agregarPaso" @click.prevent="handleClick">
                        <font-awesome-icon icon="fa-solid fa-plus" />
                        Agregar paso
                    </button>
                </div>
            </div>

            <div class="buttons-section__container">
                <button class="btn btn-cancelar" @click.prevent="handleClick" @click="goHome">Cancelar</button>
                <input class="btn btn-siguiente" type="sumbit" value="Siguiente">
            </div>
        </form>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';
import { onMounted, ref, defineAsyncComponent, defineComponent } from 'vue';

export default defineComponent({
    name: 'PasosForm',
    setup() {
        const router = useRouter();
        const pasos = ref([]);


        onMounted(() => {
            agregarPaso();
        })


        const agregarPaso = () => {
            pasos.value.push(pasos.value.length + 1);
        }
        const eliminarPaso = (index) => {
            pasos.value.splice(index, 1);
        }


        const handleClick = (event) => {
            event.preventDefault();
        }

        const goHome = () => {
            router.push('/');
        }

        return {
            goHome,
            pasos,
            agregarPaso,
            eliminarPaso,
            handleClick
        }
    },
    components: {
        InputPaso: defineAsyncComponent(() => import('@/components/nueva-receta/InputPaso'))
    }
})
</script>