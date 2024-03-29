<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <RosConnectionStatus />
  <EgoStatus />
  <CameraView />
  <GpsStatus />
  <ImuStatus />
</template>

<script>
import RosConnectionStatus from "./components/RosConnectionStatus.vue";
import EgoStatus from "./components/EgoStatus.vue";
import CameraView from './components/CameraView.vue'
import GpsStatus from './components/GpsStatus.vue'
import ImuStatus from './components/ImuStatus.vue'

export default {
  name: "App",
  components: {
    RosConnectionStatus,
    EgoStatus,
    CameraView,
    GpsStatus,
    ImuStatus,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
