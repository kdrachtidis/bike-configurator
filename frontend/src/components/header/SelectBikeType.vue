<template>
    <div class="dropdown" :class="{ show: isDropdownOpen }">
        <button class="btn btn-secondary dropdown-toggle" type="button" @click="toggleDropdown"
            :aria-expanded="isDropdownOpen">
            {{ bikeTypeStore.currentBikeType?.name || 'Type empty' }}
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
                    :class="{ active: bikeTypeStore.currentBikeType?.id === bikeType.id }"
                    @click="selectBikeType(bikeType)" @mousedown.prevent>
                    {{ bikeType.name }}
                </button>
            </li>
        </ul>
    </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import { useBikeTypeStore } from '@/stores/biketype'

const bikeTypeStore = useBikeTypeStore()
const isDropdownOpen = ref(false)

function handleClickOutside(event) {
    if (!event.target.closest('.dropdown')) {
        isDropdownOpen.value = false
    }
}

onMounted(async () => {
    document.addEventListener('click', handleClickOutside)
    await bikeTypeStore.getBikeTypes()

    if (!bikeTypeStore.currentBikeType && bikeTypeStore.biketypes.length > 0) {
        bikeTypeStore.setBikeType(bikeTypeStore.biketypes[0])
    }
})

onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside)
})

function toggleDropdown() {
    isDropdownOpen.value = !isDropdownOpen.value
}

function selectBikeType(bikeType) {
    bikeTypeStore.setBikeType(bikeType)
    isDropdownOpen.value = false
}
</script>