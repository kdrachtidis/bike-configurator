<template>
  <div class="card-body pt-2 pb-2 border-bottom d-flex justify-content-between bg-body">
    <div class="mt-1"><small class="text-body-secondary"><span class="badge text-bg-info">{{
      count }}</span> <span v-if="count === 1">{{ $t("message.item")
          }}</span><span v-else>{{ $t("message.items")
          }}</span></small></div>
    <button type="button" class="btn btn-sm btn-outline-secondary" :aria-label="$t('message.filter')">{{
      $t("message.filter") }}</button>
  </div>
</template>

<script setup>
  defineProps({
    count: { type: Number, required: false },
  })
</script>
