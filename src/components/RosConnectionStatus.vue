<template>
  <div>
    <p>
      ROS_bridge Connection Status: <span :style="statusStyle">{{ status }}</span>
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
        status.value = "Connected";
        statusStyle.value = "font-size: x-large; color: green;";
      });

      ros.on("error", (error) => {
        status.value = "Error";
        statusStyle.value = "font-size: x-large; color: red;";
        console.error("ROS 연결 에러:", error);
      });

      ros.on("close", () => {
        status.value = "Closed";
        statusStyle.value = "font-size: x-large; color: orange;";
      });
    });

    return { status, statusStyle };
  },
};
</script>
