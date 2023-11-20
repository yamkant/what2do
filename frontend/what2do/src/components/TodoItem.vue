<template>
  <li class="flex justify-between">
    <span>{{ todo.content }}</span>
    <button @click="removeTodo">제거</button>
  </li>
</template>
  
<script>
export default {
  props: {
    todo: Object,
  },
  methods: {
    removeTodo() {
      this.$emit('remove', this.todo);
    }
  }
};
</script>
  
<style scoped>
/* 스타일링 */
</style>