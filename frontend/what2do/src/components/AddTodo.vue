<template>
  <div>
    <div>
      <input v-model="content" placeholder="content를 입력하세요." />
      <button @click="addTodo">추가</button>
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
        console.log(response.data)
        this.$emit("todoAdded", response.data);
        console.log("정상적으로 emit 호출")

        // 입력 필드 초기화
        this.newTodo = { content: ""};
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