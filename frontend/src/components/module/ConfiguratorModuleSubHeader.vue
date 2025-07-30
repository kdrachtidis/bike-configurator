<template>
  <div class="card-body pt-2 pb-2 border-bottom d-flex justify-content-between bg-body">
    <div class="mt-1"><small class="text-body-secondary"><span class="badge text-bg-info">{{
      componentStore.assemblygroupmodules.length }}</span> {{ $t("message.items")
          }}</small></div>
    <button type="button" class="btn btn-sm btn-outline-secondary" :aria-label="$t('message.filter')">{{
      $t("message.filter") }}</button>
  </div>
</template>

<script setup>
import { useAssemblyGroupModuleStore } from '@/stores/assemblygroupmodule'

const componentStore = useAssemblyGroupModuleStore()

componentStore.getAssemblyGroupModules()
</script>
