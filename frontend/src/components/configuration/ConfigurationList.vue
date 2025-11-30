<template>
  <div class="container">
    <!-- Loading State -->
    <div v-if="isLoadingBikeComponents" class="row mt-3">
      <div class="col-12 text-center">
        <div class="alert alert-info">
          <div class="d-flex justify-content-center align-items-center">
            <div class="spinner-border spinner-border-sm me-2" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
            <span>Lade Bike Components für {{ bikeTypeStore.currentBikeType?.name }}...</span>
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

    <!-- No Bike Components -->
    <div v-else-if="bikeComponentStore.bikecomponents.length === 0" class="row mt-3">
      <div class="col-12 text-center">
        <div class="alert alert-info">
          <i class="bi bi-info-circle me-2"></i>
          Keine Bike Components für {{ bikeTypeStore.currentBikeType?.name }} gefunden.
        </div>
      </div>
    </div>

    <!-- Bike Components -->
    <div v-else class="row mt-3 row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 row-cols-xxl-4">
      <div v-for="bikecomponent in bikeComponentStore.bikecomponents" :key="bikecomponent.id">
        <ConfiguratorModule :bikecomponent="bikecomponent" :ModuleSum="ModuleSum" />
      </div>
    </div>
  </div>

</template>

<script setup>
  import { watch, onMounted, ref } from 'vue';
  import ConfiguratorModule from '../cards/CardModule.vue';

  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { useBikeTypeStore } from '@/stores/biketype'

  const bikeComponentStore = useBikeComponentStore()
  const bikeTypeStore = useBikeTypeStore()

  const ModuleSum = "150,00 €"
  const isLoadingBikeComponents = ref(false)

  // Function to load bike components for current bike type
  async function loadBikeComponents() {
    if (bikeTypeStore.currentBikeType?.id) {
      console.log('ConfigurationList: Loading bike components for bike type:', bikeTypeStore.currentBikeType.id);
      isLoadingBikeComponents.value = true;
      try {
        await bikeComponentStore.getBikeComponentsByBikeType(bikeTypeStore.currentBikeType.id);
      } catch (error) {
        console.error('ConfigurationList: Error loading bike components:', error);
      } finally {
        isLoadingBikeComponents.value = false;
      }
    } else {
      console.log('ConfigurationList: No bike type selected, clearing bike components.');
      bikeComponentStore.bikecomponents = [];
    }
  }

  // Load bike components when component mounts
  onMounted(() => {
    loadBikeComponents();
  });

  // Watch for bike type changes and reload bike components accordingly
  watch(
    () => bikeTypeStore.currentBikeType?.id,
    (newBikeTypeId, oldBikeTypeId) => {
      console.log('ConfigurationList: Bike type changed from', oldBikeTypeId, 'to', newBikeTypeId);
      if (newBikeTypeId) {
        loadBikeComponents();
      }
    }
  );
</script>
