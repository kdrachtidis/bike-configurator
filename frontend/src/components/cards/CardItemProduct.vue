<template>
  <div class="justify-content-between">
    <div class="row align-items-center">
      <div class="col-9">
        <a
          :href="getProductUrl(props.bikeproduct?.source)"
          class="link-light link-underline-secondary link-offset-1"
          :target="props.bikeproduct?.source ? '_blank' : undefined"
          :rel="props.bikeproduct?.source ? 'noopener noreferrer' : undefined"
        >
          {{ props.bikeproduct?.name || 'Product empty' }}
        </a>
      </div>
      <div class="col-3 text-end">
        <button type="button" class="btn btn-sm btn-outline-light" aria-label="Editieren">
          <i class="bi bi-pencil"></i>
        </button>
      </div>
    </div>
    <div class="row mt-1">
      <div class="col-8 text-body-tertiary">{{ props.bikepart?.name || 'Bike part is empty' }}</div>
      <div class="col-4 text-end text-body-tertiary">
        {{ formatPrice(props.bikeproduct?.price) }}
      </div>
    </div>
  </div>
</template>

<script setup>
  const props = defineProps({
    bikeproduct: { type: Object, required: true },
    bikepart: { type: Object, required: true }
  })

  const formatPrice = (value) => {
    const numeric = Number(value ?? 0)
    if (!Number.isFinite(numeric)) {
      return '0,00€'
    }
    return `${numeric.toFixed(2).replace('.', ',')}€`
  }

  const getProductUrl = (source) => {
    if (!source || typeof source !== 'string') {
      return '#'
    }

    const trimmed = source.trim()
    if (!trimmed) {
      return '#'
    }

    return /^https?:\/\//i.test(trimmed) ? trimmed : `https://${trimmed}`
  }
</script>
