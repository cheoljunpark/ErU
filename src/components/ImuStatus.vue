<template>
  <div>
    <h2>IMU Data</h2>
    <div>
      <h4>3축에 대한 선형 가속도</h4>
      <p>
        linear_acceleration_x: <span>{{ imuData.linear_acceleration.x }}</span>
      </p>
      <p>
        linear_acceleration_y: <span>{{ imuData.linear_acceleration.y }}</span>
      </p>
      <p>
        linear_acceleration_z: <span>{{ imuData.linear_acceleration.z }}</span>
      </p>
    </div>
    <div>
      <h4>Quaternion 벡터(x,y,z) 스칼라(w)</h4>
      <p>
        vector_x: <span>{{ imuData.orientation.x }}</span>
      </p>
      <p>
        vector_y: <span>{{ imuData.orientation.y }}</span>
      </p>
      <p>
        vector_z: <span>{{ imuData.orientation.z }}</span>
      </p>
      <p>
        scalar_w: <span>{{ imuData.orientation.w }}</span>
      </p>
    </div>
  </div>
</template>

<script>
import ROSLIB from "roslib";

export default {
  name: "ImuData",
  data() {
    return {
      ros: null,
      imuData: {
        linear_acceleration: { x: 0, y: 0, z: 0 },
        orientation: { x: 0, y: 0, z: 0, w: 0 },
      },
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
        this.subscribeToImuTopic();
      });

      this.ros.on("error", (error) => {
        console.error("Error connecting to ROS:", error);
      });

      this.ros.on("close", () => {
        console.log("Connection to ROS closed.");
      });
    },
    subscribeToImuTopic() {
      const imuTopic = new ROSLIB.Topic({
        ros: this.ros,
        name: "/imu",
        messageType: "sensor_msgs/Imu",
      });

      imuTopic.subscribe((message) => {
        this.imuData = message;
      });
    },
  },
};
</script>

<style scoped></style>
