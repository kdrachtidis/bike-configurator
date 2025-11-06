<script setup>
const props = defineProps({
    Product: String,
    Category: String
})
</script>

<template>
    <li class="list-group-item d-flex justify-content-between">
        <div>
            <p class="card-text lh-sm mb-1">{{ Product || "Product empty" }}
            </p>
            <p class="card-text text-secondary">{{ Category || "Category empty" }}</p>
        </div>
        <!--<div class="mt-2">
            <button type="button" class="btn btn-sm btn-outline-light" aria-label="Editieren"><i
                    class="bi bi-pencil"></i></button>
        </div>-->
    </li>
</template>