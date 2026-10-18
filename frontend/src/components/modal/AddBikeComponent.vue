<template>
  <div class="modal fade" id="AddBikeComponent" tabindex="-1" aria-labelledby="addBikeComponentModalLabel"
    aria-hidden="true" ref="modalRef">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="addBikeComponentModalLabel">{{ modalTitle }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal"
            :aria-label="$t('modal.button.close')"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="handleSave">
            <div class="mb-3 row">
              <label for="componentName" class="col-4 col-form-label">{{ $t("modal.addbikecomponent.label-component")
              }}:</label>
              <div class="col-8">
                <input type="text" class="form-control" id="componentName" v-model="componentName"
                  :placeholder="$t('modal.addbikecomponent.placeholder-component')"
                  :aria-label="$t('modal.addbikecomponent.placeholder-component')" :disabled="isLoading"
                  ref="componentInputRef">
              </div>
            </div>

            <div class="mb-3 row">
              <label class="col-4 col-form-label">{{ $t("modal.addbikecomponent.label-parts") }}:</label>
              <div class="col-8">
                <ul class="list-group mb-2 parts-list-scroll" ref="partsListRef">
                  <li v-for="part in partRows" :key="part.localId" class="list-group-item">
                    <div class="d-flex justify-content-between align-items-center gap-2">
                      <div class="flex-grow-1">
                        <input v-if="part.isEditing" type="text" class="form-control form-control-sm"
                          v-model="part.draftName" @keyup.enter="savePartInline(part)" @keyup.esc="cancelPartEdit(part)"
                          :disabled="isLoading">
                        <div v-else class="fs-6 fw-light text-break">{{ part.name || "Part empty" }}</div>
                      </div>

                      <div class="d-flex gap-2">
                        <template v-if="part.isEditing">
                          <button type="button" class="btn btn-sm btn-outline-success" @click="savePartInline(part)"
                            :disabled="isLoading || !part.draftName.trim()" title="Save" aria-label="Save">
                            <i class="bi bi-check-lg"></i>
                          </button>
                          <button type="button" class="btn btn-sm btn-outline-danger" @click="cancelPartEdit(part)"
                            :disabled="isLoading" title="Cancel" aria-label="Cancel">
                            <i class="bi bi-x-lg"></i>
                          </button>
                        </template>
                        <template v-else>
                          <button type="button" class="btn btn-sm btn-outline-secondary" @click="startPartEdit(part)"
                            :disabled="isLoading" :title="$t('card.header.edit')" :aria-label="$t('card.header.edit')">
                            <i class="bi bi-pencil-fill"></i>
                          </button>
                          <button type="button" class="btn btn-sm btn-outline-secondary" @click="removePart(part)"
                            :disabled="isLoading" title="Delete" aria-label="Delete">
                            <i class="bi bi-trash3"></i>
                          </button>
                        </template>
                      </div>
                    </div>
                  </li>
                </ul>

                <button type="button" class="btn btn-sm btn-outline-secondary" @click="addPartRow" :disabled="isLoading">
                  <i class="bi bi-plus-lg me-1"></i>
                  {{ $t("card.part.tooltip-add") }}
                </button>
              </div>
            </div>
          </form>

          <div v-if="errorMessage" class="alert alert-danger" role="alert">
            {{ errorMessage }}
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t("modal.button.close") }}</button>
          <button type="button" class="btn btn-primary" @click="handleSave" :disabled="isLoading || !componentName.trim()">
            <span v-if="isLoading" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
            {{ $t("modal.button.save") }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed, nextTick, onMounted, onUnmounted, ref } from 'vue'
  import { useI18n } from 'vue-i18n'
  import { Modal } from 'bootstrap'
  import { useBikeComponentStore } from '@/stores/bikecomponent'
  import { useBikePartStore } from '@/stores/bikepart'
  import { useBikeTypeStore } from '@/stores/biketype'

  const modalRef = ref(null)
  const componentInputRef = ref(null)
  const partsListRef = ref(null)
  const bikeComponentStore = useBikeComponentStore()
  const bikePartStore = useBikePartStore()
  const bikeTypeStore = useBikeTypeStore()
  const { t } = useI18n()
  const componentName = ref('')
  const partRows = ref([])
  const deletedPartIds = ref([])
  const isLoading = ref(false)
  const errorMessage = ref('')
  const nextLocalId = ref(1)

  const isEditMode = computed(() => Boolean(bikeComponentStore.currentEditComponent?.id))
  const modalTitle = computed(() => {
    return isEditMode.value
      ? `${bikeComponentStore.currentEditComponent?.name ?? ''} (${String(t("card.header.edit"))})`
      : t("modal.addbikecomponent.modal-title")
  })

  const buildPartRow = (part = null) => ({
    localId: nextLocalId.value++,
    id: part?.id ?? null,
    name: part?.name ?? '',
    originalName: part?.name ?? '',
    draftName: part?.name ?? '',
    isNew: !part?.id,
    isEditing: !part?.id
  })

  const resetForm = () => {
    componentName.value = ''
    partRows.value = []
    deletedPartIds.value = []
    errorMessage.value = ''
    isLoading.value = false
  }

  const preloadForCurrentMode = async () => {
    resetForm()

    if (isEditMode.value) {
      const selectedComponent = bikeComponentStore.currentEditComponent
      componentName.value = selectedComponent.name ?? ''

      const bikeTypeId = bikeTypeStore.currentBikeType?.id
      if (bikeTypeId && selectedComponent?.id) {
        const parts = await bikePartStore.getBikePartsByComponent(bikeTypeId, selectedComponent.id)
        partRows.value = parts.map((part) => buildPartRow(part))
      }
    } else {
      partRows.value = []
    }
  }

  const addPartRow = async () => {
    partRows.value.push(buildPartRow())
    await nextTick()
    if (partsListRef.value) {
      partsListRef.value.scrollTop = partsListRef.value.scrollHeight
    }
  }

  const startPartEdit = (part) => {
    part.draftName = part.name
    part.isEditing = true
  }

  const cancelPartEdit = (part) => {
    if (part.isNew && !part.name.trim()) {
      partRows.value = partRows.value.filter((row) => row.localId !== part.localId)
      return
    }

    part.draftName = part.name
    part.isEditing = false
  }

  const savePartInline = (part) => {
    const nextName = part.draftName.trim()
    if (!nextName) return
    part.name = nextName
    part.isEditing = false
  }

  const removePart = (part) => {
    if (part.id) {
      deletedPartIds.value.push(part.id)
    }
    partRows.value = partRows.value.filter((row) => row.localId !== part.localId)
  }

  const openModal = async () => {
    if (!modalRef.value) return
    const modal = Modal.getOrCreateInstance(modalRef.value)
    await preloadForCurrentMode()
    modal.show()
  }

  const closeModal = () => {
    if (!modalRef.value) return
    const modal = Modal.getOrCreateInstance(modalRef.value)
    modal.hide()
  }

  const handleSave = async () => {
    if (!componentName.value.trim()) {
      errorMessage.value = 'Bitte geben Sie einen Namen ein'
      return
    }

    if (!bikeTypeStore.currentBikeType?.id) {
      errorMessage.value = 'Bitte wählen Sie zuerst einen Fahrradtyp aus'
      return
    }

    isLoading.value = true
    errorMessage.value = ''

    try {
      const bikeTypeId = bikeTypeStore.currentBikeType.id
      let componentId = bikeComponentStore.currentEditComponent?.id

      if (isEditMode.value) {
        if (componentName.value.trim() !== bikeComponentStore.currentEditComponent.name) {
          await bikeComponentStore.updateBikeComponentByBikeType(
            bikeTypeId,
            componentId,
            componentName.value.trim()
          )
        }
      } else {
        const createdComponent = await bikeComponentStore.createBikeComponent(
          bikeTypeId,
          componentName.value.trim()
        )
        componentId = createdComponent.id
      }

      if (!componentId) {
        throw new Error('Component ID is missing after save.')
      }

      for (const partId of deletedPartIds.value) {
        await bikePartStore.deleteBikePartByComponent(bikeTypeId, componentId, partId)
      }

      for (const part of partRows.value) {
        const name = part.name.trim()
        if (!name) continue

        if (part.id) {
          if (name !== part.originalName) {
            await bikePartStore.updateBikePartByComponent(bikeTypeId, componentId, part.id, name)
          }
        } else {
          await bikePartStore.createBikePartByComponent(bikeTypeId, componentId, name)
        }
      }

      await bikePartStore.getBikePartsByComponent(bikeTypeId, componentId)
      closeModal()
    } catch (error) {
      console.error('Error saving bike component modal data:', error)
      if (error.response?.status === 401) {
        errorMessage.value = 'Nicht autorisiert. Bitte melden Sie sich an.'
      } else if (error.response?.status === 404) {
        errorMessage.value = 'Fahrradtyp oder Komponente nicht gefunden'
      } else {
        errorMessage.value = 'Fehler beim Speichern. Bitte versuchen Sie es erneut.'
      }
    } finally {
      isLoading.value = false
    }
  }

  const handleShown = () => {
    componentInputRef.value?.focus()
  }

  const handleHidden = () => {
    resetForm()
    bikeComponentStore.clearEditComponent()
  }

  onMounted(() => {
    window.addEventListener('open-add-bike-component-modal', openModal)
    modalRef.value?.addEventListener('shown.bs.modal', handleShown)
    modalRef.value?.addEventListener('hidden.bs.modal', handleHidden)
  })

  onUnmounted(() => {
    window.removeEventListener('open-add-bike-component-modal', openModal)
    modalRef.value?.removeEventListener('shown.bs.modal', handleShown)
    modalRef.value?.removeEventListener('hidden.bs.modal', handleHidden)
    if (modalRef.value) {
      Modal.getOrCreateInstance(modalRef.value).dispose()
    }
  })

  defineExpose({
    openModal,
    closeModal
  })
</script>

<style scoped>
  .parts-list-scroll {
    max-height: 240px;
    overflow-y: auto;
    overflow-x: hidden;
    scrollbar-gutter: stable;
    padding-right: 2px;
  }
</style>
