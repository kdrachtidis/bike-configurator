<template>
  <div class="card-header d-flex justify-content-between align-items-center bg-body-secondary">
    <h4 class="card-title mb-0 fw-light">{{ bikecomponent.name || "Component Name Empty" }}</h4>

    <div class="d-flex gap-2">
      <button type="button" class="btn btn-sm btn-outline-secondary" @click="openEditComponentModal"
        :title="$t('card.header.edit')" :aria-label="$t('card.header.edit')">
        <i class="bi bi-pencil-fill"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
  import { useBikeComponentStore } from '@/stores/bikecomponent'

  const props = defineProps({
    bikecomponent: { type: Object, required: true }, // Bike component object
  })

  const bikeComponentStore = useBikeComponentStore() // Store instance

  const openEditComponentModal = () => {
    bikeComponentStore.setEditComponent(props.bikecomponent)
    window.dispatchEvent(new CustomEvent('open-add-bike-component-modal'))
  }
</script>
