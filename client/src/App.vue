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
    setDark() {
      this.isDark = true
    },
    setLight() {
      this.isDark = false
    },
  },

  created() {},
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

.btn-theme-lg {
  margin: 5px;
  background-color: #ed4959;
  border: 0;
  color: #fff;
  font-size: 1rem;
  font-weight: 700;
  width: 10rem;
  height: 3.5rem;
  border-radius: 8px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.btn-theme {
  background-color: #0b1b38;
  width: 50%;
  height: 2.5rem;
  border-radius: 8px;
  border: 0;
  color: #fff;
  font-weight: 700;
}

.text-fff {
  color: #fff;
}

.ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>
