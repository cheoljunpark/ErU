<template>
  <div class="out">
    <div class="headbox">
      <RosConnectionStatus />
    </div>
    <div class="container">
      <div class="unit">
        <div class="camera">
          <CameraView />
        </div>
        <div class="imu">
          <ImuStatus />
        </div>
      </div>
      <div class="map">
        <GpsStatus />
      </div>
      <div class="unit2">
        <div class="speed">
          <EgoStatus />
        </div>
        <div class="another">
          <p style height="60px;">heloo</p>
        </div>
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
.headbox {
  background-color: blue;
  height: 10%;
  width: auto;
  border-radius: 5%;
}
/* .out {
  display: grid;
  width: 100%;
} */

.container {
  display: grid;
  width: 100%;
  grid-template-columns: 30% 40% 30%;
  border-radius: 5%;
}

.unit {
  display: grid;
  height: auto;
  grid-template-rows: 1fr 1fr;
  background-color: brown;
  margin: 3%;
  border-radius: 5%;
}

.camera {
  background-color: aquamarine;
  border-radius: 5%;
  margin: 3% 3% 1.5% 3%;
}

.imu {
  background-color: beige;
  border-radius: 5%;
  margin: 1.5% 3% 3% 3%;
}

.map {
  display: grid;
  background-color: black;
  border-radius: 5%;
  margin: 3%;
}

.unit2 {
  display: grid;
  border-radius: 5%;
}

.speed {
  display: grid;
  background-color: blueviolet;
  border-radius: 5%;
  margin: 3% 3% 1.5% 3%;
}

.another {
  display: grid;
  background-color: chartreuse;
  border-radius: 5%;
  margin: 1.5% 3% 3% 3%;
}
</style>
