<template>
    <div class="page-wrapper">
        <!-- Preloader -->
        <div class="preloader"></div>

        <HeaderWrapper />

    </div>
</template>
<script>
import HeaderWrapper from '@/components/page-wrapper/Header.vue';

export default {
    components: {
        HeaderWrapper
    }
}
</script>