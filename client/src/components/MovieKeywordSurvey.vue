<template>
  <div class="row justify-content-center align-items-center mt-5">
    <div class="col-6 d-flex justify-content-center">
      <div @click="onClick(leftMovie)">
        <movie-card class="selection-card" :movieCard="leftMovie"></movie-card>
      </div>
    </div>
    <div class="col-6 d-flex justify-content-center">
      <div @click="onClick(rightMovie)">
        <movie-card class="selection-card" :movieCard="rightMovie"></movie-card>
      </div>
    </div>
    <p class="versus-text translate-middle">VS</p>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MovieKeywordSurvey',

  components: {
    MovieCard,
  },

  data() {
    return {
      progressCount: 0,
      selectionResult: [],
      resultToSend: [],
    }
  },

  computed: {
    ...mapGetters(['profile', 'movieCards',]),
    leftMovie() {
      return this.movieCards[this.progressCount]
    },
    rightMovie() {
      return this.movieCards[this.progressCount+1]
    },
  },

  methods: {
    ...mapActions(['setSurvey',]),
    onClick(movie) {
      this.selectionResult.push(movie)
      if (this.progressCount !== 8) {
        this.progressCount += 2
      } else {
        this.selectionResult.forEach(movie => {
          movie._keywords.forEach(kwrd => {
            this.resultToSend.push(kwrd)
          })
        })
        this.setSurvey(this.resultToSend)

        this.progressCount = 0
        this.selectionResult = []
        this.resultToSend = []
        this.$router.push({ name: 'movies' })
      }
    },
  },
}
</script>

<style>
.selection-card:hover {
  cursor: pointer;
  background: #333;
}

.versus-text {
  position: absolute;
  color: #fff;
  width: fit-content;
  top: 50%;
  left: 50%;
  font-size: 4rem;
  font-weight: 700;
}
</style>