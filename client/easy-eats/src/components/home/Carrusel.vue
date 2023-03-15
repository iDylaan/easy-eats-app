<template>
    <div>
        <Swiper
        :modules="modules"
        :spaces-between="20"
        :loop="true"
        :pagination="{clickable: true}"
        :autoplay="{
            delay: 3000,
            disableOnInteractions: false,
            pauseOnMouseEnter: true
        }">

            <swiper-slide v-for="text in swiperTextBase" :key="text.description">
                <div>
                    <h1>{{ text.author }}</h1>
                    <p>{{ text.description }}</p>
                </div>
                <img :src="text.image" alt="image">
            </swiper-slide>
        </Swiper>
    </div>
</template>
<script>
import { Swiper, SwiperSlide} from 'swiper/vue';
import { Autoplay, Pagination } from 'swiper';
import { ref } from 'vue';

export default {
    name: 'Carrusel',
    components: {Swiper, SwiperSlide},
    setup() {
        const swiperTextBase = ref([
            {
                author: 'Elon musk',
                description: 'Esta es una descripcion de Elon Musk',
                image: '../assets/imgs/Banner-Food1.png'
            },
            {
                author: 'Bill Gates',
                description: 'Esta es una descripcion de Bill Gates',
                image: '../assets/imgs/Banner-Food2.png'
            },
            {
                author: 'Jeff Bezos',
                description: 'Esta es una descripcion de Jeff Bezos',
                image: '../assets/imgs/Banner-Food3.png'
            },
        ])
        return {modules: [Pagination, Autoplay], swiperTextBase}
    }
}
</script>