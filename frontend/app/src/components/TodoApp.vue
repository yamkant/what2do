<template>
  <StopWatch />
  <h1>Todo List</h1>
  <div class="space-y-2">
    <AddTodo @todoAdded="addTodo" />
    <h1>Uncompleted</h1>
    <TodoList
      :todos="uncompleted_todos"
      @remove="removeTodo"
      @toggle="checkTodo"
      @changeTodo="changeTodo"
    />
    <div class="flex justify-between">
      <h1>Completed</h1>
      <label class="relative inline-flex items-center cursor-pointer">
          <input
            type="checkbox" value="" class="sr-only peer"
            @change="toggle_flag = !toggle_flag"
          >
          <div class="w-11 h-6 bg-gray-200 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"
          ></div>
      </label>
    </div>
    <TodoList
      v-if="toggle_flag"
      :todos="completed_todos"
      @remove="removeTodo"
      @toggle="checkTodo"
    />
    <TodoChart
      :todos="uncompleted_todos"
      :chart_data="chart_data"
    />
  </div>
</template>
  
<script>
import AddTodo from './AddTodo.vue';
import TodoList from './TodoList.vue';
import StopWatch from './StopWatch.vue';
import TodoChart from './TodoChart.vue';
import GChartHelper from '../classes/GChartHelper.js';

export default {
  components: {
    AddTodo,
    TodoList,
    TodoChart,
    StopWatch,
},
  data() {
    return {
      todos: [],
      completed_todos: [],
      toggle_flag: false,
      uncompleted_todos: [],
      chart_data: [],
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
      this.completed_todos = this.getTodosByCompleted(this.todos, "N");
      this.uncompleted_todos = this.getTodosByCompleted(this.todos, "Y");
      const gchart = new GChartHelper(this.$moment, this.todos);
      this.chart_data = gchart.getChartData(this.todos);
    },
    async getTodos() {
      try {
        const response = await this.$axios.get("/todos");
        this.todos = response.data;
        this.setTodoList();
      } catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    addTodo(newTodo) {
      this.todos.unshift(newTodo);
      this.setTodoList();
    },
    removeTodo(todo) {
      this.todos = this.todos.filter(t => t.id !== todo.id);
      this.setTodoList();
    },
    checkTodo(todo) {
      for (const t of this.todos) {
        if (t.id === todo.id) {
          t.completed = todo.completed;
        }
      }
      this.setTodoList();
    },
    async changeTodo(todo) {
      this.setTodoList();
    },
  }
};
</script>
  
<style scoped>
/* 스타일링 */
</style>
