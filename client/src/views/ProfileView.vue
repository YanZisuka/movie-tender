<template>
  <div class="row justify-content-center align-items-center">
    <div class="col-6 body d-flex flex-column justify-content-center text-start">

      <div class="profile d-flex flex-row my-5 justify-content-start align-items-center">

        <div>
          <img class="profile-img me-2" :src="profileImg" alt="profile-img">
        </div>

        <div class="userinfo d-flex flex-column align-items-start justify-content-around">
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
        <li v-for="movie in profile.watch_movies" :key="movie.id">
          <router-link :to="{ name: 'movie', params: { moviePk: movie.id } }">
            {{ movie.title }}
          </router-link>
        </li>
      </ul>
      <h3 class="profile-content">작성한 리뷰</h3>
      <ul>
        <review-item v-for="review in profile.review_set" :key="review.id" :review="review">
        </review-item>
      </ul>
      
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
  async created() {
    this.$emit('light-emit')
    document.body.setAttribute('style', 'background-color: #fafafa;')
    const payload = { username: this.$route.params.username }
    await this.fetchProfile(payload)
  },
}
</script>

<style scoped>
ul {
  margin: 0;
  padding: 0;
}

ul li {
  list-style: none;
}

h3 {
  text-align: left;
  margin: 2rem 0 1rem 0;
  font-weight: 700;
  font-size: 2rem;
}

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

</style>