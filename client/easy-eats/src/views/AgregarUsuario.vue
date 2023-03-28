<template>
      <FondoFrutas />
        <Navbar/>
         <!-- Edit Modal HTML -->
         <div id="addEmployeeModal" class="modal fade">
            <div class="modal-dialog">
                <div class="modal-content">
                    <form>
                        <div class="modal-header">
                            <h4 class="modal-title">Agregar Usuario</h4>
                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                        </div>
                        <div class="modal-body">
                            <div class="form-group">
                                <label>Username</label>
                                <input type="text" class="form-control" required>
                            </div>
                            <div class="form-group">
                                <label>username</label>
                                <input type="email" class="form-control" required>
                            </div>
                            <div class="form-group">
                                <label>tagline</label>
                                <textarea class="form-control" required></textarea>
                            </div>
                            <div class="form-group">
                                <label>Nombre</label>
                                <input type="text" class="form-control" required>
                            </div>
                            <div class="form-group">
                                <label>Correo</label>
                                <input type="text" class="form-control" required>
                            </div>


                        </div>
                        <div class="modal-footer">
                            <input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
                            <input type="submit" class="btn btn-success" value="Add">
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