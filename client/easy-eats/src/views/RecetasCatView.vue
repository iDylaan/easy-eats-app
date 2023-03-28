<template>
    <div class="recetasCategoria">
        <FondoFrutas />
        <Navbar/>
        <div class="titlePrin">
			<h1 style="text-align:center">Recetas por Categoria</h1>
		</div>

		<div class="form-cate">
			<div class="form-group">
			    <label for="eres_diabetico" class="form-label">Recetas para Dibeticos:</label> 
				<div class="form-input">
					<select class="form-control" id="eres_Diabético" name="eres_diabetico">
						<option value="Ens">Ensalada</option>
						<option value="Ens"></option>
					</select>
				</div>
			
		    </div>

			<div class="form-group">
				<label for="receta-nav" class="col-sm-2 control-label">Recetas Navideñas:</label>
				<div class="form-input">
					<select class="form-control" id="eres_Diabético" name="eres_diabetico">
						<option value="Ens">Pavo</option>
					</select>
				</div>
			</div>

			<div class="form-group">
				<label for="#receta_amor" class="col-sm-2 control-label">Recetas de Amor:</label>
				<div class="form-input">
					<select class="form-control" id="eres_Diabético" name="eres_diabetico">
						<option value="Ens">Fresas con crema</option>
						<option value="Ens">Cupcakes 14 de Febrero</option>
					</select>
				</div>
			</div>

			<div class="form-group">
				<label for="rectea_cumple" class="col-sm-2 control-label">Recetas para cumpleaños</label>
				<div class="form-input">
					<select class="form-control" id="eres_Diabético" name="eres_diabetico">
						<option value="Ens">Pastel de 3 leches</option>
						<option value="Ens">Pozole</option>
						<option value="Ens">Gelatina</option>
					</select>
				</div>
			</div>

			<div class="options-group">
				<div class="opciones">
					<a href="#" class="btn btn-default">Regresar</a>
					<button type="submit" class="btn btn-primary">Guardar</button>
				</div>
			</div>
		</div>    
		<Footer />    
    </div>
</template>
<script>
import FondoFrutas from '../components/layout/FondoFrutas';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer.vue'; 

export default {
  name: "recetasCategoria",
  
  components: {
    Navbar,
    FondoFrutas,
	Footer
  }
}
</script>

