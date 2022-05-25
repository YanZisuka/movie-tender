<template>
  <div>
    <h2>reviewDetail</h2>

    <h3>content : {{review.content}}</h3>
    <div v-if="isAuthor">
      <router-link :to="{ name : 'reviewEdit', params : {reviewPk} }">
      <button>Edit</button>
      </router-link>

      <button @click="deleteReview(reviewPk)">Delete</button>
    </div>
    <div>
      Likeit:
      <button @click="likeReview(reviewPk)">
        {{ likeCount }}
      </button>
    </div>
    <!-- <comment-list></comment-list> -->
    <comment-list :comments="review.comment_set"></comment-list>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'

  export default {
    components : { CommentList }, 
    name : 'ReviewDetail',
    data(){
      return {
        reviewPk : this.$route.params.reviewPk,
      }
    },
    computed: {
        ...mapGetters(['isAuthor', 'review', 'likeCount']),
      // likeCount(){
      //   return this.likeCount?.like_users_count 
      // },
    },
    methods: {
      ...mapActions([
        'fetchReview',
        'likeReview',
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