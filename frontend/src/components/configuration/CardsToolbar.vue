<template>
  <nav class="navbar bs-dark-bg-subtle rounded">
    <div class="container-fluid">
        <ul class="nav">
          <li class="nav-item me-2">
            <button type="button" class="btn btn-md btn-dark" @click="openAddBikeComponentModal"
              data-toggle="tooltip" data-placement="bottom" :title="$t('toolbar.addcomponent')"
              :aria-label="$t('toolbar.addcomponent')">
              {{ $t('toolbar.addcomponent') }}
            </button>
          </li>
          <li class="nav-item">
            <button type="button" class="btn btn-md btn-dark" data-toggle="tooltip" data-placement="bottom"
              :title="$t('toolbar.resetproducts')" :aria-label="$t('toolbar.resetproducts')" @click="resetProducts"
              :disabled="isResettingProducts || !bikeTypeStore.currentBikeType?.id">
              <span v-if="isResettingProducts" class="spinner-border spinner-border-sm me-2" role="status"
                aria-hidden="true"></span>
              {{ $t('toolbar.resetproducts') }}
            </button>
          </li>
        </ul>
    </div>
    <div v-if="resetProductsError" class="alert alert-danger mt-2 mb-0" role="alert">
      {{ resetProductsError }}
    </div>
  </nav>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { useBikeComponentStore } from '@/stores/bikecomponent'
import { useBikeProductStore } from '@/stores/bikeproduct'
import { useBikeTypeStore } from '@/stores/biketype'
import { ref } from 'vue'

const bikeTypeStore = useBikeTypeStore()
const bikeComponentStore = useBikeComponentStore()
const bikeProductStore = useBikeProductStore()
const { t } = useI18n()
const isResettingProducts = ref(false)
const resetProductsError = ref('')

// Function to open the Add Bike Component modal
function openAddBikeComponentModal() {
  bikeComponentStore.clearEditComponent()
  window.dispatchEvent(new CustomEvent('open-add-bike-component-modal'))
}

async function resetProducts() {
  const bikeTypeId = bikeTypeStore.currentBikeType?.id
  if (!bikeTypeId || isResettingProducts.value) return

  if (!window.confirm(t('toolbar.resetproducts-confirm'))) return

  isResettingProducts.value = true
  resetProductsError.value = ''
  try {
    await bikeProductStore.resetProductsForBikeType(bikeTypeId)
  } catch (error) {
    console.error('Failed to reset assigned products:', error)
    resetProductsError.value = t('toolbar.resetproducts-error')
  } finally {
    isResettingProducts.value = false
  }
}
</script>
