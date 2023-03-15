<template>
    <div>
        <h1 class="legend__title">
        ¡Ediat tu perfil!
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


