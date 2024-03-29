<template>
  <div>
    <h2>Camera Image from ROS</h2>
    <img :src="imageSrc" alt="Camera Image" width="500" height="400" />
  </div>
</template>

<script>
import ROSLIB from "roslib";

export default {
  name: "CameraImage",
  data() {
    return {
      imageSrc: "",
      ros: null,
    };
  },
  mounted() {
    this.connectToRos();
  },
  methods: {
    connectToRos() {
      this.ros = new ROSLIB.Ros({
        url: "ws://localhost:9090",
      });

      this.ros.on("connection", () => {
        console.log("Connected to ROS.");
        this.subscribeToCameraTopic();
      });

      this.ros.on("error", (error) => {
        console.error("Error connecting to ROS:", error);
      });

      this.ros.on("close", () => {
        console.log("Connection to ROS closed.");
      });
    },
    subscribeToCameraTopic() {
      const listener = new ROSLIB.Topic({
        ros: this.ros,
        name: "/image_jpeg/compressed",
        messageType: "sensor_msgs/CompressedImage",
      });

      listener.subscribe((message) => {
        this.imageSrc = `data:image/jpeg;base64,${message.data}`;
      });
    },
  },
};
</script>

<style scoped></style>
