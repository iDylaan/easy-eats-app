<template>
    <div class="subirReceta">
        <div class="row">
			<h1 style="text-align:center">Crea Tú Receta</h1>
		</div>

		<div class="form-group">
			<label for="eres_diabetico" class="col-sm-2 control-label">¿Eres Diabético?:</label>
				<div class="col-sm-10">
					<select class="form-control" id="eres_Diabético" name="eres_diabetico">
						<option value="Si">SI</option>
						<option value="No">NO</option>
					</select>
				</div>
		</div>

		<div class="form-group">
			<label for="estatura" class="col-sm-2 control-label">Ingrese su Estatura:</label>
			<div class="col-sm-10">
				<input type="tagline" class="form-control" id="tagline" name="estatura" placeholder="estatura" required>
			</div>
		</div>

		<div class="form-group">
			<label for="peso" class="col-sm-2 control-label">Ingrese su Peso:</label>
			<div class="col-sm-10">
				<input type="peso" class="form-control" id="peso" name="peso" placeholder="peso">
			</div>
		</div>

		<div class="form-group">
			<div class="opciones">
				<a href="#" class="btn btn-default">Regresar</a>					<button type="submit" class="btn btn-primary">Guardar</button>
			</div>
		</div>
        
    </div>
</template>

