<template>
  <div class="modal fade" id="EditBikeProduct" tabindex="-1" aria-labelledby="editBikeProductModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="fs-5" id="editBikeProductModalLabel">{{ $t("modal.editbikeproduct.title") }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" :aria-label="$t('message.modal-close')"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label">{{ $t("modal.addbikepart.part-label") }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control-plaintext" :value="bikePartStore.currentEditPart?.name || 'No part selected'" readonly>
            </div>
          </div>

          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label">{{ $t("modal.addbikepart.product-name-label") }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" v-model="productName" :placeholder="$t('modal.addbikepart.product-name-placeholder')">
            </div>
          </div>

          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label">{{ $t("modal.addbikepart.product-price-label") }}:</label>
            <div class="col-sm-2">
              <input type="text" class="form-control" v-model="priceEuros">
            </div>
            <span class="col-auto col-form-label">,</span>
            <div class="col-sm-2">
              <input type="text" class="form-control col-sm-1" v-model="priceCents" placeholder="00">
            </div>
            <span class="col-auto col-form-label">{{ $t("modal.addbikepart.product-price-currency") }}</span>
          </div>

          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label">{{ $t("modal.addbikepart.product-source-label") }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" v-model="productSource" :placeholder="$t('modal.addbikepart.product-source-placeholder')">
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t("modal.close") }}</button>
          <button type="button" class="btn btn-primary" @click="saveBikeProductChanges">{{ $t("modal.save") }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, watch } from 'vue'
  import { useBikePartStore } from '@/stores/bikepart'
  import { useBikeProductStore } from '@/stores/bikeproduct'

  const bikePartStore = useBikePartStore()
  const bikeProductStore = useBikeProductStore()

  const productName = ref('')
  const priceEuros = ref('')
  const priceCents = ref('00')
  const productSource = ref('')

  const resetForm = () => {
    productName.value = ''
    priceEuros.value = ''
    priceCents.value = '00'
    productSource.value = ''
  }

  const fillFormFromSelection = () => {
    const selected = bikeProductStore.currentEditProduct
    if (!selected) {
      resetForm()
      return
    }

    productName.value = selected.name || ''
    productSource.value = selected.source || ''
    const numeric = Number(selected.price ?? 0)
    const safePrice = Number.isFinite(numeric) ? numeric : 0
    const [euros, cents] = safePrice.toFixed(2).split('.')
    priceEuros.value = euros
    priceCents.value = cents
  }

  watch(
    () => bikeProductStore.currentEditProduct,
    () => {
      fillFormFromSelection()
    },
    { immediate: true }
  )

  const saveBikeProductChanges = async () => {
    try {
      const partId = bikePartStore.currentEditPart?.id
      const productId = bikeProductStore.currentEditProduct?.id

      if (!partId || !productId) {
        alert('Bitte wähle zuerst ein Bike Product aus')
        return
      }

      const euros = parseFloat(priceEuros.value) || 0
      const cents = parseFloat(priceCents.value) || 0
      const totalPrice = euros + (cents / 100)

      const productData = {
        name: productName.value || 'No bike product name',
        source: productSource.value || 'Unknown',
        price: totalPrice
      }

      await bikeProductStore.updateBikeProduct(partId, productId, productData)
      await bikeProductStore.getBikeProductsByPart(partId)

      const modalElement = document.getElementById('EditBikeProduct')
      const closeButton = modalElement?.querySelector('[data-bs-dismiss="modal"]')
      if (closeButton) {
        closeButton.click()
      }
    } catch (error) {
      console.error('Error updating bike product:', error)
      alert('Fehler beim Speichern des Bike Products')
    }
  }
</script>
