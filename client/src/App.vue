<template>
  <div id="app" class="container-fluid">
    <nav-bar></nav-bar>
    
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

export default {
  components: {NavBar,},
  name: 'App',
}
</script>


<style>
#app {
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0b1b38;
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
