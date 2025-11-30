<template> <!-- Edit Bike Component Modal -->
  <div class="modal fade" id="EditBikeComponent" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="fs-5" id="exampleModalLabel">{{ $t("message.modal-editcomponent-title") }}
          </h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal"
            :aria-label="$t('message.modal-close')"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3 row">
            <label class="form-label col-5 col-form-label" for="componentName">{{ $t("message.modal-editcomponent-name-label") }} :</label>
            <div class="col-7">
              <input type="text" class="form-control" v-model="componentName"
                :placeholder="$t('message.modal-editcomponent-name-placeholder')"
                :aria-label="$t('message.modal-addbikecomponent-product-name-placeholder')"
                aria-describedby="basic-addon2" @keyup.enter="saveGroup" />
            </div>
          </div>
          <div v-if="errorMessage" class="alert alert-danger" role="alert">
            {{ errorMessage }}
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t("message.modal-close")
            }}</button>
          <button type="button" class="btn btn-primary" @click="saveGroup"
            :disabled="isLoading || !componentName.trim()">
            <span v-if="isLoading" class="spinner-border spinner-border-sm me-2" role="status"
              aria-hidden="true"></span>
            {{ $t("message.modal-save") }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, watch, computed } from 'vue'
  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { useBikeTypeStore } from '@/stores/biketype'
  import { Modal } from 'bootstrap'

  // Emits für Events
  const emit = defineEmits(['componentUpdated', 'close']) // Emit event when group is updated

  // Reactive data
  const componentName = ref('') // Name of the component being edited
  const isLoading = ref(false) // Loading state for save operation
  const errorMessage = ref('') // Error message display

  // Store
  const bikeComponentStore = useBikeComponentStore() // Store instance
  const bikeTypeStore = useBikeTypeStore() // Bike type store instance

  // Computed properties for current edit component
  const currentComponent = computed(() => bikeComponentStore.currentEditComponent) // Currently edited component
  const componentId = computed(() => currentComponent.value?.id) // ID of the component being edited

  // Function to properly close modal and clean up backdrop
  const closeModal = async () => {
    const modalElement = document.getElementById('EditComponentName') // Get modal element
    if (modalElement) {
      // Try to get existing instance first
      let modal = Modal.getInstance(modalElement)

      if (!modal) {
        // If no instance exists, create one
        modal = new Modal(modalElement)
      }

      // Hide the modal
      modal.hide()

      // Wait a bit for animation
      await new Promise(resolve => setTimeout(resolve, 150))

      // Force remove backdrop if it still exists
      const backdrop = document.querySelector('.modal-backdrop')
      if (backdrop) {
        backdrop.remove()
      }

      // Ensure body classes are cleaned up
      document.body.classList.remove('modal-open')
      document.body.style.overflow = ''
      document.body.style.paddingRight = ''
    }
  }

  // Watch for current edit component changes to initialize the form
  watch(currentComponent, (newComponent) => {
    console.log('🔍 Watch triggered - newComponent:', newComponent)
    if (newComponent) {
      console.log('✅ Setting componentName to:', newComponent.name)
      componentName.value = newComponent.name || '' // Set group name in form
      errorMessage.value = '' // Clear error message
    } else {
      console.log('❌ newComponent is null/undefined')
    }
  }, { immediate: true })

  // Save function
  const saveGroup = async () => {
    console.log('SaveComponent called - currentGroup:', currentComponent.value)
    console.log('SaveComponent called - groupId:', componentId.value)
    console.log('SaveComponent called - groupName:', componentName.value)

    if (!componentName.value.trim()) { // Validate component name
      errorMessage.value = 'Component name cannot be empty.'
      return
    }

    if (!componentId.value) {
      errorMessage.value = 'Invalid component ID'
      return
    }

    isLoading.value = true
    errorMessage.value = ''

    try {
      // Check if we have a bike type selected
      if (!bikeTypeStore.currentBikeType?.id) {
        errorMessage.value = 'No bike type selected. Please select a bike type.'
        return
      }

      console.log('Updating component with ID:', componentId.value, 'for bike type:', bikeTypeStore.currentBikeType.id, 'New name:', componentName.value.trim())
      const updatedComponent = await bikeComponentStore.updateBikeComponentByBikeType(bikeTypeStore.currentBikeType.id, componentId.value, componentName.value.trim())
      console.log('Component updated successfully:', updatedComponent)

      // Reload bike components for current bike type to ensure reactivity
      console.log('Reloading bike components for current bike type...')
      await bikeComponentStore.getBikeComponentsByBikeType(bikeTypeStore.currentBikeType.id)
      console.log('Bike components reloaded')

      // Emit success event
      emit('componentUpdated', updatedComponent)

      // Close modal properly
      await closeModal()

      // Clear edit component and reset form
      bikeComponentStore.clearEditComponent()
      componentName.value = ''

    } catch (error) {
      console.error('Fehler beim Speichern der Gruppe:', error)
      if (error.response?.status === 401) {
        errorMessage.value = 'Sie müssen sich anmelden, um Änderungen zu speichern.'
        // Close this modal properly
        await closeModal()

        // Open login modal after a short delay
        setTimeout(() => {
          const loginModalElement = document.getElementById('LoginModal')
          if (loginModalElement) {
            const loginModal = new Modal(loginModalElement)
            loginModal.show()
          }
        }, 300)
      } else {
        errorMessage.value = 'Fehler beim Speichern der Gruppe. Bitte versuchen Sie es erneut.'
      }
    } finally {
      isLoading.value = false
    }
  }

  // Reset form when modal is closed
  const resetForm = () => {
    componentName.value = currentComponent.value?.name || '' // Reset to current group name
    errorMessage.value = '' // Clear error message
    isLoading.value = false // Reset loading state
  }

  // Listen for modal close events
  watch(() => currentComponent.value, (newGroup) => {
    if (!newGroup) {
      componentName.value = '' // Clear group name
      errorMessage.value = '' // Clear error message
      isLoading.value = false // Reset loading state
    }
  })

  // Expose reset function for parent component
  defineExpose({
    resetForm
  })
</script>

<style scoped></style>
