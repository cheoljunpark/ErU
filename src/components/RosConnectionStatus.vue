<template>
  <div>
    <p>
      차량번호(51사 3429): <span :style="statusStyle">{{ status }}</span>
    </p>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import ROSLIB from "roslib";

export default {
  setup() {
    const status = ref("Disconnected");
    const statusStyle = ref("");

    onMounted(() => {
      const ros = new ROSLIB.Ros({
        url: "ws://localhost:9090",
      });

      ros.on("connection", () => {
        status.value = "연결 성공";
        statusStyle.value = "font-size: x-large; color: green;";
      });

      ros.on("error", (error) => {
        status.value = "연결 에러";
        statusStyle.value = "font-size: x-large; color: red;";
        console.error("ROS 연결 에러:", error);
      });

      ros.on("close", () => {
        status.value = "연결 취소";
        statusStyle.value = "font-size: x-large; color: orange;";
      });
    });

    return { status, statusStyle };
  },
};
</script>

<style>
p {
  font-family: GoryeongStrawberry;
  font-style: normal;
  font-weight: normal;
}
</style>
