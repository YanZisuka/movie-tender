<template>
  <div>
    <h1>{{profile.nickname}}'s Profile</h1>
    <button>Follow</button>
    <h4>{{profile.username}}</h4>
    <p>follower {{profile.followers_count}} following {{profile.followings_count}}</p>


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
      <li v-for="review in profile.review_set" :key="review.pk">
        <router-link :to="{ name: 'review', params: { reviewPk: review.pk } }">
          {{ review.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>

</style>