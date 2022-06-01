<template>
  <div class="d-flex flex-column align-items-center card-frame">
    <img class="movie-card-img" :src="movieCard.poster_path" alt="movie-card">
    <img class="card-shadow mt-5" :src="movieCard.poster_path" alt="card-shadow">
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieCard',

  data() {
    return {}
  },

  props: {
    movieCard: Object,
  },

  computed: {
    ...mapGetters([]),
  },

  methods: {
    ...mapActions([])
  },

  created() {
  },
}
</script>

<style scoped>
.card-frame {
  background-color: #141414;
  border-radius: 2rem;
  width: 80vh;
  height: 80vh;
  overflow: hidden;
}

.movie-card-img {
  width: 45vh;
}

.card-bg {
  position: absolute;
  background-color: #2d2d2d;
  width: 1000px;
  height: 1000px;
}

.card-shadow {
  width: 45vh;
  
  filter: blur(30px);
  transform: rotate(-180deg);
}

</style>