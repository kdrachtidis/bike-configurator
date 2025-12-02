<template>
  <dialog ref="dialogRef" id="AddBikeComponent" @close="handleClose" @click="handleBackdropClick">
    <div class="modal-dialog">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h1 class="modal-title fs-5">{{ $t("message.modal-addcomponent-title") }}</h1>
          <button type="button" class="btn-close" @click="closeModal" :aria-label="$t('message.modal-close')"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3 row">
              <label for="groupName" class="col-4 col-form-label">{{ $t("message.modal-addcomponent-name-label")
              }}:</label>
              <div class="col-8">
                <input type="text" class="form-control" id="groupName" v-model="groupName"
                  :placeholder="$t('message.modal-addcomponent-name-placeholder')"
                  :aria-label="$t('message.modal-addcomponent-name-placeholder')" aria-describedby="basic-addon2"
                  :disabled="isLoading" @keyup.enter="handleSave" ref="inputRef">
              </div>
            </div>
          </form>
          <div v-if="errorMessage" class="alert alert-danger" role="alert">
            {{ errorMessage }}
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="closeModal">{{ $t("message.modal-close")
          }}</button>
          <button type="button" class="btn btn-primary" @click="handleSave" :disabled="isLoading || !groupName.trim()">
            <span v-if="isLoading" class="spinner-border spinner-border-sm me-2" role="status"
              aria-hidden="true"></span>
            {{ $t("message.modal-save") }}
          </button>
        </div>
      </div>
    </div>
  </dialog>
</template>

<script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { useBikeTypeStore } from '@/stores/biketype'

  // Refs
  const dialogRef = ref(null)
  const inputRef = ref(null)

  // Store instances
  const bikeComponentStore = useBikeComponentStore()
  const bikeTypeStore = useBikeTypeStore()

  // Reactive data
  const groupName = ref('') // Name of the component being created
  const isLoading = ref(false)
  const errorMessage = ref('')

  // Function to open the modal
  const openModal = () => {
    if (dialogRef.value) {
      dialogRef.value.showModal()
      // Focus the input field after a short delay
      setTimeout(() => {
        if (inputRef.value) {
          inputRef.value.focus()
        }
      }, 100)
    }
  }

  // Function to close the modal
  const closeModal = () => {
    if (dialogRef.value) {
      dialogRef.value.close()
    }
  }

  // Handle close event
  const handleClose = () => {
    resetForm()
  }

  // Handle backdrop click (click outside dialog)
  const handleBackdropClick = (event) => {
    if (event.target === dialogRef.value) {
      closeModal()
    }
  }

  // Reset form when modal is hidden
  const resetForm = () => {
    groupName.value = ''
    errorMessage.value = ''
    isLoading.value = false
  }

  // Handle save
  const handleSave = async () => {
    if (!groupName.value.trim()) {
      errorMessage.value = 'Bitte geben Sie einen Namen ein'
      return
    }

    // Check if a bike type is selected
    if (!bikeTypeStore.currentBikeType) {
      errorMessage.value = 'Bitte wählen Sie zuerst einen Fahrradtyp aus'
      return
    }

    isLoading.value = true
    errorMessage.value = ''

    try {
      // Create the bike component
      await bikeComponentStore.createBikeComponent(
        bikeTypeStore.currentBikeType.id,
        groupName.value.trim()
      )

      // Close modal
      closeModal()
    } catch (error) {
      console.error('Error creating bike component:', error)
      if (error.response?.status === 401) {
        errorMessage.value = 'Nicht autorisiert. Bitte melden Sie sich an.'
      } else if (error.response?.status === 404) {
        errorMessage.value = 'Fahrradtyp nicht gefunden'
      } else {
        errorMessage.value = 'Fehler beim Erstellen der Komponente. Bitte versuchen Sie es erneut.'
      }
    } finally {
      isLoading.value = false
    }
  }

  // Listen for custom event to open modal
  onMounted(() => {
    window.addEventListener('open-add-bike-component-modal', openModal)
  })

  onUnmounted(() => {
    window.removeEventListener('open-add-bike-component-modal', openModal)
  })

  // Expose openModal for parent components
  defineExpose({
    openModal,
    closeModal
  })
</script>

<style scoped>
  ::backdrop {
    background-color: #000;
    opacity: 0.75;
  }

  dialog {
    border: none;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
</style>
