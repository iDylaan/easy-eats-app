<template>
	<div class="subirReceta">
		<FondoFrutas />
		<Navbar />
		<div class="title">
			<h1 style="text-align:center">Nueva Receta</h1>
		</div>

		<div class="form-recet">
			<div class="form-group">
				<label for="nomReceta" class="form-label">Nombre de su receta:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" id="tagline" name="Nombre de la Receta" placeholder="nomReceta"
						required>
				</div>
			</div>
			<div class="form-group">
				<label for="categoria" class="form-label">Categoria:</label>
				<div class="form-input">
					<select class="form-control" id="Eres diabetico" name="Eres diabetico">
						<option value="Ens">Ensalada</option>
						<option value="Navi">Navideña</option>
						<option value="Diab">Diabetico</option>
						<option value="Feb">14 de Febrero</option>
					</select>
				</div>
			</div>

			<div class="form-group">
				<label for="imagen" class="form-label">Imagen:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" id="tagline" name="imagen" placeholder="Imagen" required>
				</div>
			</div>

			<div class="form-group">
				<label for="ingredientes" class="form-label">Ingredientes:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" id="tagline" name="ingredientes" placeholder="Ingredientes"
						required>
				</div>
			</div>

			<div class="form-group">
				<label for="porciones" class="form-label">Porciones:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" id="tagline" name="porciones" placeholder="Porciones"
						required>
				</div>
			</div>

			<div class="form-group">
				<label for="pasos" class="form-label">Pasos a seguir:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" name="pasos" placeholder="Pasos">
				</div>
			</div>

			<div class="form-group">
				<label for="time" class="form-label">Cooking-time:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" name="time" placeholder="Cook Time">
				</div>
			</div>

			<div class="form-group">
				<label for="personas" class="form-label">No. de personas:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" name="personas" placeholder="Personas">
				</div>
			</div>

			<div class="form-group">
				<label for="calorías" class="form-label">Calorias:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" name="calorías" placeholder="Calorías">
				</div>
			</div>

			<div class="form-group">
				<label for="carbohidratos" class="form-label">Carbohidratos:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" name="carbohidratos" placeholder="Carbohidratos">
				</div>
			</div>

			<div class="form-group">
				<label for="proteínas" class="form-label">Proteínas:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" name="proteínas" placeholder="Proteínas">
				</div>
			</div>

			<div class="form-group">
				<label for="sodio" class="form-label">Sodio:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" name="sodio" placeholder="Sodio">
				</div>
			</div>

			<div class="form-group">
				<label for="azucares" class="form-label">Azucares:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" name="azucares" placeholder="Azucares">
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
	name: "subirReceta",

	components: {
		Navbar,
		FondoFrutas,
		Footer
	}
}
</script>

