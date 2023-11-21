<template>
  <div class="flex justify-end space-x-5">
    <label for="startTime" @click="setStartTimeNow" class="cursor-pointer">
      <font-awesome-icon icon="fa-solid fa-circle-play" />
    </label>
    <input type="time" id="startTime" v-model="startTime" @change="activateEndTime" />

    <label for="endTime" @click="setEndTimeNow" class="cursor-pointer">
      <font-awesome-icon icon="fa-solid fa-circle-stop" />
    </label>
    <input type="time" id="endTime" v-model="endTime" :disabled="!isEndTimeEnabled" @input="validateEndTime" />
  </div>
</template>
  
<script>
function getTimeNow() {
  const now = new Date();
  function padZero(value) {
    return value < 10 ? `0${value}` : value;
  }
  const formattedDateTime = `${now.getFullYear()}-${padZero(now.getMonth() + 1)}-${padZero(now.getDate())} ${padZero(now.getHours())}:${padZero(now.getMinutes())}`;
  return formattedDateTime.substring(formattedDateTime.length - 5)
}

export default {
  mounted() {
    this.startTime = this.todo.startTime
    this.endTime = this.todo.endTime
  },
  data() {
    return {
      'startTime': "",
      'endTime': "",
      'isEndTimeEnabled': false
    }
  },
  props: {
    todo: Object,
  },
  methods: {
    activateEndTime() {
      if (this.startTime) {
        this.isEndTimeEnabled = true;
      }
    },
    setStartTimeNow() {
      this.startTime = getTimeNow();
      this.activateEndTime();
    },
    setEndTimeNow() {
      if (!this.isEndTimeEnabled) {
        alert("시작시간을 먼저 설정해주세요.")
        return ;
      }
      this.endTime = getTimeNow();
      this.validateEndTime();
    },
    validateEndTime() {
      if (this.endTime < this.startTime) {
        alert('시작 시간보다 이후의 시간으로 등록해야합니다.')
        this.endTime = '';
        return
      }
    }
  }
};
</script>
  
<style scoped>
/* 스타일링 */
</style>