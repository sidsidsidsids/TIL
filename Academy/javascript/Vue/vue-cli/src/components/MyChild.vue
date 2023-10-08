<template>
  <div>
    <h3>This is child component</h3>
    <p>{{ staticProps }}</p>
    <p>{{ cProps }}</p>
    <button @click="childToParent">CLICK</button>
    <input type="text" v-model="childInputData" @keyup.enter="childInput">
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  data() {
    return {
      childInputData: null,
    }
  },
  props: {
    staticProps: String,
    cProps: String,
  },
  methods:{
    childToParent: function() {
      this.$emit('child-to-parent', 'child Data')
    },
    childInput: function() {
      this.$emit('child-input', this.childInputData)
      this.childInputData = ""
    }
  }
}
</script>

<style>

</style>