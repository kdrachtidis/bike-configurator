<template>
  <ConfiguratorComponent />
  <EditBikeProduct />
  <AddBikeComponent />
  <LoginModal />
  <AppHeader />
  <main class="container-fluid">
    <div class="row mt-3">
      <div class="col">
        
        <ConfiguratorTabs v-model="activeConfigurationTab" />
        <div class="tab-content">
          <div id="configuration-panel-components" class="tab-pane"
            :class="{ show: activeConfigurationTab === 'components', active: activeConfigurationTab === 'components' }"
            role="tabpanel" aria-labelledby="configuration-tab-components">
            <ConfiguratorToolbar />
            <ConfiguratorList />
          </div>
          <div id="configuration-panel-accessories" class="tab-pane"
            :class="{ show: activeConfigurationTab === 'accessories', active: activeConfigurationTab === 'accessories' }"
            role="tabpanel" aria-labelledby="configuration-tab-accessories">
            <ConfiguratorToolbar />
            <ConfiguratorAccessories />
          </div>
          <div id="configuration-panel-basket" class="tab-pane"
            :class="{ show: activeConfigurationTab === 'basket', active: activeConfigurationTab === 'basket' }"
            role="tabpanel" aria-labelledby="configuration-tab-basket">
            <ConfiguratorProductList />
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import AppHeader from './components/ui/AppHeader.vue'
import ConfiguratorToolbar from './components/configuration/ConfigurationToolbar.vue'
import ConfiguratorList from './components/configuration/ConfigurationList.vue'
import ConfiguratorTabs from './components/configuration/ConfigurationTabs.vue'
import ConfiguratorAccessories from './components/accessories/AccessoryList.vue'
import ConfiguratorProductList from './components/basket/List.vue'
import ConfiguratorComponent from './components/modal/AddBikeProduct.vue'
import EditBikeProduct from './components/modal/EditBikeProduct.vue'
import LoginModal from './components/modal/LoginModal.vue'
import AddBikeComponent from './components/modal/AddBikeComponent.vue'

const activeConfigurationTab = ref('components')
</script>
