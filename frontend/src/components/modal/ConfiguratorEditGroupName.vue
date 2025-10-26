<template>
  <!-- Modal für Gruppen-Name bearbeiten -->
  <div class="modal fade" id="EditGroupName" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-addbikecomponent-title fs-5" id="exampleModalLabel">{{ $t("message.modal-editgroup-title") }}
          </h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal"
            :aria-label="$t('message.modal-close')"></button>
        </div>
        <div class="modal-body">
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon2">{{ $t("message.modal-editgroup-name-label") }}</span>
            <input type="text" class="form-control" v-model="groupName"
              :placeholder="$t('message.modal-editgroup-name-placeholder')"
              :aria-label="$t('message.modal-addbikecomponent-product-name-placeholder')"
              aria-describedby="basic-addon2" @keyup.enter="saveGroup">
          </div>
          <div v-if="errorMessage" class="alert alert-danger" role="alert">
            {{ errorMessage }}
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t("message.modal-close")
            }}</button>
          <button type="button" class="btn btn-primary" @click="saveGroup" :disabled="isLoading || !groupName.trim()">
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
  import { useAssemblyGroupStore } from '@/stores/assemblygroups'
  import { Modal } from 'bootstrap'

  // Emits für Events
  const emit = defineEmits(['groupUpdated', 'close']) // Emit event when group is updated

  // Reactive data
  const groupName = ref('') // Name of the group being edited
  const isLoading = ref(false) // Loading state for save operation
  const errorMessage = ref('') // Error message display

  // Store
  const assemblyGroupStore = useAssemblyGroupStore() // Store instance

  // Computed properties for current edit group
  const currentGroup = computed(() => assemblyGroupStore.currentEditGroup) // Currently edited group
  const groupId = computed(() => currentGroup.value?.id) // ID of the group being edited

  // Function to properly close modal and clean up backdrop
  const closeModal = async () => {
    const modalElement = document.getElementById('EditGroupName') // Get modal element
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

  // Watch for current edit group changes to initialize the form
  watch(currentGroup, (newGroup) => {
    if (newGroup) {
      groupName.value = newGroup.name || '' // Set group name in form
      errorMessage.value = '' // Clear error message
    }
  }, { immediate: true })

  // Save function
  const saveGroup = async () => {
    console.log('SaveGroup called - currentGroup:', currentGroup.value)
    console.log('SaveGroup called - groupId:', groupId.value)
    console.log('SaveGroup called - groupName:', groupName.value)

    if (!groupName.value.trim()) { // Validate group name
      errorMessage.value = 'Gruppenname darf nicht leer sein'
      return
    }

    if (!groupId.value) {
      errorMessage.value = 'Keine gültige Gruppen-ID'
      return
    }

    isLoading.value = true
    errorMessage.value = ''

    try {
      console.log('Updating group with ID:', groupId.value, 'New name:', groupName.value.trim())
      const updatedGroup = await assemblyGroupStore.updateAssemblyGroup(groupId.value, groupName.value.trim())
      console.log('Group updated successfully:', updatedGroup)

      // Reload all assembly groups to ensure reactivity
      console.log('Reloading all assembly groups...')
      await assemblyGroupStore.getAssemblyGroups()
      console.log('Assembly groups reloaded')

      // Emit success event
      emit('groupUpdated', updatedGroup)

      // Close modal properly
      await closeModal()

      // Clear edit group and reset form
      assemblyGroupStore.clearEditGroup()
      groupName.value = ''

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
    groupName.value = currentGroup.value?.name || '' // Reset to current group name
    errorMessage.value = '' // Clear error message
    isLoading.value = false // Reset loading state
  }

  // Listen for modal close events
  watch(() => currentGroup.value, (newGroup) => {
    if (!newGroup) {
      groupName.value = '' // Clear group name
      errorMessage.value = '' // Clear error message
      isLoading.value = false // Reset loading state
    }
  })

  // Global cleanup function for modal backdrops (as emergency fallback)
  const cleanupModalBackdrops = () => {
    // Remove any orphaned modal backdrops
    const backdrops = document.querySelectorAll('.modal-backdrop') // Select all backdrops
    backdrops.forEach(backdrop => backdrop.remove()) // Remove each backdrop

    // Clean up body styles
    if (!document.querySelector('.modal.show')) { // If no modals are shown
      document.body.classList.remove('modal-open') // Remove modal-open class
      document.body.style.overflow = ''
      document.body.style.paddingRight = ''
    }
  }

  // Run cleanup every few seconds as fallback
  setInterval(cleanupModalBackdrops, 3000)

  // Expose reset function for parent component
  defineExpose({
    resetForm
  })
</script>
