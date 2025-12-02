<template>
  <!-- Für Entwicklung: Modal immer sichtbar mit persistentem Backdrop -->
  <div v-if="isDevelopment" class="dev-modal-backdrop"></div>
  <div :class="['modal', isDevelopment ? 'show dev-modal' : 'fade']" id="AddBikeProduct" tabindex="-1"
    aria-labelledby="exampleModalLabel" :aria-hidden="!isDevelopment"
    :style="isDevelopment ? 'display: block; position: fixed; z-index: 1055;' : ''">
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
              <input type="text" class="form-control" :placeholder="$t('modal.addbikepart.component-label')"
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
  import { ref } from 'vue'

  // Development flag - set to false for production
  const isDevelopment = ref(true) // Set to true to always show modal in development
</script>

<style scoped>
  .dev-modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1050;
    pointer-events: none;
  }

  .dev-modal {
    pointer-events: auto;
  }

  .dev-modal .modal-dialog {
    margin: 1.75rem auto;
  }
</style>
