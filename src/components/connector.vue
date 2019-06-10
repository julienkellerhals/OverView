<template>
  <div class="conn">
    <p>icon</p>
    <h3>{{ connName }}</h3>
  </div>
</template>

<script>
export default {
  name: 'connector',
  props: {
    connName: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 0 0;
}
</style>
