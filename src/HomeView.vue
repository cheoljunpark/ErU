<template>
  <div class="container mt-3 d-flex flex-column text-center">
    <div class="card container mb-5 mt-5 shadow rounded">
      <div class="col fs-1 fw-bold">
        <RosConnectionStatus />
      </div>
    </div>
    <div class="row">
      <div class="mt-3 col-4 d-flex flex-column">
        <div class="row mb-3">
          <div class="col">
            <CameraView class="card shadow rounded p-3" />
          </div>
        </div>
        <div class="row mt-3">
          <div class="col">
            <ImuStatus class="card shadow rounded p-3" />
          </div>
        </div>
      </div>
      <div class="mt-3 col-4 shadow rounded p-3">
        <GpsStatus class="card" />
      </div>
      <div class="mt-3 col-4 d-flex flex-column">
        <EgoStatus class="card shadow rounded" />
      </div>
    </div>
  </div>
</template>

<script setup>
import RosConnectionStatus from "./components/RosConnectionStatus.vue";
import CameraView from "./components/CameraView.vue";
import ImuStatus from "./components/ImuStatus.vue";
import GpsStatus from "./components/GpsStatus.vue";
import EgoStatus from "./components/EgoStatus.vue";
</script>

<style>
/* 전체 배경에 적용할 스타일 */
body,
.main-container {
  margin: 0; /* 기본 마진 제거 */
  height: 100vh; /* 뷰포트의 높이에 맞춤 */
  background: linear-gradient(to top left, #fffffe, #daf015); /* 대각선 그라디언트 */
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}

/* 카드 스타일 */
.card {
  background: #ffffff; /* 밝은 카드 배경 */
  border-radius: 10px; /* 둥근 모서리 */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* 부드러운 그림자 */
  margin: 1rem;
  padding: 1rem;
  transition: transform 0.3s ease;
}

/* 카드 호버 효과 */
.card:hover {
  transform: translateY(-5px); /* 호버 시 약간 위로 움직임 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); /* 그림자 강조 */
}

/* 카드 내부 텍스트 스타일링 */
.card h1,
.card h2,
.card h3,
.card p {
  color: #333; /* 짙은 글자색 */
  margin: 0.5rem 0;
}

/* 카드 내부 요소 (예: 버튼, 입력필드 등) */
.card .button {
  background-color: #ff758c; /* 버튼 배경색 */
  color: #ffffff; /* 버튼 글자색 */
  border: none;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.card .button:hover {
  background-color: #f06478; /* 호버 시 버튼색 변경 */
}

/* 세부 구조에 맞는 CSS 클래스를 추가하거나 조정해야 할 수도 있습니다. */
</style>
