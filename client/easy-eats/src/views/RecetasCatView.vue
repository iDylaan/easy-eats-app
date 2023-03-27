<template>
    <div class="recetasCategoria">
        <FondoFrutas />
        <Navbar/>
        <div class="row">
			<h1 style="text-align:center">Recetas por Categoria</h1>
		</div>


		<div class="form-recet">
			<label for="eres_diabetico" class="col-sm-2 control-label">Categoria:</label> 
				<div class="col-sm-10">
					<select class="form-control" id="eres_Diabético" name="eres_diabetico">
						<option value="Ens">Ensalada</option>
						<option value="Navi">Navideña</option>
						<option value="Diab">Diabetico</option>
						<option value="Feb">14 de Febrero</option>
					</select>
				</div>
		</div>

		<div class="form-recet">
			<label for="pasos" class="col-sm-2 control-label">.....:</label>
			<div class="col-sm-10">
				<input type="tagline" class="form-control" name="pasos" placeholder="pasos">
			</div>
		</div>

		<div class="form-recet">
			<div class="opciones">
				<a href="#" class="btn btn-default">Regresar</a>
				<button type="submit" class="btn btn-primary">Guardar</button>
			</div>
		</div>
          
    </div>
</template>
<script>
import FondoFrutas from '../components/layout/FondoFrutas';
import Navbar from '../components/layout/Navbar';


export default {
  name: "recetasCategoria",
  
  components: {
    Navbar,
    FondoFrutas
  }
}
</script>

