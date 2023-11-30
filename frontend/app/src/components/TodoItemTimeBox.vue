<template>
  <div class="flex justify-end space-x-5">
    <label for="startTime" @click="setStartTimeNow" class="cursor-pointer">
      <font-awesome-icon icon="fa-solid fa-circle-play" />
    </label>
    <input type="time" v-model="startTime" @change="setStartTimeCustomized" class="w-28"/>

    <label for="endTime" @click="setEndTimeNow" class="cursor-pointer">
      <font-awesome-icon icon="fa-solid fa-circle-stop" />
    </label>
    <input type="time" v-model="endTime" :disabled="!isEndTimeEnabled" @input="setEndTimeCustomized" class="w-28"/>
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
    async activateEndTime() {
      if (this.startTime) {
        this.isEndTimeEnabled = true;
      }
    },

    async setStartTimeCustomized() {
      await this.setStartTime();
    },
    async setStartTimeNow() {
      this.startTime = getTimeNow();
      await this.setStartTime();
    },
    async setStartTime() {
      this.activateEndTime();
      await axiosInstance.patch(
        `/todos/${this.todo.id}`,
        cvtTodoToRequestData({ ...this.todo, started_at:this.startTime, ended_at: null})
      ).then(() => {
        this.endTime = ""
      }).catch((err) => {
        console.error("Error updating todo start time:", err);
      });
    },

    async setEndTimeCustomized() {
      if (!this.isValidateEndTime()) {
        return ;
      }
      await this.setEndTime()
    },
    async setEndTimeNow() {
      this.endTime = getTimeNow();
      if (!this.isValidateEndTime()) {
        return ;
      }
      await this.setEndTime()
    },
    async setEndTime() {
      if (!this.isEndTimeEnabled) {
        alert("시작시간을 먼저 설정해주세요.")
        this.endTime = ""
        return ;
      }

      await axiosInstance.patch(
        `/todos/${this.todo.id}`,
        cvtTodoToRequestData({ ...this.todo, completed: "Y", started_at:this.startTime, ended_at:this.endTime})
      ).then(() => {
        location.reload()
      }).catch ((err) => {
        console.error("Error updating todo end time:", err);
      })
    },
    isValidateEndTime() {
      if (this.endTime < this.startTime) {
        alert('시작 시간보다 이후의 시간으로 등록해야합니다.')
        this.endTime = ""
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
