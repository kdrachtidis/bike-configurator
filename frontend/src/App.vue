<template>
  <ConfiguratorComponent />
  <EditBikeProduct />
  <AddBikeComponent />
  <LoginModal />
  <AppHeader />
  <main class="container-fluid">
    <div class="row mt-3">
      <div class="col">
        <ConfiguratorHeader />
        <ConfiguratorTabs v-model="activeConfigurationTab" />
        <div
          id="configuration-panel-components"
          class="tab-content"
          role="tabpanel"
          aria-labelledby="configuration-tab-components"
          v-show="activeConfigurationTab === 'components'"
        >
          <ConfiguratorList />
        </div>
        <div
          id="configuration-panel-accessories"
          class="tab-content"
          role="tabpanel"
          aria-labelledby="configuration-tab-accessories"
          v-show="activeConfigurationTab === 'accessories'"
        >
          <ConfiguratorAccessories />
        </div>
        <div
          id="configuration-panel-basket"
          class="tab-content"
          role="tabpanel"
          aria-labelledby="configuration-tab-basket"
          v-show="activeConfigurationTab === 'basket'"
        >
          <ConfiguratorProductList />
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import AppHeader from './components/ui/AppHeader.vue';
import ConfiguratorHeader from './components/configuration/ConfigurationHeader.vue';
import ConfiguratorList from './components/configuration/ConfigurationList.vue';
import ConfiguratorTabs from './components/configuration/ConfigurationTabs.vue';
import ConfiguratorAccessories from './components/accessories/AccessoryList.vue';
import ConfiguratorProductList from './components/basket/List.vue';
import ConfiguratorComponent from './components/modal/AddBikeProduct.vue';
import EditBikeProduct from './components/modal/EditBikeProduct.vue';
import LoginModal from './components/modal/LoginModal.vue';
import AddBikeComponent from './components/modal/AddBikeComponent.vue';

const activeConfigurationTab = ref('components');
</script>
