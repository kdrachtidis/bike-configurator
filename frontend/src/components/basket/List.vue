<template>
  <section class="card border-secondary mb-3">
    <ConfiguratorProductListHeader :grouped="groupedView" @toggle-view="toggleView" />
    <div v-if="assignedProducts.length === 0" class="card-body text-secondary">
      {{ $t('message.productlist-empty') }}
    </div>
    <template v-else-if="groupedView">
      <ConfiguratorProductListGroup
        v-for="group in productsBySource"
        :key="group.source"
        :source="group.source"
        :products="group.products"
      />
    </template>
    <ul v-else class="list-group list-group-flush">
      <li class="list-group-item bg-dark-subtle">
        <ConfiguratorProductListItem
          v-for="entry in assignedProducts"
          :key="`${entry.part.id}-${entry.product.id}`"
          :bikeproduct="entry.product"
          :part="entry.part"
          show-source
        />
      </li>
    </ul>
  </section>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useBikeComponentStore } from '@/stores/bikecomponent'
import { useBikePartStore } from '@/stores/bikepart'
import { useBikeProductStore } from '@/stores/bikeproduct'
import { useAccessoryStore } from '@/stores/accessory'
import ConfiguratorProductListHeader from './ListHeader.vue'
import ConfiguratorProductListGroup from './ListGroup.vue'
import ConfiguratorProductListItem from './ListItem.vue'

defineOptions({ name: 'ConfiguratorProductList' })

const bikeComponentStore = useBikeComponentStore()
const bikePartStore = useBikePartStore()
const bikeProductStore = useBikeProductStore()
const accessoryStore = useAccessoryStore()

const groupedView = ref(true)

const assignedProducts = computed(() =>
  [
    ...bikeComponentStore.bikecomponents.flatMap((component) =>
      bikePartStore
        .getBikePartsForComponent(component.id)
        .flatMap((part) =>
          bikeProductStore.getBikeProductsForPart(part.id).map((product) => ({ product, part })),
        ),
    ),
    ...accessoryStore.categories.flatMap((category) =>
      accessoryStore
        .getTypesForCategory(category.id)
        .flatMap((type) =>
          accessoryStore.getProductsForType(type.id).map((product) => ({ product, part: type })),
        ),
    ),
  ],
)

const productsBySource = computed(() => {
  const groups = new Map()

  for (const entry of assignedProducts.value) {
    const source =
      typeof entry.product.source === 'string' && entry.product.source.trim()
        ? entry.product.source.trim()
        : 'Unknown'
    const group = groups.get(source) || []
    group.push(entry)
    groups.set(source, group)
  }

  return Array.from(groups, ([source, products]) => ({ source, products }))
})

const toggleView = () => {
  groupedView.value = !groupedView.value
}
</script>
