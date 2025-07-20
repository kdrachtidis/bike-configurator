<script setup>
const props = defineProps({
    Product: String,
    Category: String
})
</script>

<template>
    <li class="list-group-item justify-content-between bg-dark-subtle">
        <div class="row">
            <div class="col-10"><a href="#" class="link-light link-underline-secondary link-offset-1">{{ Product ||
                "Product empty" }}</a></div>
            <div class="col-2 text-end"> <button type="button" class="btn btn-sm btn-outline-light"
                    aria-label="Editieren"><i class="bi bi-pencil"></i></button></div>
        </div>
        <div class="row">
            <div class="col-9 text-body-tertiary">{{ Category || "Category empty" }}</div>
            <div class="col-3 text-end text-body-tertiary">150,00€</div>
        </div>

    </li>
</template>