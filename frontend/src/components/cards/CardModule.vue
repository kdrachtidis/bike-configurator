<template>
  <section class="card border-secondary mb-3">
    <BikeComponentHeader :bikecomponent="bikecomponent" />
    <BikeComponentSubHeader :count="currentBikeParts.length" />
    <div class="collapse show" :id="'collapse-' + bikecomponent.id">
      <div class="card-body p-0 overflow-auto" style="height: 300px;">
        <!-- Loading State -->
        <div v-if="isLoadingParts" class="alert alert-info m-2">
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

        <!-- No Parts Found -->
        <div v-else-if="currentBikeParts.length === 0">
          <BikePartUnassigned :bikecomponent="bikecomponent" />
        </div>

        <ul class="list-group list-group-flush">
          <li v-for="bikepart in currentBikeParts" :key="bikepart.id"
            class="list-group-item bg-dark-subtle">
            <BikePart v-if="moduleState" :bikepart="bikepart" :bikecomponent="bikecomponent" />
            <BikeProduct v-else :bikepart="bikepart" :Category="wtf" />
          </li>
        </ul>
      </div>
    </div>
    <BikeComponentFooter :Sum="ModuleSum" />
  </section>
</template>

<script setup>
  import { onMounted, watch, computed, ref } from 'vue'
  import BikeComponentHeader from './CardHeader.vue'
  import BikeComponentSubHeader from './CardSubHeader.vue'
  import BikePart from './CardItemCategory.vue'
  import BikeProduct from './CardItemProduct.vue'
  import BikePartUnassigned from './CardItemEmpty.vue'
  import BikeComponentFooter from './CardFooter.vue'

  import { useBikePartStore } from '@/stores/bikepart'
  import { useBikeTypeStore } from '@/stores/biketype'

  const componentStore = useBikePartStore() // Store instance
  const bikeTypeStore = useBikeTypeStore() // Bike type store instance

  const moduleState = true // true = Categories, false = Products

  const props = defineProps({ // Define props
    bikecomponent: { type: Object, required: true }, // Bike component object
    ModuleSum: String
  })

  // Loading state for parts
  const isLoadingParts = ref(false)

  // Computed property for the parts of this specific group
  const currentBikeParts = computed(() => { // Compute parts for the current bike component
    if (props.bikecomponent?.id) { // Check if bikecomponent and its id exist
      return componentStore.getBikePartsForComponent(props.bikecomponent.id) // Get parts for the specific group
    }
    return []
  })

  // Load parts for the specific Bike Component
  const loadPartsForComponent = async () => {
    console.log('loadPartsForComponent called with bikecomponent:', props.bikecomponent) // Debug log
    console.log('bikecomponent.id:', props.bikecomponent?.id) // Log bikecomponent id
    console.log('current biketype:', bikeTypeStore.currentBikeType?.id) // Log current bike type id

    if (props.bikecomponent?.id && bikeTypeStore.currentBikeType?.id) { // Check if both bikecomponent and biketype exist
      console.log('Loading parts for bike type:', bikeTypeStore.currentBikeType.id, 'component ID:', props.bikecomponent.id) // Debug log
      isLoadingParts.value = true // Set loading state
      try {
        await componentStore.getBikePartsByComponent(bikeTypeStore.currentBikeType.id, props.bikecomponent.id) // Use hierarchical API
        console.log('Parts loaded for group', props.bikecomponent.id, ':', currentBikeParts.value) // Log loaded parts
      } catch (error) {
        console.error('Error in loadPartsForComponent:', error)
      } finally {
        isLoadingParts.value = false // Clear loading state
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
    loadPartsForComponent()
  })

  // Reload modules when the bikecomponent changes
  watch(() => props.bikecomponent?.id, (newId, oldId) => { // Watch for changes in bikecomponent id
    console.log('BikeComponent ID changed from', oldId, 'to', newId)
    if (newId) { // If newId is valid
      loadPartsForComponent() // Reload modules when bikecomponent changes
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
      loadPartsForComponent() // Reload modules when bike type changes
    }
  })
</script>
