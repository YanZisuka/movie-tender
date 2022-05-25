<template>
  <div>
    <h1>COMMUNITY</h1>
    <search-bar></search-bar>
    <h4>Latest Reviews</h4>
    <ul>
      <review-card v-for="review in reviews" :key="review.id" :review="review">
      </review-card>
    </ul>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import ReviewCard from '@/components/ReviewCard.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
  name : 'ReviewList',
  components : { SearchBar, ReviewCard },
  computed : {
    ...mapGetters(['reviews',])
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

</style>