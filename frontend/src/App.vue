<template>
  <ConfiguratorComponent />
  <AddBikeComponent />
  <LoginModal />
  <AppHeader />
  <main class="container-fluid">
    <div class="row mt-3">
      <div class="col">
        <ConfiguratorHeader />
        <ConfiguratorList />
      </div>
      <div class="col-sm-3">
        <ConfiguratorProductList />
      </div>
    </div>
  </main>
</template>

<script setup>
import AppHeader from './components/ui/AppHeader.vue';
import ConfiguratorHeader from './components/configuration/ConfigurationHeader.vue';
import ConfiguratorList from './components/configuration/ConfigurationList.vue';
import ConfiguratorProductList from './components/basket/List.vue';
import ConfiguratorComponent from './components/modal/ConfiguratorComponent.vue';
import LoginModal from './components/modal/LoginModal.vue';
import AddBikeComponent from './components/modal/AddBikeComponent.vue';
</script>
