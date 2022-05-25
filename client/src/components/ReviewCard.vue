<template>
  <div>
    <div class="card">
      <div class="card-body">
        <img :src="posterPath" class="card-img-top h-50" alt="POSTER" align="left">
        <router-link :to="{ name: 'reviewDetail', params: { reviewPk} }" class="text-deco" >
          <h4>{{ review.user.username }}</h4>
          <h2>{{ review.movie.title }}</h2>
          <!-- <span>{{ likeCount }}</span> -->
          <h5>{{ review.content }}</h5>
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: "ReviewCard",
  props: {
    review : Object,
  },
  data(){
    return {
      reviewPk : this.review.id,
      }
    },
  computed : {
    posterPath(){
      return this.review.movie.poster_path
    },
    ...mapGetters(['isAuthor', 'isReview'])
  },
  methods : {
    ...mapActions(['fetchReview'])
  },
  created(){
    this.fetchReview(this.reviewPk)
  }
}
</script>

<style>
.card-img-top {
    width: 10%;
    height: 15vw;
    object-fit: cover;
}
.text-deco {
  text-decoration: none;
  color: black;
}
</style>