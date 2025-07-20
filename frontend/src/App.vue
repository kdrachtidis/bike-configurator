<script setup>
import groupData from './assets/groups.json';
import AppHeader from './components/ui/AppHeader.vue';
import ConfiguratorHeader from './components/ui/ConfiguratorHeader.vue';
import ConfiguratorProductList from './components/basket/ConfiguratorProductList.vue';
import ConfiguratorModule from './components/module/ConfiguratorModule.vue';

const ModuleItemCount = 10
const ModuleSum = "150,00 €"
const groups = groupData
</script>

<template>
  <AppHeader />
  <main class="container-fluid">
    <div class="row mt-3">
      <div class="col">
        <ConfiguratorHeader />
        <div class="container">
          <div class="row mt-3 row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 row-cols-xxl-4">
            <div v-for="group in groups">
              <ConfiguratorModule :ModuleId="group.id" :ModuleGroup="group.name" :ModuleItemCount="ModuleItemCount"
                :ModuleSum="ModuleSum" />
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-3">
        <ConfiguratorProductList />
      </div>
    </div>
  </main>
</template>

<style scoped>

</style>
