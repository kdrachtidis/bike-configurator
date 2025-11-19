<template>
  <section class="card border-secondary mb-3">
    <ConfiguratorModuleHeader :assemblygroup="assemblygroup" />
    <ConfiguratorModuleSubHeader :count="currentGroupModules.length" />
    <div class="collapse show" :id="'collapse-' + assemblygroup.id">
      <div class="card-body p-0 overflow-auto" style="height: 300px;">
        <!-- Loading State -->
        <div v-if="isLoadingModules" class="alert alert-info m-2">
          <div class="d-flex align-items-center">
            <div class="spinner-border spinner-border-sm me-2" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
            <small>Lade Module für {{ assemblygroup?.name }}...</small>
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
        <div v-else-if="currentGroupModules.length === 0" class="alert alert-info m-2">
          <small>
            <i class="bi bi-info-circle me-1"></i>
            Keine Module für {{ assemblygroup?.name }} verfügbar.
          </small>
        </div>

        <ul class="list-group list-group-flush">
          <li v-for="assemblygroupmodule in currentGroupModules" :key="assemblygroupmodule.id"
            class="list-group-item bg-dark-subtle">
            <ConfiguratorModuleItemCategory v-if="moduleState" :assemblygroupmodule="assemblygroupmodule" />
            <ConfiguratorModuleItemProduct v-else :assemblygroupmodule="assemblygroupmodule" :Category="wtf" />
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

  import { useAssemblyGroupModuleStore } from '@/stores/assemblygroupmodule'
  import { useBikeTypeStore } from '@/stores/biketype'

  const componentStore = useAssemblyGroupModuleStore() // Store instance
  const bikeTypeStore = useBikeTypeStore() // Bike type store instance

  const moduleState = true // true = Categories, false = Products

  const props = defineProps({
    assemblygroup: { type: Object, required: true },
    ModuleSum: String
  })

  // Loading state for modules
  const isLoadingModules = ref(false)

  // Computed property for the modules of this specific group
  const currentGroupModules = computed(() => { // Compute modules for the current assembly group
    if (props.assemblygroup?.id) { // Check if assemblygroup and its id exist
      return componentStore.getAssemblyGroupModulesForGroup(props.assemblygroup.id) // Get modules for the specific group
    }
    return []
  })

  // Load modules for the specific Assembly Group
  const loadModulesForGroup = async () => {
    console.log('loadModulesForGroup called with assemblygroup:', props.assemblygroup)
    console.log('assemblygroup.id:', props.assemblygroup?.id)
    console.log('current biketype:', bikeTypeStore.currentBikeType?.id)

    if (props.assemblygroup?.id && bikeTypeStore.currentBikeType?.id) { // Check if both assemblygroup and biketype exist
      console.log('Loading modules for bike type:', bikeTypeStore.currentBikeType.id, 'group ID:', props.assemblygroup.id)
      isLoadingModules.value = true // Set loading state
      try {
        await componentStore.getAssemblyGroupModulesByGroup(bikeTypeStore.currentBikeType.id, props.assemblygroup.id) // Use hierarchical API
        console.log('Modules loaded for group', props.assemblygroup.id, ':', currentGroupModules.value)
      } catch (error) {
        console.error('Error in loadModulesForGroup:', error)
      } finally {
        isLoadingModules.value = false // Clear loading state
      }
    } else {
      console.warn('Missing assemblygroup.id or biketype.id:', {
        assemblygroupId: props.assemblygroup?.id,
        bikeTypeId: bikeTypeStore.currentBikeType?.id
      })
    }
  }

  // Load modules when component is mounted
  onMounted(() => {
    loadModulesForGroup()
  })

  // Reload modules when the assemblygroup changes
  watch(() => props.assemblygroup?.id, (newId, oldId) => { // Watch for changes in assemblygroup id
    console.log('AssemblyGroup ID changed from', oldId, 'to', newId)
    if (newId) { // If newId is valid
      loadModulesForGroup() // Reload modules when assemblygroup changes
    }
  })

  // Also watch for name changes to detect updates
  watch(() => props.assemblygroup?.name, (newName, oldName) => {
    console.log('AssemblyGroup name changed from', oldName, 'to', newName)
    // Name changes don't require module reload, but good for debugging
  })

  // Watch for bike type changes and reload modules
  watch(() => bikeTypeStore.currentBikeType?.id, (newBikeTypeId, oldBikeTypeId) => {
    console.log('CardModule: Bike type changed from', oldBikeTypeId, 'to', newBikeTypeId)
    if (newBikeTypeId && props.assemblygroup?.id) {
      loadModulesForGroup() // Reload modules when bike type changes
    }
  })
</script>
