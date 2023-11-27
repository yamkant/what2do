<template>
  <li class="flex flex-col px-2">
    <div class="flex justify-between h-8">
      <div class="flex items-center">
        <svg v-if="todo.completed === 'N'"
          class="w-6 h-6 mr-2 text-gray-500 dark:text-gray-400 flex-shrink-0 cursor-pointer" aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20" @click="checkTodo">
          <path
            d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z">
          </path>
        </svg>
        <svg v-else-if="todo.completed === 'Y'"
          class="w-6 h-6 mr-2 text-green-500 dark:text-green-400 flex-shrink-0 cursor-pointer" aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20" @click="checkTodo">
          <path
            d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z">
          </path>
        </svg>
        <button>
          <label for="checkbox-e4ec4dd7-d4f8-45ae-9ec7-57339b937677">
          </label>
        </button>
        <input @change="changeTodoContent" v-model="inputValue" />
      </div>
      <button @click="removeTodo" class="hover:bg-gray-100 w-8 rounded-full">
        <font-awesome-icon icon="fa-solid fa-trash" />
      </button>
    </div>
    <TodoItemTimeBox :todo="todo" />
  </li>
</template>
  
<script>
import TodoItemTimeBox from "@/components/TodoItemTimeBox.vue";
import axiosInstance from "../libs"
import {
  cvtTodoToRequestData,
} from "../libs/todo.js"

export default {
  components: {
    TodoItemTimeBox
  },
  mounted() {
    this.inputValue = this.todo.content
  },
  data() {
    return {
      'inputValue': "",
    }
  },
  props: {
    todo: Object,
  },
  methods: {
    async removeTodo() {
      if (!confirm("정말 삭제하시겠습니까?")) {
        return;
      }
      await axiosInstance.delete(
        `/todos/${this.todo.id}`,
      ).then(() => {
        this.$emit('remove', this.todo);
      }).catch((err) => {
        console.error("Error removing todos:", err);
      });
    },
    async checkTodo() {
      if (this.todo.completed === 'Y') {
        await axiosInstance.patch(
          `/todos/${this.todo.id}`, cvtTodoToRequestData({ ...this.todo, completed: "N" })
        ).then(() => {
          this.$emit('toggle', { ...this.todo, completed: "N" });
        }).catch((err) => {
          console.error("Error complete todo:", err);
        })
      } else if (this.todo.completed === 'N') {
        await axiosInstance.patch(
          `/todos/${this.todo.id}`, cvtTodoToRequestData({ ...this.todo, completed: "Y" })
        ).then(() => {
          this.$emit('toggle', { ...this.todo, completed: "Y" });
        }).catch((err) => {
          console.error("Error complete todo:", err);
        })
      }
    },
    async changeTodoContent() {
      await axiosInstance.patch(
        `/todos/${this.todo.id}`, cvtTodoToRequestData({ ...this.todo, content: this.inputValue })
      ).then(() => {
        this.$emit('inputChange', { ...this.todo, content: this.inputValue })
      }).catch((err) => {
        console.error("Error changing todo content:", err);
      })
    },
  }
};
</script>
  
<style scoped>
/* 스타일링 */
</style>