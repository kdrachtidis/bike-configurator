<template>
  <section class="card border-secondary mb-3">
    <ConfiguratorModuleHeader :assemblygroup="assemblygroup" />
    <ConfiguratorModuleSubHeader />
    <div class="collapse show" :id="assemblygroup.id">
      <div class="card-body p-0 overflow-auto" style="height: 300px;">
        <ul class="list-group list-group-flush">
          <li v-for="assemblygroupmodule in componentStore.assemblygroupmodules" :key="assemblygroupmodule.id" class="list-group-item">
            <ConfiguratorModuleItemCategory :assemblygroupmodule="assemblygroupmodule" />
          </li>
        </ul>
      </div>
    </div>
    <ConfiguratorModuleFooter :Sum="ModuleSum" />
  </section>
</template>

<script setup>
import ConfiguratorModuleHeader from './ConfiguratorModuleHeader.vue'
import ConfiguratorModuleFooter from './ConfiguratorModuleFooter.vue'
import ConfiguratorModuleSubHeader from './ConfiguratorModuleSubHeader.vue'
import ConfiguratorModuleItemCategory from './ConfiguratorModuleItemCategory.vue'

import { useAssemblyGroupModuleStore } from '@/stores/assemblygroupmodule'

const componentStore = useAssemblyGroupModuleStore()
componentStore.getAssemblyGroupModules()

defineProps({
  assemblygroup: { type: Object, required: true },
  ModuleId: String,
  ModuleGroup: String,
  ModuleSum: String
})
</script>
