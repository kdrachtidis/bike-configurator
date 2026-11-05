<template>
  <!-- Für Entwicklung: Modal immer sichtbar mit persistentem Backdrop -->
  <div v-if="isDevelopment" class="dev-modal-backdrop"></div>
  <div :class="['modal', isDevelopment ? 'show dev-modal' : 'fade']" id="LoginModal" tabindex="-1" 
       aria-labelledby="loginModalLabel" :aria-hidden="!isDevelopment"
       :style="isDevelopment ? 'display: block; position: fixed; z-index: 1055;' : ''">
    <div class="modal-dialog modal-sm">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="loginModalLabel">Anmelden</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Schließen"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="handleLogin">
            <div class="mb-3">
              <label for="username" class="form-label">Benutzername</label>
              <input type="text" class="form-control" id="username" v-model="username" required :disabled="isLoading">
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Passwort</label>
              <input type="password" class="form-control" id="password" v-model="password" required
                :disabled="isLoading">
            </div>
            <div v-if="errorMessage" class="alert alert-danger" role="alert">
              {{ errorMessage }}
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Abbrechen</button>
          <button type="button" class="btn btn-primary" @click="handleLogin"
            :disabled="isLoading || !username || !password">
            <span v-if="isLoading" class="spinner-border spinner-border-sm me-2" role="status"
              aria-hidden="true"></span>
            Anmelden
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import { Modal } from 'bootstrap';

  // Development flag - set to false for production
  const isDevelopment = ref(false) // Set to true to always show modal in development

  const authStore = useAuthStore();

  const username = ref('');
  const password = ref('');
  const isLoading = ref(false);
  const errorMessage = ref('');

  // Function to properly close login modal
  const closeLoginModal = async () => {
    const modalElement = document.getElementById('LoginModal')
    if (modalElement) {
      // Try to get existing instance first
      let modal = Modal.getInstance(modalElement)

      if (!modal) {
        // If no instance exists, create one
        modal = new Modal(modalElement)
      }

      // Hide the modal
      modal.hide()

      // Wait a bit for animation
      await new Promise(resolve => setTimeout(resolve, 150))

      // Force remove backdrop if it still exists
      const backdrop = document.querySelector('.modal-backdrop')
      if (backdrop) {
        backdrop.remove()
      }

      // Ensure body classes are cleaned up
      document.body.classList.remove('modal-open')
      document.body.style.overflow = ''
      document.body.style.paddingRight = ''
    }
  }

  const handleLogin = async () => {
    if (!username.value || !password.value) {
      errorMessage.value = 'Bitte geben Sie Benutzername und Passwort ein';
      return;
    }

    isLoading.value = true;
    errorMessage.value = '';

    try {
      await authStore.login(username.value, password.value);

      // Close modal properly
      await closeLoginModal();

      // Reset form
      username.value = '';
      password.value = '';

    } catch (error) {
      console.error('Login failed:', error);
      if (error.response?.status === 400) {
        errorMessage.value = 'Benutzername oder Passwort ist falsch';
      } else {
        errorMessage.value = 'Anmeldung fehlgeschlagen. Bitte versuchen Sie es erneut.';
      }
    } finally {
      isLoading.value = false;
    }
  };
</script>

<style scoped>
.dev-modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1050;
  pointer-events: none; /* Backdrop doesn't interfere with modal interactions */
}

.dev-modal {
  pointer-events: auto; /* Modal can be interacted with */
}

.dev-modal .modal-dialog {
  margin: 1.75rem auto;
}
</style>
