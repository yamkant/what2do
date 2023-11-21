<template>
  <div class="flex justify-end space-x-5">
    <label for="startTime" @click="setStartTimeNow" class="cursor-pointer">
      <font-awesome-icon icon="fa-solid fa-circle-play" />
    </label>
    <input type="time" v-model="startTime" @change="activateEndTime" />

    <label for="endTime" @click="setEndTimeNow" class="cursor-pointer">
      <font-awesome-icon icon="fa-solid fa-circle-stop" />
    </label>
    <input type="time" v-model="endTime" :disabled="!isEndTimeEnabled" @input="validateEndTime" />
  </div>
</template>
  
<script>
import axiosInstance from "../libs"
import {
  getTimeNow,
  cvtIsoStringToTime,
  cvtTodoToRequestData,
} from "../libs/todo.js"

export default {
  mounted() {
    this.startTime = cvtIsoStringToTime(this.todo.started_at)
    this.endTime = cvtIsoStringToTime(this.todo.ended_at)
    this.activateEndTime()
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
    async setStartTimeNow() {
      this.startTime = getTimeNow();
      this.activateEndTime();

      const reqData = cvtTodoToRequestData({ ...this.todo, started_at:this.startTime})
      try {
        const response = await axiosInstance.patch(
          `/todos/${this.todo.id}`, reqData
        );
        this.endTime = ""
      }catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    async setEndTimeNow() {
      if (!this.isEndTimeEnabled) {
        alert("시작시간을 먼저 설정해주세요.")
        return ;
      }
      this.endTime = getTimeNow();
      if (!this.isValidateEndTime()) {
        return ;
      }

      const reqData = cvtTodoToRequestData({ ...this.todo, ended_at:this.endTime})
      try {
        const response = await axiosInstance.patch(
          `/todos/${this.todo.id}`, reqData
        );
      }catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    isValidateEndTime() {
      if (this.endTime < this.startTime) {
        alert('시작 시간보다 이후의 시간으로 등록해야합니다.')
        this.endTime = '';
        return false
      }
      return true
    },
  }
};
</script>
  
<style scoped>
/* 스타일링 */
</style>