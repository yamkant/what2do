<template>
  <div>
    <AddTodo @todoAdded="handleTodoAdded" />
    <h2>Todo List</h2>
    <TodoList :todos="todos" />
  </div>
</template>
  
<script>
import axios from 'axios';
import TodoItem from "@/components/TodoItem.vue";
import AddTodo from './AddTodo.vue';
import TodoList from './TodoList.vue';

export default {
  components: {
    TodoItem,
    AddTodo,
    TodoList
},
  props: {
    todos: Array,
  },
  data() {
    return {
      todos: []
    }
  },
  mounted() {
    this.fetchTodos();
  },
  methods: {
    async fetchTodos() {
      try {
        const response = await axios.get("http://localhost:8000/todos/");
        console.log(response.data)
        this.todos = response.data;
      } catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    handleTodoAdded(newTodo) {
      this.todos.push(newTodo);
    }
  }
};
</script>
  
<style scoped>
/* 스타일링 */
</style>