<script setup>
import { onMounted, watch } from 'vue'
import SearchBar from './components/SearchBar.vue'
import BottomBar from './components/BottomBar.vue'
import { useConnected } from './store/connected.js'
import { useRouter } from 'vue-router'
import { useSearchResults, useShowProgressbar } from './store/searchBar'
import { storeToRefs } from 'pinia'

const { show_progressbar } = storeToRefs(useShowProgressbar())
const { search_results } = storeToRefs(useSearchResults())

const router = useRouter()

onMounted(() => {
  setTimeout(() => {
    useConnected().connect()
  }, 2000)
})

function goSearch() {
  router.push({ name: 'search' })
}

watch(search_results, () => {
  goSearch()
})

window.electron.ipcRenderer.on('search_result', (event, args) => {
  search_results.value = args
  show_progressbar.value = false
})
</script>
<template>
  <div class="container">
    <SearchBar />
    <RouterView class="a-content" />
    <BottomBar />
  </div>
</template>
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  width: 100%;
  height: 100%;
  padding: 10px;
  margin-bottom: 25px;
  margin-top: 40px;
}

.a-content {
  width: 100%;
  height: 100%;
}
</style>
