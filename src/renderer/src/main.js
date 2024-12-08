import 'primeicons/primeicons.css'
//PrimeVue
import PrimeVue from 'primevue/config'
import { definePreset } from '@primevue/themes'
import Aura from '@primevue/themes/aura'
import { Button, InputText, Carousel, Select, FileUpload, ProgressBar } from 'primevue'

const Noir = definePreset(Aura, {
  semantic: {
    primary: {
      50: '{zinc.50}',
      100: '{zinc.100}',
      200: '{zinc.200}',
      300: '{zinc.300}',
      400: '{zinc.400}',
      500: '{zinc.500}',
      600: '{zinc.600}',
      700: '{zinc.700}',
      800: '{zinc.800}',
      900: '{zinc.900}',
      950: '{zinc.950}'
    },
    colorScheme: {
      light: {
        primary: {
          color: '{zinc.950}',
          inverseColor: '#ffffff',
          hoverColor: '{zinc.900}',
          activeColor: '{zinc.800}'
        },
        highlight: {
          background: '{zinc.950}',
          focusBackground: '{zinc.700}',
          color: '#ffffff',
          focusColor: '#ffffff'
        }
      },
      dark: {
        primary: {
          color: '{zinc.950}',
          inverseColor: '#ffffff',
          hoverColor: '{zinc.900}',
          activeColor: '{zinc.800}'
        },
        highlight: {
          background: '{zinc.950}',
          focusBackground: '{zinc.700}',
          color: '#ffffff',
          focusColor: '#ffffff'
        }
      }
    }
  }
})

//Vue
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)
app.use(PrimeVue, {
  theme: {
    preset: Noir,
    options: {
      darkModeSelector: ''
    }
  }
})

//Primevue
app.component('Button', Button)
app.component('InputText', InputText)
app.component('Carousel', Carousel)
app.component('Select', Select)
app.component('FileUpload', FileUpload)
app.component('ProgressBar', ProgressBar)

//Pinia
import { createPinia } from 'pinia'
const pinia = createPinia()
app.use(pinia)

//Vue router
import { createMemoryHistory, createRouter } from 'vue-router'
import Home from './views/Home.vue'
import Search from './views/Search.vue'
import Detail from './views/Detail.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/search', component: Search, name: 'search' },
  { path: '/detail', component: Detail, name: 'detail' }
]

const router = createRouter({
  history: createMemoryHistory(),
  routes
})
app.use(router)

app.mount('#app')
