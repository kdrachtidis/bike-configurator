<template>
    <div class="locale-changer me-2">
        <select class="form-select form-select-l" aria-label="Select Language" v-model="$i18n.locale" data-toggle="tooltip" data-placement="bottom" :title="$t('message.header-language')">
            <option v-for="locale in $i18n.availableLocales" :key="`locale-${locale}`" :value="locale">{{ locale }}
            </option>
        </select>
    </div>
</template>
