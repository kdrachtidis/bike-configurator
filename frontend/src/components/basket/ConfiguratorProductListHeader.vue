<template>
    <header>
        <div class="card-header d-flex justify-content-between bg-body-secondary">
            <h3 class="card-title mb-0 fs-4 fw-light">{{ $t("message.productlist") }}
            </h3>
            <div>
                <button type="button" class="btn btn-sm btn-outline-secondary" :aria-label="$t('message.filter')">{{ $t("message.filter") }}</button>
            </div>
        </div>
    </header>
</template>