<template>
    <FondoFrutas />
        <Navbar/>
        <div id="addEmployeeModal" class="modal fade">
			<div class="modal-dialog">
				<div class="modal-content">
					<form>
						<div class="modal-header">
							<h4 class="modal-title">Agregar Ingrediente</h4>
							
						</div>
						<div class="modal-body">
							<div class="form-group">
								<label>Nombre</label>
								<input type="nombre" class="form-control" required>
							</div>
							<div class="form-group">
								<label>Descripcion</label>
								<input type="descripcion" class="form-control" required>
							</div>
							<div class="form-group">
								<label>Precio</label>
								<input type="precio" class="form-control" required>
							</div>
							
						</div>
						<div class="modal-footer">
							<input type="button"   class="btn btn-default" data-dismiss="modal" value="Regresar">
							<input type="submit" class="btn btn-success" value="Agregar">
						</div>
					</form>
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
