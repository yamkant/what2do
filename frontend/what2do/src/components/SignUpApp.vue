<template>
  <div class="w-80 m-auto">
    <div class="my-3 font-bold">Sign Up Page</div>
    <form @submit.prevent="signUp" class="space-y-3">
      <div>
        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Your email</label>
        <input type="email" id="email"
          v-model="email"
          class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
          placeholder="test@example.com"
          required
        >
      </div>

      <div>
        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Your password</label>
        <input type="password" id="password"
          v-model="password"
          class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
          placeholder="********"
          required
        >
      </div>

      <div>
        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Check password</label>
        <input type="password" id="password"
          v-model="check_password"
          class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
          placeholder="********"
          required
        >
      </div>

      <div class="flex justify-between items-center">
        <a href="login/"
          class="font-medium text-blue-600 hover:underline dark:text-blue-500 ">Go to login page</a>
        <button type="submit"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2.5 text-center"
        >Register new account</button>
      </div>
    </form>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      check_password: '',
    };
  },
  methods: {
    async signUp() {
      try {
        const response = await axios.post(
          `http://localhost:8000/users`,
          {
            email: this.email,
            password: this.password,
          }
        );
      } catch (err) {
        console.error("Error signup process:", err);
      }
    },
  },
};
</script>