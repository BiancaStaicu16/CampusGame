<template>
  <div class="container">
    <p id="back" @click="$router.go(-1)">
      <font-awesome-icon :icon="['fas', 'arrow-left']" />
      Back
    </p>
    <div class="register-form">
      <div class="header">
        <div class="logo-container">
          <img
            class="logo-container"
            id="mainimg"
            src="@/assets/website-logo.png"
          />
        </div>
      </div>
      <div v-if="showRequirements" class="pass-requirements">
        <p>Password requirements:</p>
        <ul>
          <li :class="{ fulfilled: lowercase }">At least 1 lower case</li>
          <li :class="{ fulfilled: uppercase }">At least 1 upper case</li>
          <li :class="{ fulfilled: containsNumber }">A number</li>
          <li :class="{ fulfilled: noSpaces }">No spaces</li>
          <li :class="{ fulfilled: nineChars }">At least 9 characters long</li>
        </ul>
      </div>

      <div class="title">
        <h1>Update Your Password</h1>
      </div>

      <div>
        <div class="input">
          <input v-model="password" placeholder="Password" type="password" />
        </div>
        <div class="input">
          <input
            v-model="passwordConfirmation"
            placeholder="Confirm Password"
            type="password"
          />
          <p style="color: red; font-size: 12px">{{ errMessage }}</p>
        </div>

        <div>
          <p style="color: red; font-size: 12px">{{ termErrMessage }}</p>
        </div>
        <div>
          <button class="register-btn" @click="registerUser()">Update</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterPage",
  data() {
    return {
      password: "",
      passwordConfirmation: "",

      showRequirements: false,
      lowercase: false,
      uppercase: false,
      nineChars: false,
      noSpaces: true,
      containsNumber: false,

      errMessage: "",
      termErrMessage: "",
    };
  },
  watch: {

    password: function () {
      // Check 9 character password
      this.nineChars = this.password.length >= 9;
      // Check for white space
      this.noSpaces = !/\s/g.test(this.password) ? true : false;
      this.lowercase = /[a-z]/.test(this.password) ? true : false;
      this.uppercase = /[A-Z]/.test(this.password) ? true : false;
      this.containsNumber = /[0-9]/.test(this.password) ? true : false;
    },
    passwordConfirmation: function () {
      if (
        this.passwordConfirmation !== "" &&
        this.passwordConfirmation !== this.password
      ) {
        this.errMessage = "Passwords do not match";
      } else {
        this.errMessage = "";
      }
    },

    isTermsAgreed: function () {
      if (this.termErrMessage !== "" && this.isTermsAgreed) {
        this.termErrMessage = "";
      }
    },
  },
  methods: {
    navigate(path) {
      this.$router.push(path);
    },
    registerUser() {
      if (this.validatePassword() === false) {
        this.showRequirements = true;
        return false;
      }

      axios
        .get("/api/users/me")
        .then((response) => {
          axios
            .put("/api/users/me", {
              email: response.data.email,
              username: response.data.username,
              password: this.password,
              first_name: response.data.firstName,
              last_name: response.data.lastName,
              is_teacher: response.data.isTeacher,
              password_repeat: this.passwordConfirmation,
            })
            .then(() => {
              this.errMessage = "";
              this.termErrMessage = "";
              this.$router.push({ name: "LoginPage" });
            })
            .catch((error) => {
              this.errMessage = error.response.data;
            });
        })
        .catch((error) => {
          this.errMessage = error.response.data;
        });
    },

    validatePassword() {
      if (this.password.length >= 9) {
        this.nineChars = true;
      } else {
        this.nineChars = false;
        return false;
      }
      // Check for white space
      if (/\s/g.test(this.password)) {
        this.noSpaces = false;
        return false;
      } else {
        this.noSpaces = true;
      }
      if (/[a-z]/.test(this.password)) {
        this.lowercase = true;
      } else {
        this.lowercase = false;
        return false;
      }
      if (/[A-Z]/.test(this.password)) {
        this.uppercase = true;
      } else {
        this.uppercase = false;
        return false;
      }
      if (/[0-9]/.test(this.password)) {
        this.containsNumber = true;
      } else {
        this.containsNumber = false;
        return false;
      }
    },
  },
};
</script>


<style scoped src="@/assets/styling.css">
</style>
