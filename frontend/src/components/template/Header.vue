<template>
  <nav class="navbar navbar-expand-md bg-light-subtle rounded">
    <div class="container-fluid">
      <span class="navbar-brand">Template</span>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#bikeType"
        aria-controls="bikeType" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="bikeType">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">{{ $t("message.components") }}</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">{{ $t("message.accessories") }}</a>
          </li>
        </ul>
      </div>
      <div class="col-md-6 text-end">
        <button type="button" class="btn btn-sm btn-outline-secondary" data-bs-toggle="modal"
          data-bs-target="#AddAssemblyGroup" data-toggle="tooltip" data-placement="bottom" :title="$t('message.subheader-             add')"
          :aria-label="$t('message.subheader-add')">{{
            $t('message.subheader-add') }}</button>
      </div>
    </div>
  </nav>
</template>
