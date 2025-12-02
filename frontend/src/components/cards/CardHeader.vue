<template>
  <div class="card-header d-flex justify-content-between align-items-center bg-body-secondary">
    <!-- Show input when editing -->
    <div v-if="isEditing" class="flex-grow-1 me-2">
      <input type="text" class="form-control form-control-sm" v-model="editedName" @keyup.enter="saveName"
        @keyup.esc="cancelEdit" @blur="saveName" ref="editInput"
        :placeholder="$t('message.modal-editcomponent-name-placeholder')" />
    </div>
    <!-- Show title when not editing -->
    <h4 v-else class="card-title mb-0 fw-light">{{ bikecomponent.name || "Component Name Empty" }}</h4>

    <div class="d-flex gap-2">
      <!-- Edit/Save/Cancel buttons -->
      <button v-if="!isEditing" type="button" class="btn btn-sm btn-outline-secondary" @click="startEdit"
        :title="$t('card.header.edit')" :aria-label="$t('card.header.edit')">
        <i class="bi bi-pencil-fill"></i>
      </button>
      <button v-if="isEditing" type="button" class="btn btn-sm btn-outline-success" @click="saveName"
        :disabled="isLoading || !editedName.trim()" title="Save" aria-label="Save">
        <span v-if="isLoading" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
        <i v-else class="bi bi-check-lg"></i>
      </button>
      <button v-if="isEditing" type="button" class="btn btn-sm btn-outline-danger" @click="cancelEdit" title="Cancel"
        aria-label="Cancel">
        <i class="bi bi-x-lg"></i>
      </button>

      <!-- Collapse button -->
      <button type="button" class="btn btn-sm btn-outline-secondary" @click="toggleCollapseManually"
        data-toggle="tooltip" data-placement="bottom" :title="$t('card.header.expand')"
        :aria-label="$t('card.header.expand')">
        <i :class="isCollapsed ? 'bi bi-chevron-down' : 'bi bi-chevron-up'"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, nextTick } from 'vue'
  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { useBikeTypeStore } from '@/stores/biketype'
  import { Collapse } from 'bootstrap'

  const props = defineProps({
    bikecomponent: { type: Object, required: true }, // Bike component object
  })

  const bikeComponentStore = useBikeComponentStore() // Store instance
  const bikeTypeStore = useBikeTypeStore() // Bike type store instance
  const isCollapsed = ref(false) // Track collapse state
  const isEditing = ref(false) // Track edit mode
  const editedName = ref('') // Edited name
  const isLoading = ref(false) // Loading state
  const editInput = ref(null) // Reference to input element
  let collapseInstance = null // Bootstrap Collapse instance

  // Start editing
  const startEdit = async () => {
    isEditing.value = true
    editedName.value = props.bikecomponent.name
    await nextTick()
    editInput.value?.focus()
  }

  // Cancel editing
  const cancelEdit = () => {
    isEditing.value = false
    editedName.value = ''
  }

  // Save the edited name
  const saveName = async () => {
    if (!editedName.value.trim() || isLoading.value) {
      return
    }

    // If name hasn't changed, just cancel
    if (editedName.value.trim() === props.bikecomponent.name) {
      cancelEdit()
      return
    }

    isLoading.value = true

    try {
      if (!bikeTypeStore.currentBikeType?.id) {
        console.error('No bike type selected')
        return
      }

      await bikeComponentStore.updateBikeComponentByBikeType(
        bikeTypeStore.currentBikeType.id,
        props.bikecomponent.id,
        editedName.value.trim()
      )

      // Reload bike components
      await bikeComponentStore.getBikeComponentsByBikeType(bikeTypeStore.currentBikeType.id)

      // Exit edit mode
      isEditing.value = false
      editedName.value = ''
    } catch (error) {
      console.error('Error saving component name:', error)
      alert('Error saving component name. Please try again.')
    } finally {
      isLoading.value = false
    }
  }

  const toggleCollapseManually = async () => { // Manually toggle collapse
    await nextTick() // Wait for DOM updates

    const collapseElement = document.getElementById(`collapse-${props.bikecomponent.id}`) // Get the collapse element
    if (collapseElement) { // Check if collapse element exists
      // Get or create Bootstrap Collapse instance
      if (!collapseInstance) {
        collapseInstance = Collapse.getOrCreateInstance(collapseElement) // Create instance if it doesn't exist
      }

      // Toggle the collapse
      collapseInstance.toggle()
    }
  }  // Initialize collapse state on mount
  onMounted(async () => {
    await nextTick() // Ensure DOM is ready

    const collapseElement = document.getElementById(`collapse-${props.bikecomponent.id}`) // Get the collapse element
    if (collapseElement) { // Check if collapse element exists
      // Initialize Bootstrap Collapse
      collapseInstance = new Collapse(collapseElement, {
        toggle: false // Don't auto-toggle on initialization
      })

      // Set initial state
      isCollapsed.value = !collapseElement.classList.contains('show') // true if collapsed

      // Listen for Bootstrap collapse events
      collapseElement.addEventListener('shown.bs.collapse', () => { // Update state when shown
        isCollapsed.value = false
      })

      collapseElement.addEventListener('hidden.bs.collapse', () => { // Update state when hidden
        isCollapsed.value = true
      })
    }
  })
</script>
