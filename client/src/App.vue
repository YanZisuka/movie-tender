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
:root {
  --mainBgColor: #6495ed;
  --active: #ed4959;
  --inactive: #ffb2b2;
  --white: #fff;
  --offwhite: #fbfbfb;
  --gray: #c4c4c4;
  --black: #000;
  --dark: #171717;
  --border: #ddd;
  --warning: #db2828;

  --adaptiveGrey50: #f9fafb;
  --adaptiveGrey100: #f2f4f6;
  --adaptiveGrey200: #e5e8eb;
  --adaptiveGrey300: #d1d6db;
  --adaptiveGrey400: #b0b8c1;
  --adaptiveGrey500: #8b95a1;
  --adaptiveGrey600: #6b7684;
  --adaptiveGrey700: #4e5968;
  --adaptiveGrey800: #333d4b;
  --adaptiveGrey900: #191f28;
  --adaptiveOpacity50: rgba(0, 23, 51, 0.02);
  --adaptiveOpacity100: rgba(2, 32, 71, 0.05);
  --adaptiveOpacity200: rgba(0, 27, 55, 0.1);
  --adaptiveOpacity300: rgba(0, 29, 58, 0.18);
  --adaptiveOpacity400: rgba(0, 29, 54, 0.31);
  --adaptiveOpacity500: rgba(3, 24, 50, 0.46);
  --adaptiveOpacity600: rgba(0, 19, 43, 0.58);
  --adaptiveOpacity700: rgba(3, 18, 40, 0.7);
  --adaptiveOpacity800: rgba(0, 12, 30, 0.8);
  --adaptiveOpacity900: rgba(2, 9, 19, 0.91);
}

#app {
  font-family: 'IBM Plex Sans KR', sans-serif, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: var(--black);
  min-width: 100%;
  min-height: 100%;
  backdrop-filter: blur(40px);
}

.btn-theme-lg {
  margin: 5px;
  background-color: var(--mainBgColor);
  border: 0;
  color: var(--white);
  font-size: 1rem;
  font-weight: 700;
  width: 10rem;
  height: 3.5rem;
  border-radius: 8px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.btn-theme {
  background-color: var(--mainBgColor);
  width: 50%;
  height: 2.5rem;
  border-radius: 8px;
  border: 0;
  color: var(--white);
  font-weight: 700;
}

.text-fff {
  color: var(--white);
}

.ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

input {
  border: 2px solid var(--border);
  border-radius: 8px;
}
</style>
