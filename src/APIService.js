import axios from 'axios';
import AuthService from '../auth/AuthService';
const API_URL = 'http://localhost:8000';

export class APIService {
    constructor() {

    }

    getWeights() {
        const url = `${API_ROOT}/api/v1/weights`
        return axios.get(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` } }).then(response => response.data);
    }
    getWeight(pk) {
        const url = `${API_URL}/api/v1/weights/${pk}`;
        return axios.get(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` } }).then(response => response.data);
    }

    getWeightsByURL(link) {
        const url = `${API_URL}${link}`;
        return axios.get(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` } }).then(response => response.data);

    }

    deleteWeight(weight) {
        const url = `${API_URL}/api/v1/weights/${weight.pk}`;
        return axios.delete(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` } });

    }

    createWeight(weight) {
        const url = `${API_URL}/api/v1/weights/`;
        const headers = { Authorization: `Bearer ${AuthService.getAuthToken()}` };
        return axios.post(url, weight, { headers: headers });
    }

    updateWeight(weight) {
        const url = `${API_URL}/api/weights/${product.pk}`;
        const headers = { Authorization: `Bearer ${AuthService.getAuthToken()}` };
        return axios.put(url, weight, { headers: headers });
    }
}