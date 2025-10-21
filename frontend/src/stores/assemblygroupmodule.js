import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAssemblyGroupModuleStore = defineStore('assemblygroupmodules', () => {
  const assemblygroupmodules = ref([]);

  async function getAssemblyGroupModules() {
    try {
      const {data} = await axios.get('api/assemblygroupmodules');
      assemblygroupmodules.value = data;
    } catch (error) {
      console.error('Error fetching assembly group modules:', error);
    }
  };
  return { assemblygroupmodules, getAssemblyGroupModules};
});
