import axios from 'axios';

const checkingApi = axios.create({
  baseURL: 'http://localhost:8082', // адрес сервиса проверки
  headers: { 'Content-Type': 'application/json' }
});

// Можно добавить перехватчик для токена авторизации, если требуется
checkingApi.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default checkingApi;