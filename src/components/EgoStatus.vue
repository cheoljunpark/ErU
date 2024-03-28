<template>
  <div>
    <h2>Ego Vehicle Status</h2>
    <p>Accel (%): <span>{{ accel }}</span></p>
    <p>Brake (%): <span>{{ brake }}</span></p>
    <p>Position X (UTM): <span>{{ positionX }}</span></p>
    <p>Position Y (UTM): <span>{{ positionY }}</span></p>
    <p>Velocity (km/h): <span>{{ velocity }}</span></p>
  </div>
</template>

<script>
import ROSLIB from 'roslib';

export default {
  name: 'EgoStatus',
  data() {
    return {
      accel: 0,
      brake: 0,
      positionX: 0,
      positionY: 0,
      velocity: 0,
      ros: null,
    };
  },
  mounted() {
    this.connectToRos();
  },
  methods: {
    connectToRos() {
      this.ros = new ROSLIB.Ros({
        url: 'ws://localhost:9090'
      });

      this.ros.on('connection', () => {
        console.log('Connected to ROS.');
        this.subscribeToEgoStatusTopic();
      });

      this.ros.on('error', (error) => {
        console.error('Error connecting to ROS:', error);
      });

      this.ros.on('close', () => {
        console.log('Connection to ROS closed.');
      });
    },
    subscribeToEgoStatusTopic() {
      const listener = new ROSLIB.Topic({
        ros: this.ros,
        name: '/Ego_topic',
        messageType: 'morai_msgs/EgoVehicleStatus'
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
      });
    }
  }
};
</script>

<style scoped>
</style>
