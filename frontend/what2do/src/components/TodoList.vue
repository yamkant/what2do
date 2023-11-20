<template>
  <div>
    <h2>Todo List</h2>
    <ul>
      <TodoItem v-for="todo in todos" :key="todo.id" :todo="todo" />
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import TodoItem from "@/components/TodoItem.vue";

export default {
  components: {
    TodoItem,
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
        this.todos = response.data;
      } catch (err) {
        console.error("Error fetching todos:", err);
      }
    }
  }
};
</script>

<style scoped>
/* 스타일링 */
</style>