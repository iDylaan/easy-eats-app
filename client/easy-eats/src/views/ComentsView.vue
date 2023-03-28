<template>
    <FondoFrutas />
        <Navbar/>
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Comentarios</title>
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
                            <h2>Tabla <b>Comentarios</b></h2>
                        </div>
                       
                    </div>
                </div>
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th>
                                <span class="custom-checkbox">
                                    <input type="checkbox" id="selectAll">
                                    
                                </span>
                            </th>
                            <th>Comentarios</th>
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
                            <td>lsbe</td>

                            <td>
                               
                                <a href="#" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <span class="custom-checkbox">
                                    <input type="checkbox" id="checkbox2" name="options[]" value="1">
                                    <label for="checkbox2"></label>
                                </span>
                            </td>
                            <td>Sal</td>
                            <td>

                                <a href="#" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <span class="custom-checkbox">
                                    <input type="checkbox" id="checkbox3" name="options[]" value="1">
                                    <label for="checkbox3"></label>
                                </span>
                            </td>
                            <td>Cebolla</td>
                            <td>
                                
                                <a href="#" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                            </td>
                        </tr>				
                    </tbody>
                </table>
                
            </div>
        </div>        
    </div>
   
  
    <Footer/>
    </body>
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
    
    
    