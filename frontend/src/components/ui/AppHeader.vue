<template>
  <header>
    <nav class="navbar bg-dark-subtle" :aria-label="$t('message.title')">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          <h1 class="display-6"><i class="bi bi-bicycle me-3"></i>{{ $t("message.header-title") }}</h1>
        </a>
        <form class="d-flex">
          <div class="navbar-brand">{{ $t("message.header-language") }}: </div>
          <SwitchLanguage />
          <ul class="navbar-nav flex-row flex-wrap">
            <li class="nav-item vr h-100 mx-lg-2 text-white">
              <hr class="d-lg-none my-2 text-white-50" />
            </li>
            <li class="nav-item">
              <div class="btn-group me-2" role="group" :aria-label="$t('message.header-theme')">
                <button type="button" class="btn btn-outline-secondary active" @click="theme" data-toggle="tooltip" data-placement="bottom" :title="$t('message.header-dark')"
                  :aria-label="$t('message.header-dark')">{{
                    $t("message.header-dark")
                  }}</button>
                <button type="button" class="btn btn-outline-secondary" data-toggle="tooltip" data-placement="bottom" :title="$t('message.header-light')" :aria-label="$t('message.header-light')">{{
                  $t("message.header-light") }}</button>
              </div>
            </li>
            <li class="nav-item">
              <button type="button" class="btn btn-outline-secondary me-2" data-toggle="tooltip" data-placement="bottom" :title="$t('message.header-export')" :aria-label="$t('message.header-export')">{{
                $t("message.header-export") }}</button>
            </li>
            <li class="nav-item">
              <button type="button" class="btn btn-outline-secondary" data-toggle="tooltip" data-placement="bottom" :title="$t('message.header-load')" :aria-label="$t('message.header-load')">{{
                $t("message.header-load") }}</button>
            </li>
            <li class="nav-item vr h-100 mx-lg-2 text-white">
              <hr class="d-lg-none my-2 text-white-50" />
            </li>
            <li class="nav-item" v-if="!authStore.isAuthenticated">
              <button type="button" class="btn btn-outline-primary" @click="showLoginModal" data-toggle="tooltip" data-placement="bottom" :title="$t('message.header-login')" :aria-label="$t('message.header-login')">
                <i class="bi bi-person-circle me-1"></i>{{ $t('message.header-login') }}
              </button>
            </li>
            <li class="nav-item" v-else>
              <button type="button" class="btn btn-outline-danger" @click="logout" data-toggle="tooltip" data-placement="bottom" :title="$t('message.header-logout')" :aria-label="$t('message.header-logout')">
                <i class="bi bi-box-arrow-right me-1"></i>{{ $t('message.header-logout') }}
              </button>
            </li>
          </ul>
        </form>
      </div>
    </nav>
  </header>
</template>

<script setup>
  import SwitchLanguage from '../ui/SwitchLanguage.vue'
  import { useAuthStore } from '@/stores/auth'
  import { Modal } from 'bootstrap'

  const authStore = useAuthStore() // Store instance

  function theme() {
    alert('Hallo');
  }

  function showLoginModal() { // Corrected function name
    const modal = new Modal(document.getElementById('LoginModal')) // Create modal instance
    modal.show()
  }

  function logout() {
    authStore.logout()
  }
</script>
