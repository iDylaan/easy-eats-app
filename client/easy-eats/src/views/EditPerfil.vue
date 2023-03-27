<template>
	<nav class="navbar">

<div class="logo_containes">
   
        <!-- <img src="../../assets/imgs/icono_fondos_pscuros.png"> -->
    
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
  

    <button v-if="isLoged" @click="cerrarSesion">
        Cerrar Sesión
        <div class="arrow-wrapper">
            <div class="arrow"></div>

        </div>
    </button>

</div>

<div class="nav-item dropdown">
				<a href="#" data-toggle="dropdown" class="nav-item nav-link dropdown-toggle user-action"><img src="https://www.tutorialrepublic.com/examples/images/avatar/3.jpg" class="avatar" alt="Avatar"> Romo Mañon <b class="caret"></b></a>
				<div class="dropdown-menu">
					<a href="#" class="dropdown-item"><i class="fa fa-user-o"></i> Editar perfil</a>
					
					<div class="divider dropdown-divider"></div>
					<a href="#" class="dropdown-item"><i class="material-icons">&#xE8AC;</i> Cerrar Sesión</a>
				</div>
			</div>
			

<!-- <div class="btn">
    <font-awesome-icon icon="fa-solid fa-bars" />
</div> -->
</nav>
    <div>
        <h1 class="legend__title">
        ¡Edita tu perfil!
        </h1>

        <div class="container">
			<div class="row">
				<h3 style="text-align:center">Editar perfil</h3>
			</div>
			
			<form class="form-horizontal" method="POST" action="#" autocomplete="off">
				<div class="form-group">
					<label for="user" class="col-sm-2 control-label">user</label>
					<div class="col-sm-10">
						<input type="text" class="form-control" id="user" name="user" placeholder="user" required>
					</div>
				</div>
				
				<div class="form-group">
					<label for="tagline" class="col-sm-2 control-label">Tagline</label>
					<div class="col-sm-10">
						<input type="tagline" class="form-control" id="tagline" name="tagline" placeholder="tagline" required>
					</div>
				</div>
				
				<div class="form-group">
					<label for="imagen" class="col-sm-2 control-label">imagen</label>
					<div class="col-sm-10">
						<input type="imagen" class="form-control" id="imagen" name="imagen" placeholder="imagen">
					</div>
				</div>
				
				<div class="form-group">
					<label for="correo" class="col-sm-2 control-label">correo</label>
					<div class="col-sm-10">
						<input type="correo" class="form-control" id="correo" name="correo" placeholder="correo">
					</div>
				</div>

                <div class="form-group">
					<label for="contraseña" class="col-sm-2 control-label">contraseña</label>
					<div class="col-sm-10">
						<input type="contraseña" class="form-control" id="contraseña" name="contraseña" placeholder="contraseña">
					</div>
				</div>

                 <div class="form-group">
					<label for="estatura" class="col-sm-2 control-label">estatura</label>
					<div class="col-sm-10">
						<input type="estatura" class="form-control" id="estatura" name="estatura" placeholder="estatura">
					</div>
				</div>

                 <div class="form-group">
					<label for="peso" class="col-sm-2 control-label">peso</label>
					<div class="col-sm-10">
						<input type="peso" class="form-control" id="peso" name="peso" placeholder="peso">
					</div>
				</div>

				<div class="form-group">
					<div class="col-sm-offset-2 col-sm-10">
						<a href="#" class="btn btn-default">Regresar</a>
						<button type="submit" class="btn btn-primary">Guardar</button>
					</div>
				</div>
			</form>
		</div>
    </div>
</template>

<script>
export default {
    
}
</script>
