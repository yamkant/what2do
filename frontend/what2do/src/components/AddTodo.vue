<template>
  <div>
    <div class="relative">
      <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none">
          <path
            d="M17 8H10V1C10 0.734784 9.89464 0.48043 9.70711 0.292893C9.51957 0.105357 9.26522 0 9 0C8.73478 0 8.48043 0.105357 8.29289 0.292893C8.10536 0.48043 8 0.734784 8 1V8H1C0.734784 8 0.48043 8.10536 0.292893 8.29289C0.105357 8.48043 0 8.73478 0 9C0 9.26522 0.105357 9.51957 0.292893 9.70711C0.48043 9.89464 0.734784 10 1 10H8V17C8 17.2652 8.10536 17.5196 8.29289 17.7071C8.48043 17.8946 8.73478 18 9 18C9.26522 18 9.51957 17.8946 9.70711 17.7071C9.89464 17.5196 10 17.2652 10 17V10H17C17.2652 10 17.5196 9.89464 17.7071 9.70711C17.8946 9.51957 18 9.26522 18 9C18 8.73478 17.8946 8.48043 17.7071 8.29289C17.5196 8.10536 17.2652 8 17 8Z"
            fill="#2F2F38" />
        </svg>
      </div>
      <input v-model="content" placeholder="content를 입력하세요."
        class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
      <button @click="addTodo"
        class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">추가</button>
    </div>
  </div>
</template>
  
<script>
import axios from "axios";

export default {
  data() {
    return {
      content: "",
    };
  },
  methods: {
    async addTodo() {
      try {
        const response = await axios.post(
          "http://localhost:8000/todos/",
          {
            content: this.content,
          }
        );

        // 이벤트를 통해 새로운 Todo를 부모 컴포넌트에 전달
        this.$emit("todoAdded", response.data);

        // 입력 필드 초기화
        this.newTodo = { content: "" };
      } catch (error) {
        console.error("Error adding todo:", error);
      }
    },
  },
};
</script>
  
<style scoped>
/* 스타일링 */
</style>