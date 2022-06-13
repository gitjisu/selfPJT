<template>
  <div>
    <h1>B</h1>
    <span>결과: {{ data1 }}</span>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    data1: String,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
