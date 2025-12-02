<template>
  <div class="d-flex justify-content-between">
    <div class="fs-5 fw-light">
      {{ props.bikepart.name || 'Category Empty' }}
    </div>
    <button type="button" class="btn btn-sm btn-outline-secondary" aria-label="Hinzufügen"
      @click="openModal" data-bs-toggle="modal" data-bs-target="#AddBikeProduct" data-toggle="tooltip" data-placement="bottom" :title="$t('card.part.tooltip-add')">
      <i class="bi bi-plus-lg"></i>
    </button>
  </div>
</template>

<script setup>
  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { useBikePartStore } from '@/stores/bikepart'

  const props = defineProps({
    bikepart: { type: Object, required: true },
    bikecomponent: { type: Object, required: true },
  })

  const bikeComponentStore = useBikeComponentStore()
  const bikePartStore = useBikePartStore()

  const openModal = () => {
    // Set the current component and part before opening the modal
    bikeComponentStore.setEditComponent(props.bikecomponent)
    bikePartStore.setEditPart(props.bikepart)
  }
</script>
