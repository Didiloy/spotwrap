<script setup>
import { useConnected } from '../store/connected.js'
import { storeToRefs } from 'pinia'
import logo from '../assets/icon.png'
const { is_connected } = storeToRefs(useConnected())

function connectHandle() {
  useConnected().connect()
}
</script>

<template>
  <div class="h-container">
    <img :src="logo" class="logo" />
    <Button
      :label="is_connected ? 'Connected' : 'Retry to connect'"
      icon="pi pi-refresh"
      :disabled="is_connected"
      @click="connectHandle"
    />
  </div>
</template>
<style scoped>
.h-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: calc(100vh - 100px);
}

.logo {
  width: 200px;
  height: 200px;
  margin-bottom: 50px;
}
</style>
