import axios from 'axios';
import store from '@/stores';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
});

axiosInstance.interceptors.request.use(
  config => {
    const token = store.state.token;

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