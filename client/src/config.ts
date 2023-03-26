const { ENVIRONMENT } = process.env;
const API_URL =
  ENVIRONMENT === 'docker' ? 'http://nginx/api' : 'http://localhost:8080/api';
export default API_URL;
