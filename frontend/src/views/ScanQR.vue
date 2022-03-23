<template>
    <div id="app">
                <div class="card">
                    <qrcode-stream width@decode="onDecode" @init="onInit"/>
                    <p> class="center">THIS IS JUST A TEST</p>
                </div>
    </div>
</template>

<script>
import { QrcodeStream } from 'vue-qrcode-reader'
export default {
  name: 'app',  

  components: { QrcodeStream },
  methods: {
    async onDecode (result) {
      var audio = new Audio(require('../assets/unlock.mp3'))
      audio.play()
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
<style>
#app {
  color: #404040;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size:30px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center+50px;
  color: #FFFFFFFF;
  width: 65vh;
  margin-top: 2vh;
  margin-left: 20vh;
}
