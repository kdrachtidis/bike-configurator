<template>
  <div class="container">
    <div class="row mt-3 row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 row-cols-xxl-4">
      <div v-for="assemblygroup in assemblygroupStore.assemblygroups" :key="assemblygroup.id">
        <ConfiguratorModule :assemblygroup="assemblygroup" :ModuleSum="ModuleSum" />
      </div>
    </div>
  </div>

</template>

<script setup>
import ConfiguratorModule from '../assemblygroup/CardModule.vue';

import { useAssemblyGroupStore } from '@/stores/assemblygroups'

const assemblygroupStore = useAssemblyGroupStore()
assemblygroupStore.getAssemblyGroups()

const ModuleSum = "150,00 €"
</script>
