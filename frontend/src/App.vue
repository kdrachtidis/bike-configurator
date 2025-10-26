<template>
  <ConfiguratorComponent />
  <ConfiguratorEditGroupName />
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
import ConfiguratorHeader from './components/ui/ConfiguratorHeader.vue';
import ConfiguratorProductList from './components/basket/ConfiguratorProductList.vue';
import ConfiguratorList from './components/module/ConfiguratorList.vue';
import ConfiguratorComponent from './components/modal/ConfiguratorComponent.vue';
import ConfiguratorEditGroupName from './components/modal/ConfiguratorEditGroupName.vue';
import LoginModal from './components/modal/LoginModal.vue';
</script>
