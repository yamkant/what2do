<template>
  <div class="todo-list-container p-10 max-w-screen-sm md:max-w-screen-md mx-auto">
    <div class="flex flex-col space-y-2">
      <div class="text-left font-bold">Todo List</div>
      <div class="todo-form-container">
        <form class="todo-form">
          <label for="default-search"
            class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none">
                <path
                  d="M17 8H10V1C10 0.734784 9.89464 0.48043 9.70711 0.292893C9.51957 0.105357 9.26522 0 9 0C8.73478 0 8.48043 0.105357 8.29289 0.292893C8.10536 0.48043 8 0.734784 8 1V8H1C0.734784 8 0.48043 8.10536 0.292893 8.29289C0.105357 8.48043 0 8.73478 0 9C0 9.26522 0.105357 9.51957 0.292893 9.70711C0.48043 9.89464 0.734784 10 1 10H8V17C8 17.2652 8.10536 17.5196 8.29289 17.7071C8.48043 17.8946 8.73478 18 9 18C9.26522 18 9.51957 17.8946 9.70711 17.7071C9.89464 17.5196 10 17.2652 10 17V10H17C17.2652 10 17.5196 9.89464 17.7071 9.70711C17.8946 9.51957 18 9.26522 18 9C18 8.73478 17.8946 8.48043 17.7071 8.29289C17.5196 8.10536 17.2652 8 17 8Z"
                  fill="#2F2F38" />
              </svg>
            </div>
            <input type="text" id="default-search"
              class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="What do you need to do?" required>
            <button type="submit"
              class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              v-on:click="onClickAddBtn">Add</button>
          </div>
        </form>
      </div>
    </div>

    <div class="todo-ul-container mt-5">
      <div>
        <div class="my-3 text-left font-bold">Uncompleted</div>
        <ul class="todo-ul-uncompleted w-full space-y-2 text-gray-500 list-inside dark:text-gray-400"></ul>
      </div>
      <div class="todo-completed-container">
        <div class="flex justify-between my-3">
          <div class="my-3 text-left font-bold">Completed</div>
          <div>
            <label class="relative inline-flex items-center cursor-pointer">
              <input type="checkbox" value="" class="sr-only peer" onchange="showTodoCompletedList(this);">
              <div
                class="w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600">
              </div>
              <span class="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300">Show done</span>
            </label>
          </div>
        </div>
        <ul class="todo-ul-completed hidden w-full space-y-2 text-gray-500 list-inside dark:text-gray-400"></ul>
      </div>
    </div>

    <div id="todo-chart" class="w-full"></div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    onClickAddBtn: async function (e) {
      const target = e.target
      // const todoUlContainer = document.querySelector('.todo-ul-container')
      // const todoUl = todoUlContainer.querySelector('.todo-ul-uncompleted')

      const inputObj = target.closest('.todo-form').querySelector('input')

      // console.log(todoUl)
      console.log(inputObj)
      // const resData = await axios({
      //     method: 'post',
      //     url: '/api/v1/todos/',
      //     headers: {
      //         'Content-Type': 'application/json'
      //     },
      //     data: {
      //         content: inputObj.value,
      //     }
      // })
      // .then((response) => {
      //     return getAxiosResponseData(response)
      // })
      // .catch((err) => {
      //     console.error(err)
      // })
      location.reload()
    }
  }
}
</script>
