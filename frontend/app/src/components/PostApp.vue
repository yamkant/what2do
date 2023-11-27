<template>
  <div
    id="bottom-banner"
    tabindex="-1"
    class="fixed bottom-0 start-0 z-50 flex justify-between w-full p-4 border-t border-gray-200 bg-gray-50 dark:bg-gray-700 dark:border-gray-600"
  >
    <div class="flex items-center w-4/5 mx-auto">
      <p class="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400 space-x-2">
        <font-awesome-icon icon="fa-solid fa-money-bill-trend-up" class="mr-2" />
        <span>{{ title }}
          <a
            v-bind:href="url"
            target="_blank"
            class="flex items-center ms-0 text-sm font-medium text-blue-600 md:ms-1 md:inline-flex dark:text-blue-500 hover:underline space-x-2"
          >
            <span>Open this news</span>
            <font-awesome-icon icon="fa-solid fa-arrow-up-right-from-square" />
          </a>
        </span>
      </p>
    </div>
    <div class="flex items-center">
      <button data-dismiss-target="#bottom-banner" type="button"
        class="flex-shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white">
        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
        </svg>
        <span class="sr-only">Close banner</span>
      </button>
    </div>
  </div>
</template>
  
<script>
import axiosInstance from "../libs"

export default {
  data() {
    return {
      title: "",
      url: "",
      news: [],
      current_index: 0,
    };
  },
  mounted() {
    this.getNewsPosts();
    setInterval(this.updateTitle, 4000);;
  },
  methods: {
    async getNewsPosts() {
      try {
        const response = await axiosInstance.get("/posts/news");
        this.news = this.shuffle(response.data);
        this.title = this.news[0].title;
        this.url = this.news[0].url;
      } catch (err) {
        console.error("Error fetching todos:", err);
      }
    },
    updateTitle() {
      this.current_index = (this.current_index + 1) % this.news.length;
      this.title = this.news[this.current_index].title
      this.url = this.news[this.current_index].url
    },
    shuffle(array) { 
      for (let i = array.length - 1; i > 0; i--) { 
        const j = Math.floor(Math.random() * (i + 1)); 
        [array[i], array[j]] = [array[j], array[i]]; 
      } 
      return array; 
    }
  }
};
</script>
  
<style scoped>/* 스타일링 */</style>