<template>
  <div v-if="isMyReview">
    <h1>Edit Review</h1>
    <review-form
      :review="review"
      action="update"
      ></review-form>
  </div>
</template>

<script>
import ReviewForm from '@/components/ReviewForm.vue'

import { mapGetters, mapActions } from 'vuex'

export default {
  name : 'ReviewEditView',

  components : {
    ReviewForm,
  },

  computed : {
    ...mapGetters(['review', 'movie']),
    isMyReview() {
      return this.review.id === this.$route.params.reviewPk
    }
  },

  methods: {
    ...mapActions(['fetchReview', 'fetchMovie']),
  },

  created() {
    this.fetchReview(this.$route.params.reviewPk)
  },
}
</script>

<style>

</style>