<template>
  <div class="song-container">
    <p>{{ song.track_number }}</p>
    <p>{{ song.name }}</p>
    <p>{{ convertMsToMinutes(song.duration_ms) }}</p>
    <Button
      title="Delete song"
      severity="danger"
      icon="pi pi-trash"
      :pt="{
        root: {
          style: 'height: 80%; margin: auto'
        }
      }"
      @click="$emit('delete_song', song)"
    />
    <Button
      title="Open in Spotify"
      severity="info"
      icon="pi pi-external-link"
      :pt="{
        root: {
          style: 'height: 80%; margin: auto'
        }
      }"
      @click="openLink"
    />
    <Button
      title="Download"
      icon="pi pi-download"
      :pt="{
        root: {
          style: 'height: 80%; margin: auto'
        }
      }"
      @click="onDownloadClick"
    />
  </div>
</template>
<script setup>
const { song } = defineProps(['song'])
import { useShowProgressbar } from '../store/searchBar'
import { useDownloadInfos } from '../store/download_infos'
import { storeToRefs } from 'pinia'
const { show_progressbar } = storeToRefs(useShowProgressbar())
const { path, format, bitrate } = storeToRefs(useDownloadInfos())

defineEmits(['delete_song'])

function onDownloadClick() {
  window.electron.ipcRenderer.send('download', {
    link: song.external_urls.spotify,
    path: path.value,
    format: format.value,
    bitrate: bitrate.value,
    songs_to_delete: []
  })
  show_progressbar.value = true
}

function openLink() {
  window.electron.ipcRenderer.send('open-link', song.external_urls.spotify)
}

function convertMsToMinutes(duration_ms) {
  const minutes = Math.floor(duration_ms / 60000)
  const seconds = ((duration_ms % 60000) / 1000).toFixed(0)
  return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`
}
</script>
<style scoped>
.song-container {
  width: 100%;
  display: grid;
  grid-template-columns: 25px auto 50px 60px 60px 60px;
  border-bottom: 1px solid black;
}
</style>
