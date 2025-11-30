import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useBikeComponentStore = defineStore('bikecomponents', () => { // Define the bike components store
  const bikecomponents = ref([]); // All bike components
  const currentEditComponent = ref(null); // Currently editing component
  const currentBikeTypeId = ref(null); // Currently selected bike type ID

  async function getBikeComponents() { // Fetch all bike components (deprecated - use getBikeComponentsByBikeType instead)
    try {
      const { data } = await axios.get('api/bikecomponents'); // Fetch all bike components
      bikecomponents.value = data; // Store all bike components
    } catch (error) {
      console.error('Error fetching bike components:', error);
    }
  };

  async function getBikeComponentsByBikeType(bikeTypeId) { // Fetch bike components for specific bike type
    try {
      console.log('BikeComponentStore: Fetching components for bike type ID:', bikeTypeId);
      const { data } = await axios.get(`api/biketypes/${bikeTypeId}/bikecomponents`); // Use hierarchical API
      bikecomponents.value = data; // Store bike components for this bike type
      currentBikeTypeId.value = bikeTypeId; // Store the current bike type ID
      console.log('BikeComponentStore: Components loaded:', data);
      return data;
    } catch (error) {
      console.error('Error fetching bike components by bike type:', error);
      bikecomponents.value = []; // Clear on error
      return [];
    }
  };

  async function getBikeComponentById(componentId) { // Fetch a specific bike component by ID
    try {
      const { data } = await axios.get(`api/bikecomponents/${componentId}`); // API call to get bike component by ID
      return data;
    } catch (error) {
      console.error('Error fetching bike component by id:', error);
      return null;
    }
  };

  async function updateBikeComponent(componentId, newName) { // Update a bike component name (deprecated - use updateBikeComponentByBikeType)
    try {
      const { data } = await axios.put(`api/bikecomponents/${componentId}`, {
        name: newName
      }); // API call to update bike component

      // Update the local store reactively
      const index = bikecomponents.value.findIndex(component => component.id === componentId);
      if (index !== -1) {
        // Update properties instead of replacing the whole object to maintain reactivity
        Object.assign(bikecomponents.value[index], data);
      }

      return data;
    } catch (error) {
      console.error('Error updating bike component:', error);
      throw error;
    }
  };

  async function updateBikeComponentByBikeType(bikeTypeId, componentId, newName) { // Update a bike component name using hierarchical API
    try {
      console.log('BikeComponentStore: Updating component', componentId, 'for bike type', bikeTypeId, 'with name:', newName);
      const { data } = await axios.put(`api/biketypes/${bikeTypeId}/bikecomponents/${componentId}`, {
        name: newName
      }); // Use hierarchical API
      console.log('BikeComponentStore: Component updated successfully:', data);

      // Update the local store reactively
      const index = bikecomponents.value.findIndex(component => component.id === componentId);
      if (index !== -1) {
        // Update properties instead of replacing the whole object to maintain reactivity
        Object.assign(bikecomponents.value[index], data);
      }

      return data;
    } catch (error) {
      console.error('Error updating bike component by bike type:', error);
      throw error;
    }
  };

  // Function to set the component to edit
  function setEditComponent(component) {
    currentEditComponent.value = component;
  }

  // Function to clear the edit component
  function clearEditComponent() {
    currentEditComponent.value = null;
  }

  return {
    bikecomponents,
    currentEditComponent,
    currentBikeTypeId,
    getBikeComponents,
    getBikeComponentsByBikeType,
    getBikeComponentById,
    updateBikeComponent,
    updateBikeComponentByBikeType,
    setEditComponent,
    clearEditComponent
  };
});
