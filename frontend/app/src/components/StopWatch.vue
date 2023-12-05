<template>
  <div class="flex justify-end items-center group/item">
    <div class="flex flex-col border-2 p-2">
      <div class="flex justify-between items-center w-28">
        <font-awesome-icon icon="fa-solid fa-fire" class="mr-2" />
        <div class="flex justify-center mr-2">
          {{ dispElapsedMinutes }}분
          {{ dispElapsedSeconds }}초
        </div>
      </div>
      <div class="group-hover/controller hidden group-hover/item:flex flex justify-center items-center space-x-5 h-10">
        <button @click="start" class="hover:bg-gray-200 w-8 h-8 rounded-full">
          <font-awesome-icon icon="fa-solid fa-play" />
        </button>
        <button @click="reset" class="hover:bg-gray-200 w-8 h-8 rounded-full">
          <font-awesome-icon icon="fa-solid fa-stop" />
        </button>
      </div>
    </div>
  </div>
</template>
  
<script>
import moment from 'moment';

export default {
  data() {
    return {
      'isRunning': false,
      'elapsedMinutes': 0,
      'elapsedSeconds': 0,
      'dispElapsedMinutes': 0,
      'dispElapsedSeconds': 0,
      'elapsedTime': 0,
      'startTime': 0,
    }
  },
  mounted() {
    const tmpStartTime = this.getFromSessionStorage('startTime');
    this.isRunning = this.getFromSessionStorage('isRunning');
    if (!(tmpStartTime && this.isRunning === 'true')) {
      return ;
    }
    this.startTime = moment(tmpStartTime).toDate();
    this.isRunning = this.getFromSessionStorage('isRunning');
    this.timer = setInterval(this.updateTime, 1000);
  },
  props: {
    todo: Object,
  },
  methods: {
    saveToSessionStorage(key, value) {
      sessionStorage.setItem(key, value);
    },
    getFromSessionStorage(key) {
      return sessionStorage.getItem(key);
    },
    removeFromSessionStorage(key) {
      sessionStorage.removeItem(key);
    },
    start() {
      if (!confirm("타이머를 시작할까요?")) {
        return ;
      }
      this.isRunning = true;
      this.saveToSessionStorage('isRunning', this.isRunning);
      this.startTime = this.$moment();
      this.saveToSessionStorage('startTime', this.startTime);
      this.timer = setInterval(this.updateTime, 1000);
    },
    reset() {
      if (!confirm("타이머를 리셋할까요?")) {
        return ;
      }
      this.dispElapsedMinutes = String(0).padStart(1, '0');
      this.dispElapsedSeconds = String(0).padStart(1, '0');
      clearInterval(this.timer);
      this.removeFromSessionStorage('startTime');
      this.isRunning = false;
      this.saveToSessionStorage('isRunning', this.isRunning);
    },
    updateTime() {
      if (!this.isRunning) {
        return ;
      }
      this.elapsedTime = this.$moment() - this.startTime;
      this.elapsedSeconds = Math.floor(this.elapsedTime / 1000) % 60;
      this.dispElapsedSeconds = String(this.elapsedSeconds).padStart(2, '0');
      this.elapsedMinutes = Math.floor(Math.floor(this.elapsedTime / 1000) / 60);
      this.dispElapsedMinutes = String(this.elapsedMinutes).padStart(1, '0');
    },
  }
};
</script>
  
<style scoped>
/* 스타일링 */
</style>
