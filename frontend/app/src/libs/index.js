import axios from 'axios';
import VueCookies from "vue-cookies";

const axiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  // baseURL: '/api',
  withCredentials: false, // CORS 요청에 대한 쿠키 전송 여부 설정
});

axiosInstance.interceptors.request.use(
  config => {
    const token = VueCookies.get('auth_token');

    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
      config.headers['Access-Control-Allow-Origin'] = '*';
    }

    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default axiosInstance;