import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import routers from './routers'
import store from './stores';

const app = createApp(App)
app.use(store)
app.use(routers)
app.mount('#app')