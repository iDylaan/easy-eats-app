<template>
    <div class="signin">
        <Logo />
        <FormSignin />
    </div>
</template>
<script>
import FormSignin from '@/components/login-signin/FormSignin'; 
import Logo from '@/components/login-signin/LogoFixed';

export default {
    name: 'Signin',
    components: {
        FormSignin,
        Logo
    },
    setup() {

    }
}
</script>