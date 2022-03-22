<!--<template>
  <div class="bg-gray-50 px-8">
    <p>{{ error }}</p>
    <p>{{ decodedString }}</p>
    <qrcode-stream @init="onInit" @decode="onDecode"></qrcode-stream>
  </div>
</template>

<script>
import { QrcodeStream } from "vue3-qrcode-reader";
export default {
  data() {
    return {
      error: "",
      decodedString: "",
    };
  },
  components: {
    QrcodeStream,
  },
  methods: {
    async onInit(promise) {
      try {
        //successfully initialized
      } catch (error) {
        if (error.name === "NotAllowedError") {
          this.error = "user denied camera access permisson";
        } else if (error.name === "NotFoundError") {
          this.error = "no suitable camera device installed";
        } else if (error.name === "NotSupportedError") {
          this.error = "page is not served over HTTPS (or localhost)";
        } else if (error.name === "NotReadableError") {
          this.error = "maybe camera is already in use";
        } else if (error.name === "OverconstrainedError") {
          this.error =
            "did you requested the front camera although there is none?";
        } else if (error.name === "StreamApiNotSupportedError") {
          this.error = "browser seems to be lacking features";
        }
      } finally {
        //hide loading indicator
      }
    },
    onDecode(decodedString) {
      this.decodedString = decodedString;
      window.location.replace(decodedString);
    },
  },
};
</script>
-->
<template>
  <div
    style="
      width: 75%;
      height: 75%;
      margin-left: auto;
      background-color: white;
      border-radius: 25px;
    "
  >
    <h1 style="color: black">Scan QR Code Page</h1>
  </div>
</template>


<style scoped>
h1 {
  left: 0;
  font-size: 2em;
}

p a {
  color: white;
}
