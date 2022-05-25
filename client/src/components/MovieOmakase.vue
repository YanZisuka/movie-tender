<template>
  <div>
    <p class="mt-5">{{ profile.nickname }}님이 좋아하실 영화들이에요!</p>

    <div
    v-for="movie in movies"
    :key="movie.id"
    >{{ movie.title }}</div>
    
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieOmakase',

  data() {
    return {}
  },

  computed: {
    ...mapGetters(['profile', 'movies']),
  },

  methods: {
    ...mapActions(['fetchMovies'])
  },

  created() {
    this.fetchMovies()
  },
}
</script>

<style>

</style>