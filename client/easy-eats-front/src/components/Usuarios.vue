<template>
  <h1>Usuarios registrados</h1>
  <ul>
    <template v-for="user in users" :key="user.id">
        <li v-if="user.rol === 2">{{ user.name }} <button @click="eliminarUser(user.id)">Eliminar</button></li>
    </template>
  </ul>
  <h1>Admins registrados</h1>
  <ul>
    <template v-for="user in users" :key="user.id">
        <li v-if="user.rol === 1">{{ user.name }} <button @click="eliminarUser(user.id)">Eliminar</button></li>
    </template>
  </ul>
</template>

<script>
import { ref } from "vue";
export default {

    setup() {
        let users = ref( [
            {id: 1, name: "Daniel", rol: 2},
            {id: 2, name: "Ana Lilia", rol: 2},
            {id: 3, name: "Brandon", rol: 2},
            {id: 4, name: "Lucero", rol: 2},
            {id: 5, name: "Jesús", rol: 2},
            {id: 6, name: "Admin todopoderoso", rol: 1},
            {id: 7, name: "Otro admin", rol: 1}
        ] );

        const eliminarUser = (id) => {
          console.log(users.value['target'])
          const user = users.value.filter( function(user) {
            return user.id === id
          })
          console.log('Eliminando... a', user[0].name)

          // Proceso de eliminar
          users.value =  users.value.filter(user => {
            return user.id !== id
          }) 
          console.log(users)
        }

        return { users, eliminarUser };
    }
};
</script>

<style>

</style>