<template>
  <section class="mt-3">
    <form class="row g-2 mb-3" @submit.prevent="addCategory">
      <div class="col">
        <input
          v-model="categoryName"
          class="form-control"
          :placeholder="$t('accessories.category-placeholder')"
          :aria-label="$t('accessories.category-placeholder')"
          :disabled="isSaving"
          required
        >
      </div>
      <div class="col-auto">
        <button class="btn btn-outline-secondary" type="submit" :disabled="isSaving || !categoryName.trim()">
          {{ $t('accessories.add-category') }}
        </button>
      </div>
    </form>

    <div v-if="accessoryStore.loading" class="alert alert-info" role="status">
      {{ $t('accessories.loading') }}
    </div>
    <div v-else-if="errorMessage" class="alert alert-danger" role="alert">
      {{ errorMessage }}
    </div>
    <div v-else-if="accessoryStore.categories.length === 0" class="alert alert-info">
      {{ $t('accessories.empty') }}
    </div>
    <AccessoryCategoryCard
      v-for="category in accessoryStore.categories"
      :key="category.id"
      :category="category"
    />
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useAccessoryStore } from '@/stores/accessory'
import AccessoryCategoryCard from './AccessoryCategoryCard.vue'

const accessoryStore = useAccessoryStore()
const { t } = useI18n()
const categoryName = ref('')
const errorMessage = ref('')
const isSaving = ref(false)

async function addCategory() {
  const name = categoryName.value.trim()
  if (!name) return

  isSaving.value = true
  errorMessage.value = ''
  try {
    await accessoryStore.createCategory(name)
    categoryName.value = ''
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || t('accessories.save-error')
  } finally {
    isSaving.value = false
  }
}

onMounted(async () => {
  try {
    await accessoryStore.getCategories()
  } catch {
    errorMessage.value = accessoryStore.error || t('accessories.load-error')
  }
})
</script>
