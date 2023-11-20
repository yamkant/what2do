<template>
  <h1>Todo List</h1>
  <div class="space-y-2">
    <AddTodo @todoAdded="handleTodoAdded" />
    <h1>Uncompleted</h1>
    <TodoList :todos="completed_todos" @remove="removeTodo" @toggle="toggleTodo"/>
    <h1>Completed</h1>
    <TodoList :todos="uncompleted_todos" @remove="removeTodo" @toggle="toggleTodo"/>
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
  data() {
    return {
      todos: [],
      completed_todos: [],
      uncompleted_todos: [],
    }
  },
  mounted() {
    this.getTodos();
  },
  methods: {
    getTodosByCompleted (todos, status) {
      return todos.filter(t => t.completed !== status);
    },
    setTodoList() {
        this.completed_todos = this.getTodosByCompleted(this.todos, "Y");
        this.uncompleted_todos = this.getTodosByCompleted(this.todos, "N");
    },
    async getTodos() {
      try {
        const response = await axios.get("http://localhost:8000/todos/");
        this.todos = response.data;
        this.setTodoList();
      } catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    handleTodoAdded(newTodo) {
      this.todos.push(newTodo);
    },
    async removeTodo(todo) {
      this.todos = this.todos.filter(t => t.id !== todo.id);
      try {
        const response = await axios.delete(
          `http://localhost:8000/todos/${todo.id}`,
        );
        this.setTodoList();
      } catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    async toggleTodo(todo) {
      try {
        const response = await axios.patch(
          `http://localhost:8000/todos/${todo.id}`,
          {
            completed: todo.completed
          }
        );
        if (todo.completed === 'Y') {
          todo.completed = 'N';
          this.setTodoList();
        } else if (todo.completed === 'N') {
          todo.completed = 'Y';
          this.setTodoList();
        }
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