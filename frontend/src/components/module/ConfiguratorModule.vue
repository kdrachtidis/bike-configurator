<template>
  <section class="card border-secondary mb-3">
    <ConfiguratorModuleHeader :assemblygroup="assemblygroup" />
    <ConfiguratorModuleSubHeader :count="currentGroupModules.length" />
    <div class="collapse show" :id="'collapse-' + assemblygroup.id">
      <div class="card-body p-0 overflow-auto" style="height: 300px;">
        <!-- Debug Info -->
        <div v-if="currentGroupModules.length === 0" class="alert alert-info m-2">
          <small>
            Debug: Group ID: {{ assemblygroup?.id || 'undefined' }}<br>
            Debug: Module Count: {{ currentGroupModules.length }}<br>
            Debug: Modules: {{ JSON.stringify(currentGroupModules) }}
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
  import { onMounted, watch, computed } from 'vue'
  import ConfiguratorModuleHeader from './ConfiguratorModuleHeader.vue'
  import ConfiguratorModuleFooter from './ConfiguratorModuleFooter.vue'
  import ConfiguratorModuleSubHeader from './ConfiguratorModuleSubHeader.vue'
  import ConfiguratorModuleItemCategory from './ConfiguratorModuleItemCategory.vue'
  import ConfiguratorModuleItemProduct from './ConfiguratorModuleItemProduct.vue'

  import { useAssemblyGroupModuleStore } from '@/stores/assemblygroupmodule'

  const componentStore = useAssemblyGroupModuleStore() // Store instance

  const moduleState = true // true = Categories, false = Products

  const props = defineProps({
    assemblygroup: { type: Object, required: true },
    ModuleSum: String
  })

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

    if (props.assemblygroup?.id) { // Check if assemblygroup and its id exist
      console.log('Loading modules for group ID:', props.assemblygroup.id)
      try {
        await componentStore.getAssemblyGroupModulesByGroup(props.assemblygroup.id) // Fetch modules from store
        console.log('Modules loaded for group', props.assemblygroup.id, ':', currentGroupModules.value)
      } catch (error) {
        console.error('Error in loadModulesForGroup:', error)
      }
    } else {
      console.warn('No assemblygroup.id available')
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
</script>
