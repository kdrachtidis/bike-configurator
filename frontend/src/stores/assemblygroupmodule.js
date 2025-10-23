import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAssemblyGroupModuleStore = defineStore('assemblygroupmodules', () => { // Define the assembly group modules store
  const assemblygroupmodules = ref([]); // All modules
  const assemblygroupmodulesByGroup = ref(new Map()); // Grouped modules by group_id

  async function getAssemblyGroupModules() { // Fetch all modules
    try {
      const { data } = await axios.get('api/assemblygroupmodules'); // Fetch all modules
      assemblygroupmodules.value = data; // Store all modules
    } catch (error) {
      console.error('Error fetching assembly group modules:', error);
    }
  };

  async function getAssemblyGroupModulesByGroup(groupId) { // Fetch modules for a specific group
    try {
      console.log('Store: Fetching modules for group ID:', groupId)
      const url = `api/assemblygroups/${groupId}/assemblygroupmodules` // Construct API URL
      console.log('Store: API URL:', url)

      const { data } = await axios.get(url); // Fetch modules for the group
      console.log('Store: API Response:', data)
      console.log('Store: Number of modules received:', data?.length || 0)

      // Store modules in the Map instead of overwriting global state
      assemblygroupmodulesByGroup.value.set(groupId, data); // Map groupId to its modules
      console.log('Store: modulesByGroup updated for group', groupId, ':', data)

      return data;
    } catch (error) {
      console.error('Store: Error fetching assembly group modules by group:', error)
      console.error('Store: Error details:', error.response?.data || error.message)
      // Set empty array for this group on error
      assemblygroupmodulesByGroup.value.set(groupId, []); // Avoid stale data
      return [];
    }
  };

  // Function to get modules for a specific group
  function getAssemblyGroupModulesForGroup(groupId) {
    return assemblygroupmodulesByGroup.value.get(groupId) || [];
  }

  return {
    assemblygroupmodules,
    assemblygroupmodulesByGroup,
    getAssemblyGroupModules,
    getAssemblyGroupModulesByGroup,
    getAssemblyGroupModulesForGroup
  };
});
