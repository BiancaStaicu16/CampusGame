<template>
  <div id="app">

     <qrcode-stream id="qrscan" @decode="onDecode" @init="onInit"></qrcode-stream>
   <div class="login-page">

      <div class="container">
         <div class="row">
            <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
               <div v-if="!registerActive" class="card login" v-bind:class="{ error: emptyFields }">
                  <h1>Sign In</h1>
                  <form class="form-group">
                     <input v-model="emailLogin" type="email" class="form-control" placeholder="Email" required>
                     <br><br><input v-model="passwordLogin" type="password" class="form-control" placeholder="Password" required>
                     <br><br><input type="submit" class="btn btn-primary" @click="doLogin">
                    <br><br>
                     <input type="checkbox" id="login" />
                     <label><a href="url_for('gdpr_policy')">Read our GDPR policy</a></label>
                     <br>
                     <p><a href="url_for('gdpr_policy')">Campus Game | Terms and Conditions</a></p>
                  </form>
               </div>

               <div v-if="!registerActive" class="card login" v-bind:class="{ error: emptyFields }">
                  <h1>Sign Up</h1>
                  <form class="form-group">
                     <input v-model="emailReg" type="email" class="form-control" placeholder="Email" required>
                     <br><br><input v-model="passwordReg" type="password" class="form-control" placeholder="Password" required>
                     <br><br><input v-model="confirmReg" type="password" class="form-control" placeholder="Confirm Password" required>
                     <br><br><input type="submit" class="btn btn-primary" @click="doRegister">
                     <p>Already have an account? <a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign in here</a>
                     </p>
                  </form>
               </div>
            </div>
         </div>

      </div>
   </div>
</div>
</template>
<!--<div id="app">
  <h1>Login Page</h1>
  <ul>
    <li>
      <login></login>
    </li>
  </ul>
  </div>-->
<script>

import Login from './components/Login.vue'

export default {
  name: 'App',
  components: {
    Login
  },
  methods: {
    onDecode (url) {
      window.location.href = url
    },
    onInit (promise) {
      promise
        .then(console.log)
        .catch(console.error)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#qrscan {
  width:600px;
}

</style>
