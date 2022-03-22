<template>
  <div
    style="
      width: 74%;
      height: 75%;
      margin-left: auto;
      margin-right: 1%;
      border-radius: 25px;
    "
  >
    <h1 style="color: white">Settings</h1>

    <div class="sign-out" @click="signOut()">
      <p>Log out</p>
    </div>

    <div>
      <p class="tc-link" @click="showTC = true">
        Terms and Conditions | GDPR Policy
      </p>
    </div>

    <div class="TC-popup">
      <div class="close-TC" v-if="showTC">
        <font-awesome-icon :icon="['fa', 'times']" @click="showTC = false" />
      </div>
      <TermsAndConditionsPopup v-if="showTC" />
    </div>

    <!-- <div style="position: relative; top: -50px">
      <label class="switch" v-if="hideLeaderboard !== null">
        <input type="checkbox" v-model="hideLeaderboard" />
        <span class="slider round"></span>
      </label>
    </div>-->

    <div class="small-sign-out" @click="changePassword()">
      <p>Change your password</p>
    </div>
    <div class="small-sign-out" @click="deleteAccount()">
      <p>Delete your account</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TermsAndConditionsPopup from "@/components/TermsAndConditionsPopup.vue";

export default {
  components: {
    TermsAndConditionsPopup,
  },
  data() {
    return {
      hideLeaderboard: null,
      showTC: false,
    };
  },
  mounted() {
    this.toggle();
    axios.get("/api/users/me").then((response) => {
      this.hideLeaderboard = !response.data.hide_leaderboard;
    });
  },
  watch: {
    hideLeaderboard: function () {
      axios.get("/api/users/me").then((response) => {
        axios
          .put("/api/users/me", {
            email: response.data.email,
            first_name: response.data.first_name,
            last_name: response.data.last_name,
            hide_leaderboard: !this.hideLeaderboard,
            username: response.data.username,
            description: response.data.description,
          })
          .then(() => {})
          .catch((error) => {
            console.error(error.response.data);
          });
      });
    },
  },
  methods: {
    changePassword() {
      this.$router.push({ name: "ChangePassword" });
    },
    deleteAccount() {
      this.$router.push({ name: "DeleteCheck" });
    },
    signOut() {
      axios.post("/api/logout");
      this.$router.push("/login");
    },
    toggle() {
      axios.get("/api/users/me").then((response) => {
        this.hideLeaderboard = response.data.hideLeaderboard;
      });
    },
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>

<style scoped src="@/assets/styling.css">
</style>

<style scoped>
h1 {
  left: 0;
  color: white;
  font-size: 2em;
}

p {
  color: white;
}
</style>