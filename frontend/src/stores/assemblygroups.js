import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAssemblyGroupStore = defineStore('assemblygroups', () => { // Define the assembly groups store
  const assemblygroups = ref([]); // All assembly groups
  const currentEditGroup = ref(null); // Currently editing group

  async function getAssemblyGroups() { // Fetch all assembly groups
    try {
      const { data } = await axios.get('api/assemblygroups'); // Fetch all assembly groups
      assemblygroups.value = data; // Store all assembly groups
    } catch (error) {
      console.error('Error fetching assembly groups:', error);
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

  return { assemblygroups, currentEditGroup, getAssemblyGroups, getAssemblyGroupById, updateAssemblyGroup, setEditGroup, clearEditGroup };
});
