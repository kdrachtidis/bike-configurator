<template>
  <div class="modal fade" id="EditBikeProduct" tabindex="-1" aria-labelledby="editBikeProductModalLabel"
    aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="editBikeProductModalLabel">{{ $t("modal.editbikeproduct.modal-title") }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal"
            :aria-label="$t('modal.button.tooltip-close')" data-toggle="tooltip" data-placement="bottom"
            :title="$t('modal.button.tooltip-close')"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon1">{{ $t("modal.editbikeproduct.label-component")
              }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control-plaintext"
                :value="bikeComponentStore.currentEditComponent?.name || 'No component selected'"
                :aria-label="$t('modal.editbikeproduct.label-component')" aria-describedby="basic-addon1" readonly>
            </div>
          </div>

          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon2">{{ $t("modal.editbikeproduct.label-part")
              }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control-plaintext"
                :value="bikePartStore.currentEditPart?.name || 'No part selected'"
                :aria-label="$t('modal.editbikeproduct.label-part')" aria-describedby="basic-addon2" readonly>
            </div>
          </div>

          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon3">{{ $t("modal.editbikeproduct.label-product")
              }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" v-model="productName"
                :placeholder="$t('modal.editbikeproduct.placeholder-name')"
                :aria-label="$t('modal.editbikeproduct.placeholder-name')" aria-describedby="basic-addon3">
            </div>
          </div>

          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon4">{{ $t("modal.editbikeproduct.label-price")
              }}:</label>
            <div class="col-sm-2">
              <input type="text" class="form-control" v-model="priceEuros"
                :aria-label="$t('modal.editbikeproduct.label-price')" aria-describedby="basic-addon4">
            </div>
            <span class="col-auto col-form-label">,</span>
            <div class="col-sm-2">
              <input type="text" class="form-control col-sm-1" v-model="priceCents" placeholder="00"
                :aria-label="$t('modal.editbikeproduct.label-price')" aria-describedby="basic-addon4">
            </div>
            <span class="col-auto col-form-label">{{ $t("modal.editbikeproduct.label-currency") }}</span>
          </div>

          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon5">{{ $t("modal.editbikeproduct.label-source")
              }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" v-model="productSource"
                :placeholder="$t('modal.editbikeproduct.placeholder-source')"
                :aria-label="$t('modal.editbikeproduct.placeholder-source')" aria-describedby="basic-addon5">
            </div>
          </div>
        </div>
        <div class="modal-footer justify-content-between">
          <button type="button" class="btn btn-danger" @click="deleteBikeProduct"
            :aria-label="$t('modal.button.tooltip-delete')" data-toggle="tooltip" data-placement="bottom"
            :title="$t('modal.button.tooltip-delete')">{{ $t("modal.button.delete") }}</button>
          <div class="justify-content-end d-flex">
            <button type="button" class="btn btn-secondary me-2" data-bs-dismiss="modal"
              :aria-label="$t('modal.button.tooltip-close')" data-toggle="tooltip" data-placement="bottom"
              :title="$t('modal.button.tooltip-close')">{{ $t("modal.button.close") }}</button>
            <button type="button" class="btn btn-primary" @click="saveBikeProductChanges"
              :aria-label="$t('modal.button.tooltip-save')" data-toggle="tooltip" data-placement="bottom"
              :title="$t('modal.button.tooltip-save')">{{ $t("modal.button.save") }}</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, watch } from 'vue'
  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { useBikePartStore } from '@/stores/bikepart'
  import { useBikeProductStore } from '@/stores/bikeproduct'

  const bikeComponentStore = useBikeComponentStore()
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

  const deleteBikeProduct = async () => {
    try {
      const partId = bikePartStore.currentEditPart?.id
      const productId = bikeProductStore.currentEditProduct?.id

      if (!partId || !productId) {
        alert('Bitte wähle zuerst ein Bike Product aus')
        return
      }

      const confirmed = window.confirm('Soll dieses Produkt wirklich gelöscht werden?')
      if (!confirmed) {
        return
      }

      await bikeProductStore.deleteBikeProduct(partId, productId)
      await bikeProductStore.getBikeProductsByPart(partId)

      const modalElement = document.getElementById('EditBikeProduct')
      const closeButton = modalElement?.querySelector('[data-bs-dismiss="modal"]')
      if (closeButton) {
        closeButton.click()
      }
    } catch (error) {
      console.error('Error deleting bike product:', error)
      alert('Fehler beim Löschen des Bike Products')
    }
  }
</script>
