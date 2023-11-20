<template>
  <h1>Todo List</h1>
  <div class="space-y-2">
    <AddTodo @todoAdded="handleTodoAdded" />
    <TodoList :todos="todos" @remove="removeTodo" @toggle="toggleTodo"/>
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
        this.todos = response.data;
      } catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    handleTodoAdded(newTodo) {
      this.todos.push(newTodo);
    },
    removeTodo(todo) {
      this.todos = this.todos.filter(t => t.id !== todo.id);
    },
    toggleTodo(todo) {
      console.log(todo)
      if (todo.completed === 'Y') {
        todo.completed = 'N';
      } else if (todo.completed === 'N') {
        todo.completed = 'Y';
      }
    }
  }
};
</script>
  
<style scoped>
/* 스타일링 */
</style>