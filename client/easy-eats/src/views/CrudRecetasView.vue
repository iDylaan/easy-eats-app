<template>
    <div class="recetasCategoria"></div>
    <FondoFrutas />
        <Navbar/>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Recetas</title>
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
                                <h2>Tabla <b>Recetas</b></h2>
                            </div>
                            <div class="col-sm-6">
                                <a href="" class="btn btn-success" data-toggle="modal"><i
                                        class="material-icons">&#xE147;</i> <span>Agregar</span></a>
                                <a href="#" class="btn btn-danger" data-toggle="modal"><i
                                        class="material-icons">&#xE15C;</i> <span>Eliminar</span></a>
                            </div>
                        </div>
                    </div>
                    <table class="table table-striped table-hover">
                        <thead>
                            <tr>
                                <th>
                                    <span class="custom-checkbox">
                                        <input type="checkbox" id="selectAll">
                                        <label for="selectAll"></label>
                                    </span>
                                </th>
                                <th>id</th>
                                <th>Nombre</th>
                                <th>Ingredientes</th>
                                <th></th>
                                <th></th>
                                <th></th>
                                <th></th>
                                <th>Calificación</th>
                                <th>Operaciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <span class="custom-checkbox">
                                        <input type="checkbox" id="checkbox1" name="options[]" value="1">
                                        <label for="checkbox1"></label>
                                    </span>
                                </td>
                                <td>1</td>
                                <td>Yesos</td>
                                <td>Yisus</td>
                                <td>Rodrigo de Jesus</td>
                                <td>jesusmanon00@gmail.com</td>
                                <td>
                                    <a href="#" class="edit" data-toggle="modal"><i class="material-icons"
                                            data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                    <a href="#" class="delete" data-toggle="modal"><i class="material-icons"
                                            data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <span class="custom-checkbox">
                                        <input type="checkbox" id="checkbox2" name="options[]" value="1">
                                        <label for="checkbox2"></label>
                                    </span>
                                </td>
                                <td>2</td>
                                <td>Brandon</td>
                                <td>Lic</td>
                                <td>Brandon Figueroa</td>
                                <td>brandon00@gmail.com</td>
                                <td>
                                    <a href="#" class="edit" data-toggle="modal"><i class="material-icons"
                                            data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                    <a href="#" class="delete" data-toggle="modal"><i class="material-icons"
                                            data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <span class="custom-checkbox">
                                        <input type="checkbox" id="checkbox3" name="options[]" value="1">
                                        <label for="checkbox3"></label>
                                    </span>
                                </td>
                                <td>3</td>
                                <td>Dany</td>
                                <td>Danyyy</td>
                                <td>Chaparro Marín</td>
                                <td>chaparro00@gmail.com</td>
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
  name: "prefere",
  
  components: {
    Navbar,
    FondoFrutas,
	Footer
  }
}
</script>
    
    
    