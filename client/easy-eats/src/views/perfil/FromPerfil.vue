<template>
    <div class="fromPerfil">
        <Navbar />
        <FondoFrutas />
        
        <div class="formulario">
           

            <div class="input__container">
                <label class="input__label">Nombre de usuario</label>
                <input placeholder="Escribe tu nombre de usuario" class="input" name="text" type="text">
                <label class="input__label">TagLine</label>
                <input placeholder="TagLine" class="input" name="text" type="text">
                <label class="input__label">Fecha de nacimiento</label>
                <input placeholder="Fecha de nacimiento" class="input" name="date" type="date">
                <label class="input__label">Correo electronico</label>     
                <input placeholder="example@example.com" class="input" name="email" type="email">
                <!-- <p class="input__description">What do you want to call yourself?</p> -->


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


            </div>
            
        
        </div>
   
        <!-- <Footer /> -->
    </div>
</template>
<script>
import FondoFrutas from '@/components/layout/FondoFrutas';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';

import { useRouter } from 'vue-router';

export default {
    name: "fromPerfil",
    setup(){
        const router = useRouter();
        const perfil = () => router.push("/detallesPerfil");

        return{
            perfil,
        }
    },
    components: {
    Navbar,
    FondoFrutas,
    Footer
  }

    
}
</script>