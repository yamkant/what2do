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
      todos: [],
    };
  },
};
</script>
  
<style scoped>
/* 스타일링 */
</style>