<template>
  <nav class="navbar navbar-expand-md bg-light-subtle rounded">
    <div class="container-fluid">
      <div class="dropdown" :class="{ show: isDropdownOpen }">
        <button class="btn btn-secondary dropdown-toggle" type="button" @click="toggleDropdown"
          :aria-expanded="isDropdownOpen">
          {{ bikeTypeStore.currentBikeType?.name || "Type empty" }}
        </button>
        <ul class="dropdown-menu" :class="{ show: isDropdownOpen }">
          <li v-if="bikeTypeStore.loading">
            <span class="dropdown-item-text">Loading...</span>
          </li>
          <li v-if="bikeTypeStore.error">
            <span class="dropdown-item-text text-danger">{{ bikeTypeStore.error }}</span>
          </li>
          <li v-if="!bikeTypeStore.loading && bikeTypeStore.biketypes.length === 0">
            <span class="dropdown-item-text">No bike types available</span>
          </li>
          <li v-for="bikeType in bikeTypeStore.biketypes" :key="bikeType.id">
            <button type="button" class="dropdown-item"
              :class="{ 'active': bikeTypeStore.currentBikeType?.id === bikeType.id }" @click="selectBikeType(bikeType)"
              @mousedown.prevent>
              {{ bikeType.name }}
            </button>
          </li>
        </ul>
      </div>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#bikeType"
        aria-controls="bikeType" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="bikeType">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">{{ $t("message.subheader-tab-components") }}</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">{{ $t("message.subheader-tab-accessories") }}</a>
          </li>
        </ul>
      </div>
      <div class="col-md-6 text-end">
        <button type="button" class="btn btn-sm btn-outline-secondary" data-bs-toggle="modal"
          data-bs-target="#AddBikeComponent" data-toggle="tooltip" data-placement="bottom"
          :title="$t('message.subheader-add')" :aria-label="$t('message.subheader-add')">{{
            $t('message.subheader-add') }}</button>
      </div>
    </div>
  </nav>
</template>

<script setup>
  import { useBikeTypeStore } from '@/stores/biketype';
  import { onMounted, ref, onUnmounted } from 'vue';

  const bikeTypeStore = useBikeTypeStore(); // Store instance
  const isDropdownOpen = ref(false); // Dropdown state

  // Close dropdown when clicking outside
  function handleClickOutside(event) {
    const dropdown = event.target.closest('.dropdown'); // Check if click is inside dropdown
    if (!dropdown) {
      closeDropdown();
    }
  }

  // Load bike types when component mounts
  onMounted(async () => {
    // Add click outside listener
    document.addEventListener('click', handleClickOutside);
    console.log('ConfigurationHeader: Loading bike types...');
    await bikeTypeStore.getBikeTypes(); // Fetch bike types from API
    console.log('ConfigurationHeader: Bike types loaded:', bikeTypeStore.biketypes);
    console.log('ConfigurationHeader: Number of bike types:', bikeTypeStore.biketypes.length);

    // If no bike type is selected and we have bike types, select the first one
    if (!bikeTypeStore.currentBikeType && bikeTypeStore.biketypes.length > 0) {
      console.log('ConfigurationHeader: Auto-selecting first bike type');
      bikeTypeStore.setBikeType(bikeTypeStore.biketypes[0]); // Set first bike type
    }
  });

  // Cleanup event listener
  onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside); // Remove listener
  });

  // Dropdown control functions
  function toggleDropdown() {
    isDropdownOpen.value = !isDropdownOpen.value; // Toggle state
    console.log('Dropdown toggled:', isDropdownOpen.value);
  }

  function closeDropdown() {
    isDropdownOpen.value = false; // Close dropdown
  }

  // Function to select a bike type
  function selectBikeType(bikeType) {
    console.log('selectBikeType called with:', bikeType);

    try { // Error handling
      bikeTypeStore.setBikeType(bikeType); // Set selected bike type
      console.log('Bike type set successfully in store');
      console.log('Current bike type in store:', bikeTypeStore.currentBikeType);

      // Close dropdown after selection
      closeDropdown();
    } catch (error) { // Error handling
      console.error('Error setting bike type:', error);
    }
  }

</script>
