<template>
  <div class="container">
    <p class="title" style="font-weight: bold; font-size: 20px">
      Terms and conditions:
    </p>
    <p class="point" style="font-weight: bold; font-size: 20px">GDPR Policy</p>
    <p class="point">The stuff</p>
    <div>
      <p class="point">Important to know:</p>
      <div class="subpoints">
        <p class="point">
          a. Posting in a community will make that post visible to all members
          in that specific community.
        </p>
        <p class="point">
          b. Liking a post or a comment in a community will make that like
          visible to all members in that specific community.
        </p>
        <p class="point">
          c. Commenting on a post in a community will make that comment visible
          to all members in that community.
        </p>
      </div>
    </div>

    <p class="point">Hello</p>

    <p class="point">Good morning</p>

    <p class="point">Apurva K.</p>

    <p class="point">What is important to know</p>

    <p class="point">The stuff</p>

    <p class="point">
      10. Upon deleting your account, the account becomes inactive so it cannot
      be used anymore. The data left from the user (including any created
      communities, posts, likes and further interaction) will still be visible
      to other users because community interaction is vital to the use of the
      application, thus any content which other users have interacted with will
      be kept.
    </p>

    <p class="point">
      11. Upon deleting your account, your personal information will no longer
      be visible to other users - including your profile and name tagged on any
      posts/comments/and other interactions.
    </p>
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
  padding-bottom: 15%;
  margin-top: 1%;
  margin-bottom: 5%;
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
