import { createApp, Vue } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import $ from 'jquery';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faRightToBracket, faUser } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(
    faRightToBracket,
    faUser
)


createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(store).use(router).mount('#app')