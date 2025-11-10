import axios from 'axios';
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useBikeTypeStore = defineStore('biketypes', () => {
  const biketypes = ref([]); // All bike types
  const currentBikeType = ref(null); // Currently selected bike type
  const loading = ref(false); // Loading state
  const error = ref(null); // Error state

  async function getBikeTypes() { // Fetch all bike types
    loading.value = true; // Set loading state
    error.value = null; // Clear previous errors
    try {
      const { data } = await axios.get('api/biketypes'); // API call to get bike types
      biketypes.value = data; // Store bike types
      console.log('Store: Fetched bike types:', data);
      return data;
    } catch (err) { // Handle errors
      console.error('Error fetching bike types:', err);
      error.value = err.response?.data?.message || err.message || 'Failed to fetch bike types'; // Set error message
      biketypes.value = [];
      return [];
    } finally {
      loading.value = false; // Reset loading state
    }
  }

  async function getBikeTypeById(id) { // Fetch bike type by ID
    loading.value = true; // Set loading state
    error.value = null; // Clear previous errors
    try { // API call to get bike type by ID
      const { data } = await axios.get(`api/biketypes/${id}`); // Fetch bike type by ID
      console.log('Store: Fetched bike type by ID:', data); // Log fetched data
      return data;
    } catch (err) { // Handle errors
      console.error('Error fetching bike type by ID:', err);
      error.value = err.response?.data?.message || err.message || 'Failed to fetch bike type'; // Set error message
      return null;
    } finally {
      loading.value = false; // Reset loading state
    }
  }

  function setBikeType(bikeType) { // Set the current bike type
    currentBikeType.value = bikeType; // Update state
    console.log('Store: Set current bike type:', bikeType);
  }

  function clearBikeType() { // Clear the current bike type
    currentBikeType.value = null; // Reset state
    console.log('Store: Cleared current bike type');
  }

  function getBikeTypeByName(name) { // Get bike type by name
    return biketypes.value.find(type => type.name === name) || null;
  }

  // Get bike type names for dropdowns/selectors
  const bikeTypeNames = computed(() => {
    return biketypes.value.map(type => type.name);
  });

  return {
    // State
    biketypes,
    currentBikeType,
    loading,
    error,

    // Actions
    getBikeTypes,
    getBikeTypeById,
    setBikeType,
    clearBikeType,
    getBikeTypeByName,

    // Getters
    bikeTypeNames
  };
});
