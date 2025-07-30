<template>
    <div class="card-footer justify-content-between bg-body-tertiary text-end">
        <div class="card-text text-body-secondary">{{ $t("message.partialsum") }}: {{ Sum || "Summary empty" }}</div>
    </div>
</template>

<script setup>
const props = defineProps({
    Sum: String
})
</script>
