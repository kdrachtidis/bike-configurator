<template>
  <!-- Für Entwicklung: Modal immer sichtbar -->
  <div class="modal fade" id="EditGroupName" tabindex="-1" aria-labelledby="exampleModalLabel"
    aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-addbikecomponent-title fs-5" id="exampleModalLabel">{{ $t("message.modal-editgroup-title") }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" :aria-label="$t('message.modal-close')"></button>
        </div>
        <div class="modal-body">
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon2">{{ $t("message.modal-editgroup-name-label") }}</span>
            <input type="text" class="form-control" :placeholder="$t('message.modal-editgroup-name-placeholder')" :aria-label="$t('message.modal-addbikecomponent-product-name-placeholder')"
              aria-describedby="basic-addon2">
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
