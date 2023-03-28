<template>
    <div class="reviewComments">
        <FondoFrutas />
        <Navbar/>
        <div class="titlePrin">
			<h1 style="text-align:center">Reseñas y Comentarios</h1>
		</div>

		<div class="form-deta">
			<div class="form-group">
					<label for="estatura" class="form-label">Reseña de la Receta:</label>
					<div class="form-input">
						<input type="tagline" class="form-control" id="tagline" name="estatura" placeholder="Estatura" required>
					</div>
			</div>

            <div class="form-group">
				<label for="estatura" class="form-label">Comentario de la Receta:</label>
				<div class="form-input">
					<input type="tagline" class="form-control" id="tagline" name="estatura" placeholder="Estatura" required>
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
  name: "reviewComments",
  
  components: {
    Navbar,
    FondoFrutas,
    Footer
  }
}
</script>

