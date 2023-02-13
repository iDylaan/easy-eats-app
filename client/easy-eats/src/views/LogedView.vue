<template>
    <div class="loged_page">
        <span v-if="isAdmin"> <AdminPage /> </span>
        <span v-else> <LogedPage /> </span>
    </div>
</template>
<script>
import LogedPage from '../components/login-signin/LogedPage';
import AdminPage from '../components/login-signin/AdminPage';
import jwtDecode from 'jwt-decode'
import { ref, onMounted } from 'vue';

export default {
    name: 'Loged',
    setup() {
        let isAdmin = ref(false);

        onMounted(() => {
            if (!localStorage.getItem('token')) {
                router.push('/login');
            }

            let decoded = jwtDecode(localStorage.getItem('token'));
            console.log(decoded['user_role'])
            isAdmin.value = decoded['user_role'] === 1 ? true : false;
        });

        return {
            isAdmin,
        };
    },
    components: {
        LogedPage,
        AdminPage
    }
}
</script>