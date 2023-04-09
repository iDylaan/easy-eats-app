<template>
    <div class="detallesPerfil">

        <Navbar />
        <FondoFrutas />

        <div class="actualizar-perfil__container">
            <div class="form-actualizar__container">
                <span class="bg-toggle" @click="hideFotoForm"></span>
                <FormActualizaFoto />
            </div>
        </div>

        <section class="seccion-perfil-usuario">
            <div class="perfil-usuario-header">
                <div class="perfil-usuario-portada">
                    <div class="perfil-usuario-avatar">
                        <img :src="avatarUrl" alt="">
                        <button type="button" class="boton-avatar" @click="showFotoForm">
                            <i class="far fa-image">Editar</i>
                        </button>
                    </div>
                </div>
            </div>
            <div class="perfil-usuario-body">
                <div class="perfil-usuario-bio">
                    <h3 class="titulo">{{ user.username }}<strong>#</strong>
                        <span class="tagline">{{ user.tagline }}</span>
                    </h3>
                </div>
                <div class="perfil-usuario-footer">
                    <ul class="lista-datos">
                        <li v-if="user.name !== ''"><i class="icono fas fa-map-signs"></i> Nombre completo: <strong>{{
                            user.name }}</strong></li>
                        <li><i class="icono fas fa-building"></i> Corre electrónico: <strong>{{ user.email }}</strong></li>
                        <li><i class="icono fas fa-briefcase"></i> Edad: <strong>{{ user.age_years }} años</strong> y
                            <strong>{{ user.age_months }} meses</strong>
                        </li>
                        <li><i class="icono fas fa-briefcase"></i> Fecha de nacimiento: <strong>{{ user.date_of_birth
                        }}</strong></li>
                    </ul>
                </div>
            </div>
            <div class="boton">
                <button @click="fromPerfil"> Editar
                </button>
            </div>
        </section>
        <Footer />

    </div>
</template>


<script>
import FormActualizaFoto from '@/components/perfil/ActualizarFoto';
import FondoFrutas from '@/components/layout/FondoFrutas';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';

import { useRouter } from 'vue-router';
import { onMounted, ref, toDisplayString } from 'vue';

import axios from 'axios';
import jwtDecode from 'jwt-decode'
// import { URL } from 'url';

export default {
    name: "detallesPerfil",
    setup() {
        const router = useRouter();
        const isLoged = ref(false);
        // Datos del usuario
        const avatarUrl = ref('');
        // Declaramos la APIURL de la API
        const APIURL = 'http://127.0.0.1:4000'; // TODO: Cambiar a la IP pública de la API en producción
        const URL = window.URL || window.webkitURL;
        const user = ref({
            date_of_birth: null,
            email: null,
            username: null,
            tagline: null,
            name: null,
            height: null,
            weight: null,
            age_years: null,
            age_months: null,
        })


        onMounted(async () => {
            isLoged.value = Boolean(localStorage.getItem('token'));

            if (!isLoged.value) {
                router.push('/login');
            }

            let decoded = jwtDecode(localStorage.getItem('token'));

            // await nextTick();
            await init(decoded.user_id);
        })


        const init = async (id_user) => {
            await cargarImagen(id_user);
            await cargarDatosUsuario(id_user);
        }

        const cargarImagen = async (id_user) => {
            const ROUTE = '/pic_user';

            try {
                const response = await axios({
                    method: 'GET',
                    url: APIURL + ROUTE + '/' + id_user,
                    responseType: 'blob',
                })

                if (response.data instanceof Blob) {
                    // Crear objeto URL a partir del Blob recibido
                    const objectUrl = URL.createObjectURL(response.data);

                    if (objectUrl) {
                        avatarUrl.value = objectUrl;
                    } else {
                        console.error('Error al crear el objeto URL');
                    }

                } else {
                    alert('No se pudo obtener la imagen');
                }
            } catch (error) {
                alert('Ha ocurrido un error al cargar la imagen del usuario');
                // TODO: Quitar los console.log
                console.log(error);
            }
        }

        const cargarDatosUsuario = async (id_user) => {
            const ROUTE = '/users';

            try {
                const response = await axios({
                    method: 'GET',
                    url: APIURL + ROUTE + '/' + id_user,
                })
                const result = response.data;

                if (result.status === 200) {
                    const data = result.data

                    // Se almacenan los datos del usuario
                    user.value.username = data.username;
                    user.value.tagline = data.tagline;
                    user.value.name = data.name;
                    user.value.height = data.height;
                    user.value.weight = data.weight;
                    user.value.email = data.email;


                    // Evaluacion de las fechas
                    let fecha_de_nacimiento = new Date(data.date_of_birth);
                    // Fecha de nacimiento con formato dd/mm/aaaa
                    user.value.date_of_birth =
                        fecha_de_nacimiento.getDate().toString().padStart(2, '0') + '/' +
                        (fecha_de_nacimiento.getMonth() + 1).toString().padStart(2, '0') + '/' +
                        fecha_de_nacimiento.getFullYear();

                    // Calcular años y meses transcurridos
                    const today = new Date();
                    let edadAnios = today.getFullYear() - fecha_de_nacimiento.getFullYear();
                    let edadMeses = today.getMonth() - fecha_de_nacimiento.getMonth();
                    let edadDias = today.getDate() - fecha_de_nacimiento.getDate();

                    if (edadMeses < 0 || (edadMeses === 0 && edadDias < 0)) {
                        edadAnios--;
                        if (edadMeses < 0) {
                            edadMeses += 12;
                        }
                        edadMeses--;
                        edadDias += 30; // Asignamos un valor máximo de 30 días para simplificar
                    }

                    if (edadDias < 0) {
                        edadMeses--;
                        edadDias += 30; // Asignamos un valor máximo de 30 días para simplificar
                    }

                    if (edadMeses < 0) {
                        edadAnios--;
                        edadMeses += 12;
                    }

                    user.value.age_years = edadAnios;
                    user.value.age_months = edadMeses;
                }

            } catch (error) {
                alert('Ha ocurrido un error al cargar los datos del usuario');
                // TODO: Quitar los console.log
                console.log(error);
            }
        }


        const hideFotoForm = () => document.querySelector(".actualizar-perfil__container").style.display = "none";
        const showFotoForm = () => document.querySelector(".actualizar-perfil__container").style.display = "grid";


        const fromPerfil = () => router.push("/fromPerfil");

        return {
            fromPerfil,
            hideFotoForm,
            showFotoForm,
            user
        }
    },
    components: {
        Navbar,
        FondoFrutas,
        Footer,
        FormActualizaFoto
    },

}
</script>
