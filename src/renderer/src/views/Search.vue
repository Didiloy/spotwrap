<template>
  <div class="s-container">
    <div class="result-row">
      <h3>Tracks</h3>
      <Carousel
        :value="search_results.tracks.items"
        class="carousel"
        :responsive-options="responsiveOptions"
      >
        <template #item="slotProps">
          <div class="carousel-item">
            <img :src="slotProps.data.album.images[0].url" class="carousel-image" />
            <div
              style="
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
                max-width: 250px;
                height: 50px;
              "
            >
              <span>{{ slotProps.data.name }} - {{ slotProps.data.artists[0].name }}</span>
            </div>
            <Button label="details" class="carousel-button" @click="goToDetails(slotProps.data)" />
          </div>
        </template>
      </Carousel>
    </div>
    <div class="result-row">
      <h3>Albums</h3>
      <Carousel
        :value="search_results.albums.items"
        class="carousel"
        :responsive-options="responsiveOptions"
      >
        <template #item="slotProps">
          <div class="carousel-item">
            <img :src="slotProps.data?.images[0]?.url" class="carousel-image" />
            <div
              style="
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
                max-width: 250px;
                height: 50px;
              "
            >
              <span
                >{{ slotProps.data?.name ? slotProps.data.name : '' }} -
                {{ slotProps.data?.artists[0].name ? slotProps.data.artists[0].name : '' }}</span
              >
            </div>
            <Button label="details" class="carousel-button" @click="goToDetails(slotProps.data)" />
          </div>
        </template>
      </Carousel>
    </div>
    <div class="result-row">
      <h3>Artists</h3>
      <Carousel
        :value="search_results.artists.items"
        class="carousel"
        :responsive-options="responsiveOptions"
      >
        <template #item="slotProps">
          <div class="carousel-item">
            <img :src="slotProps.data.images[0]?.url" class="carousel-image" />
            <div
              style="
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
                max-width: 250px;
                height: 50px;
              "
            >
              <span>{{ slotProps.data.name }}</span>
            </div>
            <Button label="details" class="carousel-button" @click="goToDetails(slotProps.data)" />
          </div>
        </template>
      </Carousel>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useSearchResults, useDetail, useShowProgressbar } from '../store/searchBar'
import { storeToRefs } from 'pinia'
const router = useRouter()

const { search_results } = storeToRefs(useSearchResults())
const { detail } = storeToRefs(useDetail())
const { show_progressbar } = storeToRefs(useShowProgressbar())

function goToDetails(data) {
  show_progressbar.value = true
  detail.value = data
  router.push({
    name: 'detail'
  })
}

const responsiveOptions = ref([
  {
    breakpoint: '3000px',
    numVisible: 5,
    numScroll: 1
  },
  {
    breakpoint: '1500px',
    numVisible: 4,
    numScroll: 1
  },
  {
    breakpoint: '1100px',
    numVisible: 3,
    numScroll: 1
  },
  {
    breakpoint: '880px',
    numVisible: 2,
    numScroll: 1
  },
  {
    breakpoint: '575px',
    numVisible: 2,
    numScroll: 1
  }
])
</script>
<style scoped>
.s-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.result-row {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  width: 100%;
  height: 100%;
}

.carousel {
  width: 100%;
}

.carousel-image {
  border-radius: 15px;
  width: 250px;
  height: 210px;
}

.carousel-item {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: 250px;
  height: 250px;
  border-radius: 10px;
}

.p-button {
  width: 100%;
}
</style>
