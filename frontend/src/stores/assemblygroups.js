import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAssemblyGroupStore = defineStore('assemblygroups', () => {
  const assemblygroups = ref([]);

  async function getAssemblyGroups() {
    const response = await fetch('api/assemblygroups');
    assemblygroups.value = await response.json();
  };
  return { assemblygroups, getAssemblyGroups};
});
