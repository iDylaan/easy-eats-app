<template>
    <div class="actualizarFoto">
        <Navbar />
        <FondoFrutas />

        <div class="fromFoto">
            <form class="form">
                <span class="form-title">Actualizar Foto</span>
                <p class="form-paragraph">
                    El archivo debe ser una imagen
                    </p>
                <label for="file-input" class="drop-container">
                <span class="drop-title">Arrastre una imagen</span>
                o
                <input type="file" accept="image/*" required="" id="file-input">
                </label>


                <div class="boton">
                    <button>
                        <div class="svg-wrapper-1">
                            <div class="svg-wrapper">
                            <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z" fill="currentColor"></path>
                            </svg>
                            </div>
                        </div>
                        <span>Guardar</span>
                    </button>
                </div>


                <div class="botonCancelar">
                    
                    <button class="noselect" @click="perfil">
                        <span class="text" >Cancelar</span>
                        <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M24 20.188l-8.315-8.209 8.2-8.282-3.697-3.697-8.212 8.318-8.31-8.203-3.666 3.666 8.321 8.24-8.206 8.313 3.666 3.666 8.237-8.318 8.285 8.203z">
                        </path></svg></span>
                    </button>
                </div>
            </form>


            
        </div>


    </div>
</template>
<script>


import FondoFrutas from '@/components/layout/FondoFrutas';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';

import { useRouter } from 'vue-router';

export default {
  name: "actualizarFoto",
  setup() {
    const fromPerfil = () => router.push("/fromPerfil");
    const router = useRouter();
    const perfil = () => router.push("/detallesPerfil");

    return{
        fromPerfil,
        perfil
    }
  },
  components: {
    Navbar,
    FondoFrutas,
    Footer,
  },

}
</script>