<template>
    <div>
      <h2>GPS Data</h2>
      <p>Altitude: <span>{{ gpsData.altitude }}</span></p>
      <p>Latitude: <span>{{ gpsData.latitude }}</span></p>
      <p>Longitude: <span>{{ gpsData.longitude }}</span></p>
    </div>
  </template>
  
  <script>
  import ROSLIB from 'roslib';
  
  export default {
    name: 'GpsData',
    data() {
      return {
        ros: null,
        gpsData: {
          altitude: 0,
          latitude: 0,
          longitude: 0,
        },
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
          this.subscribeToGpsTopic();
        });
  
        this.ros.on('error', (error) => {
          console.error('Error connecting to ROS:', error);
        });
  
        this.ros.on('close', () => {
          console.log('Connection to ROS closed.');
        });
      },
      subscribeToGpsTopic() {
        const listener = new ROSLIB.Topic({
          ros: this.ros,
          name: '/gps',
          messageType: 'morai_msgs/GPSMessage'
        });
  
        listener.subscribe((message) => {
          this.gpsData.altitude = message.altitude;
          this.gpsData.latitude = message.latitude;
          this.gpsData.longitude = message.longitude;
        });
      }
    }
  };
  </script>
  
  <style scoped>
  </style>
  