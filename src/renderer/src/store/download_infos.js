import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useDownloadInfos = defineStore('download_infos', () => {
  const path = ref('')
  const format = ref('mp3')
  const bitrate = ref('320k')
  return { path, format, bitrate }
})
