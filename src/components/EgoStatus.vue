<template>
  <div class="p-3">
    <h2>실시간 차량 정보</h2>
    <div id="chart" style="width: 100%; height: 300px; margin-bottom: 30px"></div>
    <p>
      속력 (km/h): <span>{{ velocity }}</span>
    </p>
    <p>
      액셀 (%): <span>{{ accel }}</span>
    </p>
    <p>
      브레이크 (%): <span>{{ brake }}</span>
    </p>
    <p>
      X 좌표 (UTM): <span>{{ positionX }}</span>
    </p>
    <p>
      Y 좌표 (UTM): <span>{{ positionY }}</span>
    </p>
  </div>
</template>

<script>
import ROSLIB from "roslib";
import Dygraph from "dygraphs";

export default {
  name: "EgoStatus",
  data() {
    return {
      accel: 0,
      brake: 0,
      positionX: 0,
      positionY: 0,
      velocity: 0,
      ros: null,
      graph: null,
      data: [],
    };
  },
  mounted() {
    this.connectToRos();
    this.initializeGraph();
  },

  methods: {
    connectToRos() {
      this.ros = new ROSLIB.Ros({
        url: "ws://localhost:9090",
      });

      this.ros.on("connection", () => {
        console.log("Connected to ROS.");
        this.subscribeToEgoStatusTopic();
      });

      this.ros.on("error", (error) => {
        console.error("Error connecting to ROS:", error);
      });

      this.ros.on("close", () => {
        console.log("Connection to ROS closed.");
      });
    },
    subscribeToEgoStatusTopic() {
      const listener = new ROSLIB.Topic({
        ros: this.ros,
        name: "/Ego_topic",
        messageType: "morai_msgs/EgoVehicleStatus",
      });

      listener.subscribe((message) => {
        this.accel = (message.accel * 100).toFixed(2);
        this.brake = (message.brake * 100).toFixed(2);
        this.positionX = message.position.x.toFixed(2);
        this.positionY = message.position.y.toFixed(2);
        let velocity = message.velocity.x;
        if (velocity < 0) {
          velocity = 0;
        }
        this.velocity = (velocity * 3.6).toFixed(2); // m/s to km/h
        // Update Dygraphs data array
        this.data.push([
          new Date(),
          parseFloat(this.accel),
          parseFloat(this.brake),
          parseFloat(this.velocity),
        ]);
        this.graph.updateOptions({ file: this.data });
      });
    },
    initializeGraph() {
      this.graph = new Dygraph(document.getElementById("chart"), this.data, {
        labels: ["Time", "Accel", "Brake", "Velocity"],
        // Include additional Dygraphs options here
      });
    },
  },
};
</script>

<style scoped>
p {
  font-family: GoryeongStrawberry;
  font-style: normal;
  font-weight: normal;
}

h2 {
  font-family: GoryeongStrawberry;
  font-style: normal;
  font-weight: normal;
}
</style>
