<template>
  <div>
    <div class="review-item d-flex flex-row align-items-center mb-5">

      <div>
        <img :src="posterPath" :alt="`${review.movie.title}'s poster`">
      </div>

      <div class="text-start mx-5" style="width: 100%;">
        
        <router-link class="text-decoration-none" :to="{ name: 'movie', params: { moviePk: review.movie.id } }">
          <h1>{{ review.movie.title }}</h1>
        </router-link>

        <router-link class="text-decoration-none" :to="{ name: 'profile', params: { username: review.user.username } }">
          <h2>{{ review.user.nickname }}</h2>
        </router-link>

        <p class="lead ellipsis pe-5">{{ review.content }}</p>

        <div class="d-flex">
          <div @click="likeReview(review.id)" class="btn-like me-3">
            <i :class="isLike ? 'active' : 'inactive'" class="ms-0 me-2 fa-solid fa-heart"></i>
            <span>{{ likeCount }}</span>
          </div>
          <div @click="isOpenComment = !isOpenComment" class="btn-comment ms-3">
            <span class="me-1">댓글</span>
            <span>{{ review.comment_set.length }}</span>
          </div>
        </div>

        <div v-if="isOpenComment" class="comment-box">
          <comment-list
            :comments="review.comment_set"
            :review="review"
            ></comment-list>
        </div>

      </div>
    </div>

    <!-- use the modal component, pass in the prop -->
    <modal-detail
      :show="showModal"
      @close="showModal = false"
      >
      <div slot="body" class="d-flex text-start">

        <img class="modal-poster" :src="posterPath" alt="">
        <div class="d-flex flex-column justify-content-between modal-body ms-5">
          <div>
            <!-- 작성자 -->
            <div>
              <h2 class="mt-3">
                <router-link class="modal-author text-decoration-none" :to="{ name: 'profile', params: { username: review.user.username } }">
                  {{ review.user.nickname }}
                </router-link>
              </h2>
              <span v-if="review.user.id === currentUser.pk && !isEditing" >
                <button @click="switchIsEditing" class="btn"><i class="fa-solid fa-pen"></i></button>
                <button @click="onDelete(review.id)" class="btn"><i class="fa-solid fa-xmark"></i></button>
              </span>
            </div>
            <!-- 영화제목 -->
            <h1 class="modal-title">
              {{ review.movie.title }}
            </h1>
            <!-- 좋아요 버튼 -->
            <button @click="likeReview(review.id)" class="like-btn d-flex justify-content-between align-items-center px-3">
              <div class="d-flex flex-row align-items-center">
                <i class="ms-0 me-2 fa-solid fa-heart"></i>
                <p class="m-0">Like</p>
              </div>
              <span>{{ likeCount }}</span>
            </button>
            <!-- 내용 -->
            <span v-if="!isEditing">
              <div class="lead mt-3">
                {{ review.content }}
              </div>
            </span>
            <span v-if="isEditing">
              <p>
              <input type="text" v-model="newReview.content">
              </p>
              <button class="btn" @click="onUpdate(newReview)"><i class="fa-solid fa-pen"></i></button> |
              <button class="btn" @click="switchIsEditing"><i class="fa-solid fa-arrow-left-long"></i></button>
            </span>

          </div>

          <hr>

          <div style="">
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
  name: "ReviewItem",

  components: {
    ModalDetail,
    CommentList,
  },

  props: {
    review : Object,
  },

  data() {
    return {
      isEditing: false,
      isOpenComment: false,
      reviewPk: this.review.id,
      likeCount: this.review.like_users.length,
      likeUsers: this.review.like_users,
      showModal: false,
      }
  },

  computed: {
    ...mapGetters(['currentUser', 'isAuthor', 'isReview', 'authHeader']),
    posterPath() {
      return this.review.movie.poster_path
    },
    isLike() {
      return this.likeUsers.includes(parseInt(this.currentUser.pk))
    },
  },

  methods: {
    ...mapActions(['fetchReview', 'updateReview', 'deleteReview']),

    switchIsEditing() {
      this.isEditing = !this.isEditing
    },

    likeReview(reviewPk) {
      axios({
        url : drf.community.review(reviewPk),
        method : 'post',
        headers : this.authHeader,
      })
        .then(res => {
          this.likeCount = res.data.like_users_count

          if (res.data.is_like) {
            this.likeUsers.push(this.currentUser.pk)
          } else {
            this.likeUsers = this.likeUsers.filter(userPk => {
              return userPk !== this.currentUser.pk
            })
          }

          this.$emit('like-emit', this.reviewPk, this.likeUsers)
        })
        .catch(err => console.error(err.response))
    },

    onUpdate(review) {
      this.updateReview(review)
    },

    onDelete(reviewPk) {
      this.deleteReview(reviewPk)
    }
  },

  created() {}
}
</script>

<style scoped>
.review-item {
  background-color: #fbfbfb;
  border-radius: 8px;
  border: 1px solid #ddd;
  width: 100%;
}

.review-item img {
  width: 13rem;
  border-radius: 8px 0 0 8px;
}

.review-item h1 {
  font-size: 2rem;
  font-weight: 700;
  color: #0b1b38;
}

.review-item h2 {
  font-size: 1rem;
  font-weight: 700;
  color: #c4c4c4;
}

.review-item h2:hover {
  color: #171717;
}

.btn-like:hover {
  cursor: pointer;
}

.active {
  color: #ed4959;
}

.inactive {
  color: #ffb2b2;
}

.btn-comment:hover {
  cursor: pointer;
}

.modal-poster {
  width: 30rem;
  border-radius: 8px 0 0 8px;
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