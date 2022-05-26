<template>
  <div v-if="isMovie && isProfile" :style="{'background-image': `url${movie.poster_path}`}" class="row justify-content-center align-items-center p-5">
    <div class="col-6 text-start">
      <h1 class="movie-title text-white">{{ movie.title }}</h1>
      <h2 class="movie-subtitle text-white">{{ releaseDate }} | {{ genres }} | {{ runtime }}</h2>
      <button class="provider-btn d-flex justify-content-start align-items-center text-white mt-3" v-if="movie.providers[0]">
        <img v-if="movie.providers[0] === 'Netflix'" :src="netflixLogo" alt="netflix-logo">
        <span>
          {{ movie.providers[0] }}
        </span>
      </button>
    </div>

    <div class="col-6">
      <movie-info
        :movieDetail="movie"
        :profile="profile"
        ></movie-info>
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
    return {
      netflixLogo: 'https://image.tmdb.org/t/p/original/t2yyOv40HZeVlLjYsCsPHnWLk4W.jpg',
    }
  },

  computed: {
    ...mapGetters(['currentUser','profile', 'movie']),
    isMovie() {
      return this.movie.id === this.$route.params.moviePk
    },
    isProfile() {
      return this.currentUser.username === this.profile.username
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
    ...mapActions(['fetchProfile', 'fetchMovie'])
  },

  created() {
    this.fetchMovie(this.$route.params.moviePk)
    this.fetchProfile(this.currentUser.username)
  },
}
</script>

<style>
.movie-title {
  font-size: 4.5rem;
  font-weight: 600;
}

.movie-subtitle {
  font-size: 1.5rem;
  font-weight: 600;
}

.provider-btn {
  background-color: #000;
  color: #fff;
  font-size: 1.5rem;
  font-weight: 500;
  width: 13rem;
  height: 4rem;
  border-radius: 0.5rem;
}

.provider-btn > img {
  width: 3rem;
}

.provider-btn > span {
  width: 100%;
}
</style>