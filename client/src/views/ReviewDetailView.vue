<template>
  <div>
    <h2>reviewDetail</h2>
    <div class="card">
      <div class="card-body">
        <img :src="posterPath" class="card-img-top h-100" alt="POSTER" align="left">
        <h4>{{ review.user.username }}</h4>
        <h2>{{ review.movie.title }}</h2>
        <h3>{{ review.content }}</h3>

    <div v-if="isAuthor">
      <router-link :to="{ name : 'reviewEdit', params : {reviewPk} }">
      <button>Edit</button>
      </router-link>

      <button @click="deleteReview(reviewPk)">Delete</button>
    </div>
      <!-- <button @click="likeReview(reviewPk)">
        {{ likeCount }}
      </button> -->
    <comment-list :comments="review.comment_set"></comment-list>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'

  export default {
    components : { CommentList }, 
    name : 'ReviewDetailView',
    data(){
      return {
        reviewPk : this.$route.params.reviewPk,
      }
    },
    computed: {
        ...mapGetters(['isAuthor', 'review', 'likeCount']),
      posterPath(){
        return this.review.movie.poster_path
    },
      // likeCount(){
      //   return this.likeCount? this.likeCount: 0
      // },
    },
    methods: {
      ...mapActions([
        'fetchReview',
        // 'likeReview',
        'deleteReview',
      ])
    },
    created() {
      this.fetchReview(this.reviewPk)
},
}
</script>

<style>

</style>