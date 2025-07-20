<script setup>
import groupmodulesData from '../../assets/groupmodules.json'

import ConfiguratorModuleHeader from './ConfiguratorModuleHeader.vue'
import ConfiguratorModuleFooter from './ConfiguratorModuleFooter.vue'
import ConfiguratorModuleSubHeader from './ConfiguratorModuleSubHeader.vue'
import ConfiguratorModuleItemCategory from './ConfiguratorModuleItemCategory.vue'
import ConfiguratorModuleItemProduct from './ConfiguratorModuleItemProduct.vue'

const groupmodules = groupmodulesData

const props = defineProps({
    ModuleId: String,
    ModuleGroup: String,
    ModuleItemCount: Number,
    ModuleSum: String
})
</script>

<template>
    <section class="card border-secondary mb-3">
        <ConfiguratorModuleHeader :Id="'#' + ModuleId" :Group="ModuleGroup" />
        <ConfiguratorModuleSubHeader :ItemCount="ModuleItemCount" />
        <div class="collapse show" :id="ModuleId">
            <div class="card-body p-0 overflow-auto" style="height: 300px;">
                <ul v-for="groupmodule in groupmodules" class="list-group list-group-flush">
                    <ConfiguratorModuleItemCategory :Category="groupmodule.name" />
                </ul>
            </div>
        </div>
        <ConfiguratorModuleFooter :Sum="ModuleSum" />
    </section>
</template>