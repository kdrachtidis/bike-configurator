<template>
  <nav class="navbar" :aria-label="$t('appheader.title')">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <h1 class="display-6">
          {{ $t('appheader.title') }}
        </h1>
      </a>
      <form class="d-flex">
        <ul class="navbar-nav flex-row flex-wrap">
          <li class="nav-item vr h-100 mx-lg-2 text-white">
            <hr class="d-lg-none my-2 text-white-50" />
          </li>

          <li class="nav-item">
            <button type="button" class="btn btn-outline-secondary me-2" data-toggle="tooltip" data-placement="bottom"
              :title="$t('message.header-export')" :aria-label="$t('message.header-export')">
              {{ $t('message.header-export') }}
            </button>
          </li>
          <li class="nav-item">
            <button type="button" class="btn btn-outline-secondary" data-toggle="tooltip" data-placement="bottom"
              :title="$t('message.header-load')" :aria-label="$t('message.header-load')">
              {{ $t('message.header-load') }}
            </button>
          </li>
          
        </ul>
      </form>
    </div>
  </nav>
</template>

<script setup>





</script>
