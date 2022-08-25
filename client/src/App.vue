<template>
  <div id="app" class="container-fluid p-0">
    <nav-bar :isDark="isDark"></nav-bar>

    <router-view @dark-emit="setDark" @light-emit="setLight" />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
  name: "App",

  components: {
    NavBar,
  },

  data() {
    return {
      isDark: false,
    };
  },

  methods: {
    setDark() {
      this.isDark = true;
    },
    setLight() {
      this.isDark = false;
    },
  },

  created() {},
};
</script>

<style lang="scss">
#app {
  font-family: "IBM Plex Sans KR", Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-width: 100%;
  min-height: 100%;
  backdrop-filter: blur(40px);
}
</style>
