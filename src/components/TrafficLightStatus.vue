<template>
    <div>
        <h2>Traffic Light Status</h2>
        <p>Traffic Light Index: <span>{{ trafficLightIndex }}</span></p>
        <p>Traffic Light Type: <span>{{ trafficLightType }}</span></p>
        <p>Traffic Light Status: <span>{{ trafficLightStatus }}</span></p>
    </div>
</template>

<script>
import ROSLIB from "roslib";

export default {
    name: 'TrafficLightStatus',
    data() {
        return {
            trafficLightIndex: '',
            trafficLightType: 0,
            trafficLightStatus: 0,
            ros: null,
        };
    },
    mounted() {
        this.connectToRos();
    },
    methods: {
        connectToRos() {
            // ROS 연결 설정
            this.ros = new ROSLIB.Ros({
                url: 'ws://localhost:9090',
            });

            // 연결이 성공했을 때의 처리
            this.ros.on('connection', () => {
                console.log('Connected to ROS.');
                this.subscribeToTrafficLightStatus();
            });

            // 에러 발생 시 처리
            this.ros.on('error', (error) => {
                console.error('Error connecting to ROS:', error);
            });

            // 연결 종료 시 처리
            this.ros.on('close', () => {
                console.log('Connection to ROS closed.');
            });
        },
        subscribeToTrafficLightStatus() {
            // Traffic Light Status 메시지를 구독
            const listener = new ROSLIB.Topic({
                ros: this.ros,
                name: '/traffic_light_status',
                messageType: 'morai_msgs/GetTrafficLightStatus'
            });

            // 메시지를 받을 때의 처리
            listener.subscribe((message) => {
                this.trafficLightIndex = message.trafficLightIndex;
                this.trafficLightType = message.trafficLightType;
                this.trafficLightStatus = message.trafficLightStatus;
            });
        },
    }
};
</script>

<style scoped>
/* 여기에 필요한 CSS 스타일을 추가하세요 */
</style>