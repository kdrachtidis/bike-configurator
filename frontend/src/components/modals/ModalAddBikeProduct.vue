<template>
  <div ref="modalElement" class="modal fade" id="AddBikeProduct" tabindex="-1"
    aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">{{ $t("modal.addbikeproduct.modal-title") }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal"
            :aria-label="$t('modal.button.tooltip-close')" data-toggle="tooltip" data-placement="bottom"
            :title="$t('modal.button.tooltip-close')"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon1">{{ accessoryStore.currentEditType ? $t('accessories.category') : $t("modal.addbikeproduct.label-component")
              }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control-plaintext"
                :value="accessoryStore.currentEditType?.categoryName || bikeComponentStore.currentEditComponent?.name || 'No component selected'"
                :aria-label="$t('modal.addbikeproduct.label-component')" aria-describedby="basic-addon1" readonly>
            </div>

          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon1">{{ accessoryStore.currentEditType ? $t('accessories.type') : $t("modal.addbikeproduct.label-part")
              }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control-plaintext"
                :value="accessoryStore.currentEditType?.name || bikePartStore.currentEditPart?.name || 'No part selected'"
                :aria-label="$t('modal.addbikeproduct.label-part')" aria-describedby="basic-addon1" readonly>
            </div>

          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon2">{{ $t("modal.addbikeproduct.label-product")
              }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" v-model="productName"
                :placeholder="$t('modal.addbikeproduct.placeholder-name')"
                :aria-label="$t('modal.addbikeproduct.placeholder-name')" aria-describedby="basic-addon2">
            </div>
          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon3">{{ $t("modal.addbikeproduct.label-price")
              }}:</label>
            <div class="col-sm-2">
              <input type="text" class="form-control" v-model="priceEuros"
                :aria-label="$t('modal.addbikeproduct.label-price')" aria-describedby="basic-addon3">
            </div>
            <span class="col-auto col-form-label">,</span>
            <div class="col-sm-2">
              <input type="text" class="form-control col-sm-1" v-model="priceCents" placeholder="00"
                :aria-label="$t('modal.addbikeproduct.label-price')" aria-describedby="basic-addon3">
            </div>
            <span class="col-auto col-form-label">{{ $t("modal.addbikeproduct.label-currency")
              }}</span>
          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon4">{{ $t("modal.addbikeproduct.label-source")
              }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" v-model="productSource"
                :placeholder="$t('modal.addbikeproduct.placeholder-source')"
                aria-label="$t('modal.addbikeproduct.placeholder-source')" aria-describedby="basic-addon4">
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
            :aria-label="$t('modal.button.tooltip-close')" data-toggle="tooltip" data-placement="bottom"
            :title="$t('modal.button.tooltip-close')">{{ $t("modal.button.close") }}</button>
          <button type="button" class="btn btn-primary" @click="saveBikeProduct"
            :aria-label="$t('modal.button.tooltip-save')" data-toggle="tooltip" data-placement="bottom"
            :title="$t('modal.button.tooltip-save')">{{ $t("modal.button.save") }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { onBeforeUnmount, onMounted, ref } from 'vue'
  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { useBikePartStore } from '@/stores/bikepart'
  import { useBikeProductStore } from '@/stores/bikeproduct'
  import { useAccessoryStore } from '@/stores/accessory'

  // Store instances
  const bikeComponentStore = useBikeComponentStore()
  const bikePartStore = useBikePartStore()
  const bikeProductStore = useBikeProductStore()
  const accessoryStore = useAccessoryStore()

  const modalElement = ref(null)

  // Form data
  const productName = ref('')
  const priceEuros = ref('')
  const priceCents = ref('00')
  const productSource = ref('')

  // Save bike product
  async function saveBikeProduct() {
    try {
      const accessoryType = accessoryStore.currentEditType
      const part = bikePartStore.currentEditPart
      if (!accessoryType?.id && !part?.id) {
        alert('Please select a component part or accessory type first.')
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

      if (accessoryType?.id) {
        await accessoryStore.createProduct(accessoryType.id, productData)
      } else {
        await bikeProductStore.createBikeProduct(part.id, productData)
        await bikeProductStore.getBikeProductsByPart(part.id)
      }

      // Reset form
      resetForm()

      // Close modal by simulating click on close button (works correctly)
      const modalElement = document.getElementById('AddBikeProduct')
      const closeButton = modalElement.querySelector('[data-bs-dismiss="modal"]')
      if (closeButton) {
        closeButton.click()
      }

      alert('Product assigned successfully!')
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

  function handleHidden() {
    resetForm()
    accessoryStore.clearEditType()
  }

  onMounted(() => {
    modalElement.value?.addEventListener('show.bs.modal', resetForm)
    modalElement.value?.addEventListener('hidden.bs.modal', handleHidden)
  })

  onBeforeUnmount(() => {
    modalElement.value?.removeEventListener('show.bs.modal', resetForm)
    modalElement.value?.removeEventListener('hidden.bs.modal', handleHidden)
  })
</script>
