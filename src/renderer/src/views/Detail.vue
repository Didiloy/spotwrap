<template>
  <div class="d-container">
    <div class="d-left-infos">
      <img
        v-if="detail.type == 'album' || detail.type == 'artist'"
        :src="detail.images[0].url"
        class="d-left-image"
      />
      <img
        v-else-if="detail.type == 'track'"
        :src="detail.album.images[0].url"
        class="d-left-image"
      />
      <h3 class="mt-10">
        {{ detail.name }} {{ detail.type !== 'artist' ? ' - ' + detail.artists[0].name : '' }}
      </h3>
      <p v-if="detail.type === 'album'" class="mt-10">
        <i>{{ detail.total_tracks }} tracks</i>
      </p>
      <p v-if="detail.type === 'album'" class="mt-10">
        {{ detail.release_date }}
      </p>
      <p v-else-if="detail.type === 'track'" class="mt-10">
        {{ detail.album.release_date }}
      </p>
      <div class="d-select">
        <Select v-model="format" :options="output_format" class="mt-10" />
        <Select
          v-model="bitrate"
          :options="bitrates_options"
          style="margin-top: 10px"
          class="mt-10"
        />
      </div>
      <div class="file-path">
        <span :title="path">{{ path.length > 25 ? path.slice(0, 25) + '..' : path }}</span>
        <Button
          label="Select a directory"
          class="mt-10"
          severity="info"
          @click="onSelectDirectoryClick"
        />
      </div>
      <Button
        v-if="detail.type !== 'artist'"
        label="Download all"
        style="width: 250px"
        class="mt-10"
        @click="onDownloadClick"
      />
    </div>
    <div v-if="!error" class="d-content">
      <Song
        v-for="song in individuals_songs"
        :key="song.id"
        :song="song"
        @delete_song="handleDelete"
      />
    </div>
    <div v-else class="d-content">
      <h4>{{ error_detail }}</h4>
    </div>
  </div>
</template>
<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import Song from '../components/Song.vue'
import { useDetail, useShowProgressbar } from '../store/searchBar'
import { useDownloadInfos } from '../store/download_infos'
import { storeToRefs } from 'pinia'
const { detail } = storeToRefs(useDetail())
const { show_progressbar } = storeToRefs(useShowProgressbar())
const { path, format, bitrate } = storeToRefs(useDownloadInfos())

const output_format = ['mp3', 'flac', 'm4a', 'ogg', 'opus']

const bitrates_options = ['8k', '16k', '32k', '96k', '128k', '192k', '256k', '320k']

const individuals_songs = ref([])
const song_to_delete = []

const error = ref(false)
const error_detail = ref('')

function onSelectDirectoryClick() {
  window.electron.ipcRenderer.send('select-directory')
}

window.electron.ipcRenderer.on('selected-directory', (event, args) => {
  path.value = args
})

window.electron.ipcRenderer.on('search_album_result', (event, args) => {
  error.value = args.error
  if (error.value) {
    error_detail.value = 'An error occured while searching the album. Please try again later.'
  } else {
    individuals_songs.value = args.tracks.items
  }
  show_progressbar.value = false
})

window.electron.ipcRenderer.on('search_track_result', (event, args) => {
  error.value = args.error
  if (error.value) {
    error_detail.value = 'An error occured while searching the track. Please try again later.'
  } else {
    individuals_songs.value = [args]
  }
  show_progressbar.value = false
})

window.electron.ipcRenderer.on('search_artist_result', (event, args) => {
  error.value = args.error
  if (error.value) {
    error_detail.value = 'An error occured while searching the artist. Please try again later.'
  } else {
    individuals_songs.value = args.tracks
  }
  show_progressbar.value = false
})

function handleDelete(song) {
  song_to_delete.push(song.artists[0].name + ' - ' + song.name)
  individuals_songs.value = individuals_songs.value.filter((s) => s.id !== song.id)
}

function onDownloadClick() {
  window.electron.ipcRenderer.send('download', {
    link: detail.value.external_urls.spotify,
    path: path.value,
    format: format.value,
    bitrate: bitrate.value,
    songs_to_delete: song_to_delete
  })
  show_progressbar.value = true
}

window.electron.ipcRenderer.on('update_in_download', (event, arg) => {
  if (arg === 'Done') {
    show_progressbar.value = false
  }
})

onMounted(() => {
  switch (detail.value.type) {
    case 'album':
      window.electron.ipcRenderer.send('search_album', detail.value.id)
      break
    case 'track':
      window.electron.ipcRenderer.send('search_track', detail.value.id)
      break
    case 'artist':
      window.electron.ipcRenderer.send('search_artist', detail.value.id)
      break
    default:
      break
  }
})

onUnmounted(() => {
  detail.value = {}
})
</script>
<style scoped>
.d-container {
  width: 100%;
  height: calc(100vh - 85px);
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
}

.d-left-infos {
  width: 350px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  background-color: #e0e0e0;
  border-radius: 15px;
  padding: 10px;
}

.d-left-image {
  width: 250px;
  height: 250px;
  object-fit: cover;
  border-radius: 10px;
}

.d-select {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  margin-top: 10px;
  width: 100%;
}

.file-path {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
  width: 100%;
}

.d-content {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  background-color: #e0e0e0;
  border-radius: 15px;
  padding: 10px;
  margin-left: 10px;
  overflow-y: scroll;
}

.mt-10 {
  margin-top: 10px;
}
p,
h3 {
  margin: 0;
}
</style>
