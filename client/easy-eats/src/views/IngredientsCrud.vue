<template>
	<FondoFrutas />
        <Navbar/>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<title>Ingredientes</title>
		<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round">
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
		<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

	</head>

	<body>
		<div class="container-xl">
			<div class="table-responsive">
				<div class="table-wrapper">
					<div class="table-title">
						<div class="row">
							<div class="col-sm-6">
								<h2>Tabla <b>Ingredientes</b></h2>
							</div>
							<div class="col-sm-6">
								<a href="#" class="btn btn-success" data-toggle="modal"><i
										class="material-icons">&#xE147;</i> <span>Agregar</span></a>
								
							</div>
						</div>
					</div>
					<table class="table table-striped table-hover">
						<thead>
							<tr>
								<th>
									
								</th>
								<th>Nombre</th>
								<th>Descripcion</th>
								<th>Precio</th>
							
								<th>Operaciones</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>
									
								</td>
								<td>Jitomate</td>
								<td>Tiene hojas fuertemente aromáticas con bordes dentados. Florece con abundancia y sus
									flores pequeñas y amarillas producen frutos muy coloreados —de tonos que van del
									amarillento al rojo—,
									debido a la presencia de pigmentos como el licopeno y los carotenos.</td>
								<td>$13</td>
								
								<td>
									<a href="#" class="edit" data-toggle="modal"><i class="material-icons"
											data-toggle="tooltip" title="Edit">&#xE254;</i></a>
									<a href="#" class="delete" data-toggle="modal"><i class="material-icons"
											data-toggle="tooltip" title="Delete">&#xE872;</i></a>
								</td>
							</tr>
							<tr>
								<td>
									
								</td>
								<td>Sal</td>
								<td>Sustancia consistente en cloruro de sodio, ordinariamente blanca, cristalina, de sabor
									propio y muy soluble en agua, que se emplea para sazonar y conservar alimentos,
									es muy abundante en las aguas del mar y también se encuentra en la corteza terrestre.
								</td>
								<td>$17</td>
								
								<td>
									<a href="#" class="edit" data-toggle="modal"><i class="material-icons"
											data-toggle="tooltip" title="Edit">&#xE254;</i></a>
									<a href="#" class="delete" data-toggle="modal"><i class="material-icons"
											data-toggle="tooltip" title="Delete">&#xE872;</i></a>
								</td>
							</tr>
							<tr>
								<td>
									
								</td>
								<td>Cebolla</td>
								<td>Forma parte de la familia de las liliáceas, a la que pertenece también el ajo y el
									puerro. Es una planta bienal de tallo subterráneo y reducido. El bulbo no es una raíz,
									sino un engrosamiento subterráneo del tallo de la planta.
									La verdadera raíz está formada por los filamentos que nacen en la parte inferior del
									bulbo.</td>
								<td>$27</td>
							
								<td>
									<a href="#" class="edit" data-toggle="modal"><i class="material-icons"
											data-toggle="tooltip" title="Edit">&#xE254;</i></a>
									<a href="#" class="delete" data-toggle="modal"><i class="material-icons"
											data-toggle="tooltip" title="Delete">&#xE872;</i></a>
								</td>
							</tr>
						</tbody>
					</table>
					
				</div>
			</div>
		</div>
		
</body>
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

