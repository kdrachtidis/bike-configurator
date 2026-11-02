<template>
  <section class="card border-secondary mb-3">
    <header class="card-header d-flex justify-content-between align-items-center bg-body-secondary">
      <h4 class="card-title mb-0 fw-light">{{ category.name }}</h4>
    </header>

    <div class="card-body">
      <form class="row g-2 mb-3" @submit.prevent="addType">
        <div class="col">
          <input
            v-model="typeName"
            class="form-control form-control-sm"
            :placeholder="$t('accessories.type-placeholder')"
            :aria-label="$t('accessories.type-placeholder')"
            :disabled="isSaving"
            required
          >
        </div>
        <div class="col-auto">
          <button
            class="btn btn-sm btn-outline-secondary"
            type="submit"
            :disabled="isSaving || !typeName.trim()"
          >
            {{ $t('accessories.add-type') }}
          </button>
        </div>
      </form>

      <div v-if="errorMessage" class="alert alert-danger py-2" role="alert">
        {{ errorMessage }}
      </div>
      <div v-else-if="isLoading" class="text-body-secondary">
        {{ $t('accessories.loading') }}
      </div>
      <div v-else-if="types.length === 0" class="text-body-secondary">
        {{ $t('accessories.no-types') }}
      </div>

      <ul v-else class="list-group list-group-flush">
        <li v-for="type in types" :key="type.id" class="list-group-item px-0">
          <div class="d-flex justify-content-between align-items-start gap-2">
            <h6 class="mb-0 fw-normal">{{ type.name }}</h6>
            <button
              type="button"
              class="btn btn-sm btn-outline-secondary"
              data-bs-toggle="modal"
              data-bs-target="#AddBikeProduct"
              :aria-label="$t('accessories.assign-product')"
              :title="$t('accessories.assign-product')"
              @click="openProductModal(type)"
            >
              <i class="bi bi-plus-lg"></i>
            </button>
          </div>
          <div v-if="accessoryStore.getProductsForType(type.id).length" class="mt-2">
            <div
              v-for="product in accessoryStore.getProductsForType(type.id)"
              :key="product.id"
              class="d-flex justify-content-between text-body-secondary"
            >
              <span>{{ product.name || 'Product empty' }}</span>
              <span>{{ formatPrice(product.price) }}</span>
            </div>
          </div>
          <div v-else class="small text-body-tertiary mt-1">
            {{ $t('accessories.no-products') }}
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useAccessoryStore } from '@/stores/accessory'
import { useBikeComponentStore } from '@/stores/bikecomponent'
import { useBikePartStore } from '@/stores/bikepart'

const props = defineProps({
  category: { type: Object, required: true },
})

const accessoryStore = useAccessoryStore()
const bikeComponentStore = useBikeComponentStore()
const bikePartStore = useBikePartStore()
const { t } = useI18n()
const typeName = ref('')
const isLoading = ref(false)
const isSaving = ref(false)
const errorMessage = ref('')

const types = computed(() => accessoryStore.getTypesForCategory(props.category.id))

async function loadTypes() {
  isLoading.value = true
  errorMessage.value = ''
  try {
    const loadedTypes = await accessoryStore.getTypes(props.category.id)
    await Promise.all(loadedTypes.map((type) => accessoryStore.getProducts(type.id)))
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || t('accessories.load-error')
  } finally {
    isLoading.value = false
  }
}

async function addType() {
  const name = typeName.value.trim()
  if (!name) return

  isSaving.value = true
  errorMessage.value = ''
  try {
    const type = await accessoryStore.createType(props.category.id, name)
    await accessoryStore.getProducts(type.id)
    typeName.value = ''
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || t('accessories.save-error')
  } finally {
    isSaving.value = false
  }
}

function openProductModal(type) {
  bikeComponentStore.clearEditComponent()
  bikePartStore.clearEditPart()
  accessoryStore.setEditType({ ...type, categoryName: props.category.name })
}

function formatPrice(value) {
  const numeric = Number(value ?? 0)
  return Number.isFinite(numeric) ? `${numeric.toFixed(2).replace('.', ',')}€` : '0,00€'
}

onMounted(loadTypes)
</script>
