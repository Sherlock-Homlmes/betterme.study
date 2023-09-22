const {ENVIRON} = process.env;
const fetchLink =
  ENVIRON === 'docker'
  ? 'http://server:8080/api'
  : ENVIRON === 'production'
  ? process.env.BASE_URL
  : 'http://localhost:8080/api';
export default fetchLink;
