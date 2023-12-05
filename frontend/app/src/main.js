import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import routers from './routers'
import store from './stores';
import VueCookies from 'vue-cookies';
import axiosInstance from './libs/index'

import { library } from '@fortawesome/fontawesome-svg-core'
import {
    faUserSecret,
    faCirclePlay,
    faCircleStop,
    faMoneyBillTrendUp,
    faArrowUpRightFromSquare,
    faTrash,
    faFire,
    faPlay,
    faStop,
} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import moment from 'moment';
import 'moment-timezone'

moment.tz.setDefault('Asia/Seoul');

library.add(
    faUserSecret,
    faCirclePlay,
    faCircleStop,
    faMoneyBillTrendUp,
    faArrowUpRightFromSquare,
    faTrash,
    faFire,
    faPlay,
    faStop,
)

const app = createApp(App)
app.config.globalProperties.$axios = axiosInstance;
app.config.globalProperties.$moment = moment;
app.use(VueCookies)
app.use(store)
app.use(routers)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')