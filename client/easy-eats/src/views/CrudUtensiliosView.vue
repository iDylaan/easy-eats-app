<template>
	<div class="prefere">
		<FondoFrutas />
        <Navbar/>
		<div class="container">
			<div class="title_container">
				<h1 style="text-align:center">Preferencias</h1>
			</div>

			<div class="form__container">
				<div class="form-group">
					<label for="eres_Diabetico" class="form-label">¿Eres Diabético?</label>
					<div class="form-input">
						<select class="form-control" id="eres_Diabético" name="eres_Diabetico" >
							<option value="Si">SI</option>
							<option value="No">NO</option>
						</select>
					</div>
				</div>

				<div class="form-group">
					<label for="estatura" class="form-label">Ingrese su Estatura:</label>
					<div class="form-input">
						<input type="tagline" class="form-control" id="tagline" name="estatura" placeholder="Estatura" required>
					</div>
				</div>

				<div class="form-group">
					<label for="peso" class="form-label">Ingrese su Peso:</label>
					<div class="form-input">
						<input type="peso" class="form-control" id="peso" name="peso" placeholder="Peso">
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
	</div>
</template>
<script>
import FondoFrutas from '../components/layout/FondoFrutas';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer.vue'; 

export default {
  name: "prefere",
  
  components: {
    Navbar,
    FondoFrutas,
	Footer
  }
}
</script>


