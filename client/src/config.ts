const {ENVIRON} = process.env;
const fetchLink =
  ENVIRON === 'docker' ? 'http://server:8080/api' : 'http://localhost:8080/api';
export default fetchLink;