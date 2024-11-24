import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useConnected = defineStore('connected', () => {
  const is_connected = ref(false)
  const time_left = ref(0)
  const try_connect = ref(false)

  function connect() {
    window.electron.ipcRenderer.send('get-token')
    try_connect.value = true
  }

  window.electron.ipcRenderer.on('get-token', (event, args) => {
    is_connected.value = args
    try_connect.value = false
    if (is_connected.value) {
      time_left.value = 3600
      setInterval(() => {
        time_left.value -= 60
        if (time_left.value <= 0) {
          is_connected.value = false
        }
      }, 1000 * 60) //30 seconds
    }
  })
  return { is_connected, time_left, connect, try_connect }
})
