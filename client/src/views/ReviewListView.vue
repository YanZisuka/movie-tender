<template>
  <div v-if="isReviews" class="community row justify-content-center align-items-center">

    <div class="col-6">
      <div class="community-header d-flex flex-column align-items-start">
        <div class="mb-5">
          <search-bar></search-bar>
        </div>
        <p class="mb-2">Latest Reviews</p>
      </div>

      <review-item
        v-for="review in reviews"
        :key="review.id"
        :review="review"
        @like-emit="onLike"
        ></review-item>
    </div>

  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import ReviewItem from '@/components/ReviewItem.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
  name : 'ReviewListView',

  components : {
    SearchBar,
    ReviewItem,
  },

  computed : {
    ...mapGetters(['reviews',]),
    isReviews() {
      return !!this.reviews.length
    },
  },

  methods : {
    ...mapActions(['fetchCurrentUser', 'fetchReviews']),
    onLike(reviewPk, likeUsers) {
      const curReview = this.reviews.filter(review => {
        return review.id === reviewPk
      })[0]

      curReview.like_users = likeUsers
    },
  },

  created() {
    this.$emit('light-emit')
    document.body.setAttribute('style', 'background-color: #fafafa;')
    this.fetchCurrentUser()
    this.fetchReviews()
  }
}
</script>

<style>
.community {
  padding: 2rem 5rem;
}

.community-header p {
  font-size: 1rem;
  font-weight: 700;
  color: #c4c4c4;
}
</style>