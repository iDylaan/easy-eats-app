<template>
    <div>
        <div class="carousel__container">
            <div class="carousel__wrapper">
                <div v-for="(slide, index) in slides" :key="index" class="carousel__slide">
                    <img :src="slide.image" alt="Slide image">
                </div>
            </div>
            <div class="carousel__pagination"></div>
            <div class="carousel-button-prev"></div>
            <div class="carousel-button-next"></div>
        </div>
    </div>
</template>
<script>
import Swiper from 'swiper';

export default {
    name: 'Carrusel',
    setup() {
        const slides = [
            { image: '../../assets/imgs/Banner-Food1.png' },
            { image: '../../assets/imgs/Banner-Food2.png' },
            { image: '../../assets/imgs/Banner-Food3.png' }
        ];
        let currentIndex = 0;
        let intervalId = null;
        let swiper = null;

        const startCarousel = () => {
            intervalId = setInterval(() => {
                goToSlide(currentIndex + 1);
            }, 5000);
        }

        const goToSlide = index => {
            const numSlides = slides.length;
            currentIndex = (index + numSlides) % numSlides;

            clearInterval(intervalId);
            startCarousel();
        }

        const initSwiper = () => {
            swiper = new Swiper('.carousel__container', {
                loop: true,
                effect: 'coverflow',
                centeredSlides: true,
                autoplay: {
                    delay: 3000,
                    disableOnInteraction: false
                },
                coverflowEffect: {
                    rotate: 0,
                    stretch: 50,
                    depth: 100,
                    modifier: 1,
                    slideShadows: false,
                },
                pagination: {
                    el: '.carousel__pagination',
                    clickable: true
                },
                navigation: {
                    nextEl: '.carousel-button-next',
                    prevEl: '.carousel-button-prev',
                }
            })
            swiper.on('slideChange', () => {
                currentIndex = swiper.realIndex;
            });
        }

        initSwiper();
        startCarousel();

        return {
            slides
        }
    }
}
</script>