<template>
    <div id="app">
                <div class="card">
                    <qrcode-stream @decode="onDecode" @init="onInit" />
                </div>
    </div>
</template>

<script>
import { QrcodeStream } from 'vue-qrcode-reader'
export default {
  name: 'app',
  data() {},
  components: { QrcodeStream },
  methods: {
    async onDecode (result) {
      window.location.replace(result)
    },
    async onInit (promise) {
      try {
        await promise
      } catch (error) {
        if (error.name === 'NotAllowedError') {
          this.alert = 'alert-danger'
          this.status = "ERROR: you need to grant camera access permisson"
        } else if (error.name === 'NotFoundError') {
          this.alert = 'alert-danger'
          this.status = "ERROR: no camera on this device"
        } else if (error.name === 'NotSupportedError') {
          this.alert = 'alert-danger'
          this.status = "ERROR: secure context required (HTTPS, localhost)"
        } else if (error.name === 'NotReadableError') {
          this.alert = 'alert-danger'
          this.status = "ERROR: is the camera already in use?"
        } else if (error.name === 'OverconstrainedError') {
          this.alert = 'alert-danger'
          this.status = "ERROR: installed cameras are not suitable"
        } else if (error.name === 'StreamApiNotSupportedError') {
          this.alert = 'alert-danger'
          this.status = "ERROR: Stream API is not supported in this browser"
        }
      }
    }
  }
}
</script>


