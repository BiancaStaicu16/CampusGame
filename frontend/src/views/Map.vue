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
    <gmap-map
      :center="center"
      :zoom="19"
      style="width: 800px; height: 400px; margin: 30px auto"
    >
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m"
        @click="center = m"
      ></gmap-marker>
    </gmap-map>

    <input
      onclick="https://www.google.com/"
      value="Scan QR Code"
      type="submit"
      class="login-btn"
      style="width: 20%; margin: 1%"
    />
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
</style>