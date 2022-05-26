<template>
  <div>
    <h1 class="logo">movietender</h1>
    <p class="index-text mt-3">지금,</p>
    <p class="index-text mb-5">어떤 영화를 볼지 고민된다면?</p>
    <router-link v-if="!isCurrentUser" :to="{ name: 'signup' }">
      <button class="default-btn">Signup!</button>
    </router-link>  
    <router-link v-if="!isCurrentUser" :to="{ name: 'login' }">
      <button class="default-btn">Login!</button>
    </router-link>
    <router-link v-if="isCurrentUser" :to="{ name: 'movies' }">
      <button class="default-btn">Movie!</button>
    </router-link>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'IndexView',

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
    this.$emit('light-emit')
    document.body.setAttribute('style', 'background-color: #fff;')
    this.fetchCurrentUser()
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
  font-size: 1.5rem;
  font-weight: 600;
  width: 10rem;
  height: 3.5rem;
  border-radius: 0.5rem;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
</style>