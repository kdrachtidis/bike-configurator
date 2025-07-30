import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'bootstrap/dist/js/bootstrap'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { i18n } from './assets/i18n/index.js'

import App from './App.vue'

const app = createApp(App);
const pinia = createPinia();

app.use(i18n)
app.use(pinia)
app.mount('#app');
