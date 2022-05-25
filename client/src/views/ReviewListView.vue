<template>
  <div v-if="isReviews" class="frame">

    <div class="community-header d-flex flex-column align-items-start">
      <div class="mb-5">
        <search-bar></search-bar>
      </div>
      <p class="mb-0">Latest Reviews</p>
    </div>

    <review-card
      v-for="review in reviews"
      :key="review.id"
      :review="review">
    </review-card>

  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import ReviewCard from '@/components/ReviewCard.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
  name : 'ReviewListView',

  components : {
    SearchBar,
    ReviewCard
  },

  computed : {
    ...mapGetters(['reviews',]),
    isReviews() {
      return !!this.reviews.length
    },
  },

  methods : {
    ...mapActions(['fetchReviews'])
  },

  created() {
    this.fetchReviews()
  }
}
</script>

<style>
.community-header p {
  font-size: 2rem;
  font-weight: 700;
  color: #c4c4c4;
}
</style>