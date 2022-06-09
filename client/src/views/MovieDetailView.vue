<template>
  <div v-if="isMovie" class="row justify-content-center align-items-center p-5">
    <div class="col-12 col-lg-6 text-start mb-5">
      <h1 class="movie-title">{{ movieDetail.title }}</h1>
      <h2 class="movie-subtitle">{{ releaseDate }} | {{ genres }} | {{ runtime }}</h2>
      <button v-if="isProvider" class="provider-btn d-flex justify-content-start align-items-center text-white mt-3">
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
    MovieInfo,
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
    moviePk() {
      return parseInt(this.$route.params.moviePk)
    },
    isMovie() {
      return this.movieDetail.id === this.moviePk
    },
    isProfile() {
      return this.currentUser.username === this.profile.username
    },
    isProvider() {
      return this.movieDetail.providers?.length !== 0
    },
    runtime() {
      const hh = parseInt(this.movieDetail.runtime / 60)
      const mm = this.movieDetail.runtime % 60

      if (hh && mm) {
        return `${hh}시간 ${mm}분`
      } else if (hh && !mm) {
        return `${hh}시간`
      } else {
        return `${mm}분`
      }
    },
    releaseDate() {
      return `${this.movieDetail.release_date?.replaceAll('-', '/')} (KR)`
    },
    genres() {
      let st = ''
      this.movieDetail.genres?.forEach(genre => {
        st += genre + ' '
      })
      return st.trim()
    },

  },

  methods: {
    ...mapActions(['fetchCurrentUser', 'fetchProfile', 'fetchMovie',])
  },

  async created() {
    this.$emit('dark-emit')
    document.body.setAttribute('style', 'background-color: #171717;')
    await this.fetchCurrentUser()
    await this.fetchProfile(this.currentUser)
    this.fetchMovie(this.moviePk)
  },
}
</script>

<style scoped>
h1, h2 {
  color: #fff;
}

.movie-title {
  font-size: 4.5rem;
  font-weight: 700;
}

.movie-subtitle {
  font-size: 1.5rem;
  font-weight: 700;
}

.provider-btn {
  background-color: #000;
  color: #fff;
  font-size: 1rem;
  font-weight: 700;
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