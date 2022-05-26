<template>
  <nav v-if="isCurrentUser" class="d-flex justify-content-between sticky-top p-3">
    <router-link :to="{ name: 'index' }" class="navbar-brand mx-3">
      <div :class="isDark ? 'text-white' : 'text-black'" class="navbar-logo">movietender</div>
    </router-link>
    <div class="d-flex align-items-center">
      <router-link :to="{ name: 'movies' }" :class="isDark ? 'text-white' : 'text-black'" class="text-decoration-none mx-5">OMAKASE</router-link>
      <router-link :to="{ name: 'reviews' }" :class="isDark ? 'text-white' : 'text-black'" class="text-decoration-none mx-5">COMMUNITY</router-link>
      <router-link :to="{ name: 'profile', params: { username: currentUser.username } }" class="ms-5 me-3" role="button">
        <img class="profile-img me-2" src="@/assets/logo.png" alt="profile-img">
        <i :class="isDark ? 'text-white' : 'text-black'" class="fa-solid fa-angle-down"></i>
      </router-link>
    </div>
  </nav>
</template>

<script>
import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'NavBar',

  props: {
    isDark: Boolean,
  },

  computed: {
    ...mapGetters(['currentUser']),
    isCurrentUser() {
      return !_.isEmpty(this.currentUser)
    },
  },

  methods: {
    ...mapActions(['fetchCurrentUser'])
  },

  created() {
    this.fetchCurrentUser()
  }

}
</script>

<style>
.navbar-logo {
  font-family: 'Lobster', cursive;
  font-size: 2rem;
}

.profile-img {
  width: 2rem;
}
</style>