<template>
  <div v-if="isCurrentUser && isMyProfile">

    <div v-if="!isSurvey" class="row justify-content-center align-items-center p-5">
      <div class="text-start col-6 ps-5">
        <p class="main-text m-0">무비텐더가 {{ profile.nickname }}님이</p>
        <p class="main-text m-0">좋아하실만한 영화를</p>
        <p class="main-text mt-0">추천해드릴게요!</p>
        <p class="sub-text m-0">두 개의 선택지 중 더 마음에 드는 영화를 골라주시면,</p>
        <p class="sub-text mt-0">{{ profile.nickname }}님의 취향에 맞는 영화를 추천해드려요.</p>
        <router-link :to="{ name: 'movieSurvey' }">
          <button class="btn-theme-lg">Start!</button>
        </router-link>
      </div>
      <div class="col-6 d-flex justify-content-center">
        <movie-card :movieCard="movieCard"></movie-card>
      </div>
    </div>

    <div v-else>
      <movie-omakase></movie-omakase>
    </div>

  </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'

import MovieCard from '@/components/MovieCard.vue'
import MovieOmakase from '@/components/MovieOmakase.vue'

export default {
  name: 'MovieIndexView',
  
  components: {
    MovieCard,
    MovieOmakase,
  },

  data() {
    return {}
  },

  computed: {
    ...mapGetters(['currentUser', 'profile', 'movieCard',]),
    isCurrentUser() {
      return !_.isEmpty(this.currentUser)
    },
    isMyProfile() {
      return this.profile.username === this.currentUser.username
    },
    isSurvey() {
      if (this.profile.survey?.length === 0) {
        return false 
      } else {
        return true
      }
    }
  },

  methods: {
    ...mapActions(['fetchCurrentUser', 'fetchProfile', 'fetchMovieCard', 'fetchMovieCards',])
  },

  async created() {
    this.$emit('dark-emit')
    document.body.setAttribute('style', 'background-color: #171717;')
    this.fetchMovieCards(10)
    this.fetchMovieCard()
    await this.fetchCurrentUser()
    await this.fetchProfile(this.currentUser)
  },
}
</script>

<style scoped>
.main-text {
  font-size: 3.75rem;
  font-weight: 700;
  letter-spacing: -0.125rem;
  line-height: 73px;
  color: var(--white);
}

.sub-text {
  font-size: 2rem;
  line-height: 39px;
  letter-spacing: -0.125rem;
  color: var(--white);
}
</style>