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
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0b1b38;
  backdrop-filter: blur(30px);
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #0b1b38;
}

nav a.router-link-exact-active {
  color: #cf1224;
}

</style>
