import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAssemblyGroupStore = defineStore('assemblygroups', () => { // Define the assembly groups store
  const assemblygroups = ref([]); // All assembly groups

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

  return { assemblygroups, getAssemblyGroups, getAssemblyGroupById };
});
