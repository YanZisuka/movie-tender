<template>
  <div>
    <router-link
      class="text-decoration-none"
      :to="{ name: 'movie', params: { moviePk: movie.id } }"
    >
      <div class="omakase-item d-flex flex-row align-items-center mb-5">
        <div>
          <img :src="movie.poster_path" :alt="`${movie.title}'s poster`" />
        </div>
        <div class="text-start text-black ms-5">
          <h1 class="text-white">{{ movie.title }}</h1>
          <h2 class="text-white mb-4">
            <i class="fa-solid fa-star"></i> {{ rating }}
          </h2>
          <p class="lead text-white ellipsis">{{ overview }}</p>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "OmakaseItem",

  props: {
    movie: Object,
  },

  computed: {
    rating() {
      return this.movie.vote_average.toFixed(1);
    },
    overview() {
      return this.movie.overview.replaceAll("\\n", "\n");
    },
  },

  created() {},
};
</script>

<style scoped lang="scss">
.omakase-item {
  background-color: #030303;
  border: 2px solid #222;
  border-radius: 8px;
  width: 100%;
  padding: 0 3rem 0 0;

  &:hover {
    background-color: #222;
  }
  img {
    width: 13rem;
    border-radius: 4px 0 0 4px;
  }
  h1 {
    font-size: 2rem;
    font-weight: 700;
  }
  h2 {
    margin-top: 1rem;
    font-size: 1.5rem;
  }
}
</style>
