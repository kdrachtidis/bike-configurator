<template>
  <nav class="navbar" :aria-label="$t('appheader.title')">
    <div class="container-fluid">

      <ul class="nav">
        <span class="navbar-text me-2">{{ $t('configurationheader.title') }}:</span>
        <li class="nav-item">
          <SelectBikeType />
        </li>
      </ul>

      <ul class="nav">
        <li class="nav-item">
          <button type="button" class="btn btn-outline-secondary me-2" data-toggle="tooltip" data-placement="bottom"
            :title="$t('configurationheader.export')" :aria-label="$t('configurationheader.export')">
            {{ $t('configurationheader.export') }}
          </button>
        </li>
        <li class="nav-item">
          <button type="button" class="btn btn-outline-secondary" data-toggle="tooltip" data-placement="bottom"
            :title="$t('configurationheader.load')" :aria-label="$t('configurationheader.load')">
            {{ $t('configurationheader.load') }}
          </button>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import SelectBikeType from '../header/SelectBikeType.vue'
</script>
