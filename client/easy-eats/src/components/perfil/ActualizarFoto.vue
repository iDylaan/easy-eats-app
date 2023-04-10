<template>
    <div class="actualizarFoto">

        <div class="fromFoto">
            <form class="form" enctype="multipart/form-data">
                <span class="form-title">Actualizar Foto</span>

                <div class="avatar-image__container">
                    <div class="perfil-usuario-avatar">
                        <div class="perfil-usuario-image">
                            <img src="" id="imagen" alt="" :class="imageAdapter">
                        </div>
                    </div>
                </div>

                <p class="form-paragraph">
                    El archivo debe ser una imagen
                </p>
                <label for="file-input" class="drop-container">
                    <span class="drop-title">Arrastre una imagen</span>
                    o
                    <input @input="mostrarImagen" type="file" accept=".png, .jpg, .jpeg" multiple name="image"
                        id="file-input">
                </label>


                <div class="boton">
                    <button @click="guardarImagen" @click.prevent="handleClick">
                        <div class="svg-wrapper-1">
                            <div class="svg-wrapper">
                                <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M0 0h24v24H0z" fill="none"></path>
                                    <path
                                        d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"
                                        fill="currentColor"></path>
                                </svg>
                            </div>
                        </div>
                        <span>Guardar</span>
                    </button>
                </div>


                <div class="botonCancelar">

                    <button class="noselect" @click.prevent="handleClick" @click="ocultarForm">
                        <span class="text">Cancelar</span>
                        <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                                viewBox="0 0 24 24">
                                <path
                                    d="M24 20.188l-8.315-8.209 8.2-8.282-3.697-3.697-8.212 8.318-8.31-8.203-3.666 3.666 8.321 8.24-8.206 8.313 3.666 3.666 8.237-8.318 8.285 8.203z">
                                </path>
                            </svg></span>
                    </button>
                </div>
            </form>



        </div>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';

import axios from 'axios';
import jwtDecode from 'jwt-decode'


export default {
    name: "actualizarFoto",
      props: {
        user_id: {
            type: Number,
            required: true
        }
    },
    setup(props) {
        // const router = useRouter(); 
        const imageAdapter = ref('');
        const user_id = ref(props.user_id);


        const handleClick = (e) => {
            e.preventDefault();
        }

        const ocultarForm = () => {
            // handleClick(e)
            document.querySelector('.actualizar-perfil__container').style.display = 'none';
        }

        const mostrarImagen = (e) => {
            const files = e.target.files;
            if (files.length > 0) {
                const file = files[0];
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onloadend = () => {
                    const img = new Image();
                    img.src = reader.result;
                    img.onload = () => {
                        imageAdapter.value = img.width > img.height
                            ? 'contain'
                            : 'cover';
                        document.getElementById('imagen').src = reader.result;
                    };
                };
            }
        };


        const guardarImagen = async () => {
            const input = document.querySelector('#file-input');
            const file = input.files[0];
            const formData = new FormData();
            formData.append('image', file);

            try {
                const response = await axios({
                    method: 'POST',
                    url: URL + '/pic_user/' + user_id,
                    data: formData,
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
                console.log(response);
                
            } catch (error) {
                alert('Error al subir la imagen');
                console.log(error);
            }
        }



        return {
            handleClick,
            ocultarForm,
            mostrarImagen,
            imageAdapter,
            guardarImagen
        }
    }

}
</script>