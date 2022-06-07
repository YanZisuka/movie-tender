<template>
  <div>
    <router-link class="text-decoration-none" :to="{ name: 'movie', params: { moviePk: movie.id } }">
      <div class="omakase-item d-flex flex-row align-items-center my-5">
        <div>
          <img :src="movie.poster_path" :alt="`${movie.title}'s poster`">
        </div>
        <div class="text-start text-black ms-5">
          <h1 class="text-white">{{ movie.title }}</h1>
          <h2 class="text-white"><i class="fa-solid fa-star"></i> {{ movie.vote_average }}</h2>
          <p class="lead text-white ellipsis pe-5">{{ overview }}</p>
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
    overview() {
      return this.movie.overview.replaceAll('\\n', '\n')
    },
  },


  created() {},
}
</script>

<style scoped>
.omakase-item {
  background-color: #030303;
  border-radius: 8px;
  box-shadow: 5px 4px 4px rgba(0, 0, 0, 0.25);
  width: 100%;
}

.omakase-item:hover {
  background-color: #222;
}

.omakase-item img {
  width: 12rem;
  border-radius: 8px 0 0 8px;
}

.omakase-item h1 {
  font-size: 2rem;
  font-weight: 700;
}

.omakase-item h2 {
  font-size: 1.5rem;
}
</style>