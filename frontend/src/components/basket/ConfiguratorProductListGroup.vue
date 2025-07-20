<script setup>
import ConfiguratorProductListItem from './ConfiguratorProductListItem.vue';

const category = ["Adapter-Kits", "Cleats & Schuhplatten", "Fahrradkassetten", "Fahrradketten", "Fahrradkurbeln", "Innenlager", "Kettenblätter", "Kettenführungen & Bashguards", "Kleinteile", "Nabenschaltung", "Pedale", "Riemen", "Riemenscheiben", "Singlespeed", "Verschleißsets"]
const product = ["SHIMANO SLX KASSETTE CS-M7000-11 11-FACH", "SHIMANO ULTEGRA KURBELGARNITUR FC-R8000 HOLLOWTECH II"]

</script>

<template>
    <div class="col">
        <div class="card-body pt-2 pb-2 border-bottom d-flex justify-content-between bg-body">
            <h6>{{ $t("message.shop") }} <span class="badge text-bg-secondary">bike-components.de</span></h6>
        </div>
        <div class="card-body p-0">
            <ul class="list-group list-group-flush">
                <ConfiguratorProductListItem :Product=product[0] :Category=category[0] />
                <ConfiguratorProductListItem :Product=product[1] :Category=category[1] />
                <ConfiguratorProductListItem :Product=product[0] :Category=category[2] />
                <ConfiguratorProductListItem :Product=product[1] :Category=category[3] />
            </ul>
        </div>
        <div class="card-body pt-2 pb-2 border-bottom d-flex justify-content-between bg-body">
            <h6>{{ $t("message.shop") }} <span class="badge text-bg-secondary">bike24.de</span></h6>
        </div>
        <div class="card-body p-0">
            <ul class="list-group list-group-flush">
                <ConfiguratorProductListItem :Product=product[0] :Category=category[0] />
                <ConfiguratorProductListItem :Product=product[1] :Category=category[1] />
                <ConfiguratorProductListItem :Product=product[0] :Category=category[2] />
                <ConfiguratorProductListItem :Product=product[1] :Category=category[3] />
            </ul>
        </div>
    </div>
</template>