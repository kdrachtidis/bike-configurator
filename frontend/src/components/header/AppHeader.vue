<template>
    <nav class="navbar navbar-expand-lg navbar-right ">
        <div class="container-fluid">
            <span class="navbar-text">
                {{ $t('appheader.title') }}!
            </span>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item me-4">
                        <SwitchLanguage />
                    </li>

                    <li class="nav-item me-4">
                        <SwitchTheme />
                    </li>

                    <li class="nav-item" v-if="!authStore.isAuthenticated">
                        <button type="button" class="btn btn-sm btn-dark" @click="showLoginModal" data-toggle="tooltip"
                            data-placement="bottom" :title="$t('appheader.login')"
                            :aria-label="$t('appheader.login')">
                            <i class="bi bi-person-circle me-1"></i>{{ $t('appheader.login') }}
                        </button>
                    </li>
                    <li class="nav-item" v-else>
                        <button type="button" class="btn btn-sm btn-dark" @click="logout" data-toggle="tooltip"
                            data-placement="bottom" :title="$t('appheader.logout')"
                            :aria-label="$t('appheader.logout')">
                            <i class="bi bi-box-arrow-right me-1"></i>{{ $t('appheader.logout') }}
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>
<script setup>
import SwitchLanguage from '../header/SwitchLanguage.vue'
import SwitchTheme from './SwitchTheme.vue'
import { useAuthStore } from '@/stores/auth'
import { Modal } from 'bootstrap'

const authStore = useAuthStore() // Store instance



function showLoginModal() {
    // Corrected function name
    const modal = new Modal(document.getElementById('LoginModal')) // Create modal instance
    modal.show()
}

function logout() {
    authStore.logout()
}
</script>