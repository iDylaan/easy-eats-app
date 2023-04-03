<template>
    <div class="registrar-receta">
        <form>

            <div class="campos-obligatorios">
                <div class="detalles-receta-title_container">
                    <h4>Datos de la receta</h4>
                </div>
                <div class="inputs-datos-receta__container">
                    <div class="form-group">
                        <label for="name">Nombre <span class="required__text">*</span></label>
                        <input type="text" class="form-control" id="name">
                    </div>
                    <div class="form-group">
                        <label for="description">Descripción <span class="required__text">*</span></label>
                        <textarea name="description" id="description" rows="4" minlength="25" maxlength="300"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="descripcion">Tiempo de preparación <span class="required__text">*</span></label>
                        <input type="text" class="form-control" id="descripcion">
                    </div>
                    <div class="form-group">
                        <label for="dinners">Personas <span class="required__text">*</span></label>
                        <input type="number" class="form-control" id="dinners">
                    </div>
                </div>
            </div>

            <div class="datos-nutricionales">
                <div class="datos-nutricionales-title_container">
                    <h4>Datos Nutricionales <span class="optional__text">(Opcionales)</span></h4>
                </div>
                <div class="inputs-nutricionales__container">
                    <div class="form-group">
                        <label for="calories">Calorias</label>
                        <input type="number" class="form-control" id="calories">
                    </div>
                    <div class="form-group">
                        <label for="fats">Grasas</label>
                        <input type="number" class="form-control" id="fats">
                    </div>
                    <div class="form-group">
                        <label for="carbs">Carbohidratos</label>
                        <input type="number" class="form-control" id="carbs">
                    </div>
                    <div class="form-group">
                        <label for="protein">Proteina</label>
                        <input type="number" class="form-control" id="protein">
                    </div>
                    <div class="form-group">
                        <label for="satured_fats">Grasas Saturadas</label>
                        <input type="number" class="form-control" id="satured_fats">
                    </div>
                    <div class="form-group">
                        <label for="sodium">Sodio</label>
                        <input type="number" class="form-control" id="sodium">
                    </div>
                    <div class="form-group">
                        <label for="fiber">Fibra</label>
                        <input type="number" class="form-control" id="fiber">
                    </div>
                    <div class="form-group">
                        <label for="sugars">Azucares</label>
                        <input type="number" class="form-control" id="sugars">
                    </div>
                </div>
            </div>

            <div class="buttons-section__container">
                <button class="btn btn-cancelar">Cancelar</button>
                <input  class="btn btn-siguiente" type="sumbit" value="Siguiente">
            </div>
        </form>
    </div>
</template>
<script>
export default {

}
</script>