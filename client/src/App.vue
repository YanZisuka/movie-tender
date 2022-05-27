<template>
  <div id="app" class="container-fluid">
    <nav-bar
      :isDark="isDark"
      ></nav-bar>
    
    <router-view
      @dark-emit="setDark"
      @light-emit="setLight"
      />
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

import { mapActions } from 'vuex'

export default {
  name: 'App',

  components: {
    NavBar
  },

  data() {
    return {
      isDark: false,
    }
  },
  
  methods: {
    ...mapActions(['fetchCurrentUser']),
    setDark() {
      this.isDark = true
    },
    setLight() {
      this.isDark = false
    },
  },

  created() {
    this.fetchCurrentUser()
  },
}
</script>


<style>
#app {
  font-family: 'IBM Plex Sans KR', sans-serif, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0b1b38;
  min-width: 100%;
  min-height: 100%;
  backdrop-filter: blur(40px);
}

.ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>
