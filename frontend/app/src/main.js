import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import routers from './routers'
import store from './stores';
import VueCookies from 'vue-cookies';

import { library } from '@fortawesome/fontawesome-svg-core'
import {
    faUserSecret,
    faCirclePlay,
    faCircleStop,
    faMoneyBillTrendUp,
    faArrowUpRightFromSquare,
} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret, faCirclePlay, faCircleStop, faMoneyBillTrendUp, faArrowUpRightFromSquare)

const app = createApp(App)
app.use(VueCookies)
app.use(store)
app.use(routers)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')