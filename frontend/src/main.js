// Map and App functionality have been pulled from here 

import App from "./App.vue";
import Vue from "vue";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import router from "./router/router.js";
import VueGeolocation from 'vue-browser-geolocation'

Vue.config.productionTip = false
Vue.prototype.$authToken = localStorage.authToken ? JSON.parse(localStorage.authToken) : "none";
Vue.use(VueGeolocation)

Vue.component("font-awesome-icon", FontAwesomeIcon);
;

Vue.config.devtools = true;
Vue.config.productionTip = false;

// Cookie library
var VueCookie = require("vue-cookie");
Vue.use(VueCookie);

// Geo-components for Map 
import * as VueGoogleMaps from 'vue2-google-maps'
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyCGCbdVhx4c8tUTA8nvHhZuox94HC7x-VE'
  }
})
//Clipboard
import VueClipboard from "vue-clipboard2";
VueClipboard.config.autoSetContainer = true;

Vue.use(VueClipboard);
new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");

