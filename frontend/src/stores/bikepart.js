import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useBikePartStore = defineStore('bikeparts', () => { // Define the bike parts store
  const bikeparts = ref([]); // All modules
  const bikepartsByGroup = ref(new Map()); // Grouped modules by group_id

  async function getBikeParts() { // Fetch all modules
    try {
      const { data } = await axios.get('api/bikeparts'); // Fetch all modules
      bikeparts.value = data; // Store all modules
    } catch (error) {
      console.error('Error fetching bike parts:', error);
    }
  };

  async function getBikePartsByGroup(bikeTypeId, groupId) { // Fetch modules for a specific group using hierarchy
    try {
      console.log('Store: Fetching modules for bike type:', bikeTypeId, 'group ID:', groupId)
      const url = `api/biketypes/${bikeTypeId}/bikecomponents/${groupId}/bikeparts` // Use hierarchical API
      console.log('Store: API URL:', url)

      const { data } = await axios.get(url); // Fetch modules for the group
      console.log('Store: API Response:', data)
      console.log('Store: Number of modules received:', data?.length || 0)

      // Store modules in the Map instead of overwriting global state
      bikepartsByGroup.value.set(groupId, data); // Map groupId to its modules
      console.log('Store: modulesByGroup updated for group', groupId, ':', data)

      return data;
    } catch (error) {
      console.error('Store: Error fetching bike parts by group:', error)
      console.error('Store: Error details:', error.response?.data || error.message)
      // Set empty array for this group on error
      bikepartsByGroup.value.set(groupId, []); // Avoid stale data
      return [];
    }
  };

  // Function to get modules for a specific group
  function getBikePartsForGroup(groupId) {
    return bikepartsByGroup.value.get(groupId) || [];
  }

  return {
    bikeparts: bikeparts,
    bikepartsByGroup: bikepartsByGroup,
    getBikeParts: getBikeParts,
    getBikePartsByGroup: getBikePartsByGroup,
    getBikePartsForGroup: getBikePartsForGroup
  };
});
