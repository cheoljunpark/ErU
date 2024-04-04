<template>
  <div>
    <h2>실시간 GPS</h2>

    <l-map
      :zoom="zoom"
      :center="currentPosition"
      style="height: 400px; width: 100%; margin-bottom: 30px"
    >
      <l-tile-layer :url="tileUrl" />
      <l-marker :lat-lng="currentPosition">
        <l-icon :icon-url="customIcon.url" :icon-size="customIcon.size"></l-icon>
      </l-marker>
    </l-map>
    <p>
      고도: <span>{{ gpsData.altitude }}</span>
    </p>
    <p>
      위도: <span>{{ gpsData.latitude }}</span>
    </p>
    <p>
      경도: <span>{{ gpsData.longitude }}</span>
    </p>
  </div>
</template>

<script>
import ROSLIB from "roslib";
import { LMap, LTileLayer, LMarker, LIcon } from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";

export default {
  name: "GpsData",
  data() {
    return {
      ros: null,
      gpsData: {
        altitude: 0,
        latitude: 0,
        longitude: 0,
      },
      zoom: 20,
      tileUrl: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      initialPosition: [124, 33],
      currentPosition: [0, 0],
      customIcon: {
        url:
          "https://img.icons8.com/emoji/48/bus-emoji.png",
        size: [38, 95],
      },
    };
  },
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon,
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
        this.subscribeToGpsTopic();
      });

      this.ros.on("error", (error) => {
        console.error("Error connecting to ROS:", error);
      });

      this.ros.on("close", () => {
        console.log("Connection to ROS closed.");
      });
    },
    subscribeToGpsTopic() {
      const listener = new ROSLIB.Topic({
        ros: this.ros,
        name: "/gps",
        messageType: "morai_msgs/GPSMessage",
      });

      listener.subscribe((message) => {
        this.gpsData.altitude = message.altitude;
        this.gpsData.latitude = message.latitude;
        this.gpsData.longitude = message.longitude;
        this.currentPosition = [message.latitude, message.longitude]; // 현재 위치 업데이트
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
/* 지도 컨테이너의 크기를 설정합니다. */
.l-map {
  height: 400px; /* 또는 부모 요소에 따라 % 단위로 */
  /* width: 100%; */
  width: 1rem;
}

/* 마커와 같은 지도 요소에 대한 추가적인 스타일링 */
.leaflet-marker-icon {
  border-radius: 50%;
  border: 2px solid #3388ff;
}

/* Leaflet 지도 컨트롤의 스타일링을 수정할 수 있습니다. */
.leaflet-control {
  background: rgba(255, 255, 255, 0.8);
  border-radius: 4px;
}

/* 확대/축소 컨트롤에 대한 스타일링 */
.leaflet-control-zoom {
  border: none;
}

/* 특정 Leaflet 컨트롤이나 패널에 대한 스타일링 */
.leaflet-control-custom {
  /* 택배 박스의 기본 모양과 색상 */
  background-color: #c96; /* 박스의 갈색 */
  border: 2px solid #963; /* 박스의 테두리 */
  border-radius: 5px; /* 박스의 모서리를 둥글게 */
  padding: 8px; /* 내부 여백 */

  /* 박스 테이프 모양 */
  position: relative; /* 테이프의 위치를 조절하기 위해 relative 설정 */
  overflow: hidden; /* 테이프가 박스를 넘어가지 않게 */
}

.leaflet-control-custom::before,
.leaflet-control-custom::after {
  /* 택배 테이프 디자인 */
  content: "";
  position: absolute;
  left: 50%;
  width: 10px; /* 테이프의 너비 */
  height: 100%; /* 박스 높이만큼 */
  background-color: #ffc; /* 테이프의 색상 */
  transform: translateX(-50%); /* 중앙 정렬 */
}

.leaflet-control-custom::after {
  /* 테이프의 광택 효과 */
  width: 5px; /* 광택 테이프는 좀 더 얇게 */
  background-color: rgba(255, 255, 255, 0.5); /* 흰색 반투명 */
  top: 10px; /* 테이프 위쪽으로 조금 올라가게 */
}
</style>
