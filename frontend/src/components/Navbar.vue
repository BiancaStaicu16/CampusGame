<template>
  <div class="sidenav">
    <div class="logo-container clearfix">
      <h2
        class="title"
        style="
          font-weight: bolder;
          vertical-align: middle;
          font-family: 'Avenir';
        "
      >
        <img
          class="logo-container"
          style="
            width: 15%;
            border-radius: 10px;
            vertical-align: middle;
            height: 15%;
          "
          src="@/assets/website-logo.png"
        />
        ExeTour
      </h2>
    </div>

    <router-link class="nav-link" to="/" v-on:click="goTo('feed')">
      <div id="feed" style="color: white" v-on:click="goTo('feed')">
        <p
          class="nav-icon"
          style="display: inline-block; font-size: 75%; padding: 5%"
        >
          <font-awesome-icon
            :icon="['fas', 'home']"
            style="display: inline-block"
          />
          Dashboard
        </p>
      </div>
    </router-link>

    <router-link
      class="nav-link"
      to="/communities"
      v-on:click="goTo('communities')"
    >
      <div
        id="communities"
        style="color: white"
        v-on:click="goTo('communities')"
      >
        <p
          class="nav-icon"
          style="display: inline-block; font-size: 75%; padding: 5%"
        >
          <font-awesome-icon
            :icon="['fas', 'trophy']"
            style="display: inline-block"
          />
          Community
        </p>
      </div>
    </router-link>

    <router-link class="nav-link" to="/profile" v-on:click="goTo('profile')">
      <div id="profile" style="color: white" v-on:click="goTo('profile')">
        <p
          class="nav-icon"
          style="display: inline-block; font-size: 75%; padding: 5%"
        >
          <font-awesome-icon
            :icon="['fas', 'user']"
            style="display: inline-block"
          />
          My Cards
        </p>
      </div>
    </router-link>
    <router-link
      class="nav-link"
      to="/leaderboard"
      v-on:click="goTo('leaderboard')"
    >
      <div
        id="leaderboard"
        style="color: white"
        v-on:click="goTo('leaderboard')"
      >
        <p
          class="nav-icon"
          style="display: inline-block; font-size: 75%; padding: 5%"
        >
          <font-awesome-icon
            :icon="['fas', 'trophy']"
            style="display: inline-block"
          />
          Leaderboard
        </p>
      </div>
    </router-link>

    <router-link class="nav-link" to="/settings" v-on:click="goTo('settings')">
      <div id="settings" style="color: white" v-on:click="goTo('settings')">
        <p
          class="nav-icon"
          style="display: inline-block; font-size: 75%; padding: 5%"
        >
          <font-awesome-icon
            :icon="['fas', 'cog']"
            style="display: inline-block"
          />
          Settings
        </p>
      </div>
    </router-link>

    <div style="width: 100%; align-items: center">
      <img src="@/assets/nav-bar-logo.png" id="mainimg" style="width: 55%" />
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data: function () {
    return {
      pages: ["feed", "communities", "profile", "leaderboard", "settings"],
    };
  },
  mounted() {
    let pageName = this.$route.fullPath;
    let pageName2 = pageName.substring(1).split("/")[0];
    for (let i = 1; i < 5; i++) {
      if (document.getElementById(this.pages[i])) {
        document.getElementById(this.pages[i]).style.color = "white";
      }
    }

    if (pageName2 === "") {
      if (document.getElementById(this.pages[0])) {
        document.getElementById(this.pages[0]).style.color = "orange";
      }
    } else {
      if (document.getElementById(pageName2)) {
        document.getElementById(pageName2).style.color = "orange";
      }
    }
  },
  methods: {
    goTo: function (location) {
      // update the text colour depending on which is selected
      if (document.getElementById(location)) {
        document.getElementById(location).style.color = "orange";
      }
      // this.$router.replace(location)
      for (let i = 0; i < 5; i++) {
        if (this.pages[i] !== location) {
          if (document.getElementById(this.pages[i])) {
            document.getElementById(this.pages[i]).style.color = "white";
          }
        }
      }
    },
  },
};
</script>

<style scoped src="@/assets/styling.css">
</style>

<style scoped>
.sidenav {
  height: 100%;
  width: 25%;
  position: fixed;
  font-family: "Lucida Sans Unicode", "Lucida Grande", "Lucida Sans", Arial,
    sans-serif;
  font-weight: bold;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #2e5477;
  overflow-x: hidden;
  padding-top: 20px;
  font-size: 3.5vh;
  /*box-shadow: 0px 3px 20px #122230;*/
}

.nav-link {
  text-decoration: none !important;
  text-align: center;
}

.nav-icon {
  font-size: 2vh;
  margin-top: 0;
  margin-bottom: 1vh;
  text-align: center;
}

.clearfix::after {
  content: "";
  clear: both;
  display: table;
}

@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
  .sidenav a {
    font-size: 18px;
  }
}
</style>