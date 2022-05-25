<template>
  <div class="movie-info">
    <iframe
      class="movie-info-video"
      :src="`https://www.youtube.com/embed/${videoPath}`"
      frameborder="0"
      allowfullscreen
      ></iframe>

    <div class="text-start">
      <p class="mt-5 mb-3 overview-title text-white">개요</p>
      <span class="text-white">{{ movieDetail.overview }}</span>
      <hr class="mt-5 mb-3 text-white">
      <div>
        <div>
          <p class="info-title text-secondary">평균 평점</p>
          <p class="info-content text-white"><i class="fa-solid fa-star"></i> {{ movieDetail.vote_average }}</p>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieInfo',

  props: {
    movieDetail: Object,
  },

  computed: {
    videoPath() {
      const key = this.movieDetail.video_path.split('=')
      return `${key[key.length - 1]}`
    }
  },

  methods: {},
}
</script>

<style scoped>
.movie-info {
  background-color: #171717;
  border-radius: 1rem;
  padding: 2rem;
  width: 100%;
}

.movie-info-video {
  width: 100%;
  height: 60vh;
}

.overview-title {
  font-size: 2rem;
  line-height: 44px;
  font-weight: 600;
}

.info-title {
  font-size: 1rem;
  line-height: 19px;
}

.info-content {
  font-size: 2rem;
  line-height: 44px;
}
</style>