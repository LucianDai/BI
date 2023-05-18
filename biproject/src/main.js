import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'

// ajax
import http from '@/utils/http.js'
Vue.config.productionTip = false
Vue.prototype.$http = http // ajax请求方法

import Axios from "axios"					//axios接口引用
Vue.prototype.$axios = Axios

import qs from "qs"							//qs引用
Vue.prototype.$qs = qs;



new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
