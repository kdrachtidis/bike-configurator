<template>
    <div class="nav nav-tabs" role="tablist">
        <button id="configuration-tab-components" class="nav-link" :class="{ active: modelValue === 'components' }"
            type="button" role="tab" aria-controls="configuration-panel-components"
            :aria-selected="modelValue === 'components'" @click="$emit('update:modelValue', 'components')">
            {{ $t('tabs.tab-components') }}
        </button>
        <button id="configuration-tab-accessories" class="nav-link" :class="{ active: modelValue === 'accessories' }"
            type="button" role="tab" aria-controls="configuration-panel-accessories"
            :aria-selected="modelValue === 'accessories'" @click="$emit('update:modelValue', 'accessories')">
            {{ $t('tabs.tab-accessories') }}
        </button>
        <button id="configuration-tab-basket" class="nav-link" :class="{ active: modelValue === 'basket' }"
            type="button" role="tab" aria-controls="configuration-panel-basket"
            :aria-selected="modelValue === 'basket'" @click="$emit('update:modelValue', 'basket')">
            {{ $t('tabs.tab-basket') }}
        </button>
    </div>
</template>

<script setup>
defineProps({
    modelValue: { type: String, required: true },
})

defineEmits(['update:modelValue'])
</script>
