import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import SignUp from "@/views/SignUp.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  }, {
    path: "/join",
    name: "SignUp",
    component: SignUp,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;