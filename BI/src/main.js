import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// 引入字体的文件
import './assets/font/iconfont.css'
// 引入全局的样式文件
import './assets/css/global.less'
// import axios from 'axios'
// import request from './utils/request'
import axios from "axios"
// 1
// import SocketService from '@/utils/socket_service'
// 对服务端进行websocket的连接 2
// SocketService.Instance.connect()
// 其他的组件  this.$socket 3
// Vue.prototype.$socket = SocketService.Instance
// 请求基准路径的配置
// axios.defaults.baseURL = 'http://localhost:8000/keshihua/'
// axios.defaults.baseURL = '/keshihua'
// 将axios挂载到Vue的原型对象上
// 在别的组件中 this.$http
// Vue.prototype.$http = request
import request from './axios/axios.js'//封装的axios请求
Vue.prototype.$axios = axios;

Vue.prototype.$http = request

// 将全局的echarts对象挂载到Vue的原型对象上
// 别的组件中 this.$echarts
Vue.prototype.$echarts = window.echarts

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
