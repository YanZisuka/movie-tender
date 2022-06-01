<template>
  <div class="canvas" v-if="isMovie">

    <h1>{{ movieDetail.title }}</h1>

    <review-form
      :review="review"
      :movie="movieDetail"
      action="create"
      ></review-form>

  </div>
</template>

<script>
import ReviewForm from '@/components/ReviewForm.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ReviewNewView',

  components: { ReviewForm, },

  data() {
    return {
      review: {
        content: '',
      }
    }
  },

  computed: {
    ...mapGetters(['movieDetail']),
    moviePk() {
      return parseInt(this.$route.params.moviePk)
    },
    isMovie() {
      return this.movieDetail.id === this.moviePk
    },
  },

  methods: {
    ...mapActions(['fetchMovie']),
  },

  created() {
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style>
.canvas {
  width: 95vw;
  height: 100vh;
}
</style>