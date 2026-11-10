<template>
    <div ref="dropdown" class="dropdown" :class="{ show: isDropdownOpen }">
        <span class="navbar-text me-2"><small>{{ $t('appheader.language') }}:</small></span>
        <button id="languageDropdown" class="btn btn-sm btn-dark dropdown-toggle" type="button"
            aria-controls="languageMenu" :aria-expanded="isDropdownOpen" :aria-label="$t('appheader-language')"
            :title="$t('appheader.language')" @click="isDropdownOpen = !isDropdownOpen">
            {{ $i18n.locale }}
        </button>
        <ul id="languageMenu" class="dropdown-menu" :class="{ show: isDropdownOpen }"
            aria-labelledby="languageDropdown">
            <li v-for="locale in $i18n.availableLocales" :key="locale">
                <button type="button" class="dropdown-item" :class="{ active: $i18n.locale === locale }"
                    :aria-current="$i18n.locale === locale ? 'true' : undefined" @click="selectLocale(locale)">
                    {{ locale }}
                </button>
            </li>
        </ul>
    </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const dropdown = ref(null)
const isDropdownOpen = ref(false)

function selectLocale(selectedLocale) {
    locale.value = selectedLocale
    isDropdownOpen.value = false
}

function handleClickOutside(event) {
    if (!dropdown.value?.contains(event.target)) {
        isDropdownOpen.value = false
    }
}

onMounted(() => {
    document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside)
})
</script>
