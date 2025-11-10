<template>
  <!-- Für Entwicklung: Modal immer sichtbar mit persistentem Backdrop -->
  <div v-if="isDevelopment" class="dev-modal-backdrop"></div>
  <div :class="['modal', isDevelopment ? 'show dev-modal' : 'fade']" id="AddAssemblyGroup" tabindex="-1"
       aria-labelledby="exampleModalLabel" :aria-hidden="!isDevelopment"
       :style="isDevelopment ? 'display: block; position: fixed; z-index: 1055;' : ''">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-addbikecomponent-title fs-5" id="exampleModalLabel">{{ $t("message.modal-addgroup-title") }}
          </h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal"
            :aria-label="$t('message.modal-close')"></button>
        </div>
        <div class="modal-body">
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon2">{{ $t("message.modal-addgroup-name-label") }}</span>
            <input type="text" class="form-control" v-model="groupName"
              :placeholder="$t('message.modal-addgroup-name-placeholder')"
              :aria-label="$t('message.modal-addgroup-name-placeholder')"
              aria-describedby="basic-addon2">
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t("message.modal-close")
            }}</button>
          <button type="button" class="btn btn-primary">
            {{ $t("message.modal-save") }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  // Development flag - set to false for production
  const isDevelopment = ref(false) // Set to false to hide modal in production

  // Reactive data
  const groupName = ref('') // Name of the group being created
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
