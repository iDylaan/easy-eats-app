<template>
    <div class="receta-imagen">
        <form>

            <h4>Selecciona una imagen para tu receta</h4>
            <div class="image-section__container">
                <div class="image__container">
                    <div class="add-new-iamge" @click="clickInputFile">
                        <span><img src="" id="imagen" alt=""></span>
                        <span class="icono" id="icono-imagen"><font-awesome-icon icon="fa-solid fa-image" style="color: #ffae00;" /></span>
                    </div>
                    <input 
                    @change="mostrarImagen" 
                    type="file"
                    accept=".png, .jpg, .jpeg" 
                    multiple 
                    name="image" 
                    id="input-add-image">
                </div>
            </div>

            <div class="buttons-section__container">
                <button class="btn btn-cancelar" @click="goHome">Cancelar</button>
                <button class="btn btn-cancelar">Omitir</button>
                <input class="btn btn-siguiente" type="sumbit" value="Siguiente">
            </div>
        </form>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';

export default {
    name: 'ImagenForm',
    setup() {
        const router = useRouter();

        const goHome = () => {
            router.push('/');
        }

        const clickInputFile = () => {
            document.getElementById('input-add-image').click();
        }

        const mostrarImagen = (e) => {
            const files = e.target.files;
            if (files.length > 0) {
                ocultarIconoImagen();
                const file = files[0];
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onloadend = () => {
                    document.getElementById('imagen').src = reader.result;
                    document.querySelector('.add-new-iamge').style.opacity = '1';
                }
            }
        }

        function ocultarIconoImagen () {
            document.getElementById('icono-imagen').style.display = 'none';
        }

        return {
            goHome,
            clickInputFile,
            mostrarImagen
        }
    }
}
</script>