<template>
  <div id="bottom-banner" tabindex="-1"
    class="fixed bottom-0 start-0 z-50 flex justify-between w-full p-4 border-t border-gray-200 bg-gray-50 dark:bg-gray-700 dark:border-gray-600">
    <div class="flex items-center mx-auto">
      <p class="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400 space-x-2">
        <font-awesome-icon icon="fa-solid fa-money-bill-trend-up" />
        <span>{{ title }}
          <a href="https://flowbite.com"
            class="flex items-center ms-0 text-sm font-medium text-blue-600 md:ms-1 md:inline-flex dark:text-blue-500 hover:underline space-x-2"
          > <span>Open this news</span> <font-awesome-icon icon="fa-solid fa-arrow-up-right-from-square" />
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
export default {
  data() {
    return {
      title: "This is space for a news title.",
    };
  },
};
</script>
  
<style scoped>/* 스타일링 */</style>