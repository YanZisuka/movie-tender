<template>
  <div class="review-item d-flex flex-row align-items-center mb-5">

    <div>
      <img :src="posterPath" :alt="`${review.movie.title}'s poster`">
    </div>

    <div class="text-start mx-5" style="width: 100%;">
      
      <div class="d-flex justify-content-between">
        <router-link class="text-decoration-none" :to="{ name: 'movie', params: { moviePk: review.movie.id } }">
          <h1>{{ review.movie.title }}</h1>
        </router-link>
        <span v-if="review.user.id === currentUser.pk && !isEditing" >
          <button v-if="false" @click="switchIsEditing" class="btn btn-sm"><i class="fa-solid fa-pen"></i></button>
          <button @click="onDelete(review.id)" class="btn btn-sm"><i class="fa-solid fa-delete-left"></i></button>
        </span>
      </div>

      <router-link class="text-decoration-none" :to="{ name: 'profile', params: { username: review.user.username } }">
        <h2>{{ review.user.nickname }}</h2>
      </router-link>

      <p class="lead ellipsis pe-5">{{ review.content }}</p>

      <div class="d-flex">
        <div @click="likeReview(review.id)" class="btn-like me-3">
          <i :class="isLike ? 'active' : 'inactive'" class="me-2 fa-solid fa-heart"></i>
          <span>{{ likeCount }}</span>
        </div>
        <div @click="isOpenComment = !isOpenComment" class="btn-comment ms-3">
          <i class="me-2 fa-regular fa-comment"></i>
          <span>{{ review.comment_set.length }}</span>
        </div>
      </div>

      <div v-if="isOpenComment" class="comment-box">
        <comment-list
          :comments="review.comment_set"
          :review="review"
          @comment-emit="onCommentEmit"
          ></comment-list>
      </div>

    </div>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'

import drf from '@/api/drf'
import axios from 'axios'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: "ReviewItem",

  components: {
    CommentList,
  },

  props: {
    review : Object,
  },

  data() {
    return {
      isEditing: false,
      isOpenComment: false,
      likeCount: this.review.like_users.length,
      likeUsers: this.review.like_users,
      }
  },

  computed: {
    ...mapGetters(['currentUser', 'authHeader']),
    posterPath() {
      return this.review.movie.poster_path
    },
    isLike() {
      return this.likeUsers.includes(parseInt(this.currentUser.pk))
    },
  },

  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
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

          this.$emit('like-emit', this.review.id, this.likeUsers)
        })
        .catch(err => console.error(err.response))
    },
    onUpdate(review) {
      this.updateReview(review)
    },
    onDelete(reviewPk) {
      this.deleteReview(reviewPk)
    },
    onCommentEmit(reviewPk, commentSet) {
      this.$emit('comment-emit', reviewPk, commentSet)
    },
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
  transition: color 0.2s ease;
}

.inactive {
  color: #ffb2b2;
  transition: color 0.2s ease;
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