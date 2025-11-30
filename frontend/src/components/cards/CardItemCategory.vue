<template>
  <div class="d-flex justify-content-between">
    <div class="fs-5 fw-light">
      {{ props.bikepart.name || 'Category Empty' }}
    </div>
    <button type="button" class="btn btn-sm btn-outline-light" aria-label="Hinzufügen" data-bs-toggle="modal"
      data-bs-target="#AddBikeComponent">
      <i class="bi bi-plus-lg"></i>
    </button>
  </div>
</template>

<script setup>
  const props = defineProps({
    bikepart: { type: Object, required: true },
  })
</script>
