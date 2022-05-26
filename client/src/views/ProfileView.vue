<template>
  <div class="body d-flex flex-column justify-content-center">
    <div class="profile d-flex flex-row my-5 justify-content-start align-items-center">
      <div>
        <img class="profile-img me-2" src="@/assets/logo.png" alt="profile-img">
      </div>
      <div class="userinfo d-flex flex-column align-items-start justify-content-around">
        <span class="profile-button">
          <h3 class="profile-nickname">{{profile.nickname}}</h3>
          <button v-if="!isProfileUser " @click="followUser(profile.username)" class="btn btn-danger shadow">Follow</button>
          <span v-if="isProfileUser">
            <router-link :to="{name : 'profileEdit', params : { username } }">
              <button class="btn btn-outline-dark">Edit</button> 
            </router-link> |
             <button @click="deleteUser(username)" class="btn btn-outline-danger">Delete </button>
            | <router-link :to="{name : 'logout'}">
              <button class="btn btn-outline-secondary">Logout</button>
            </router-link>
          </span>
        </span>
        <h4 class="profile-username">{{profile.username}}</h4>
          <span class="profil-follow"> 
            follower <span class="follow-count">{{ followers_count }}</span> 
            following <span class="follow-count">{{ profile.followings_count }}</span>
          </span>
      </div>
    </div>

    <!-- 영화 리뷰 정보 -->
    <h3 class="profile-content">감상한 영화</h3>
    <ul>
      <li v-for="movie in profile.watch_movies" :key="movie.pk">
        <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
          {{ movie.title }}
        </router-link>
      </li>
    </ul>
    <h3 class="profile-content">작성한 리뷰</h3>
    <ul>
      <review-card v-for="review in profile.review_set" :key="review.id" :review="review">
      </review-card>
    </ul>
  </div>
</template>

<script>
import ReviewCard from '@/components/ReviewCard.vue'
import { mapGetters, mapActions } from 'vuex'
import drf from '@/api/drf'
import axios from 'axios'

export default {
  name: 'ProfileView',
  components : { ReviewCard },
  data() {
    return {
      username : this.$route.params.username,
      followers_count : 0,
    }
  },
  computed: {
    ...mapGetters(['profile', 'currentUser', 'authHeader']),
    isProfileUser() {
      return this.profile.username === this.currentUser.username
    },
    followerCount(){
      return this.profile.followers_count
    }

  },
  methods: {
    ...mapActions(['fetchProfile', 'deleteUser',]),
    followUser(username){
      axios({
        url : drf.accounts.profile(username),
        method : 'post',
        headers : this.authHeader,
      })
        .then(res => {
          this.followers_count = res.data.followers_count
        })
        .catch(err => console.error(err.response))
    }
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style scoped>
.profile-nickname {
  margin-right: 20px;
  font-size: 40px;
  display : inline;
  text-align: left;
  font-weight: bold;
}
.body {
  margin: 30px;
}

.profile {
  padding-left : 32px;
}

img {
  height : 150px;
  width : 150px;
}

.userinfo {
  margin-top: 8px;
  height : 150px;
  width : 750px;
}

.profile-username {
  font-size: 25px;
  font-weight: 700;
  color: #c4c4c4;
}

.follow-count {
  font-weight : 600;
}

.profile-follow {
  font-size: 15;
}

.profile-button {
  vertical-align: middle;
}

.profile-content {
  text-align: left;
  padding-left : 32px;
  font-weight: 600;
  font-size: 20px;
}
</style>