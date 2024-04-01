<template>
  <HomeView />
</template>

<script>
import HomeView from "./HomeView.vue";
import "bootstrap/dist/css/bootstrap.css";

export default {
  name: "App",
  components: {
    HomeView,
  },
};
</script>

<style scoped>
@font-face {
  font-family: "GoryeongStrawberry";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/GoryeongStrawberry.woff2")
    format("woff2");
  font-weight: bold;
  font-size: large;
  font-style: normal;
}
</style>
