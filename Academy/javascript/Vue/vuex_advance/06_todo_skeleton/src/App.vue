<template>
  <div id="app">
    <h1>Todo</h1>
    <h1>총 할일 : {{ allTodocount }}</h1>
    <h1>완료된 할일 : {{ restCount }}</h1>
    <h1>남은 할일 : {{ rest }}</h1>
    <TodoForm/>
    <TodoList />
    <button @click="loadTodos">Load Data</button>
  </div>
</template>

<script>
import TodoForm from './components/TodoForm.vue'
import TodoList from './components/TodoList.vue'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    allTodocount() {
      return this.$store.getters.alltodosCount
    },
    restCount() {
      if (this.allTodocount !== 0) { 
        return this.$store.getters.restCount
      } else {
        return 0
      }
      
    },
    rest() {
      if (this.allTodocount !== 0) {
        
        return this.allTodocount - this.restCount
      } else {
        return 0
      }
    }
  },
  methods: {
    loadTodos() {
      this.$store.dispatch('loadTodos')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
