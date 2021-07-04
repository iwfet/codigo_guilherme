import axios from 'axios';
const api = axios.create({
    baseURL: 'http://127.0.0.1:5000/',
    timeout:10000
    
    //baseURL: 'https://api.tvmaze.com/search/shows?q='
})
export default api;