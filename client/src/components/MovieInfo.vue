<template>
  <div class="movie-info">
    
    <iframe
      class="movie-info-video"
      :src="videoPath"
      frameborder="0"
      allowfullscreen
      ></iframe>

    <div class="text-start">
      <p class="mt-5 mb-3 overview-title text-white">개요</p>
      <span class="overview-content text-white">{{ movieDetail.overview }}</span>
      <hr class="mt-5 mb-3 text-white">
      <div class="d-flex flex-row justify-content-between">
        <div>
          <p class="info-title text-secondary">평균 평점</p>
          <p class="info-content text-white"><i class="fa-solid fa-star"></i> {{ movieDetail.vote_average }}</p>
        </div>
        <div>
          <p class="info-title text-secondary">나의 평점</p>
          <p class="info-content text-secondary"><i class="fa-solid fa-star"></i> <i class="fa-solid fa-star"></i> <i class="fa-solid fa-star"></i> <i class="fa-solid fa-star"></i> <i class="fa-solid fa-star"></i></p>
        </div>
        <div>
          <p class="info-title text-secondary">출연진</p>
          <ul class="info-content text-white p-0">
            <li v-for="actor in credits" :key="actor.id">{{ actor.name }}</li>
          </ul>
        </div>
        <div>
          <p class="info-title text-secondary">리뷰쓰기</p>
          <router-link :to="{ name: 'reviewNew' }">
            <p class="info-content text-white"><i class="fa-solid fa-feather"></i></p>
          </router-link>
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
      return `https://www.youtube.com/embed/${key[key.length - 1]}`
    },
    credits() {
      return this.movieDetail.credits.filter(actor => {
        return actor.role === 'Actor' && this.movieDetail.credits.indexOf(actor) < 4
      })
    },
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

.overview-content {
  font-size: 1rem;
  font-weight: 500;
}

.info-title {
  font-size: 1rem;
  line-height: 19px;
}

.info-content {
  font-size: 2rem;
  line-height: 44px;
  list-style: none;
}

.info-content > li {
  font-size: 1rem;
  line-height: 22px;
  list-style: none;
}
</style>