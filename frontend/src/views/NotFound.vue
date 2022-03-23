<template>
  <div>
    <h1>Welcome to the ExeTour Game!</h1>
    <p><a href="/">Go home?</a></p>
  </div>
</template>

<script>
export default {
  name: "NotFound",

  methods: {
    headers: { Authorization: this.$authToken },
  },
};
</script>

<style scoped>
h1 {
  left: 0;
  color: white;
  font-size: 2em;
}

p a {
  color: white;
}
</style>
