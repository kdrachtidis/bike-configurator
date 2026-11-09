import axios from 'axios';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useBikeProductStore = defineStore('bikeproducts', () => {
  const bikeproducts = ref([]);
  const bikeproductsByPart = ref(new Map());
  const currentEditProduct = ref(null);

  // Create a new bike product for a specific part
  async function createBikeProduct(partId, productData) {
    try {
      const { data } = await axios.post(`api/bikeparts/${partId}/bikeproducts/`, productData);
      const currentProducts = bikeproductsByPart.value.get(partId) || [];
      bikeproductsByPart.value.set(partId, [...currentProducts, data]);
      bikeproducts.value = [...bikeproducts.value, data];
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

  async function updateBikeProduct(partId, productId, productData) {
    try {
      const { data } = await axios.put(`api/bikeparts/${partId}/bikeproducts/${productId}`, productData);
      const currentProducts = bikeproductsByPart.value.get(partId) || [];
      const updatedProducts = currentProducts.map((product) =>
        product.id === productId ? data : product
      );
      bikeproductsByPart.value.set(partId, updatedProducts);
      bikeproducts.value = bikeproducts.value.map((product) =>
        product.id === productId ? data : product
      );
      return data;
    } catch (error) {
      console.error('Error updating bike product:', error);
      throw error;
    }
  }

  async function deleteBikeProduct(partId, productId) {
    try {
      await axios.delete(`api/bikeparts/${partId}/bikeproducts/${productId}`);
      for (const [bikePartId, products] of bikeproductsByPart.value) {
        bikeproductsByPart.value.set(
          bikePartId,
          products.filter((product) => product.id !== productId)
        );
      }
      bikeproducts.value = bikeproducts.value.filter((product) => product.id !== productId);
      if (currentEditProduct.value?.id === productId) {
        currentEditProduct.value = null;
      }
    } catch (error) {
      console.error('Error deleting bike product:', error);
      throw error;
    }
  }

  async function resetProductsForBikeType(bikeTypeId) {
    try {
      const { data: components } = await axios.get(`api/biketypes/${bikeTypeId}/bikecomponents`);
      if (!Array.isArray(components)) {
        throw new Error('Bike component response was not a list.');
      }

      const productAssignments = new Map();
      for (const component of components) {
        const { data: parts } = await axios.get(
          `api/biketypes/${bikeTypeId}/bikecomponents/${component.id}/bikeparts`
        );
        if (!Array.isArray(parts)) {
          throw new Error(`Bike part response for component ${component.id} was not a list.`);
        }

        for (const part of parts) {
          const { data: products } = await axios.get(`api/bikeparts/${part.id}/bikeproducts/`);
          if (!Array.isArray(products)) {
            throw new Error(`Bike product response for part ${part.id} was not a list.`);
          }

          for (const product of products) {
            if (!productAssignments.has(product.id)) {
              productAssignments.set(product.id, part.id);
            }
          }
        }
      }

      for (const [productId, partId] of productAssignments) {
        await deleteBikeProduct(partId, productId);
      }

      return productAssignments.size;
    } catch (error) {
      console.error('Error resetting products for bike type:', error);
      throw error;
    }
  }

  // Get products for a specific part from store
  function getBikeProductsForPart(partId) {
    return bikeproductsByPart.value.get(partId) || [];
  }

  function setEditProduct(product) {
    currentEditProduct.value = product;
  }

  function clearEditProduct() {
    currentEditProduct.value = null;
  }

  return {
    bikeproducts,
    bikeproductsByPart,
    currentEditProduct,
    createBikeProduct,
    getBikeProductsByPart,
    updateBikeProduct,
    deleteBikeProduct,
    resetProductsForBikeType,
    getBikeProductsForPart,
    setEditProduct,
    clearEditProduct
  };
});
