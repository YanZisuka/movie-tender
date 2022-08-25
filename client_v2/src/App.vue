<script lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
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

<template>
  <div id="app" class="container-fluid">
    <NavBar :isDark="isDark"></NavBar>

    <router-view @dark-emit="setDark" @light-emit="setLight" />
  </div>
</template>

<style scoped>
.btn-theme-lg {
  margin: 5px;
  background-color: var(--mainBgColor);
  border: 0;
  color: var(--white);
  font-size: 1rem;
  font-weight: 700;
  width: 10rem;
  height: 3.5rem;
  border-radius: 0.5rem;
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
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
