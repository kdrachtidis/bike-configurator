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
              <input type="text" class="form-control" :value="bikeComponentStore.currentEditComponent?.name || 'No component selected'"
                :aria-label="$t('modal.addbikepart.component-label')" aria-describedby="basic-addon1" disabled>
            </div>

          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon2">{{ $t("modal.addbikepart.product-name-label")
            }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" :placeholder="$t('modal.addbikepart.product-name-placeholder')"
                :aria-label="$t('modal.addbikepart.product-name-placeholder')" aria-describedby="basic-addon2">
            </div>
          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon3">{{ $t("modal.addbikepart.product-price-label")
            }}:</label>
            <div class="col-sm-2">
              <input type="text" class="form-control" :aria-label="$t('modal.addbikepart.product-price-label')"
                aria-describedby="basic-addon3">
            </div>
            <span class="col-auto col-form-label">,</span>
            <div class="col-sm-2">
              <input type="text" class="form-control col-sm-1" placeholder="00"
                :aria-label="$t('modal.addbikepart.product-price-label')" aria-describedby="basic-addon3">
            </div>
            <span class="col-auto col-form-label">{{ $t("modal.addbikepart.product-price-currency")
            }}</span>
          </div>
          <div class="mb-3 row">
            <label class="col-sm-2 col-form-label" id="basic-addon4">{{ $t("modal.addbikepart.product-source-label")
            }}:</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" :placeholder="$t('modal.addbikepart.product-source-placeholder')"
                aria-label="$t('modal.addbikepart.product-source-placeholder')" aria-describedby="basic-addon4">
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t("modal.close")
          }}</button>
          <button type="button" class="btn btn-primary">{{ $t("modal.save") }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useBikeComponentStore } from '@/stores/bikecomponent'

  // Store instance
  const bikeComponentStore = useBikeComponentStore()
</script>
