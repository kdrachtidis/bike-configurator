<template>
  <div class="container">
    <!-- Loading State -->
    <div v-if="isLoadingAssemblyGroups" class="row mt-3">
      <div class="col-12 text-center">
        <div class="alert alert-info">
          <div class="d-flex justify-content-center align-items-center">
            <div class="spinner-border spinner-border-sm me-2" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
            <span>Lade Assembly Groups für {{ bikeTypeStore.currentBikeType?.name }}...</span>
          </div>
        </div>
      </div>
    </div>

    <!-- No Bike Type Selected -->
    <div v-else-if="!bikeTypeStore.currentBikeType" class="row mt-3">
      <div class="col-12 text-center">
        <div class="alert alert-warning">
          <i class="bi bi-exclamation-triangle me-2"></i>
          Bitte wählen Sie einen Fahrradtyp aus dem Dropdown-Menü oben aus.
        </div>
      </div>
    </div>

    <!-- No Assembly Groups -->
    <div v-else-if="assemblygroupStore.assemblygroups.length === 0" class="row mt-3">
      <div class="col-12 text-center">
        <div class="alert alert-info">
          <i class="bi bi-info-circle me-2"></i>
          Keine Assembly Groups für {{ bikeTypeStore.currentBikeType?.name }} gefunden.
        </div>
      </div>
    </div>

    <!-- Assembly Groups -->
    <div v-else class="row mt-3 row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 row-cols-xxl-4">
      <div v-for="assemblygroup in assemblygroupStore.assemblygroups" :key="assemblygroup.id">
        <ConfiguratorModule :assemblygroup="assemblygroup" :ModuleSum="ModuleSum" />
      </div>
    </div>
  </div>

</template>

<script setup>
  import { watch, onMounted, ref } from 'vue';
  import ConfiguratorModule from '../cards/CardModule.vue';

  import { useAssemblyGroupStore } from '@/stores/assemblygroups'
  import { useBikeTypeStore } from '@/stores/biketype'

  const assemblygroupStore = useAssemblyGroupStore()
  const bikeTypeStore = useBikeTypeStore()

  const ModuleSum = "150,00 €"
  const isLoadingAssemblyGroups = ref(false)

  // Function to load assembly groups for current bike type
  async function loadAssemblyGroups() {
    if (bikeTypeStore.currentBikeType?.id) {
      console.log('ConfigurationList: Loading assembly groups for bike type:', bikeTypeStore.currentBikeType.id);
      isLoadingAssemblyGroups.value = true;
      try {
        await assemblygroupStore.getAssemblyGroupsByBikeType(bikeTypeStore.currentBikeType.id);
      } catch (error) {
        console.error('ConfigurationList: Error loading assembly groups:', error);
      } finally {
        isLoadingAssemblyGroups.value = false;
      }
    } else {
      console.log('ConfigurationList: No bike type selected, clearing assembly groups');
      assemblygroupStore.assemblygroups = [];
    }
  }

  // Load assembly groups when component mounts
  onMounted(() => {
    loadAssemblyGroups();
  });

  // Watch for bike type changes and reload assembly groups
  watch(
    () => bikeTypeStore.currentBikeType?.id,
    (newBikeTypeId, oldBikeTypeId) => {
      console.log('ConfigurationList: Bike type changed from', oldBikeTypeId, 'to', newBikeTypeId);
      if (newBikeTypeId) {
        loadAssemblyGroups();
      }
    }
  );
</script>
