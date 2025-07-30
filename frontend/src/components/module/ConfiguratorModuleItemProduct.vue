<template>
  <div class="justify-content-between">
    <div class="row">
      <div class="col-9"><a href="#" class="link-light link-underline-secondary link-offset-1">{{ Product ||
        "Product empty" }}</a></div>
      <div class="col-3 text-end"> <button type="button" class="btn btn-sm btn-outline-light" aria-label="Editieren"><i
            class="bi bi-pencil"></i></button></div>
    </div>
    <div class="row">
      <div class="col-8 text-body-tertiary">{{ assemblygroupmodule.name || "Category empty" }}</div>
      <div class="col-4 text-end text-body-tertiary">150,00€</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  assemblygroupmodule: { type: Object, required: true },
  Category: String
})
</script>
