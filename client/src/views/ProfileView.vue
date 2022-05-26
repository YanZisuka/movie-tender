<template>
  <div>
    <h1>{{profile.nickname}}'s Profile</h1>
    <h4>{{profile.username}}</h4>
    <span v-if="isProfileUser">
      <router-link :to="{name : 'profileEdit', params : { username } }">
      <button>Edit</button> 
      </router-link>
     | <button @click="deleteUser(username)">Delete</button> |
     <router-link :to="{name : 'logout'}">
       <button>Logout</button>
     </router-link>
    </span>
    <button v-if="!isProfileUser" @click="followUser(profile.username)">Follow</button>
    <p>follower {{ followers_count }}</p>
    <p>following {{ profile.followings_count }}</p>


    <h3>감상한 영화</h3>
    <ul>
      <li v-for="movie in profile.watch_movies" :key="movie.pk">
        <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
          {{ movie.title }}
        </router-link>
      </li>
    </ul>
    <h3>작성한 리뷰</h3>
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

<style>

</style>