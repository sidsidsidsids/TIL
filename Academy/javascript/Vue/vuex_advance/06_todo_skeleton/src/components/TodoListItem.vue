<template>
  <div>
    <li @click="updateTodo" :class="{ 'is-completed' : todo.isCompleted}">{{ todo.title }} </li>
    <button @click="deleteTodo">X</button>
  </div>
  
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods:{
    deleteTodo() {
      this.$store.dispatch('deleteTodo', this.todo)
    },
    updateTodo() {
      // console.log('updateTodo')
      this.$store.dispatch('updateTodo', this.todo)
    }
  },
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>
