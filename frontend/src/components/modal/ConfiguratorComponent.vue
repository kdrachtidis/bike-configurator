<template>
  <!-- Für Entwicklung: Modal immer sichtbar mit persistentem Backdrop -->
  <div v-if="isDevelopment" class="dev-modal-backdrop"></div>
  <div :class="['modal', isDevelopment ? 'show dev-modal' : 'fade']" id="AddBikeComponent" tabindex="-1"
       aria-labelledby="exampleModalLabel" :aria-hidden="!isDevelopment"
       :style="isDevelopment ? 'display: block; position: fixed; z-index: 1055;' : ''">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-addbikecomponent-title fs-5" id="exampleModalLabel">{{ $t("message.modal-addbikecomponent-title") }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" :aria-label="$t('message.modal-close')"></button>
        </div>
        <div class="modal-body">
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">{{ $t("message.modal-addbikecomponent-component") }}</span>
            <input type="text" class="form-control" :placeholder="$t('message.modal-addbikecomponent-component')" :aria-label="$t('message.modal-addbikecomponent-component')"
              aria-describedby="basic-addon1" disabled>
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon2">{{ $t("message.modal-addbikecomponent-product-name-label") }}</span>
            <input type="text" class="form-control" :placeholder="$t('message.modal-addbikecomponent-product-name-placeholder')" :aria-label="$t('message.modal-addbikecomponent-product-name-placeholder')"
              aria-describedby="basic-addon2">
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon3">{{ $t("message.modal-addbikecomponent-product-price") }}</span>
            <input type="text" class="form-control" :aria-label="$t('message.modal-addbikecomponent-product-price')">
            <span class="input-group-text">,</span>
            <input type="text" class="form-control" placeholder="00" :aria-label="$t('message.modal-addbikecomponent-product-price')">
            <span class="input-group-text">€</span>
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon4">{{ $t("message.modal-addbikecomponent-product-source-label") }}</span>
            <input type="text" class="form-control" :placeholder="$t('message.modal-addbikecomponent-product-source-placeholder')" aria-label="$t('message.modal-addbikecomponent-product-source-placeholder')"
              aria-describedby="basic-addon4">
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t("message.modal-close") }}</button>
          <button type="button" class="btn btn-primary">{{ $t("message.modal-save") }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  // Development flag - set to false for production
  const isDevelopment = ref(false) // Set to true to always show modal in development
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
