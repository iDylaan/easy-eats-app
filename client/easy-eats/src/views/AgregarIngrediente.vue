<template>
   <div class="subirReceta">
		<FondoFrutas />
		<Navbar />
		<div class="title">
			<h1 style="text-align:center">Nueva Ingrediente</h1>
		</div>

		<div class="form-recet">
			<div class="form-group">
				<label for="nomReceta" class="form-label">Nombre:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" id="tagline" name="nomReceta" 
						required>
				</div>
			</div>
			<div class="form-group">
				<label for="nomReceta" class="form-label">Descripción:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" id="tagline" name="nomReceta" 
						required>
				</div>
			</div>
			<div class="form-group">
				<label for="nomReceta" class="form-label">Precio:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" id="tagline" name="nomReceta" 
						required>
				</div>
			</div>
			
			
			<div class="form-group">
				<label for="imagen" class="form-label">Imagen:</label>
				<div class="form-input">
					<input type="file" class="form-control" id="tagline" name="imagen"  required>
				</div>
			</div>

			<div class="options-group">
				<div class="opciones">
					<a href="#" class="btn btn-default">Regresar</a>
					<button type="submit" class="btn btn-primary">Guardar</button>
				</div>
			</div>

		</div>
	</div>
	<Footer/>
</template>
<script>
import FondoFrutas from '../components/layout/FondoFrutas';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer.vue'; 

export default {
  name: "prefe",
  
  components: {
	Navbar,
	FondoFrutas,
	Footer
  }
}
</script>
