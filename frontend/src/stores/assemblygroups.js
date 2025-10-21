import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAssemblyGroupStore = defineStore('assemblygroups', () => {
  const assemblygroups = ref([]);

  async function getAssemblyGroups() {
    try {
      const {data} = await axios.get('api/assemblygroups');
      assemblygroups.value = data;
    } catch (error) {
      console.error('Error fetching assembly groups:', error);
    }
  };
  return { assemblygroups, getAssemblyGroups};
});
