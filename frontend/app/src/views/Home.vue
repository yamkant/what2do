<template>
  <TodoApp />
  <PostApp />
</template>
  
<script>
import TodoApp from '../components/TodoApp.vue';
import PostApp from '../components/PostApp.vue';


export default {
  components: {
    TodoApp,
    PostApp,
}
};
</script>
  
<style scoped>
/* 스타일링 */
</style>