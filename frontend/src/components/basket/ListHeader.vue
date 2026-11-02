<template>
  <header>
    <div class="card-header d-flex justify-content-between bg-body-secondary">
      <h3 class="card-title mb-0 fs-4 fw-light">{{ $t('message.productlist') }}</h3>
      <button
        type="button"
        :class="['btn btn-sm', grouped ? 'btn-secondary' : 'btn-outline-secondary']"
        :aria-label="$t(grouped ? 'message.productlist-view-list' : 'message.productlist-view-grouped')"
        :aria-pressed="grouped"
        :title="$t(grouped ? 'message.productlist-view-list' : 'message.productlist-view-grouped')"
        @click="emit('toggle-view')"
      >
        <i :class="grouped ? 'bi bi-list-ul' : 'bi bi-grid-3x3-gap-fill'"></i>
      </button>
    </div>
  </header>
</template>

<script setup>
defineProps({
  grouped: { type: Boolean, default: true }
})

const emit = defineEmits(['toggle-view'])
</script>