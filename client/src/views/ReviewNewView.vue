<template>
  <div v-if="isMovie">

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
    isMovie() {
      return this.movieDetail.id === this.$route.params.moviePk
    },
  },

  methods: {
    ...mapActions(['fetchMovie']),
  },

  created() {
    this.fetchMovie(this.$route.params.moviePk)
  }
}
</script>

<style>

</style>