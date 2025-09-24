import Vue from 'vue'
import App from './App.vue'
import router from './router'
import dataV from '@jiaminghi/data-view'  //导入datav框架
import "./components/index.css"
import "./mock/index"
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.config.productionTip = false
Vue.use(dataV)  //添加到vue原型里去
Vue.use(ElementUI);
new Vue({
  el: '#app',
  router,
  render: h => h(App)
}).$mount('#app')
