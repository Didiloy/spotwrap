import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useSearchBar = defineStore('searchbar', () => {
  const search = ref('')
  return { search }
})

export const useSearchResults = defineStore('searchresults', () => {
  const search_results = ref({})
  return { search_results }
})

export const useDetail = defineStore('detail', () => {
  const detail = ref({})
  return { detail }
})

export const useShowProgressbar = defineStore('showprogressbar', () => {
  const show_progressbar = ref(false)
  return { show_progressbar }
})
