<template>
  <div>
    <h2>topic: /Ego_status</h2>
    <p>
      Accel (%): <span>{{ accel }}</span>
    </p>
    <!-- 나머지 데이터 항목들 -->
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import ROSLIB from "roslib";

export default {
  setup() {
    const accel = ref(0);
    // 나머지 데이터 항목들의 ref 정의

    onMounted(() => {
      const ros = new ROSLIB.Ros({
        url: "ws://localhost:9090",
      });

      const EgoTopicListener = new ROSLIB.Topic({
        ros: ros,
        name: "/Ego_topic",
        messageType: "morai_msgs/EgoVehicleStatus",
      });

      EgoTopicListener.subscribe((data) => {
        accel.value = data.accel * 100;
        // 나머지 데이터 업데이트
      });
    });

    return { accel /* 나머지 데이터 반환 */ };
  },
};
</script>
