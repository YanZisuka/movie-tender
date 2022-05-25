<template>
  <div>
    <router-link class="text-decoration-none" :to="{ name: 'reviewDetail', params: { reviewPk: review.id } }">
      <div class="review-item d-flex flex-row align-items-center my-5">
        <div>
          <img class="review-item-poster" :src="posterPath" :alt="`${review.movie.title}'s poster`">
        </div>
        <div class="text-start text-black ms-5">
          <h2 class="review-item-author">{{ review.user.nickname }}</h2>
          <h1 class="review-item-title">{{ review.movie.title }}</h1>
          <div class="like-meter d-flex justify-content-evenly align-items-center">
            <i class="text-white me-3 fa-solid fa-heart"></i>
            <span>{{ review.like_users.length }}</span>
          </div>
          <p class="review-item-text ellipsis pe-5">{{ review.content }}</p>
        </div>
      </div>
    </router-link>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: "ReviewCard",

  props: {
    review : Object,
  },

  data() {
    return {
      reviewPk : this.review.id,
      }
  },

  computed: {
    posterPath(){
      return this.review.movie.poster_path
    },
    ...mapGetters(['isAuthor', 'isReview'])
  },

  methods: {
    ...mapActions(['fetchReview'])
  },

  created() {
  }
}
</script>

<style>
.review-item {
  background-color: #fbfbfb;
  border-radius: 0.5rem;
  box-shadow: 5px 4px 4px rgba(0, 0, 0, 0.25);
  width: 100%;
}

.like-meter {
  border: 1px solid #cf1224;
  background: linear-gradient(90deg, #cf1224 50%, #fff 50%);
  border-radius: 0.25rem;
  color: #cf1224;
  width: 5rem;
  height: 2rem;
  margin-bottom: 1rem;
}

.like-meter span {
  font-weight: 800;
}

.review-item:hover {
  background-color: #eee;
}

.review-item-poster {
  width: 12rem;
  border-radius: 0.5rem;
}

.review-item-text {
  font-size: 1rem;
  font-weight: 500;
  line-height: 26px;
}

.review-item-title {
  font-size: 2.5rem;
  font-weight: 700;
}

.review-item-author {
  font-size: 22px;
  font-weight: 700;
  color: #c4c4c4;
}

.ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
</style>