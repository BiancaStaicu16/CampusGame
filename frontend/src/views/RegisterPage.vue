// Edit this to make it more precise with more conditions 

<template>
  <div class="container">
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
          <li :class="{ fulfilled: lowercase }">Atleast 1 lower case</li>
          <li :class="{ fulfilled: uppercase }">Atleast 1 upper case</li>
        </ul>
      </div>
      <br />
      <div class="input">
        <input v-model="name" placeholder="Full Name" type="text" />
      </div>

      <div class="input">
        <input v-model="username" placeholder="Username" type="text" />
      </div>
      <div class="input">
        <input v-model="email" placeholder="University Email" type="email" />
      </div>
      <div class="input">
        <input v-model="password" placeholder="Password" type="password" />
      </div>
      <div class="input">
        <input
          v-model="passwordConfirmation"
          placeholder="Confirm password"
          type="password"
        />
        <p style="color: red; font-size: 12px">{{ errMessage }}</p>
      </div>

      <div class="terms">
        <div id="center-TC">
          <input v-model="isTermsAgreed" type="checkbox" />
          <span class="tc-link" @click="showTC = true"
            >I agree to all terms and conditions</span
          >
        </div>
        <p style="color: red; font-size: 12px">{{ termErrMessage }}</p>
      </div>
      <div>
        <button class="register-btn" @click="registerUser()">Register</button>
      </div>
      <div class="text">
        <p>
          Already have an account?
          <a class="link" @click="navigate('login')">Sign in</a>
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
  name: "RegisterPage",
  components: {
    TermsAndConditionsPopup,
  },
  data() {
    return {
      showTC: false,
      name: "",
      username: "",
      password: "",
      passwordConfirmation: "",
      email: "",
      isTermsAgreed: false,

      // Password requirements
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
      this.nineChars = this.password.length >= 9;
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
      if (this.validateFields() === false) {
        this.errMessage = "Please fill in missing fields";
        return false;
      }

      if (this.validatePassword() === false) {
        this.showRequirements = true;
        return false;
      }

      if (!this.isTermsAgreed) {
        this.termErrMessage = "You must agree to the terms to register";
        return false;
      }

      axios
        .post("/api/users/", {
          email: this.email,
          username: this.username,
          password: this.password,
          name: this.name,
          password_repeat: this.passwordConfirmation,
        })
        .then(() => {
          this.errMessage = "";
          this.termErrMessage = "";
          this.$router.push({ name: "Map" });
        })
        .catch((error) => {
          console.error(error);
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
    validateFields() {
      return !!(
        this.name &&
        this.password &&
        this.passwordConfirmation &&
        this.email
      );
    },
  },
};
</script>

<style scoped src="@/assets/styling.css">
</style>
