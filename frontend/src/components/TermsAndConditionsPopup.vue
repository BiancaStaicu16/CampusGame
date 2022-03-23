<template>
  <div class="container">
    <p class="title" style="font-weight: bold; font-size: 20px">
      Terms and conditions:
    </p>
    <p class="point" style="font-weight: bold; font-size: 20px">
      GDPR and Privacy Policy
    </p>
    <p class="point">
      We understand that your privacy and security of your personal information
      is of vital importance. This notice serves as a reminder to all users of
      the game that all your personal information is secure and confidential.
      This policy applies if you interact with us via this mobile application.
    </p>
    <div>
      <p class="point">
        It is important for the user to be aware of the following when the
        register an account:
      </p>
      <div class="subpoints">
        <p class="point">
          a. The user consents to the share of their personal data used for the
          application.
        </p>
        <p class="point">
          b. The user consents to the use of their location when the application
          is running
        </p>
        <p class="point">
          c. The user consents the application to access their device’s camera
          in order to Scan a QR Code
        </p>
        <p class="point">
          d. The user consents to the sharing of their data involving their
          username and score for the scoreboard
        </p>
      </div>
      <p class="point">The user has rights to:</p>
      <div class="subpoints">
        <p class="point">
          a. Logout, which will delete the cookies for that session
        </p>
        <p class="point">
          b. Delete their account, which will delete all the users personal
          information mentioned above. Their scores will also no longer be able
          to be viewed.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TermsAndConditionsPopup",
};
</script>

<style scoped>
.container {
  width: 50% !important;
  background: #4881b8;
  display: flex;
  flex-direction: column;
  border-radius: 10px;
  padding-bottom: 1%;
  margin-top: 1%;
  margin-bottom: 1%;
  margin-right: auto;
  margin-left: auto;
  box-shadow: 0px 3px 20px black;
}

.point {
  padding: 3px;
  padding-left: 20px;
  text-align: left;
}

.subpoints {
  margin-left: 25px;
}
</style>
