<template>
  <li>
    {{ todo.title }} - {{ todo.description }}
  </li>
</template>
  
<script>
export default {
  props: {
    todo: Object,
  },
};
</script>
  
<style scoped>
/* 스타일링 */
</style>