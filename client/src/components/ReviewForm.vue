<template>

<form v-if="isReview" @submit.prevent="onSubmit">
  <div>
    <input
      v-model="newReview.content"
      type="text"
      id="content" />
  </div>
  <div>
    <button class="btn"><i class="fa-solid fa-pen-to-square"></i></button>
  </div>
</form>

</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ReviewForm',

  props: {
    review: Object,
    movie: Object,
    action: String,
  },

  computed: {
    isReview() {
      return this.review.id === this.$route.params.reviewPk
    },
    newReview() {
      return {
        movie: this.movie?.id || this.review.movie.id,
        content: this.review.content
      }
    },
  },

  methods : {
    ...mapActions(['createReview', 'updateReview']),

    onSubmit(){
      if (this.action === 'create') {
        this.createReview(this.newReview)
      } else if (this.action === 'update') {
        const payload = {
          reviewPk: this.review.id,
          ...this.newReview,
        }
        this.updateReview(payload)
      }
    },
  },
}
</script>

<style>

</style>