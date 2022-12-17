import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import VCalendar from 'v-calendar';
import 'v-calendar/dist/style.css';

createApp(App).use(store).use(router).use(VCalendar, {}).mount('#app')
