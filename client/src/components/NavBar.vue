<template>
  <nav class="d-flex justify-content-between sticky-top p-3">
    <router-link :to="{ name: 'index' }" class="navbar-brand mx-3">
      <div :class="isDark ? 'text-white' : 'text-theme'" class="navbar-logo">movietender</div>
    </router-link>
    <div class="d-flex align-items-center">
      <router-link :to="{ name: 'movies' }" :class="isDark ? 'text-white' : 'text-theme'" class="text-decoration-none mx-5">OMAKASE</router-link>
      <router-link :to="{ name: 'reviews' }" :class="isDark ? 'text-white' : 'text-theme'" class="text-decoration-none mx-5">COMMUNITY</router-link>
      <div class="dropdown">
        <button class="btn dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <img class="profile-img me-2" src="@/assets/logo.png" alt="profile-img">
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
          <p v-if="isCurrentUser">
            <router-link :to="{ name: 'profile', params: { username: currentUser.username } }" class="ms-5 me-3" role="button">Profile</router-link> 
          </p>
          <p v-if="isCurrentUser">
            <router-link :to="{ name: 'logout', params: { username: currentUser.username } }" class="ms-5 me-3" role="button">Logout</router-link> 
          </p>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>

export default {
  name: 'NavBar',

  props: {
    isDark: Boolean,
  },

  computed: {
  },

  methods: {
  },

  created() {
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

.text-theme {
  color: #0b1b38;
}
</style>