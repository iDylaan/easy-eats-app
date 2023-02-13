<template>
    <div>
        <h1>Hola admin {{ username }}!</h1>
        <button @click="cerrarSesion">Cerrar Sesion</button>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';

export default {
    name: 'AdminPage',
    setup() {
        const router = useRouter();
        let username = ref('');

        const cerrarSesion = () => {
            // localStorage.clear();
            localStorage.removeItem('token');
            localStorage.removeItem('username');
            localStorage.removeItem('tagline');

            router.push('/');
        }

        onMounted(() => {
            username.value = localStorage.getItem('username');
        })

        return {
            cerrarSesion,
            username
        }
    }
}
</script>