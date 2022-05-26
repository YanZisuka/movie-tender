<template>
  <div>
    <!-- <router-link class="text-decoration-none" :to="{ name: 'reviewDetail', params: { reviewPk: review.id } }"> -->
    <div @click="showModal = true" class="review-item d-flex flex-row align-items-center mb-5">
      <div>
        <img class="review-item-poster" :src="posterPath" :alt="`${review.movie.title}'s poster`">
      </div>
      <div class="text-start text-black ms-5">
        <h2 class="review-item-author">{{ review.user.nickname }}</h2>
        <h1 class="review-item-title">{{ review.movie.title }}</h1>
        <button @click="likeReview(review.id)" class="like-btn d-flex justify-content-between align-items-center px-3">
          <div class="d-flex flex-row align-items-center">
            <i class="ms-0 me-2 fa-solid fa-heart"></i>
            <p class="m-0">Like</p>
          </div>
          <span>{{ likeCount }}</span>
        </button>
        <p class="review-item-text ellipsis pe-5">{{ review.content }}</p>
      </div>
    </div>
    <!-- </router-link> -->

    <!-- use the modal component, pass in the prop -->
    <modal-detail
      :show="showModal"
      @close="showModal = false"
      >
      <div slot="body" class="d-flex text-start">

        <img class="modal-poster" :src="posterPath" alt="">
        <div class="d-flex flex-column justify-content-between modal-body ms-5">
          <div>
            <h2 class="mt-3">
              <router-link class="modal-author text-decoration-none" :to="{ name: 'profile', params: { username: review.user.username } }">
                {{ review.user.nickname }}
              </router-link>
            </h2>
            <h1 class="modal-title">
              {{ review.movie.title }}
            </h1>
            <button @click="likeReview(review.id)" class="like-btn d-flex justify-content-between align-items-center px-3">
              <div class="d-flex flex-row align-items-center">
                <i class="ms-0 me-2 fa-solid fa-heart"></i>
                <p class="m-0">Like</p>
              </div>
              <span>{{ likeCount }}</span>
            </button>
            <div class="mt-3">
              {{ review.content }}
            </div>
          </div>

          <hr>

          <div class="">
            <comment-list
              :comments="review.comment_set"
              :review="review"
              ></comment-list>
          </div>

        </div>
      </div>
    </modal-detail>

  </div>
</template>
<script>
import ModalDetail from '@/components/ModalDetail.vue'
import CommentList from '@/components/CommentList.vue'

import drf from '@/api/drf'
import axios from 'axios'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: "ReviewCard",

  components: {
    ModalDetail,
    CommentList,
  },

  props: {
    review : Object,
  },

  data() {
    return {
      reviewPk : this.review.id,
      showModal: false,
      likeCount: this.review.like_users.length,
      }
  },

  computed: {
    ...mapGetters(['isAuthor', 'isReview', 'authHeader']),
    posterPath(){
      return this.review.movie.poster_path
    },
  },

  methods: {
    ...mapActions(['fetchReview']),

    likeReview(reviewPk) {
      axios({
        url : drf.community.review(reviewPk),
        method : 'post',
        headers : this.authHeader,
      })
        .then(res=> {
          this.likeCount = res.data.like_users_count
        })
        .catch(err => console.error(err.response))
    },
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

.like-btn {
  border: 1px solid #db2828;
  background: linear-gradient(90deg, #db2828 60%, #fff 40%);
  border-radius: 0.25rem;
  color: #db2828;
  width: 8rem;
  height: 2.2rem;
  margin-bottom: 1rem;
}

.like-btn:hover {
  cursor: pointer;
}

.like-btn span {
  font-weight: 800;
}

.like-btn p {
  color: #fff;
  font-size: 0.8rem;
}

.like-btn i {
  color: #ffb2b2;
}

.review-item:hover {
  cursor: pointer;
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

.modal-poster {
  width: 30rem;
  border-radius: 8px;
}

.modal-body {
  width: 99%;
}

.modal-title {
  font-size: 3rem;
  font-weight: 700;
}

.modal-author {
  font-size: 2rem;
  font-weight: 700;
  color: #c4c4c4;
}

.modal-author:hover {
  color: #171717;
}
</style>