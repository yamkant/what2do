<template>
  <div>
    <ul class="space-y-1">
      <TodoItem v-for="todo in todos" :key="todo.id" :todo="todo" @remove="removeTodo" />
    </ul>
  </div>
</template>

<script>
import TodoItem from "@/components/TodoItem.vue";

export default {
  components: {
    TodoItem,
  },
  props: {
    todos: Array,
  },
  methods: {
    removeTodo(todo) {
      this.$emit('remove', todo);
    }
  }
};
</script>

<style scoped>
/* 스타일링 */
</style>