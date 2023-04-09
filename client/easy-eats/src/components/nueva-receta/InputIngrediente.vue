<template>
    <div class="input-ingrediente__container">
        <textarea name="paso-text" rows="5" maxlength="300" minlength="50"></textarea>
        <div>
            <button class="btn btn-rojo" @click="eliminar" @click.prevent="handleClick">
                <font-awesome-icon icon="fa-solid fa-trash-can" />
                Eliminar paso
            </button>
        </div>
    </div>
</template>
<script>
import { defineComponent } from 'vue';

export default defineComponent({
    props: {
        data: {
            type: Number,
            required: true,
        },
    },
    setup(props, {emit}) {
        const eliminar = () => {
            emit('eliminar');
        }

        return {
            data: props.data,
            eliminar
        };
    }
})
</script>