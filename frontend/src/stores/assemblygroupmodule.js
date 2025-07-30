import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAssemblyGroupModuleStore = defineStore('assemblygroupmodules', () => {
  const assemblygroupmodules = ref([]);

  async function getAssemblyGroupModules() {
    const response = await fetch('api/assemblygroupmodules');
    assemblygroupmodules.value = await response.json();
  };
  return { assemblygroupmodules, getAssemblyGroupModules};
});
