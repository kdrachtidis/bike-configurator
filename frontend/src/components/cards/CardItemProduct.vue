<template>
  <div class="justify-content-between">
    <div class="row align-items-center">
      <div class="col-9 text-body-secondary">
        <span class="me-2">{{ props.bikeproduct?.name || 'Product empty' }}</span>
        <span> <a :href="getProductUrl(props.bikeproduct?.source)"
            class="link-light link-underline-secondary link-offset-1"
            :target="props.bikeproduct?.source ? '_blank' : undefined"
            :rel="props.bikeproduct?.source ? 'noopener noreferrer' : undefined"><i
              class="bi bi-box-arrow-up-right"></i></a></span>
      </div>
      <div class="col-3 text-end">
        <button type="button" class="btn btn-sm btn-outline-light" aria-label="Editieren" data-toggle="tooltip"
          data-placement="bottom" :title="$t('card.product.tooltip-edit')" @click="openEditProductModal"
          data-bs-toggle="modal" data-bs-target="#EditBikeProduct">
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
  import { useBikePartStore } from '@/stores/bikepart'
  import { useBikeProductStore } from '@/stores/bikeproduct'

  const props = defineProps({
    bikeproduct: { type: Object, required: true },
    bikepart: { type: Object, required: true }
  })
  const bikePartStore = useBikePartStore()
  const bikeProductStore = useBikeProductStore()

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

  const openEditProductModal = () => {
    bikePartStore.setEditPart(props.bikepart)
    bikeProductStore.setEditProduct(props.bikeproduct)
  }
</script>
