<template>
  <div class="justify-content-between">
    <div class="row align-items-center">
      <div class="col-9 text-body-secondary">
        <span class="me-2">{{ bikeproduct.name || 'Product empty' }}</span>
      </div>
      <div class="col-3 justify-content-md-end d-flex">
        <span v-if="showSource" class="badge text-bg-secondary align-self-start">
          {{ bikeproduct.source || 'Unknown' }}
        </span>
      </div>
    </div>
    <div class="row mt-1">
      <div class="col-8 text-body-tertiary">{{ part.name || 'Category empty' }}</div>
      <div class="col-4 text-end text-body-tertiary">
        {{ formatPrice(bikeproduct?.price) }}
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  bikeproduct: { type: Object, required: true },
  part: { type: Object, required: true },
  showSource: { type: Boolean, default: false },
})

const formatPrice = (value) => {
  const numeric = Number(value ?? 0)
  if (!Number.isFinite(numeric)) {
    return '0,00€'
  }
  return `${numeric.toFixed(2).replace('.', ',')}€`
}
</script>
