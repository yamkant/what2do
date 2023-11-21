import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import routers from './routers'
import store from './stores';
import VueCookies from 'vue-cookies';


const app = createApp(App)
app.use(VueCookies)
app.use(store)
app.use(routers)
app.mount('#app')