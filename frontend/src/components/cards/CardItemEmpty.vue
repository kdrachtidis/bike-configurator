<template>
  <div class="alert alert-info m-2">
    <small>
      <i class="bi bi-info-circle me-1"></i>
      Keine Teile verfügbar für {{ props.bikecomponent?.name }}.
    </small>
  </div>
  <!--<div class="d-flex justify-content-between">
    <div class="fs-5 fw-light">
      No parts available yet.
    </div>
    <button type="button" class="btn btn-sm btn-outline-light" aria-label="Hinzufügen" data-bs-toggle="modal"
      data-bs-target="#AddBikeProduct">
      <i class="bi bi-plus-lg"></i>
    </button>
  </div>-->
</template>

<script setup>
  const props = defineProps({
    bikecomponent: { type: Object, required: true },
  })
</script>
