<template>
  <div>
    <TodoList :todos="todos" />
  </div>
</template>
  
<script>
import TodoList from "@/components/TodoList.vue";

export default {
  components: {
    TodoList,
  },
  data() {
    return {
      todos: [
        { id: 1, title: "Task 1", description: "Description 1" },
        { id: 2, title: "Task 2", description: "Description 2" },
        // 기본 데이터
      ],
    };
  },
};
</script>
  
<style scoped>
/* 스타일링 */
</style>