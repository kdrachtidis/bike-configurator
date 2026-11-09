<template>
  <nav class="navbar navbar-expand-lg bs-dark-bg-subtle rounded">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">{{ $t('appheader.title') }}</a>
      <SelectBikeType />
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav flex-row flex-wrap">
          <li class="nav-item">
            <button type="button" class="btn btn-md btn-outline-secondary" @click="openAddBikeComponentModal"
              data-toggle="tooltip" data-placement="bottom" :title="$t('toolbar.addcomponent')"
              :aria-label="$t('toolbar.addcomponent')">
              {{ $t('toolbar.addcomponent') }}
            </button>
          </li>
          <li class="nav-item">
            <button type="button" class="btn btn-md btn-outline-secondary" data-toggle="tooltip" data-placement="bottom"
              :title="$t('toolbar.resetproducts')" :aria-label="$t('toolbar.resetproducts')" @click="resetProducts"
              :disabled="isResettingProducts || !bikeTypeStore.currentBikeType?.id">
              <span v-if="isResettingProducts" class="spinner-border spinner-border-sm me-2" role="status"
                aria-hidden="true"></span>
              {{ $t('toolbar.resetproducts') }}
            </button>
          </li>
        </ul>
      </div>    
      
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
import SelectBikeType from './SelectBikeType.vue'
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
