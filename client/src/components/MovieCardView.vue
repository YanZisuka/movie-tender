<template>
  <div class="col-6">
    <div class="d-flex flex-column align-items-center card-frame">
      <img class="movie-card" :src="isSelection ? movieSelectionCard.poster_path : movieDisplayCard.poster_path" alt="movie-card">
      <img class="card-shadow mt-5" :src="isSelection ? movieSelectionCard.poster_path : movieDisplayCard.poster_path" alt="card-shadow">
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieCardView',

  data() {
    return {}
  },

  props: {
    movieDisplayCard: Object,
    movieSelectionCard: Object,
  },

  computed: {
    ...mapGetters([]),
    isSelection() {
      return _.isEmpty(this.movieDisplayCard)
    },
  },

  methods: {
    ...mapActions([])
  },

  created() {
  },
}
</script>

<style>
.card-frame {
  background-color: #141414;
  border-radius: 2rem;
  width: 50rem;
  height: 50rem;
  overflow: hidden;
}

.movie-card {
  width: 25rem;
}

.card-bg {
  position: absolute;
  background-color: #2d2d2d;
  width: 1000px;
  height: 1000px;
}

.card-shadow {
  width: 25rem;
  
  filter: blur(30px);
  transform: rotate(-180deg);
}
</style>