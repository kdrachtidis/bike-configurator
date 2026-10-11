<template>
  <div class="card-body pt-2 pb-2 border-bottom d-flex justify-content-between bg-body">
    <div class="mt-1"><small class="text-body-secondary"><span class="badge text-bg-info">{{
      count }}</span> <span v-if="count === 1">{{ $t("card.subheader.item")
          }}</span><span v-else>{{ $t("card.subheader.items")
          }}</span></small></div>
    <button type="button" :class="['btn btn-sm', filterActive ? 'btn-secondary' : 'btn-outline-secondary']"
      :aria-label="$t('card.subheader.filter')" :aria-pressed="filterActive ? 'true' : 'false'" data-bs-toggle="button" data-toggle="tooltip" data-placement="bottom"
      :title="$t('card.subheader.filter')" @click="emit('toggle-filter')"><i class="bi bi-funnel-fill"></i></button>
  </div>
</template>

<script setup>
  const emit = defineEmits(['toggle-filter'])

  defineProps({
    count: { type: Number, required: false },
    filterActive: { type: Boolean, default: false }
  })
</script>
