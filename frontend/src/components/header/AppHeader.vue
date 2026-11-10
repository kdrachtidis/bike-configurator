<template>
    <nav class="navbar navbar-expand-lg navbar-right bg-body">
        <div class="container-fluid">
            <span class="navbar-text">
                {{ $t('appheader.title') }}!
            </span>
            <ul class="nav">
                <li class="nav-item me-2">
                    <SwitchLanguage />
                </li>

                <li class="nav-item vr me-2 text-white">
                    <hr class="d-lg-none my-2 text-white-50" />
                </li>

                <li class="nav-item me-2">
                    <SwitchTheme />
                </li>

                <li class="nav-item vr me-2 text-white">
                    <hr class="d-lg-none my-2 text-white-50" />
                </li>

                <li class="nav-item">
                    <button type="button" class="btn btn-sm btn-dark">{{$t('appheader.register')}}</button>
                </li>

                <li class="nav-item" v-if="!authStore.isAuthenticated">
                    <button type="button" class="btn btn-sm btn-dark" @click="showLoginModal" data-toggle="tooltip"
                        data-placement="bottom" :title="$t('appheader.login')" :aria-label="$t('appheader.login')">{{
                            $t('appheader.login') }}
                    </button>
                </li>
                <li class="nav-item" v-else>
                    <button type="button" class="btn btn-sm btn-dark" @click="logout" data-toggle="tooltip"
                        data-placement="bottom" :title="$t('appheader.logout')" :aria-label="$t('appheader.logout')">{{
                            $t('appheader.logout') }}
                    </button>
                </li>
            </ul>
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