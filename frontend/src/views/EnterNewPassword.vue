//Credit to tutorials for aiding  - Coding with Justin, Traversy Media, 4ums 


<template>
  <div class="container">
    <p id="back" @click.prevent="goBack()">
      <font-awesome-icon :icon="['fas', 'arrow-left']" />
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
      <div class="title">
        <h2>Reset Your Password</h2>
      </div>
      <div class="input">
        <input
          v-model="passwordField1"
          maxlength="34"
          placeholder="New Password"
          spellcheck="false"
          type="password"
        />
      </div>
      <label
        v-if="notMatching"
        style="
          color: red;
          display: flex;
          position: relative;
          margin-left: auto;
          margin-right: auto;
          margin-bottom: 10px;
        "
      >
        Passwords don't match</label
      >
      <div class="input">
        <input
          v-model="passwordField2"
          maxlength="38"
          placeholder="Confirm New Password"
          spellcheck="false"
          type="password"
        />
      </div>
      <button
        class="login-btn"
        style="margin-left: auto; margin-right: auto"
        type="submit"
        @click.stop="submitPassword()"
      >
        Sign in
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import LoginPage from "@/views/LoginPage";

export default {
  name: "EnterNewPassword",
  data() {
    return {
      passwordField1: "",
      passwordField2: "",
      hover: false,
      notMatching: false,
    };
  },
  methods: {
    submitPassword() {
      if (this.isMatching()) {
        this.notMatching = true;
      } else {
        this.notMatching = false;
        axios
          .post("/api/users/forgot_password/change_password/", {
            user_id: this.$route.query.id,
            code: this.$route.query.code,
            password: this.passwordField1,
            password_repeat: this.passwordField2,
          })
          .then(() => {
            this.$router.push(LoginPage);
          })
          .catch((error) => {
            console.error(error.response.data);
          });
      }
    },
    goBack() {
      this.$router.push("/login");
    },
    isMatching() {
      return this.passwordField1 !== this.passwordField2;
    },
  },
};
</script><style scoped src="@/assets/styling.css">
</style>
