<template>
  <div class="sb-container">
    <div class="sb-search">
      <InputText
        v-model="value"
        type="text"
        placeholder="Search on Spotify"
        :onkeydown="keyPressedHandler"
        style="width: 70%"
      />
      <Button icon="pi pi-search" aria-label="Search" class="ml" @click="searchHandler" />
    </div>
    <div class="sb-div-progress">
      <ProgressBar
        v-if="show_progressbar"
        mode="indeterminate"
        class="sb-progress-bar"
      ></ProgressBar>
    </div>
  </div>
</template>
<script setup>
import { useSearchBar, useShowProgressbar } from '../store/searchBar'
import { storeToRefs } from 'pinia'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()

const { show_progressbar } = storeToRefs(useShowProgressbar())
const { search } = storeToRefs(useSearchBar())
const value = ref('')

function keyPressedHandler(e) {
  if (e.key === 'Enter') {
    searchHandler()
  }
}

function searchHandler() {
  if (value.value === '') {
    search.value = ''
    router.push('/')
    return
  }
  window.electron.ipcRenderer.send('search', value.value)
  search.value = value.value
  show_progressbar.value = true
}
</script>
<style scoped>
.sb-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 50px;
  position: fixed;
  top: 0;
  left: 0;
  background-color: white;
  z-index: 5;
}

.sb-search {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 40px;
}

.sb-div-progress {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 76%;
  height: 10px;
}

.sb-progress-bar {
  width: 100%;
  height: 6px;
}

.ml {
  margin-left: 20px;
}
</style>
