<template>
  <div class="index d-flex flex-column justify-content-center align-items-center">

    <h1 class="logo">movietender</h1>
    <p class="index-text mt-3">지금,</p>
    <p class="index-text mb-5">어떤 영화를 볼지 고민된다면?</p>
    <button v-if="!isLoggedIn" @click="switchShowAccountModal()" class="btn-theme-lg">Login!</button>
    <router-link v-else :to="{ name: 'logout', params: { username: currentUser.username } }">
      <button class="btn-theme-lg">Logout!</button>
    </router-link>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'IndexView',

  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
  },

  methods: {
    ...mapActions(['fetchCurrentUser', 'switchShowAccountModal'])
  },

  async created() {
    this.$emit('light-emit')
    document.body.setAttribute('style', 'background-color: #fafafa;')
    await this.fetchCurrentUser()
  },
}
</script>

<style scoped>
.index {
  width: 100%;
  height: 80vh;
}

.logo {
  font-family: 'Lobster', cursive;
  font-size: 10rem;
}

.index-text {
  font-size: 4rem;
  font-weight: 700;
  line-height: 55px;
  color: #333;
}
</style>