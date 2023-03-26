<template lang="">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
 
    <nav class="navbar">
   
   <div class="logo_containes">
      
           <img src="../../assets/imgs/icono_fondos_pscuros.png">
       
   </div>
   <div class="options_container">
   <ul>
       <li><a href="#">Home</a></li>
       <li><a href="#">Recetas</a></li>
       <li><a href="#">Saludable</a></li>
       <li><a href="#">Nosotros</a></li>
       <li><a href="#">Contacto</a></li>
   </ul>
   </div>
   
   <div class="profile-options">
       <button v-if="!isLoged" @click="iniciarSesion">
           Iniciar Sesion
           <div class="arrow-wrapper">
               <div class="arrow"></div>
   
           </div>
       </button>
   
       <button v-if="isLoged" @click="cerrarSesion">
           Cerrar Sesión
           <div class="arrow-wrapper">
               <div class="arrow"></div>
   
           </div>
       </button>
   
   </div>
   <div class="signup-form">
    <form action="#" method="post" class="form-horizontal">
      	<div class="row">
        	<div class="col-8 offset-4">
				<h2>Preferencias</h2>
			</div>
            <img src="https://www.example.com/images/dinosaur.jpg">	
      	</div>			
        <div class="form-group row">
			<label class="col-form-label col-4">Eres diabetico?</label>
			<div class="col-8">
                <input type="text" class="form-control" name="username" required="required">
            </div>        	
        </div>
		<div class="form-group row">
			<label class="col-form-label col-4">Estatura</label>
			<div class="col-8">
                <input type="email" class="form-control" name="email" required="required">
            </div>        	
        </div>
		<div class="form-group row">
			<label class="col-form-label col-4">Peso</label>
			<div class="col-8">
                <input type="password" class="form-control" name="password" required="required">
            </div>        	
        </div>       	
        </div>
		<div class="form-group row">
			<div class="col-8 offset-4">
				<button type="submit" class="btn btn-primary btn-lg">Confirmar</button>
			</div>  
		</div>		      
    </form>
</div>
   
   <!-- <div class="btn">
       <font-awesome-icon icon="fa-solid fa-bars" />
   </div> -->
   </nav>
   
   </template>
   <script>
   export default {
       
   }

   </script>