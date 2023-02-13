<template>
  <h1>Usuarios registrados</h1>
  <ul>
    <template v-for="user in users" :key="user.id">
        <li v-if="user.id_rol === 2">{{ user.name }} {{ user.username }}#{{ user.tagline }} <button @click="eliminarUser(user.id)">Eliminar</button></li>
    </template>
  </ul>
  <h1>Admins registrados</h1>
  <ul>
    <template v-for="user in users" :key="user.id">
        <li v-if="user.id_rol === 1">{{ user.name }} {{ user.username }}#{{ user.tagline }} <button @click="eliminarUser(user.id)">Eliminar</button></li>
    </template>
  </ul>

  <button @click="agregarUserPrueba()">Usuario de prueba</button>
</template>

<script>
import { onMounted, ref } from "vue";
import axios from 'axios';
export default {

    setup() {
        const formData = new FormData()

        let users = ref( [] );

        let user_post =  {
            username: "userprueba",
            tagline: "7FHE2",
            name: "Prueba POST",
            email: "prueba@correo.com",
            password: "jhfuiehfsi",
            birth_of_date: "2023-02-08",
            birth_of_date: "2023-02-08",
            id_rol: 2
          }
        formData.append('data', JSON.stringify(user_post))

        onMounted(async () => {
          const response = await axios.get('http://localhost:4000/users');
          users.value = response.data
        })

        const agregarUserPrueba = async () => {
          try {
            const response = await axios({
              method: 'POST',
              url: 'http://localhost:4000/users',
              data: formData
            });

            if (response.statusText !== 'OK') {
                throw new Error({
                    message: 'Error'
                })
            }
            console.log(response.data);
          } catch (error) {
            console.log(error);
          }
        }

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
        return { users, eliminarUser, user_post, agregarUserPrueba };
    }
};
</script>

<style>

</style>