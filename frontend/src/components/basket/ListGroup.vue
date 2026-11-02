<template>
  <div>
    <div class="card-body pt-2 pb-2 border-bottom d-flex justify-content-between bg-body">
      <h6 class="mb-0">
        {{ $t('message.shop') }} <span class="badge text-bg-secondary">{{ source }}</span>
      </h6>
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item bg-dark-subtle">
        <ConfiguratorProductListItem
          v-for="entry in products"
          :key="`${entry.part.id}-${entry.product.id}`"
          :bikeproduct="entry.product"
          :part="entry.part"
        />
      </li>
    </ul>
  </div>
</template>

<script setup>
import ConfiguratorProductListItem from './ListItem.vue'

defineProps({
  source: { type: String, required: true },
  products: { type: Array, required: true },
})
</script>
