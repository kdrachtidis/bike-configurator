<template>
  <div class="modal fade" id="AddBikeProduct" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="fs-5" id="exampleModalLabel">{{ $t("modal.addbikepart.title") }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal"
            :aria-label="$t('message.modal-close')"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon1">{{ $t("modal.addbikepart.component-label")
            }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control-plaintext"
                :value="bikeComponentStore.currentEditComponent?.name || 'No component selected'"
                :aria-label="$t('modal.addbikepart.component-label')" aria-describedby="basic-addon1" readonly>
            </div>

          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon1">{{ $t("modal.addbikepart.part-label")
            }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control-plaintext" :value="bikePartStore.currentEditPart?.name || 'No part selected'"
                :aria-label="$t('modal.addbikepart.part-label')" aria-describedby="basic-addon1" readonly>
            </div>

          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon2">{{ $t("modal.addbikepart.product-name-label")
            }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" v-model="productName" :placeholder="$t('modal.addbikepart.product-name-placeholder')"
                :aria-label="$t('modal.addbikepart.product-name-placeholder')" aria-describedby="basic-addon2">
            </div>
          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon3">{{ $t("modal.addbikepart.product-price-label")
            }}:</label>
            <div class="col-sm-2">
              <input type="text" class="form-control" v-model="priceEuros" :aria-label="$t('modal.addbikepart.product-price-label')"
                aria-describedby="basic-addon3">
            </div>
            <span class="col-auto col-form-label">,</span>
            <div class="col-sm-2">
              <input type="text" class="form-control col-sm-1" v-model="priceCents" placeholder="00"
                :aria-label="$t('modal.addbikepart.product-price-label')" aria-describedby="basic-addon3">
            </div>
            <span class="col-auto col-form-label">{{ $t("modal.addbikepart.product-price-currency")
            }}</span>
          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon4">{{ $t("modal.addbikepart.product-source-label")
            }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" v-model="productSource" :placeholder="$t('modal.addbikepart.product-source-placeholder')"
                aria-label="$t('modal.addbikepart.product-source-placeholder')" aria-describedby="basic-addon4">
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t("modal.close")
          }}</button>
          <button type="button" class="btn btn-primary" @click="saveBikeProduct">{{ $t("modal.save") }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { useBikePartStore } from '@/stores/bikepart'
  import { useBikeProductStore } from '@/stores/bikeproduct'

  // Store instances
  const bikeComponentStore = useBikeComponentStore()
  const bikePartStore = useBikePartStore()
  const bikeProductStore = useBikeProductStore()

  // Form data
  const productName = ref('')
  const priceEuros = ref('')
  const priceCents = ref('00')
  const productSource = ref('')

  // Save bike product
  async function saveBikeProduct() {
    try {
      // Validate that we have a part selected
      if (!bikePartStore.currentEditPart?.id) {
        alert('Bitte wähle zuerst ein Bike Part aus')
        return
      }

      // Calculate total price
      const euros = parseFloat(priceEuros.value) || 0
      const cents = parseFloat(priceCents.value) || 0
      const totalPrice = euros + (cents / 100)

      // Prepare product data
      const productData = {
        name: productName.value || 'No bike product name',
        source: productSource.value || 'Unknown',
        price: totalPrice
      }

      // Call API via store
      await bikeProductStore.createBikeProduct(bikePartStore.currentEditPart.id, productData)

      // Reset form
      resetForm()

      // Close modal by simulating click on close button (works correctly)
      const modalElement = document.getElementById('AddBikeProduct')
      const closeButton = modalElement.querySelector('[data-bs-dismiss="modal"]')
      if (closeButton) {
        closeButton.click()
      }

      alert('Bike Product erfolgreich erstellt!')
    } catch (error) {
      console.error('Error saving bike product:', error)
      alert('Fehler beim Speichern des Bike Products')
    }
  }

  // Reset form data
  function resetForm() {
    productName.value = ''
    priceEuros.value = ''
    priceCents.value = '00'
    productSource.value = ''
  }
</script>
