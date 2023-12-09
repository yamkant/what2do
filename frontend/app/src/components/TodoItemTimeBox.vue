<template>
  <div class="flex justify-end items-center space-x-3">
    <div class="flex flex-col">
      <div>
        <label for="startTime" @click="setStartTimeNow" class="cursor-pointer">
          <font-awesome-icon icon="fa-solid fa-circle-play" />
        </label>
        <input
          type="datetime-local" v-model="startTime"
          @change="setStartTimeCustomized"
          class="w-48"
        />
      </div>

      <div>
        <label for="endTime" @click="setEndTimeNow" class="cursor-pointer">
          <font-awesome-icon icon="fa-solid fa-circle-stop" />
        </label>
        <input
          type="datetime-local" v-model="endTime"
          @change="setEndTimeCustomized"
          :disabled="!isEndTimeEnabled"
          class="w-48"
        />
      </div>
    </div>
  </div>
</template>
  
<script>
import axiosInstance from "../libs"
import {
  cvtTodoToRequestData,
  cvtDateStringToInputDateString,
} from "../libs/todo.js"

export default {
  mounted() {
    this.startTime = cvtDateStringToInputDateString(this.todo.started_at)
    this.endTime = cvtDateStringToInputDateString(this.todo.ended_at)
    this.dispStartTime = this.startTime;
    this.dispEndTime = this.endTime;
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
    getTimeNow() {
      return this.$moment().format('YYYY-MM-DD HH:mm')
    },
    async activateEndTime() {
      if (this.startTime) {
        this.isEndTimeEnabled = true;
      }
    },

    async setStartTimeCustomized() {
      await this.setStartTime();
    },

    async setStartTimeNow() {
      this.startTime = this.getTimeNow();
      await this.setStartTime();
    },
    async setStartTime() {
      this.activateEndTime();
      await axiosInstance.patch(
        `/todos/${this.todo.id}`,
        cvtTodoToRequestData(
          { ...this.todo, started_at:this.startTime, ended_at: null},
          this.todoDate
        )
      ).then(() => {
        this.endTime = ""
        this.dispStartTime = this.startTime;
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
      this.endTime = this.getTimeNow();
      if (!this.isValidateEndTime()) {
        return ;
      }
      this.endTime = this.getTimeNow();
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
        cvtTodoToRequestData(
          { ...this.todo, completed: "Y", started_at:this.startTime, ended_at:this.endTime},
          this.todoDate
        )
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
input[type=time]::-webkit-datetime-edit-ampm-field {
    -webkit-appearance: none;
    display: none;
}
input[type=date]::-webkit-datetime-edit-year-field {
    -webkit-appearance: none;
    /* display: none; */
}
input[type=date]::-webkit-datetime-edit-month-field{
    -webkit-appearance: none;
    /* display: none; */
}
input[type=date]::-webkit-datetime-edit-day-field {
    -webkit-appearance: none;
    /* display: none; */
}
input[type=date]::-webkit-datetime-edit-text {
    -webkit-appearance: none;
    /* display: none; */
}
input[type="time"]::-webkit-datetime-edit-hour-field {
  margin-left: 15px;
  text-align: end;
}

/* input[type="datetime-local"]::-webkit-datetime-edit-hour-field {
  background-color: blue;
} */

</style>
