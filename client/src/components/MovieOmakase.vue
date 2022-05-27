<template>
  <div class="omakase row justify-content-center align-items-center">
    <p class="omakase-text mt-5">{{ profile.nickname }}님이 좋아하실 영화들이에요!</p>
    <router-link :to="{ name: 'movieSurvey' }">
      <button class="default-btn">다시하기</button>
    </router-link>

    <div class="col-6">
      <omakase-item
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        ></omakase-item>
    </div>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import OmakaseItem from '@/components/OmakaseItem.vue'

export default {
  name: 'MovieOmakase',

  components: {
    OmakaseItem,
  },

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

<style scoped>
  .omakase {
    margin: 3rem 5rem;
  }

.omakase-text {
  font-size: 3rem;
  font-weight: 700;
  line-height: 77px;
  color: #fff;
}
</style>