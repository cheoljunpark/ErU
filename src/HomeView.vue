<template>
  <div class="container mt-3 d-flex flex-column text-center">
    <div class="container mb-5 mt-5 shadow rounded">
      <div class="col fs-1 fw-bold">
        <RosConnectionStatus />
      </div>
    </div>
    <div class="row">
      <div class="mt-3 col-2 d-flex flex-column">
        <div class="row mb-3">
          <div class="col">
            <CameraView class="shadow rounded p-3" />
          </div>
        </div>
        <div class="row mt-3">
          <div class="col">
            <ImuStatus class="shadow rounded p-3" />
          </div>
        </div>
      </div>
      <div class="mt-3 col-4 shadow rounded p-3">
        <GpsStatus />
      </div>
      <div class="mt-3 col-6 d-flex flex-column">
        <EgoStatus class="shadow rounded" />
      </div>
    </div>
  </div>
</template>

<script setup>
import RosConnectionStatus from "./components/RosConnectionStatus.vue";
import CameraView from "./components/CameraView.vue";
import ImuStatus from "./components/ImuStatus.vue";
import GpsStatus from "./components/GpsStatus.vue";
import EgoStatus from "./components/EgoStatus.vue";
</script>

<style scoped>
/* 다른 스타일들과 중복되는 스타일은 생략합니다. */
.camera,
.imu,
.ego-status {
  margin-bottom: 1.5rem; /* 컨텐츠 간격을 조정합니다. */
}
</style>
