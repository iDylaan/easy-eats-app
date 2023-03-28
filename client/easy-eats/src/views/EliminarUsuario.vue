<template>
    <FondoFrutas />
        <Navbar/>
      <div id="deleteEmployeeModal" class="modal fade">
            <div class="modal-dialog">
                <div class="modal-content">
                    <form>
                        <div class="modal-header">
                            <h4 class="modal-title">Eliminar Usuario</h4>
                           
                        </div>
                        <div class="modal-body">
                            <p>Seguro que quieres eliminarlo?</p>
                            <p class="text-warning"><small>Esta acción no se podra realizar nuevamente.</small></p>
                        </div>
                        <div class="modal-footer">
                            <input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
                            <input type="submit" class="btn btn-danger" value="Delete">
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
