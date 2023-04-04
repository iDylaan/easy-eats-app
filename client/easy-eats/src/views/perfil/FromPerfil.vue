<template>
    <div class="fromPerfil">
        <Navbar />
        <FondoFrutas />

        <div class="formulario">
           
            
        
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