// Built using Geolocator and Google API 

<template>
  <div
    style="
      width: 74%;
      height: 75%;
      margin-left: auto;
      margin-right: 1%;
      background-color: white;
      border-radius: 25px;
    "
  >
    <h1 style="color: black">Map Page</h1>

    <gmap-map class="googlemaps" :center="center" :zoom="19">
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m"
        @click="center = m"
      ></gmap-marker>
    </gmap-map>

    <router-link to="/scanqr" v-on:click="goTo('scanqr')"
      ><input
        value="Scan QR Code"
        type="submit"
        class="login-btn"
        style="width: 20%; margin: 1%"
    /></router-link>
  </div>
</template>

<script>
export default {
  name: "GoogleMap",
  data() {
    return {
      center: { lat: 50.7371, lng: -3.5351 },
      markers: [],
      currentPlace: null,
    };
  },

  mounted() {
    this.geolocate();
  },

  methods: {
    setPlace(place) {
      this.currentPlace = place;
    },
    geolocate: function () {
      navigator.geolocation.getCurrentPosition((position) => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };
      });

      this.markers = [
        {
          lat: 50.73747555497765,
          lng: -3.5334623678159014,
          label: "Laver Building",
        },
        {
          lat: 50.73708852294572,
          lng: -3.536412797540645,
          label: "Forum",
        },
        {
          lat: 50.73509220167144,
          lng: -3.5341919286205656,
          label: "Physics Building",
        },
        {
          lat: 50.73782647913245,
          lng: -3.536991811820481,
          label: "Sports Park",
        },
        {
          lat: 50.73827733091095,
          lng: -3.5307060795439584,
          label: "Innovation Center",
        },
      ];
    },
  },
};
</script>

<style scoped>
h1 {
  left: 0;
  color: white;
  font-size: 2em;
}

.login-btn {
  background: white;
  width: 80px;
  height: 40px;
  left: calc(50vw - 80px);
  border-radius: 10px;
  border: 1px solid black;
  outline: none;
  cursor: pointer;
  font-weight: 600;
}

p a {
  color: white;
}

.googlemaps {
  width: 50rem;
  height: 25rem;
  margin-left: auto;
  margin-right: auto;
  overflow: hidden;
}

@media only screen and (min-width: 1200px) {
  .googlemaps {
    width: 50rem;
    height: 25rem;
    margin-left: auto;
    margin-right: auto;
    overflow: hidden;
  }
}

@media only screen and (max-width: 992px) {
  .googlemaps {
    width: 30rem;
    height: 15rem;
    margin-left: auto;
    margin-right: auto;
    overflow: hidden;
  }
}

@media only screen and (max-width: 768px) {
  .googlemaps {
    width: 20rem;
    height: 10rem;
    margin-left: auto;
    margin-right: auto;
    overflow: hidden;
  }
}
@media only screen and (max-width: 600px) {
  .googlemaps {
    width: 10rem;
    height: 5rem;
    margin-left: auto;
    margin-right: auto;
    overflow: hidden;
  }
}
</style>
