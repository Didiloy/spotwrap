<template>
  <div class="bb-container">
    <div v-if="try_connect">
      <span>Trying to connect to the Spotify api...</span>
    </div>
    <div v-else>
      <span>{{ is_connected ? 'Connected' : 'Not connected' }} to the Spotify api</span>
      <span> {{ is_connected ? '(' + time_left_in_minutes + ' minutes left)' : '' }}</span>
    </div>
    <div v-if="update_in_download !== ''">
      <span>| Downloading:</span>
      <span>{{ update_in_download }}</span>
    </div>
  </div>
</template>
<script setup>
import { useConnected } from '../store/connected.js'
import { storeToRefs } from 'pinia'
import { computed, watch, ref } from 'vue'
const { is_connected, time_left, try_connect } = storeToRefs(useConnected())

const time_left_in_minutes = computed(() => {
  const time = Math.floor(time_left.value / 60)
  return `${time}`
})

const update_in_download = ref('')

window.electron.ipcRenderer.on('update_in_download', (event, arg) => {
  update_in_download.value = arg
})
</script>
<style scoped>
.bb-container {
  width: 100%;
  height: 25px;
  background-color: white;
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 10;
  display: flex;
  justify-content: start;
  align-items: center;
  flex-direction: row;
  padding-left: 10px;
}
span {
  margin-left: 5px;
}
</style>
