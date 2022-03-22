<template>
  <div class="container">
    <div class="header"></div>
    <div class="position">
      <div class="profile-pic"></div>
      <div class="position-text">
        <font-awesome-icon :icon="['fa', 'user']"></font-awesome-icon>
        <p v-if="leaderboardPosition">
          Your Position: {{ leaderboardPosition | ordinal_suffix }}
        </p>
        <p v-else>Your position is hidden.</p>
      </div>
    </div>
    <div class="top-three" v-if="loaded">
      <div class="top">
        <p class="title">1st</p>
        <div
          class="first circle"
          @click="navigateToProfile(leaderboardUsers[0].id)"
        >
          <div class="crown">
            <font-awesome-icon :icon="['fa', 'crown']"></font-awesome-icon>
          </div>
          <p class="initials">
            {{ leaderboardUsers[0] | initials }}
          </p>
        </div>
        <div class="info">
          <p class="username">{{ leaderboardUsers[0].username }}</p>
          <p class="points">Points: {{ leaderboardUsers[0].points }}</p>
        </div>
      </div>

      <div class="top-two">
        <div class="second-place">
          <p class="title">2nd</p>
          <div
            class="second circle"
            @click="navigateToProfile(leaderboardUsers[1].id)"
          >
            <div class="medal">
              <font-awesome-icon :icon="['fa', 'medal']"></font-awesome-icon>
            </div>
            <p class="initials">
              {{ leaderboardUsers[1] | initials }}
            </p>
          </div>
          2
          <div class="info">
            <p class="username">{{ leaderboardUsers[1].username }}</p>
            <p class="points">Points: {{ leaderboardUsers[1].points }}</p>
          </div>
        </div>
        <div class="third-place">
          <p class="title">3rd</p>
          <div
            class="third circle"
            @click="navigateToProfile(leaderboardUsers[2].id)"
          >
            <div class="medal">
              <font-awesome-icon :icon="['fa', 'medal']"></font-awesome-icon>
            </div>
            <p class="initials">
              {{ leaderboardUsers[2] | initials }}
            </p>
          </div>
          <div class="info">
            <p class="username">{{ leaderboardUsers[2].username }}</p>
            <p class="points">Points: {{ leaderboardUsers[2].points }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="leaderboard-table-container" v-if="loaded">
      <table class="table">
        <tr v-for="(user, index) in leaderboardUsers.slice(3)" :key="index">
          <td>{{ user.leaderboard_position | ordinal_suffix }}</td>
          <td>
            <p style="margin: 0" @click="navigateToProfile(user.id)">
              {{ user.username }}
            </p>
          </td>
          <td class="points">Points: {{ user.points }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Leaderboard",
  filters: {
    ordinal_suffix(i) {
      var j = i % 10,
        k = i % 100;
      if (j == 1 && k != 11) {
        return i + "st";
      }
      if (j == 2 && k != 12) {
        return i + "nd";
      }
      if (j == 3 && k != 13) {
        return i + "rd";
      }
      return i + "th";
    },
    initials(user) {
      return user.first_name.charAt(0) + user.last_name.charAt(0);
    },
  },
  data() {
    return {
      leaderboardUsers: [],
      loaded: false,
      currentPage: 0,
      loadMore: false,
      leaderboardPosition: null,
    };
  },
  mounted() {
    // Fetch logged in user information
    this.getUserDetails();
    // Load first page of leaderboard user details
    this.loadMoreUsers();
    // Call scroll event function for infinite scrolling
    this.scroll();
  },
  methods: {
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow =
          document.documentElement.scrollTop + window.innerHeight >
          document.body.scrollHeight;
        if (bottomOfWindow) {
          if (this.loadMore) {
            this.loadMoreUsers();
            this.loadMore = false;
          }
        }
      };
    },
    navigateToProfile(id) {
      this.$router.push({
        name: "User",
        params: {
          id: id,
        },
      });
    },
    loadMoreUsers() {
      // On page scroll to bottom of page, display next page of users
      this.currentPage += 1;
      axios
        .get("/api/users/leaderboard", { params: { page: this.currentPage } })
        .then((response) => {
          var i;
          for (i = 0; i < response.data.data.length; i++) {
            this.leaderboardUsers.push(response.data.data[i]);
          }
          if (response.data.next_page === null) {
            this.loadMore = false;
          } else {
            this.loadMore = true;
          }
          this.loaded = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getUserDetails() {
      axios
        .get("/api/users/me")
        .then((response) => {
          this.leaderboardPosition = response.data.leaderboard_position;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>