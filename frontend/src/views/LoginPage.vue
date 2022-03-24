<template>
  <div class="container">
    <div class="login-form">
      <div class="header">
        <div class="logo-container">
          <img
            class="logo-container"
            id="mainimg"
            src="@/assets/website-logo.png"
          />
        </div>
      </div>
      <div>
        <p v-if="failedLogin" class="error-message">
          Incorrect password or email
        </p>
      </div>

      <div class="title">
        <h1>ExeTour</h1>
      </div>

      <div class="input">
        <input v-model="email" placeholder="Email" type="text" />
      </div>
      <div class="input">
        <input
          v-model="password"
          placeholder="Password"
          type="password"
          @keyup.enter="loginUser()"
        />
      </div>

      <div class="terms">
        <div id="center-TC">
          <input v-model="isTermsAgreed" type="checkbox" />
          <span class="tc-link" @click="showTC = true"
            >Terms and Conditions | GDPR Policy</span
          >
        </div>
        <p style="color: red; font-size: 12px; text-align: center">
          {{ termErrMessage }}
        </p>
      </div>
      <div>
        <button class="login-btn" @click="loginUser()">Sign in</button>
      </div>
      <div class="text" @click.stop="navigate('login/forgot')">
        <p class="link">Forgot your password?</p>
      </div>

      <div class="text" style="margin-top: 40px">
        <p>
          Don't have an account?
          <a class="link" @click="navigate('register')">Sign up</a>
        </p>
      </div>
    </div>
    <div class="TC-popup">
      <div class="close-TC" v-if="showTC">
        <font-awesome-icon :icon="['fa', 'times']" @click="showTC = false" />
      </div>
      <TermsAndConditionsPopup v-if="showTC" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TermsAndConditionsPopup from "@/components/TermsAndConditionsPopup.vue";

export default {
  name: "LoginPage",
  components: {
    TermsAndConditionsPopup,
  },
  data() {
    return {
      email: "",
      password: "",
      showTC: false,
      failedLogin: false,
      isTermsAgreed: false,
      errMessage: "",
      termErrMessage: "",
    };
  },
  methods: {
    loginUser() {
      axios.post("/api/users/login/", {email: this.email, password: this.password})
          .then((response) => {
            localStorage.authToken = JSON.stringify(response.data.token);
            this.$router.push("/dashboard");
            location.reload();  // To refresh authToken after redirect
          })
          .catch((error) => {
            console.error(error);
            this.error = true;
          })
    }
  },
  watch: {
    isTermsAgreed: function () {
      if (this.termErrMessage !== "" && this.isTermsAgreed) {
        this.termErrMessage = "";
      }
    },
  },
};
</script>

<style scoped src="@/assets/styling.css">
</style>

