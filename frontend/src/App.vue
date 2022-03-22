<template>
  <div id="app">
    <router-view />
    <!--Do not change -->
    <div
      v-if="
        this.$route.name !== 'LoginPage' &&
        this.$route.name !== 'RegisterPage' &&
        this.$route.name !== 'ForgotPassword' &&
        this.$route.name !== 'EnterNewPassword'
      "
      style="margin-bottom: 11vh"
    >
      <Navbar />
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import GoogleMap from "./views/Feed.vue";
export default {
  name: "App",
  components: {
    Navbar,
    GoogleMap,
  },
};
</script>

<style>
/* Do not change - ensures lower page content is visible above navbar */
body {
  min-height: 100vh;
  height: 100%;
  overflow: visible;
  background: #2e5477;
  margin-bottom: 11vh;
}
#app {
  font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
    "Lucida Sans", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
}
.navbar-container {
  margin-top: 200px;
}
.navigation-display {
  color: #7e7e7e;
  font-size: 12px;
  position: absolute;
  top: 10;
  left: 10;
  padding: 10px;
}

button {
  cursor: pointer;
  outline: none;
}
</style>
