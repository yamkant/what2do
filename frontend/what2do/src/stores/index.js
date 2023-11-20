import { createStore } from "vuex";

export default createStore({
    state : {
        token : null
    },
    getters: {
      isLoggedIn: state => {
        return state.token !== null;
      },
    },
    mutations : {
        setToken(state, token){
          state.token = token;
        },
        clearToken(state) {
          state.token = null;
        }
    },
});