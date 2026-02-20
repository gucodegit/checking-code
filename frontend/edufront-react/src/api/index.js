import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8081', // адрес бэкенда
  headers: { 'Content-Type': 'application/json' }
});

export default instance;
