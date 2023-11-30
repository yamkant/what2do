<template>
  <div v-if="validTimeSpent" class="w-full flex justify-start ml-10 space-x-3">
    <span>
      <font-awesome-icon icon="fa-solid fa-fire" />
    </span>
    <div class="w-full">{{ timeSpent }}분</div>
  </div>
</template>
  
<script>
export default {
  mounted() {
    this.timeSpent = this.getTimeDiff(new Date(this.todo.ended_at), new Date(this.todo.started_at));
    this.validTimeSpent = this.isValidTimeSpent()
  },
  data() {
    return {
      'timeSpent': "",
      'validTimeSpent': true,
    }
  },
  props: {
    todo: Object,
  },
  methods: {
    getTimeDiff(start, end) {
      return (start - end) / (1000 * 60)
    },
    isValidTimeSpent() {
      if (this.todo.started_at && this.todo.ended_at) {
        return true;
      }
      return false;
    }
  }
};
</script>
  
<style scoped>
/* 스타일링 */
</style>