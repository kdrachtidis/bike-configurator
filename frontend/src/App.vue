<template>
  <ModalAddBikeProduct />
  <ModalEditBikeProduct />
  <ModalAddBikeComponent />
  <ModalEditBikeComponent />
  <ModalLoginUser />
  <header>
    <AppHeader />
  </header>  
  <main class="mb-3 container-fluid">
    <ConfigurationTabs v-model="activeConfigurationTab" />
    <div class="tab-content bg-body border-bottom border-start border-end rounded-bottom">
      <div id="configuration-panel-components" class="tab-pane" :class="{
        show: activeConfigurationTab === 'components',
        active: activeConfigurationTab === 'components',
      }" role="tabpanel" aria-labelledby="configuration-tab-components">
        <CardsToolbar />
        <CardsGrid />
      </div>
      <div id="configuration-panel-accessories" class="tab-pane" :class="{
        show: activeConfigurationTab === 'accessories',
        active: activeConfigurationTab === 'accessories',
      }" role="tabpanel" aria-labelledby="configuration-tab-accessories">
        <CardsToolbar />
        <ConfiguratorAccessories />
      </div>
      <div id="configuration-panel-basket" class="tab-pane" :class="{
        show: activeConfigurationTab === 'basket',
        active: activeConfigurationTab === 'basket',
      }" role="tabpanel" aria-labelledby="configuration-tab-basket">
        <ConfiguratorProductList />
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import AppHeader from './components/ui/AppHeader.vue'
import CardsToolbar from './components/ui/CardsToolbar.vue'
import CardsGrid from './components/ui/CardsGrid.vue'
import ConfigurationTabs from './components/ui/ConfigurationTabs.vue'
import ConfiguratorAccessories from './components/accessories/AccessoryList.vue'
import ConfiguratorProductList from './components/basket/List.vue'
import ModalAddBikeProduct from './components/modals/ModalAddBikeProduct.vue'
import ModalEditBikeProduct from './components/modals/ModalEditBikeProduct.vue'
import ModalLoginUser from './components/modals/ModalLoginUser.vue'
import ModalAddBikeComponent from './components/modals/ModalAddBikeComponent.vue'
import ModalEditBikeComponent from './components/modals/ModalEditBikeComponent.vue'

const activeConfigurationTab = ref('components')
</script>
