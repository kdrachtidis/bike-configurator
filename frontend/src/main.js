import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'bootstrap/dist/js/bootstrap'

import { createApp } from 'vue'

import { i18n } from './assets/i18n/index.js'

import App from './App.vue'
//import { createPinia } from 'pinia'

//const pinia = createPinia();

createApp(App)
    .use(i18n)
    .mount('#app');
    //.use(pinia)
