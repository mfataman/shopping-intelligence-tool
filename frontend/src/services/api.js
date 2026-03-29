// api.js

import axios from 'axios';

const API_URL = 'http://your-backend-url';

const apiClient = axios.create({
    baseURL: API_URL,
    timeout: 1000,
    headers: {'Content-Type': 'application/json'},
});

// GET request example
export const fetchData = async (endpoint) => {
    try {
        const response = await apiClient.get(endpoint);
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
};

// POST request example
export const postData = async (endpoint, data) => {
    try {
        const response = await apiClient.post(endpoint, data);
        return response.data;
    } catch (error) {
        console.error('Error posting data:', error);
        throw error;
    }
};

export default apiClient;