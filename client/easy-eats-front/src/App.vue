<script setup>
  const name = 'vue dinamico';
  const styleColor = "color: blue";
  const arrayColores = ["blue","red","peru"];
  const activo = true;
</script>

<template>
  <h1>Hola {{name.toUpperCase}}</h1>
  <h2 :style="styleColor">Soy azul</h2>
  <h2>
    {{ activo ? "Estoy activo" : "Estoy inactivo" }}

    <p v-if="activo">Estoy activo</p>
    <p v-else>Estoy inactivo</p>
  </h2>
</template>

<style>
h1{
  color: red;
}
</style>