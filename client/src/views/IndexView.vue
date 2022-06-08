<template>
  <div>

    <h1 class="logo">movietender</h1>
    <p class="index-text mt-3">지금,</p>
    <p class="index-text mb-5">어떤 영화를 볼지 고민된다면?</p>
    <button v-if="!isLoggedIn" @click="switchShowAccountModal()" class="default-btn">Login!</button>
    <router-link v-else :to="{ name: 'logout', params: { username: currentUser.username } }">
      <button class="default-btn">Logout!</button>
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
    document.body.setAttribute('style', 'background-color: #fff;')
    await this.fetchCurrentUser()
  },
}
</script>

<style>
.logo {
  font-family: 'Lobster', cursive;
  font-size: 6rem;
  margin-top: 3rem;
}

.index-text {
  font-size: 4rem;
  font-weight: 700;
  line-height: 55px;
  color: #333;
}

.default-btn {
  margin: 5px;
  background-color: #cf1224;
  border: 0;
  color: #fff;
  font-size: 1rem;
  font-weight: 600;
  width: 10rem;
  height: 3.5rem;
  border-radius: 8px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.btn-theme {
  background-color: #db2828;
  width: 100%;
  height: 2.5rem;
  border-radius: 8px;
  border: 0;
  color: #fff;
  font-weight: 700;
}
</style>