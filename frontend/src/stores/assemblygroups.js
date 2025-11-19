import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAssemblyGroupStore = defineStore('assemblygroups', () => { // Define the assembly groups store
  const assemblygroups = ref([]); // All assembly groups
  const currentEditGroup = ref(null); // Currently editing group
  const currentBikeTypeId = ref(null); // Currently selected bike type ID

  async function getAssemblyGroups() { // Fetch all assembly groups (deprecated - use getAssemblyGroupsByBikeType instead)
    try {
      const { data } = await axios.get('api/assemblygroups'); // Fetch all assembly groups
      assemblygroups.value = data; // Store all assembly groups
    } catch (error) {
      console.error('Error fetching assembly groups:', error);
    }
  };

  async function getAssemblyGroupsByBikeType(bikeTypeId) { // Fetch assembly groups for specific bike type
    try {
      console.log('AssemblyGroupStore: Fetching groups for bike type ID:', bikeTypeId);
      const { data } = await axios.get(`api/biketypes/${bikeTypeId}/assemblygroups`); // Use hierarchical API
      assemblygroups.value = data; // Store assembly groups for this bike type
      currentBikeTypeId.value = bikeTypeId; // Store the current bike type ID
      console.log('AssemblyGroupStore: Groups loaded:', data);
      return data;
    } catch (error) {
      console.error('Error fetching assembly groups by bike type:', error);
      assemblygroups.value = []; // Clear on error
      return [];
    }
  };

  async function getAssemblyGroupById(groupId) { // Fetch a specific assembly group by ID
    try {
      const { data } = await axios.get(`api/assemblygroups/${groupId}`); // API call to get assembly group by ID
      return data;
    } catch (error) {
      console.error('Error fetching assembly group by id:', error);
      return null;
    }
  };

  async function updateAssemblyGroup(groupId, newName) { // Update an assembly group name
    try {
      const { data } = await axios.put(`api/assemblygroups/${groupId}`, {
        name: newName
      }); // API call to update assembly group

      // Update the local store reactively
      const index = assemblygroups.value.findIndex(group => group.id === groupId);
      if (index !== -1) {
        // Update properties instead of replacing the whole object to maintain reactivity
        Object.assign(assemblygroups.value[index], data);
      }

      return data;
    } catch (error) {
      console.error('Error updating assembly group:', error);
      throw error;
    }
  };

  // Function to set the group to edit
  function setEditGroup(group) {
    currentEditGroup.value = group;
  }

  // Function to clear the edit group
  function clearEditGroup() {
    currentEditGroup.value = null;
  }

  return { 
    assemblygroups, 
    currentEditGroup, 
    currentBikeTypeId,
    getAssemblyGroups, 
    getAssemblyGroupsByBikeType,
    getAssemblyGroupById, 
    updateAssemblyGroup, 
    setEditGroup, 
    clearEditGroup 
  };
});
