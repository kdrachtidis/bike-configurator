<template>
    <small>{{ $t('appheader.theme') }}: </small>
    <div class="btn-group btn-group-sm" role="group" :aria-label="$t('appheader.theme')">
        <button type="button" class="btn btn-outline-secondary active" @click="theme" data-toggle="tooltip"
            data-placement="bottom" :title="$t('appheader.dark')" :aria-label="$t('appheader.dark')">
            {{ $t('appheader.dark') }}
        </button>
        <button type="button" class="btn btn-outline-secondary" data-toggle="tooltip" data-placement="bottom"
            :title="$t('appheader.light')" :aria-label="$t('appheader.light')">
            {{ $t('appheader.light') }}
        </button>
    </div>
</template>

<script setup>
function theme() {
    alert('Hallo')
}
</script>