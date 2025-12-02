import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useBikePartStore = defineStore('bikeparts', () => { // Define the bike parts store
  const bikeparts = ref([]); // All bike parts
  const bikepartsByComponent = ref(new Map()); // Grouped bike parts by component_id
  const currentEditPart = ref(null); // Currently editing part

  async function getBikeParts() { // Fetch all modules
    try {
      const { data } = await axios.get('api/bikeparts'); // Fetch all modules
      bikeparts.value = data; // Store all modules
    } catch (error) { // Handle errors
      console.error('Error fetching bike parts:', error);
    }
  };

  async function getBikePartsByComponent(bikeTypeId, componentId) { // Fetch modules for a specific group using hierarchy
    try {
      console.log('Store: Fetching modules for bike type:', bikeTypeId, 'component ID:', componentId) // Log fetch attempt
      const url = `api/biketypes/${bikeTypeId}/bikecomponents/${componentId}/bikeparts` // Use hierarchical API
      console.log('Store: API URL:', url)

      const { data } = await axios.get(url); // Fetch modules for the component
      console.log('Store: API Response:', data) // Log full response
      console.log('Store: Number of parts received:', data?.length || 0) // Log number of parts

      // Store modules in the Map instead of overwriting global state
      bikepartsByComponent.value.set(componentId, data); // Map componentId to its modules
      console.log('Store: modulesByComponent updated for component', componentId, ':', data) // Log updated Map entry

      return data;
    } catch (error) {
      console.error('Store: Error fetching bike parts by component:', error)
      console.error('Store: Error details:', error.response?.data || error.message)
      // Set empty array for this component on error
      bikepartsByComponent.value.set(componentId, []); // Avoid stale data
      return [];
    }
  };

  // Function to get modules for a specific component
  function getBikePartsForComponent(componentId) {
    return bikepartsByComponent.value.get(componentId) || []; // Return modules for the component or empty array
  }

  // Function to set the part to edit
  function setEditPart(part) {
    currentEditPart.value = part;
  }

  // Function to clear the edit part
  function clearEditPart() {
    currentEditPart.value = null;
  }

  return {
    bikeparts: bikeparts, // All bike parts
    bikepartsByComponent: bikepartsByComponent, // Bike parts grouped by component
    currentEditPart: currentEditPart, // Currently editing part
    getBikeParts: getBikeParts, // Get all bike parts
    getBikePartsByComponent: getBikePartsByComponent, // Get bike parts for specific component
    getBikePartsForComponent: getBikePartsForComponent, // Get bike parts for a specific component
    setEditPart: setEditPart, // Set the part to edit
    clearEditPart: clearEditPart // Clear the edit part
  };
});
