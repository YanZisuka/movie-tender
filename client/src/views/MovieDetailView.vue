<template>
  <div v-if="isMovie" class="row justify-content-center align-items-center p-5">
    <div class="col-6 text-start">
      <h1>{{ movie.title }}</h1>
      <h2>{{ releaseDate }} | {{ genres }} | {{ runtime }}</h2>
      <button v-if="movie.providers[0]">{{ movie.providers[0] }}</button>
    </div>

    <div class="col-6">
      <movie-info :movieDetail="movie"></movie-info>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieInfo from '@/components/MovieInfo.vue'

export default {
  name: 'MovieDetailView',

  components: {
    MovieInfo
  },

  data() {
    return {}
  },

  computed: {
    ...mapGetters(['currentUser', 'movie']),
    isMovie() {
      return this.movie.id === this.$route.params.moviePk
    },
    runtime() {
      return `${parseInt(this.movie.runtime / 60)}시간 ${(this.movie.runtime % 60)}분`
    },
    releaseDate() {
      return `${this.movie.release_date.replaceAll('-', '/')} (KR)`
    },
    genres() {
      let st = ''
      this.movie.genres.forEach(genre => {
        st += genre + '  '
      })
      return st
    },

  },

  methods: {
    ...mapActions(['fetchMovie'])
  },

  created() {
    this.fetchMovie(this.$route.params.moviePk)
  },
}
</script>

<style>

</style>