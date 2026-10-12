<template>
  <div class="card-header d-flex justify-content-between align-items-center bg-body-secondary">
    <h4 class="card-title mb-0 fw-light">{{ bikecomponent.name || "Component Name Empty" }}</h4>

    <div class="d-flex gap-2">
      <button type="button" class="btn btn-sm btn-outline-secondary" @click="openEditComponentModal"
        :title="$t('card.header.edit')" :aria-label="$t('card.header.edit')">
        <i class="bi bi-pencil-fill"></i>
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
  import { Collapse } from 'bootstrap'

  const props = defineProps({
    bikecomponent: { type: Object, required: true }, // Bike component object
  })

  const bikeComponentStore = useBikeComponentStore() // Store instance
  const isCollapsed = ref(false) // Track collapse state
  let collapseInstance = null // Bootstrap Collapse instance

  const openEditComponentModal = () => {
    bikeComponentStore.setEditComponent(props.bikecomponent)
    window.dispatchEvent(new CustomEvent('open-add-bike-component-modal'))
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
