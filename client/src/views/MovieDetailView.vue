<template>
  <div v-if="isMovie" :style="{'background-image': `url${movieDetail.poster_path}`}" class="row justify-content-center align-items-center p-5">
    <div class="col-12 col-lg-6 text-start mb-5">
      <h1 class="movie-title text-white">{{ movieDetail.title }}</h1>
      <h2 class="movie-subtitle text-white">{{ releaseDate }} | {{ genres }} | {{ runtime }}</h2>
      <button class="provider-btn d-flex justify-content-start align-items-center text-white mt-3" v-if="movieDetail.providers[0]">
        <img v-if="movieDetail.providers[0] === 'Netflix'" :src="netflixLogo" alt="netflix-logo">
        <img v-if="movieDetail.providers[0] === 'Disney Plus'" :src="disneyPlusLogo" alt="disney-plus-logo">
        <img v-if="movieDetail.providers[0] === 'wavve'" :src="wavveLogo" alt="wavve-logo">
        <img v-if="movieDetail.providers[0] === 'Watcha'" :src="watchaLogo" alt="watcha-logo">
        <span>
          {{ movieDetail.providers[0] }}
        </span>
      </button>
    </div>

    <div class="col-12 col-lg-6">
      <movie-info
        :movieDetail="movieDetail"
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
      disneyPlusLogo: 'https://image.tmdb.org/t/p/original/7rwgEs15tFwyR9NPQ5vpzxTj19Q.jpg',
      watchaLogo: require('@/assets/watcha.png'),
      wavveLogo: require('@/assets/wavve.png'),
    }
  },

  computed: {
    ...mapGetters(['currentUser', 'profile', 'movieDetail',]),
    isMovie() {
      return this.movieDetail.id === this.$route.params.moviePk
    },
    isProfile() {
      return this.currentUser.username === this.profile.username
    },
    runtime() {
      const hh = parseInt(this.movieDetail.runtime / 60)
      if (hh) {
        return `${hh}시간 ${(this.movieDetail.runtime % 60)}분`
      } else {
        return `${(this.movieDetail.runtime % 60)}분`
      }
    },
    releaseDate() {
      return `${this.movieDetail.release_date.replaceAll('-', '/')} (KR)`
    },
    genres() {
      let st = ''
      this.movieDetail.genres.forEach(genre => {
        st += genre + ' '
      })
      return st.trim()
    },

  },

  methods: {
    ...mapActions(['fetchMovie',])
  },

  created() {
    this.fetchMovie(this.$route.params.moviePk)
  },
}
</script>

<style scoped>
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
  font-size: 1rem;
  font-weight: 600;
  width: 10rem;
  height: 3.5rem;
  border-radius: 0.5rem;
}

.provider-btn > img {
  width: 3rem;
}

.provider-btn > span {
  width: 100%;
}
</style>