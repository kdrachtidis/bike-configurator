import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useBikeComponentStore = defineStore('bikecomponents', () => { // Define the bike components store
  const bikecomponents = ref([]); // All bike components
  const currentEditComponent = ref(null); // Currently editing component
  const currentBikeTypeId = ref(null); // Currently selected bike type ID

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
      return data; // Return the fetched component
    } catch (error) {
      console.error('Error fetching bike component by id:', error);
      return null; // Return null on error
    }
  };

  async function createBikeComponent(bikeTypeId, name) { // Create a new bike component using hierarchical API
    try {
      console.log('BikeComponentStore: Creating component for bike type', bikeTypeId, 'with name:', name);
      const { data } = await axios.post(`api/biketypes/${bikeTypeId}/bikecomponents/`, {
        name: name // Name for the new component
      });
      console.log('BikeComponentStore: Component created successfully:', data);

      // Add the new component to the local store
      bikecomponents.value.push(data);
      console.log('BikeComponentStore: Local store updated with new component');

      return data; // Return the created component
    } catch (error) {
      console.error('Error creating bike component:', error);
      throw error;
    }
  };

  async function updateBikeComponentByBikeType(bikeTypeId, componentId, newName) { // Update a bike component name using hierarchical API
    try {
      console.log('BikeComponentStore: Updating component', componentId, 'for bike type', bikeTypeId, 'with name:', newName); // Log update attempt
      const { data } = await axios.put(`api/biketypes/${bikeTypeId}/bikecomponents/${componentId}`, { // Use hierarchical API
        name: newName // New name for the component
      });
      console.log('BikeComponentStore: Component updated successfully:', data);

      // Update the local store reactively
      const index = bikecomponents.value.findIndex(component => component.id === componentId); // Find index of updated component
      if (index !== -1) { // If component exists in store
        // Update properties instead of replacing the whole object to maintain reactivity
        Object.assign(bikecomponents.value[index], data); // Update the existing component's properties
        console.log('BikeComponentStore: Local store updated for component index', index, ':', bikecomponents.value[index]); // Log updated component
      }

      return data; // Return the updated component
    } catch (error) {
      console.error('Error updating bike component by bike type:', error); // Log error
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
    getBikeComponentsByBikeType,
    getBikeComponentById,
    createBikeComponent,
    updateBikeComponentByBikeType,
    setEditComponent,
    clearEditComponent
  };
});
