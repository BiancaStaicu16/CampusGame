(function(e){function n(n){for(var r,c,i=n[0],u=n[1],d=n[2],s=0,b=[];s<i.length;s++)c=i[s],Object.prototype.hasOwnProperty.call(l,c)&&l[c]&&b.push(l[c][0]),l[c]=0;for(r in u)Object.prototype.hasOwnProperty.call(u,r)&&(e[r]=u[r]);a&&a(n);while(b.length)b.shift()();return o.push.apply(o,d||[]),t()}function t(){for(var e,n=0;n<o.length;n++){for(var t=o[n],r=!0,i=1;i<t.length;i++){var u=t[i];0!==l[u]&&(r=!1)}r&&(o.splice(n--,1),e=c(c.s=t[0]))}return e}var r={},l={index:0},o=[];function c(n){if(r[n])return r[n].exports;var t=r[n]={i:n,l:!1,exports:{}};return e[n].call(t.exports,t,t.exports,c),t.l=!0,t.exports}c.m=e,c.c=r,c.d=function(e,n,t){c.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:t})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,n){if(1&n&&(e=c(e)),8&n)return e;if(4&n&&"object"===typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(c.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var r in e)c.d(t,r,function(n){return e[n]}.bind(null,r));return t},c.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(n,"a",n),n},c.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},c.p="/static/vue/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],u=i.push.bind(i);i.push=n,i=i.slice();for(var d=0;d<i.length;d++)n(i[d]);var a=u;o.push([0,"chunk-vendors"]),t()})({0:function(e,n,t){e.exports=t("56d7")},"56d7":function(e,n,t){"use strict";t.r(n);t("e260"),t("e6cf"),t("cca6"),t("a79d");var r=t("7a23"),l=t("76d2"),o=t.n(l),c={id:"app"},i=Object(r["d"])("img",{src:o.a,id:"mainimg"},null,-1),u={class:"login-page"},d={class:"container"},a={class:"row"},s={class:"col-lg-4 col-md-6 col-sm-8 mx-auto"},b=Object(r["d"])("h1",null,"ExeTour",-1),p={class:"form-group"},f=Object(r["d"])("br",null,null,-1),O=Object(r["d"])("br",null,null,-1),j=Object(r["d"])("br",null,null,-1),g=Object(r["d"])("br",null,null,-1),m=Object(r["d"])("br",null,null,-1),h=Object(r["d"])("br",null,null,-1),y=Object(r["d"])("input",{type:"checkbox",id:"login"},null,-1),v=Object(r["d"])("label",null,[Object(r["d"])("a",{href:"url_for('gdpr_policy')"},"Read our GDPR policy")],-1),w=Object(r["d"])("br",null,null,-1),x=Object(r["d"])("p",null,[Object(r["d"])("a",{href:"url_for('gdpr_policy')"},"Campus Game | Terms and Conditions")],-1),P=Object(r["d"])("h1",null,"Sign Up",-1),k={class:"form-group"},R=Object(r["d"])("br",null,null,-1),_=Object(r["d"])("br",null,null,-1),L=Object(r["d"])("br",null,null,-1),S=Object(r["d"])("br",null,null,-1),A=Object(r["d"])("br",null,null,-1),C=Object(r["d"])("br",null,null,-1),U=Object(r["e"])("Already have an account? ");function q(e,n,t,l,o,q){return Object(r["g"])(),Object(r["c"])("div",c,[i,Object(r["d"])("div",u,[Object(r["d"])("div",d,[Object(r["d"])("div",a,[Object(r["d"])("div",s,[e.registerActive?Object(r["b"])("",!0):(Object(r["g"])(),Object(r["c"])("div",{key:0,class:Object(r["f"])(["card login",{error:e.emptyFields}])},[b,Object(r["d"])("form",p,[Object(r["i"])(Object(r["d"])("input",{"onUpdate:modelValue":n[0]||(n[0]=function(n){return e.emailLogin=n}),type:"email",class:"form-control",placeholder:"Email",required:""},null,512),[[r["h"],e.emailLogin]]),f,O,Object(r["i"])(Object(r["d"])("input",{"onUpdate:modelValue":n[1]||(n[1]=function(n){return e.passwordLogin=n}),type:"password",class:"form-control",placeholder:"Password",required:""},null,512),[[r["h"],e.passwordLogin]]),j,g,Object(r["d"])("input",{type:"submit",class:"btn",onClick:n[2]||(n[2]=function(){return e.doLogin&&e.doLogin.apply(e,arguments)})}),m,h,y,v,w,x])],2)),e.registerActive?Object(r["b"])("",!0):(Object(r["g"])(),Object(r["c"])("div",{key:1,class:Object(r["f"])(["card login",{error:e.emptyFields}])},[P,Object(r["d"])("form",k,[Object(r["i"])(Object(r["d"])("input",{"onUpdate:modelValue":n[3]||(n[3]=function(n){return e.emailReg=n}),type:"email",class:"form-control",placeholder:"Email",required:""},null,512),[[r["h"],e.emailReg]]),R,_,Object(r["i"])(Object(r["d"])("input",{"onUpdate:modelValue":n[4]||(n[4]=function(n){return e.passwordReg=n}),type:"password",class:"form-control",placeholder:"Password",required:""},null,512),[[r["h"],e.passwordReg]]),L,S,Object(r["i"])(Object(r["d"])("input",{"onUpdate:modelValue":n[5]||(n[5]=function(n){return e.confirmReg=n}),type:"password",class:"form-control",placeholder:"Confirm Password",required:""},null,512),[[r["h"],e.confirmReg]]),A,C,Object(r["d"])("input",{type:"submit",class:"btn btn-primary",onClick:n[6]||(n[6]=function(){return e.doRegister&&e.doRegister.apply(e,arguments)})}),Object(r["d"])("p",null,[U,Object(r["d"])("a",{href:"#",onClick:n[7]||(n[7]=function(n){return e.registerActive=!e.registerActive,e.emptyFields=!1})},"Sign in here")])])],2))])])])])])}var M=Object(r["d"])("input",{type:"checkbox",id:"login"},null,-1),T=Object(r["d"])("label",{for:"login"},"My Todo Item",-1),V=[M,T];function E(e,n,t,l,o,c){return Object(r["g"])(),Object(r["c"])("div",null,V)}var F={},D=t("6b0d"),G=t.n(D);const I=G()(F,[["render",E]]);var J=I,z={name:"App",components:{Login:J},methods:{onDecode:function(e){window.location.href=e},onInit:function(e){e.then(console.log).catch(console.error)}}};t("fa87");const B=G()(z,[["render",q]]);var H=B;Object(r["a"])(H).mount("#app")},"76d2":function(e,n,t){e.exports=t.p+"img/download.ec33e3d1.jpeg"},d09d:function(e,n,t){},fa87:function(e,n,t){"use strict";t("d09d")}});
//# sourceMappingURL=index.bdbdc2b3.js.map