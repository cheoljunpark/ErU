<template>
  <!-- <PageHeader />
  <PageContent /> -->
  <RosConnectionStatus />
  <EgoStatus />
  <CameraView />
  <GpsStatus />
  <TrafficLightStatus />
  <ImuStatus />
</template>

<script>
// import PageHeader from "./components/PageHeader.vue";
// import PageContent from "./components/PageContent.vue";
import RosConnectionStatus from "./components/RosConnectionStatus.vue";
import EgoStatus from "./components/EgoStatus.vue";
import CameraView from './components/CameraView.vue'
import GpsStatus from './components/GpsStatus.vue'
import TrafficLightStatus from './components/TrafficLightStatus.vue';
import ImuStatus from './components/ImuStatus.vue'

export default {
  name: "App",
  components: {
    // PageHeader,
    // PageContent,
    RosConnectionStatus,
    EgoStatus,
    CameraView,
    GpsStatus,
    TrafficLightStatus,
    ImuStatus,
  },
};
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
