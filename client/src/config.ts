const { ENVIRONMENT } = process.env;
const API_URL =
  ENVIRONMENT === 'docker'
    ? 'http://server:8080/api'
    : 'http://localhost:8080/api';
export default API_URL;
