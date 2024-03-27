<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <EgoStatus />
  <RosConnectionStatus />
  <GPSStatus />
  <IMUStatus />
  <CameraView />
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import EgoStatus from "./components/EgoStatus.vue";
import RosConnectionStatus from "./components/RosConnectionStatus.vue";
// import GPSStatus from './components/GPSStatus.vue'
// import IMUStatus from './components/IMUStatus.vue'
// import CameraView from './components/CameraView.vue'

export default {
  name: "App",
  components: {
    // HelloWorld,
    EgoStatus,
    RosConnectionStatus,
    // GPSStatus,
    // IMUStatus,
    // CameraView
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
