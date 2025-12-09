import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useBikeProductStore = defineStore('bikeproducts', () => {
  const bikeproducts = ref([]);
  const bikeproductsByPart = ref(new Map());

  // Create a new bike product for a specific part
  async function createBikeProduct(partId, productData) {
    try {
      const { data } = await axios.post(`api/bikeparts/${partId}/bikeproducts/`, productData);
      console.log('Store: Created bike product:', data);
      return data;
    } catch (error) {
      console.error('Error creating bike product:', error);
      throw error;
    }
  }

  // Fetch all bike products for a specific part
  async function getBikeProductsByPart(partId) {
    try {
      const { data } = await axios.get(`api/bikeparts/${partId}/bikeproducts/`);
      bikeproductsByPart.value.set(partId, data);
      return data;
    } catch (error) {
      console.error('Error fetching bike products by part:', error);
      bikeproductsByPart.value.set(partId, []);
      return [];
    }
  }

  // Get products for a specific part from store
  function getBikeProductsForPart(partId) {
    return bikeproductsByPart.value.get(partId) || [];
  }

  return {
    bikeproducts,
    bikeproductsByPart,
    createBikeProduct,
    getBikeProductsByPart,
    getBikeProductsForPart
  };
});
