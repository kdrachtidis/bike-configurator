<template>
  <div class="card-header d-flex justify-content-between bg-body-secondary">
    <h4 class="card-title mb-0 fw-light">{{ bikecomponent.name || "Group Empty" }}
    </h4>
    <div>
      <button type="button" class="btn btn-sm btn-outline-secondary me-2" :aria-label="$t('message.edit')"
        @click="editGroup" data-bs-toggle="modal" data-bs-target="#EditGroupName">
        <i class="bi bi-pencil"></i>
      </button>
      <button type="button" class="btn btn-sm btn-outline-secondary" @click="toggleCollapseManually"
        :aria-label="$t('message.expand')"><i
          :class="isCollapsed ? 'bi bi-chevron-down' : 'bi bi-chevron-up'"></i></button>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, nextTick } from 'vue'
  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { Collapse } from 'bootstrap'

  const props = defineProps({
    bikecomponent: { type: Object, required: true },
  })

  const bikeComponentStore = useBikeComponentStore() // Store instance
  const isCollapsed = ref(false) // Track collapse state
  let collapseInstance = null // Bootstrap Collapse instance

  const editComponent = () => { // Function to set the component for editing
    bikeComponentStore.setEditComponent(props.bikecomponent) // Set the current component to be edited
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
