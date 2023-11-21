<template>
  <h1>Todo List</h1>
  <div class="space-y-2">
    <AddTodo @todoAdded="handleTodoAdded" />
    <h1>Uncompleted</h1>
    <TodoList :todos="completed_todos" @remove="removeTodo" @toggle="checkTodo"/>
    <div class="flex justify-between">
      <h1>Completed</h1>
      <label class="relative inline-flex items-center cursor-pointer">
          <input
            type="checkbox" value="" class="sr-only peer"
            @change="toggle_flag = !toggle_flag"
          >
          <div
            class="w-11 h-6 bg-gray-200 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"
          ></div>
      </label>
    </div>
    <TodoList v-if="toggle_flag" :todos="uncompleted_todos" @remove="removeTodo" @toggle="checkTodo"/>
  </div>
</template>
  
<script>
import axiosInstance from "../libs"
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
      toggle_flag: false,
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
        const response = await axiosInstance.get("/todos");
        this.todos = response.data;
        this.setTodoList();
      } catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    handleTodoAdded(newTodo) {
      this.todos.push(newTodo);
      this.setTodoList();
    },
    async removeTodo(todo) {
      try {
        const response = await axiosInstance.delete(
          `/todos/${todo.id}`,
        );
        this.todos = this.todos.filter(t => t.id !== todo.id);
        this.setTodoList();
      } catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    async checkTodo(todo) {
      try {
        if (todo.completed === 'Y') {
          todo.completed = 'N';
        } else if (todo.completed === 'N') {
          todo.completed = 'Y';
        }
        const response = await axiosInstance.patch(
          `/todos/${todo.id}`,
          {
            completed: todo.completed
          }
        );
        this.setTodoList();
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