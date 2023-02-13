<template>
    <div>
        <h1>Hola usuario {{ username }}!</h1>
        <button @click="cerrarSesion">Cerrar Sesion</button>
    </div>
</template>
<script>
// import axios from 'axios';
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import jwtDecode from 'jwt-decode'


export default {
    name: 'LogedPage',
    setup() {
        const router = useRouter();
        let username = ref('');
        let recetas = ref([]);


        const getRecetas = () => {
            console.log('consultando recetas');
        }

        const cerrarSesion = () => {
            // localStorage.clear();
            localStorage.removeItem('token');
            localStorage.removeItem('username');
            localStorage.removeItem('tagline');

            router.push('/');
        }

        onMounted(() => {
            if(!localStorage.getItem('token')) {
                router.push('/login');
            }
            
            getRecetas();
            username.value = localStorage.getItem('username');
        });

        return {
            username,
            getRecetas,
            cerrarSesion
        };
    }
}
</script>