import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import SignUp from "@/views/SignUp.vue";
import Login from "@/views/Login.vue";
import VueCookies from "vue-cookies";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { unauthorized: false }
  }, {
    path: "/join",
    name: "SignUp",
    component: SignUp,
    meta: { unauthorized: true }
  }, {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { unauthorized: true }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  // TODO: renew refresh token process 
  // if(VueCookies.get('token')===null && VueCookies.get('refresh_token') !== null){
  //   await refreshToken();
  // }


  if (to.matched.some(record => !record.meta.unauthorized)){
    if (VueCookies.get('auth_token')) {
      // TODO: Check correct token
      return next();
    } else {
      return next('/login');
    }
  }

  return next();
});

export default router;