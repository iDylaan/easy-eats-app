<template>
    <html lang="es">
      <FondoFrutas />
        <Navbar/>
<head>
 <meta charset="UTF-8">
<title>Mis recetas favoritas</title>
</head>
    <body>
      
      <h1>Mis Recetas Favoritas</h1>
      
      <nav>
      <ul>
        <li> <a href="#huevos">Huevos Fritos</a></li>
        <li><a href="#tortilla">Tortilla de Patatas</a></li>
        <li><a href="#Ensaladilla">Ensaladilla Rusa</a></li>
      </ul>
      </nav>
      
      <article id="huevos">
      <h2>Huevos Fritos </h2>
      
      <img src="http://www.demoslavueltaaldia.com/sites/default/files/huevos-fritos-vuelta-vuelta.jpg" alt="Foto de huevos fritos" width=200>
      
      <p>Esta va a ser mi receta favorita</p>
      <h3>Lista de ingredientes:</h3>
      <ul>
        <li>Huevos</li>
        <li>Aceite</li>
        <li>Sal</li>
      </ul>
      <h3>Preparación:</h3>
      <ol>
        <li> Calentar el aceite</li>
        <li> Cuando esté caliente, echar el huevo en la sartén</li>
        <li>Cuando tenga puntillas, sacar el huevo de la sartén</li>
        <li>Añadir sal al gusto</li>
      </ol>
      </article>
      
      <article id="tortilla">
      <h2>Tortilla de Patatas</h2>
      
      <img src="https://es.rc-cdn.community.thermomix.com/recipeimage/flz0tm0r-a2069-162740-cfcd2-zlr8kinc/733f35bb-e440-4c4f-9b87-949a0e20e384/main/tortilla-de-patatas-con-cebolla.jpg" alt="Tortilla de patata" width=200>
      
      <p>Otra receta con huevos</p>
      <h3>Lista de Ingredientes:</h3>
      <ul>
        <li>Huevos</li>
        <li>Patatas</li>
        <li>Aceite</li>
        <li>Sal</li>
      </ul>
      <h3>Preparación:</h3>
      <ol>
        <li>Picar las patatas y pochar en el aceite</li>
        <li>Batir el huevo y mezclar con las patatas pochadas y escurridas</li>
        <li>Cuajar la mezcla en la sartén</li>
        <li>Dar la vuelta y cuajar por el otro lado</li>
      </ol>
      </article>
      
      
      <article id="Ensaladilla">
      <h2>Ensaladilla Rusa</h2>
      
      <img src="https://www.hogarmania.com/archivos/201702/receta-ensaladilla-rusa-848x477x80xX.jpg" alt="Ensaladilla rusa"
width=200>      
     <p> Perfecta para el verano</p>
      <h3>Lista de ingredientes</h3>
      <ul>
        <li>Patatas</li>
        <li>Zanahorias</li>
        <li>Cebolla</li>
        <li>Guisantes</li>
        <li>Aceitunas</li>
        <li>Mayonesa</li>
      </ul>
      <h3>Preparación</h3>
      <ol>
        <li>Cocer las patatas, zanahorias y guisantes</li>
        <li>Picar todas las verduras y mezclar</li>
        <li>Añadir mayonesa a todo el conjunto</li>
      </ol>
      </article>
    </body>
    <Footer/>
</html>

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