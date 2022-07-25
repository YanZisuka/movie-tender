<template>
  <div class="index d-flex flex-column justify-content-center align-items-center">
    <video muted autoplay loop>
      <source :src="bgVideo" type="video/mp4">
    </video>

    <h1 class="logo">movietender</h1>
    <p class="index-text">지금,</p>
    <p class="index-text mb-4">어떤 영화를 볼지 고민된다면?</p>
    <!-- <button v-if="!isLoggedIn" @click="switchShowAccountModal()" class="btn-theme-lg">Login!</button> -->
    <!-- <router-link v-else :to="{ name: 'logout', params: { username: currentUser.username } }">
      <button class="btn-theme-lg">Logout!</button>
    </router-link> -->

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'IndexView',

  data() {
    return {
      bgVideo: require('@/assets/bg-video.mp4'),
    }
  },

  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
  },

  methods: {
    ...mapActions(['fetchCurrentUser', 'switchShowAccountModal'])
  },

  created() {
    this.$emit('dark-emit')
    document.body.setAttribute('style', 'background-color: #fafafa;')
    this.fetchCurrentUser()
  },
}
</script>

<style scoped>
.index {
  width: 100%;
  height: 80vh;
}

  .index > video {
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    z-index: -1;
    filter: brightness(40%);
  }

.logo {
  font-family: 'Lobster', cursive;
  font-size: 4rem;
  font-weight: 700;
  color: #fff;
}

.index-text {
  font-size: 2rem;
  font-weight: 700;
  line-height: 1.5;
  letter-spacing: -0.125rem;
  margin: 0;
  color: var(--black);
  color: #fff;
}
</style>