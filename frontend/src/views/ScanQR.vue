<template id="scanqr">
  <div
    id="app"
    style="
      width: 74%;
      height: 75%;
      margin-left: auto;
      margin-right: 1%;
      background-color: white;
      border-radius: 25px;
    "
  >
    <h1 style="color: black">Scan QR Code Page</h1>

    <div
      class="card"
      style="
        width: 50%;
        height: 50%;
        margin-left: auto;
        margin-right: auto;
        padding-bottom: 5%;
      "
    >
      <qrcode-stream @decode="onDecode" @init="onInit" />
    </div>
  </div>
</template>

<script>
import { QrcodeStream } from "vue-qrcode-reader";
export default {
  name: "app",
  data() {},
  components: { QrcodeStream },
  methods: {
    async onDecode(result) {
      window.location.replace(result);
    },
    async onInit(promise) {
      try {
        await promise;
      } catch (error) {
        if (error.name === "NotAllowedError") {
          this.alert = "alert-danger";
          this.status = "ERROR: you need to grant camera access permisson";
        } else if (error.name === "NotFoundError") {
          this.alert = "alert-danger";
          this.status = "ERROR: no camera on this device";
        } else if (error.name === "NotSupportedError") {
          this.alert = "alert-danger";
          this.status = "ERROR: secure context required (HTTPS, localhost)";
        } else if (error.name === "NotReadableError") {
          this.alert = "alert-danger";
          this.status = "ERROR: is the camera already in use?";
        } else if (error.name === "OverconstrainedError") {
          this.alert = "alert-danger";
          this.status = "ERROR: installed cameras are not suitable";
        } else if (error.name === "StreamApiNotSupportedError") {
          this.alert = "alert-danger";
          this.status = "ERROR: Stream API is not supported in this browser";
        }
      }
    },
  },
};
</script>
<style scoped>
h1 {
  left: 0;
  font-size: 2em;
}

p a {
  color: white;
}
