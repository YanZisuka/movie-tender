<template>
  <nav class="d-flex justify-content-between sticky-top p-3">
    <div>
      <router-link :to="{ name: 'index' }" class="navbar-brand mx-3">
        <img class="logo" src="@/assets/logo.png" alt="logo">
      </router-link>
    </div>
    <div class="d-flex align-items-center">
      <router-link :to="{ name: 'movies' }" class="text-decoration-none mx-5">OMAKASE</router-link>
      <router-link :to="{ name: 'reviews' }" class="text-decoration-none mx-5">COMMUNITY</router-link>
      <router-link :to="{ name: 'profile', params: { username: currentUser.username } }" class="ms-5 me-3" role="button">
        <img class="profile-img me-2" src="@/assets/logo.png" alt="profile-img">
        <i class="fa-solid fa-angle-down"></i>
      </router-link>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'NavBar',

  computed: {
    ...mapGetters(['currentUser'])
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
.logo {
  width: 3rem;
}

.profile-img {
  width: 2rem;
}
</style>