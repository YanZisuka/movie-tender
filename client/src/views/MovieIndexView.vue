<template>
  <div class="row justify-content-center align-items-center mt-5">
    <div class="text-start col-6 ps-5">
      <p class="main-text m-0">무비텐더가 {{ currentUser.username }}님이</p>
      <p class="main-text m-0">좋아하실만한 영화를</p>
      <p class="main-text mt-0">추천해드릴게요!</p>
      <p class="sub-text m-0">두 개의 선택지 중 더 마음에 드는 영화를 골라주시면,</p>
      <p class="sub-text mt-0">{{ currentUser.username }}님의 취향에 맞는 영화를 추천해드려요.</p>
      <router-link :to="{ name: 'movieOmakase' }">
        <button>Start!</button>
      </router-link>
    </div>
    <movie-card-view :movieDisplayCard="movieDisplayCard"></movie-card-view>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'
import MovieCardView from '@/components/MovieCardView.vue'

export default {
  name: 'MovieIndexView',
  
  components: {
    MovieCardView
  },

  data() {
    return {
      isDark: true
    }
  },

  computed: {
    ...mapGetters(['currentUser', 'movieDisplayCard'])
  },

  methods: {
    ...mapActions(['fetchCurrentUser', 'fetchMovieDisplayCard'])
  },

  created() {
    this.fetchCurrentUser()
    this.fetchMovieDisplayCard(_.sample([82, 162]))
  },
}
</script>

<style>
.main-text {
  font-size: 3.75rem;
  font-weight: 700;
  line-height: 73px;
}

.sub-text {
  font-size: 2rem;
  font-weight: 700;
  line-height: 39px;
}
</style>