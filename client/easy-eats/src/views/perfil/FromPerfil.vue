<template>
    <div class="fromPerfil">
        <Navbar />
        <FondoFrutas />

        <div class="formulario">
            <div class="container">
		    <form>
			    <label for="arquivo">Choose a file:</label>
			    <input accept=".jpg, .jpeg, .png, .gif, .pdf" class="inpdddut" name="arquivo" id="arquivo" type="file">
			    <input value="Send" type="submit" class="inpdddut">
		    </form>
	    </div>

        
        </div>


    </div>
</template>
<script>
import FondoFrutas from '@/components/layout/FondoFrutas';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';

export default {
    name: "fromPerfil",
    setup(){

    },
    components: {
    Navbar,
    FondoFrutas,
    Footer
  }

    
}
</script>