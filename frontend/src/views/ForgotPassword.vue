// Edit this to include more conditions (before forked to repository) 

<template>
  <div class="container">
    <p id="back" @click.prevent="goBack()">
      Back
    </p>
    <div class="forgot-form">
      <div class="header">
        <div class="logo-container">
          <img
            class="logo-container"
            id="mainimg"
            src="@/assets/website-logo.png"
          />
        </div>
      </div>
      <div v-if="!sentEmail && invalidEmail">
        <div class="title">
          <h2>Reset Your Password</h2>
        </div>

        <div
          style="
            color: red;
            z-index: 2;
            text-align: center;
            margin-bottom: 10px;
          "
        >
          {{ this.errorMessage }}
        </div>
        <div class="input">
          <input
            v-model="emailField"
            placeholder="Email address"
            type="email"
          />
        </div>
        <div class="details">
          Your password cannnot be reset if you do not know your login details.
        </div>
        <br />
        <button class="login-btn" type="submit" @click.stop="submitEmail">
          Email Me
        </button>
      </div>
      <div v-else>
        We will send you a reset email to your entered address. 
      </div>
      <br />
    </div>
  </div>
</template>

<script>
import LoginPage from "@/views/LoginPage";
import axios from "axios";

export default {
  name: "ForgotPassword",
  data() {
    return {
      emailField: "",
      hover: false,
      sentEmail: false,
      invalidEmail: true,
      errorMessage: "",
    };
  },
  methods: {
    submitEmail() {
      axios
        .post("/api/users/forgot_password/request_verification_code/", {
          email: this.emailField,
        })
        .then(() => {
          this.sentEmail = true;
          this.invalidEmail = false;
          this.errorMessage = "";
        })
        .catch((error) => {
          this.invalidEmail = true;
          this.errorMessage =
            "This email ID does not exist";
          console.error(error.response.data);
        });
    },
    goBack() {
      this.$router.push(LoginPage);
    },
  },
};
</script>


<style scoped src="@/assets/styling.css">
</style>
