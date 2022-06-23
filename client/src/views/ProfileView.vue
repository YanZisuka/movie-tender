<template>
  <div v-if="isFetchedProfile" class="row justify-content-center align-items-center">
    <div class="col-6 d-flex flex-column justify-content-center text-start">

      <div class="profile d-flex flex-row my-5 justify-content-start align-items-center">

        <img :src="profileImg" alt="">

        <div class="user-info d-flex flex-column justify-content-center align-items-start w-100 ms-5">
          <div class="d-flex justify-content-between w-100">
            
            <h1 v-if="!isEditing" class="m-0">{{profile.nickname}}</h1>
            <input v-else type="text" v-model="payload.nickname" style="height: 3rem;">

            <button v-if="isMe && !isEditing" @click="isEditing = true" class="btn-profile">프로필 편집</button>

            <div v-if="isMe && isEditing" style="height: 3rem;">
              <button @click="isEditing = false" class="btn-profile me-3" style="height: 100%; background-color: #c4c4c4;">취소</button>
              <button @click="updateUser(payload); isEditing = false" class="btn-profile" style="height: 100%;">저장</button>
            </div>

            <button v-if="!isMe" @click="followUser(profile)" class="btn-profile">
              <span v-if="!isFollowing">팔로우</span>
              <span v-else>언팔로우</span>
            </button>
          </div>

          <h2>{{profile.username}}</h2>
            <p class="m-0">
              <span>팔로워 </span><span>{{ profile.followers_count }}</span> 
              <span class="ms-3">팔로잉 </span><span>{{ profile.followings_count }}</span>
            </p>
        </div>
      </div>

      <h3 class="mt-5 mb-3">감상한 영화</h3>
      <hr class="mt-0 mb-4">
      <div class="profile-box">
        <ul class="d-flex flex-wrap justify-content-start">
          <li v-for="movie in profile.watch_movies" :key="movie.id">
            <router-link :to="{ name: 'movie', params: { moviePk: movie.id } }">
              <img class="movie-poster" :src="movie.poster_path" alt="">
            </router-link>
          </li>
        </ul>
      </div>

      <div v-if="false">
        <h3>작성한 리뷰</h3>
        <ul>
          <review-item v-for="review in profile.review_set" :key="review.id" :review="review">
          </review-item>
        </ul>
      </div>
      
    </div>
  </div>
</template>

<script>
import ReviewItem from '@/components/ReviewItem.vue'
import { mapGetters, mapActions } from 'vuex'
import drf from '@/api/drf'
import axios from 'axios'

export default {
  name: 'ProfileView',

  components : { ReviewItem },

  data() {
    return {
      profileImg: require('@/assets/default-profile.png'),
      isEditing: false,
    }
  },

  computed: {
    ...mapGetters(['profile', 'currentUser', 'authHeader',]),
    isFetchedProfile() {
      return this.$route.params.username === this.profile.username
    },
    isMe() {
      return this.profile.username === this.currentUser.username
    },
    payload() {
      return {
        username: this.currentUser.username,
        nickname: this.profile.nickname,
      }  
    },
    isFollowing() {
      return !!this.profile.followers.filter(user => {
        return user.id === this.currentUser.pk
      }).length
    },
  },

  methods: {
    ...mapActions(['fetchCurrentUser', 'fetchProfile', 'updateUser', 'deleteUser',]),
    followUser({ username }) {
      axios({
        url : drf.accounts.profile(username),
        method : 'POST',
        headers : this.authHeader,
      })
        .then(() => {
          this.fetchProfile({ username })
        })
        .catch(err => console.error(err.response))
    }
  },

  created() {
    this.$emit('light-emit')
    document.body.setAttribute('style', 'background-color: #fafafa;')
    this.fetchCurrentUser()
    this.fetchProfile({ username: this.$route.params.username })
  },

  updated() {
    if (!this.isFetchedProfile) {
      this.fetchProfile({ username: this.$route.params.username })
    }
  }
}
</script>

<style scoped>
ul {
  padding: 0;
}

ul li {
  list-style: none;
}

h3 {
  font-weight: 700;
  font-size: 1rem;
}

.profile img {
  width : 8rem;
}

.user-info h1 {
  font-weight: 700;
}

.user-info h2 {
  color: #c4c4c4;
}

.btn-profile {
  background-color: #0b1b38;
  color: #fff;
  border: 0;
  border-radius: 8px;
  width: 7rem;
}

.btn-profile:hover {
  background-color: #0b1b3880;
}

.profile-box {
  background-color: #fff;
  border-radius: 8px;
  padding: 1rem;
}

.movie-poster {
  width: 7rem;
}
</style>