<template>
  <div>
    <h1>A</h1>
    <button @click="makeO">O</button>
    <button @click="makeX">X</button>
    <br>
    {{ data1 }}를 선택하셨습니다!
    <hr>
  </div>
</template>

<script>
export default {
  name: 'pageA',
  data() {
    return {
      data1: 'o',
      data2: 'x'
    }
  },
  methods: {
    makeO() {
      this.$emit('data', this.data1)
    },
    makeX() {
      this.$emit('data', this.data2)
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
