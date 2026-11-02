import axios from 'axios'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAccessoryStore = defineStore('accessories', () => {
  const categories = ref([])
  const typesByCategory = ref(new Map())
  const productsByType = ref(new Map())
  const currentEditType = ref(null)
  const loading = ref(false)
  const error = ref('')

  async function getCategories() {
    loading.value = true
    error.value = ''
    try {
      const { data } = await axios.get('api/accessory-categories/')
      categories.value = data
      return data
    } catch (requestError) {
      error.value = requestError.response?.data?.detail || requestError.message
      throw requestError
    } finally {
      loading.value = false
    }
  }

  async function createCategory(name) {
    const { data } = await axios.post('api/accessory-categories/', { name })
    categories.value = [...categories.value, data]
    typesByCategory.value.set(data.id, [])
    return data
  }

  async function getTypes(categoryId) {
    const { data } = await axios.get(`api/accessory-categories/${categoryId}/accessory-types/`)
    typesByCategory.value.set(categoryId, data)
    return data
  }

  async function createType(categoryId, name) {
    const { data } = await axios.post(
      `api/accessory-categories/${categoryId}/accessory-types/`,
      { name },
    )
    const currentTypes = typesByCategory.value.get(categoryId) || []
    typesByCategory.value.set(categoryId, [...currentTypes, data])
    productsByType.value.set(data.id, [])
    return data
  }

  async function getProducts(typeId) {
    const { data } = await axios.get(`api/accessory-types/${typeId}/bikeproducts/`)
    productsByType.value.set(typeId, data)
    return data
  }

  async function createProduct(typeId, productData) {
    const { data } = await axios.post(
      `api/accessory-types/${typeId}/bikeproducts/`,
      productData,
    )
    const currentProducts = productsByType.value.get(typeId) || []
    productsByType.value.set(typeId, [...currentProducts, data])
    return data
  }

  function getTypesForCategory(categoryId) {
    return typesByCategory.value.get(categoryId) || []
  }

  function getProductsForType(typeId) {
    return productsByType.value.get(typeId) || []
  }

  function setEditType(type) {
    currentEditType.value = type
  }

  function clearEditType() {
    currentEditType.value = null
  }

  return {
    categories,
    typesByCategory,
    productsByType,
    currentEditType,
    loading,
    error,
    getCategories,
    createCategory,
    getTypes,
    createType,
    getProducts,
    createProduct,
    getTypesForCategory,
    getProductsForType,
    setEditType,
    clearEditType,
  }
})
