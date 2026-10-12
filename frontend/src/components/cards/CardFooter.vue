<template>
  <div class="card-footer justify-content-between bg-body-tertiary text-end">
    <div class="card-text text-body-secondary">{{ $t("card.footer.partialsum") }}: {{ Sum || "Summary empty" }} {{ $t("card.footer.currency") }}</div>
  </div>
</template>

<script setup>
  defineProps({
    Sum: String
  })
</script>
