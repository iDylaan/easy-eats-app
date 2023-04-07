<template>
    <div class="detallesPasos">
        <FondoFrutas />
        <Navbar/>
        <div class="titleDeta">
			<h1 style="text-align:center">Pasos de la Receta</h1>
		</div>

		<div class="form-deta">
			<div class="form-group">
				<label for="pasos" class="form-label">Pasos:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" id="tagline" name="pasos" placeholder="Detalles" required>
				</div>
			</div>

            <div class="options-group">
                <div class="opciones">
                    <a href="#" class="btn btn-default">Regresar</a>
                    <button type="submit" class="btn btn-primary">Guardar</button>
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
  name: "recetasCategoria",
  
  components: {
    Navbar,
    FondoFrutas,
    Footer
  }
}
</script>

