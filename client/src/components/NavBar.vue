<template>
  <nav class="d-flex justify-content-between sticky-top p-3">
    <router-link :to="{ name: 'index' }" class="navbar-brand mx-5">
      <div :class="isDark ? 'text-white' : 'text-theme'" class="navbar-logo">movietender</div>
    </router-link>
    <div class="d-flex align-items-center">
      <router-link :to="{ name: 'movies' }" :class="isDark ? 'text-white' : 'text-theme'" class="text-decoration-none mx-5">OMAKASE</router-link>
      <router-link :to="{ name: 'reviews' }" :class="isDark ? 'text-white' : 'text-theme'" class="text-decoration-none mx-5">COMMUNITY</router-link>
      <div class="dropdown mx-5">
        <button :class="isDark ? 'text-white' : 'text-theme'" class="btn dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <img class="profile-img me-2" :src="profileImg" alt="profile-img">
        </button>
        <div class="profile dropdown-menu me-5" aria-labelledby="dropdownMenuButton">
            <router-link v-if="isCurrentUser" :to="{ name: 'profile', params: { username: currentUser.username } }" class="text-decoration-none" role="button">
              <p class="text-center m-0">
              Profile
              </p>
            </router-link>
            <hr class="m-1">
            <router-link v-if="isCurrentUser" :to="{ name: 'logout', params: { username: currentUser.username } }" class="text-decoration-none" role="button">
              <p class="text-center m-0">
              Logout
              </p>
            </router-link> 
        </div>
      </div>
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

  data() {
    return {
      profileImg: require('@/assets/default-profile.png')
    }
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

<style scoped>
nav {
  padding: 2rem;
}

nav a {
  font-weight: bold;
  color: #0b1b38;
}

nav a.router-link-exact-active {
  color: #cf1224;
}

.navbar-logo {
  font-family: 'Lobster', cursive;
  font-size: 2rem;
}

.profile {
  background-color: rgba(255, 255, 255, 0.3);
  border: 0;
}

.profile-img {
  width: 2rem;
}

.text-theme {
  color: #0b1b38;
}
</style>