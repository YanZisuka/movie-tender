<template>
  <div>
    <router-link class="text-decoration-none" :to="{ name: 'movie', params: { moviePk: movie.id } }">
      <div class="movie-item d-flex flex-row align-items-center my-5">
        <div>
          <img class="movie-item-poster" :src="movie.poster_path" :alt="`${movie.title}'s poster`">
        </div>
        <div class="text-start text-black ms-5">
          <h1 class="text-white">{{ movie.title }}</h1>
          <h2 class="text-white"><i class="fa-solid fa-star"></i> {{ movie.vote_average }}</h2>
          <p class="movie-item-text text-white ellipsis pe-5">{{ movie.overview }}</p>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'OmakaseItem',

  props: {
    movie: Object,
  },

  computed: {
  },

  methods: {},

  created() {},
}
</script>

<style scoped>
.movie-item {
  background-color: #030303;
  border-radius: 0.5rem;
  box-shadow: 5px 4px 4px rgba(0, 0, 0, 0.25);
  width: 100%;
}

.movie-item:hover {
  background-color: #222;
}

.movie-item-poster {
  width: 12rem;
  border-radius: 0.5rem;
}

.movie-item-text {
  font-size: 1rem;
  font-weight: 500;
  line-height: 26px;
}

.ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>