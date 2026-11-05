<template>
  <div class="alert alert-info m-2">
    <small>
      <i class="bi bi-info-circle me-1"></i>
      {{ $t('card.list.empty-parts') }} {{ props.bikecomponent?.name }}.
    </small>
  </div>
</template>

<script setup>
  const props = defineProps({
    bikecomponent: { type: Object, required: true },
  })
</script>
