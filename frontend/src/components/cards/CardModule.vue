<template>
  <section class="card border-secondary mb-3">
    <ConfiguratorModuleHeader :bikecomponent="bikecomponent" />
    <ConfiguratorModuleSubHeader :count="currentBikeParts.length" />
    <div class="collapse show" :id="'collapse-' + bikecomponent.id">
      <div class="card-body p-0 overflow-auto" style="height: 300px;">
        <!-- Loading State -->
        <div v-if="isLoadingModules" class="alert alert-info m-2">
          <div class="d-flex align-items-center">
            <div class="spinner-border spinner-border-sm me-2" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
            <small>Lade Module für {{ bikecomponent?.name }}...</small>
          </div>
        </div>

        <!-- No Bike Type Selected -->
        <div v-else-if="!bikeTypeStore.currentBikeType?.id" class="alert alert-warning m-2">
          <small>
            <i class="bi bi-exclamation-triangle me-1"></i>
            Bitte wählen Sie einen Fahrradtyp aus, um Module zu sehen.
          </small>
        </div>

        <!-- No Modules Found -->
        <div v-else-if="currentBikeParts.length === 0" class="alert alert-info m-2">
          <small>
            <i class="bi bi-info-circle me-1"></i>
            Keine Module für {{ bikecomponent?.name }} verfügbar.
          </small>
        </div>

        <ul class="list-group list-group-flush">
          <li v-for="bikepart in currentBikeParts" :key="bikepart.id"
            class="list-group-item bg-dark-subtle">
            <ConfiguratorModuleItemCategory v-if="moduleState" :bikepart="bikepart" />
            <ConfiguratorModuleItemProduct v-else :bikepart="bikepart" :Category="wtf" />
          </li>
        </ul>
      </div>
    </div>
    <ConfiguratorModuleFooter :Sum="ModuleSum" />
  </section>
</template>

<script setup>
  import { onMounted, watch, computed, ref } from 'vue'
  import ConfiguratorModuleHeader from './CardHeader.vue'
  import ConfiguratorModuleFooter from './CardFooter.vue'
  import ConfiguratorModuleSubHeader from './CardSubHeader.vue'
  import ConfiguratorModuleItemCategory from './CardItemCategory.vue'
  import ConfiguratorModuleItemProduct from './CardItemProduct.vue'

  import { useBikePartStore } from '@/stores/bikepart'
  import { useBikeTypeStore } from '@/stores/biketype'

  const componentStore = useBikePartStore() // Store instance
  const bikeTypeStore = useBikeTypeStore() // Bike type store instance

  const moduleState = true // true = Categories, false = Products

  const props = defineProps({
    bikecomponent: { type: Object, required: true },
    ModuleSum: String
  })

  // Loading state for modules
  const isLoadingModules = ref(false)

  // Computed property for the modules of this specific group
  const currentBikeParts = computed(() => { // Compute modules for the current bike component
    if (props.bikecomponent?.id) { // Check if bikecomponent and its id exist
      return componentStore.getBikePartsForGroup(props.bikecomponent.id) // Get modules for the specific group
    }
    return []
  })

  // Load modules for the specific Bike Component
  const loadModulesForGroup = async () => {
    console.log('loadModulesForGroup called with bikecomponent:', props.bikecomponent)
    console.log('bikecomponent.id:', props.bikecomponent?.id)
    console.log('current biketype:', bikeTypeStore.currentBikeType?.id)

    if (props.bikecomponent?.id && bikeTypeStore.currentBikeType?.id) { // Check if both bikecomponent and biketype exist
      console.log('Loading modules for bike type:', bikeTypeStore.currentBikeType.id, 'component ID:', props.bikecomponent.id)
      isLoadingModules.value = true // Set loading state
      try {
        await componentStore.getBikePartsByGroup(bikeTypeStore.currentBikeType.id, props.bikecomponent.id) // Use hierarchical API
        console.log('Modules loaded for group', props.bikecomponent.id, ':', currentBikeParts.value)
      } catch (error) {
        console.error('Error in loadModulesForGroup:', error)
      } finally {
        isLoadingModules.value = false // Clear loading state
      }
    } else {
      console.warn('Missing bikecomponent.id or biketype.id:', {
        bikecomponentId: props.bikecomponent?.id,
        bikeTypeId: bikeTypeStore.currentBikeType?.id
      })
    }
  }

  // Load modules when component is mounted
  onMounted(() => {
    loadModulesForGroup()
  })

  // Reload modules when the bikecomponent changes
  watch(() => props.bikecomponent?.id, (newId, oldId) => { // Watch for changes in bikecomponent id
    console.log('BikeComponent ID changed from', oldId, 'to', newId)
    if (newId) { // If newId is valid
      loadModulesForGroup() // Reload modules when bikecomponent changes
    }
  })

  // Also watch for name changes to detect updates
  watch(() => props.bikecomponent?.name, (newName, oldName) => {
    console.log('BikeComponent name changed from', oldName, 'to', newName)
    // Name changes don't require module reload, but good for debugging
  })

  // Watch for bike type changes and reload modules
  watch(() => bikeTypeStore.currentBikeType?.id, (newBikeTypeId, oldBikeTypeId) => {
    console.log('CardModule: Bike type changed from', oldBikeTypeId, 'to', newBikeTypeId)
    if (newBikeTypeId && props.bikecomponent?.id) {
      loadModulesForGroup() // Reload modules when bike type changes
    }
  })
</script>
