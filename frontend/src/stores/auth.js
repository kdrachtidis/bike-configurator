import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token') || null);
  const isAuthenticated = ref(!!token.value);

  // Set up axios interceptor to include token in requests
  if (token.value) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token.value}`;
  }

  async function login(username, password) {
    try {
      const formData = new FormData();
      formData.append('username', username);
      formData.append('password', password);

      const { data } = await axios.post('api/auth/token', formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      token.value = data.access_token;
      isAuthenticated.value = true;

      // Save token to localStorage
      localStorage.setItem('token', data.access_token);

      // Set default authorization header
      axios.defaults.headers.common['Authorization'] = `Bearer ${data.access_token}`;

      return data;
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  }

  function logout() {
    token.value = null;
    isAuthenticated.value = false;
    localStorage.removeItem('token');
    delete axios.defaults.headers.common['Authorization'];
  }

  return { token, isAuthenticated, login, logout };
});
