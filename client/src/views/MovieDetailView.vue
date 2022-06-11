<template>
  <div v-if="isMovie" class="row justify-content-center align-items-center p-5">
    <div class="col-12 col-lg-6 text-start mb-5">
      <h1 class="movie-title">{{ movieDetail.title }}</h1>
      <h2 class="movie-subtitle">{{ releaseDate }} | {{ genres }} | {{ runtime }}</h2>
      <a :href="provider.url" target="_blank" class="text-decoration-none">
        <button v-if="isProvider" class="btn-provider d-flex justify-content-start align-items-center text-white mt-3">
          <img v-if="provider.name === 'Netflix'" :src="netflixLogo" alt="netflix-logo">
          <img v-if="provider.name === 'Disney+'" :src="disneyPlusLogo" alt="disney-plus-logo">
          <img v-if="provider.name === 'wavve'" :src="wavveLogo" alt="wavve-logo">
          <img v-if="provider.name === 'Watcha'" :src="watchaLogo" alt="watcha-logo">
          <img v-if="provider.name === 'Apple TV+'" :src="appleTvPlusLogo" alt="apple-tv-plus-logo">
          <span>
            {{ provider.name }}
          </span>
        </button>
      </a>
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
      wavveLogo: 'https://image.tmdb.org/t/p/original/2ioan5BX5L9tz4fIGU93blTeFhv.jpg',
      appleTvPlusLogo: 'https://image.tmdb.org/t/p/original/6uhKBfmtzFqOcLousHwZuzcrScK.jpg',
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
    isProvider() {
      return this.movieDetail._providers?.length !== 0
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
      this.movieDetail._genres?.forEach(genre => {
        st += genre + ' '
      })
      return st.trim()
    },
    provider() {
      if (this.isProvider) {
        const providerArray = this.movieDetail._providers[0].split('::')
        if (providerArray[0] === 'Disney Plus' || providerArray[0] === 'Apple TV Plus') {
          providerArray[0] = providerArray[0].replace(' Plus', '+')
        }
        return {
          'name': providerArray[0],
          'url': providerArray[1]
        }
      } else {
        return {}
      }
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

a {
  display: inline-block;
}

.movie-title {
  font-size: 4.5rem;
  font-weight: 700;
}

.movie-subtitle {
  font-size: 1.5rem;
  font-weight: 700;
}

.btn-provider {
  background-color: #000;
  color: #fff;
  font-size: 1rem;
  font-weight: 700;
  width: 10rem;
  height: 3.5rem;
  border-radius: 0.5rem;
}

.btn-provider > img {
  width: 3rem;
  border-radius: 16px;
}

.btn-provider > span {
  width: 100%;
}
</style>