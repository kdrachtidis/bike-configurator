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
          <button type="button" class="btn btn-dark me-2" data-toggle="tooltip" data-placement="bottom"
            :title="$t('configurationheader.duplicate')" :aria-label="$t('configurationheader.duplicate')">
            {{ $t('configurationheader.duplicate') }}
          </button>
        </li>
        <li class="nav-item vr me-2 text-white">
          <hr class="d-lg-none my-2 text-white-50" />
        </li>
        <li class="nav-item">
          <button type="button" class="btn btn-dark me-2" data-toggle="tooltip" data-placement="bottom"
            :title="$t('configurationheader.save')" :aria-label="$t('configurationheader.save')">
            {{ $t('configurationheader.save') }}
          </button>
        </li>
        <li class="nav-item">
          <button type="button" class="btn btn-dark me-2" data-toggle="tooltip" data-placement="bottom"
            :title="$t('configurationheader.delete')" :aria-label="$t('configurationheader.delete')">
            {{ $t('configurationheader.delete') }}
          </button>
        </li>
        <li class="nav-item vr me-2 text-white">
          <hr class="d-lg-none my-2 text-white-50" />
        </li>
        <li class="nav-item">
          <button type="button" class="btn btn-dark me-2" data-toggle="tooltip" data-placement="bottom"
            :title="$t('configurationheader.export')" :aria-label="$t('configurationheader.export')">
            {{ $t('configurationheader.export') }}
          </button>
        </li>
        <li class="nav-item">
          <button type="button" class="btn btn-dark" data-toggle="tooltip" data-placement="bottom"
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
