<template>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel"
    aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">{{ $t("message.modal-title") }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" :aria-label="$t('message.modal-close')"></button>
        </div>
        <div class="modal-body">
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">{{ $t("message.modal-component") }}</span>
            <input type="text" class="form-control" :placeholder="$t('message.modal-component')" :aria-label="$t('message.modal-component')"
              aria-describedby="basic-addon1" disabled>
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon2">{{ $t("message.modal-product-name-label") }}</span>
            <input type="text" class="form-control" :placeholder="$t('message.modal-product-name-placeholder')" :aria-label="$t('message.modal-product-name-placeholder')"
              aria-describedby="basic-addon2">
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon3">{{ $t("message.modal-product-price") }}</span>
            <input type="text" class="form-control" :aria-label="$t('message.modal-product-price')">
            <span class="input-group-text">,</span>
            <input type="text" class="form-control" placeholder="00" :aria-label="$t('message.modal-product-price')">
            <span class="input-group-text">€</span>
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon4">{{ $t("message.modal-product-source-label") }}</span>
            <input type="text" class="form-control" :placeholder="$t('message.modal-product-source-placeholder')" aria-label="$t('message.modal-product-source-placeholder')"
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

</script>
