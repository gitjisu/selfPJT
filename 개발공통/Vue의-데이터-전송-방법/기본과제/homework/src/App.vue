<template>
  <div>
    <A @data="data"></A>
    <B :data1="data1"></B>
  </div>
</template>

<script>
import A from './components/A.vue'
import B from './components/B.vue'

export default {
  name: 'App',
  components: {
    A,B
  },
  data() {
    return {
      data1 : " ",
    }
  },
  methods: {
    data(data) {
      this.data1 = data
    }
  }

}
</script>

<style>

</style>
