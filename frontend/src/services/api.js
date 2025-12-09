import axios from 'axios';

// Create axios instance with default config
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:5000/api',
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add token to requests if it exists
const token = localStorage.getItem('token');
if (token) {
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // Get fresh token for each request
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Interview API calls
export const interviewAPI = {
  create: (data) => api.post('/interviews/create', data),
  getAll: () => api.get('/interviews'),
  getById: (id) => api.get(`/interviews/${id}`),
  updateStatus: (id, status) => api.put(`/interviews/${id}/status`, { status }),
  delete: (id) => api.delete(`/interviews/${id}`),
  getStats: () => api.get('/interviews/stats')
};

// Feedback API calls
export const feedbackAPI = {
  submitAnswer: (data) => api.post('/feedback/submit', data),
  getFeedback: (interviewId) => api.get(`/feedback/${interviewId}`),
  getAnswers: (interviewId) => api.get(`/feedback/${interviewId}/answers`),
  generateFeedback: (answerId) => api.post(`/feedback/generate/${answerId}`)
};

// Payment API calls
export const paymentAPI = {
  createOrder: (data) => api.post('/payment/create-order', data),
  verifyPayment: (data) => api.post('/payment/verify', data),
  getHistory: () => api.get('/payment/history')
};

// Auth API calls
export const authAPI = {
  signup: (data) => api.post('/auth/signup', data),
  signin: (data) => api.post('/auth/signin', data),
  getMe: () => api.get('/auth/me'),
  updateProfile: (data) => api.put('/auth/profile', data),
  updatePassword: (data) => api.put('/auth/password', data)
};

export default api;

