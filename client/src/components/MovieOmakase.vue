<template>
  <div class="frame">
    <router-link :to="{ name: 'movieSurvey' }">
      <button>다시하기</button>
    </router-link>
    <p class="mt-5">{{ profile.nickname }}님이 좋아하실 영화들이에요!</p>

    <omakase-item
    v-for="movie in movies"
    :key="movie.id"
    :movie="movie"
    ></omakase-item>

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

<style>
.frame {
  margin: 5rem;
}
</style>