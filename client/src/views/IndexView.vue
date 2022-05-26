<template>
  <div>
    <h1 class="logo">movietender</h1>
    <p class="index-text mt-3">지금,</p>
    <p class="index-text mb-5">어떤 영화를 볼지 고민된다면?</p>
    <router-link :to="{ name: 'signup' }">
      <button class="default-btn">Signup!</button>
    </router-link>
  </div>
</template>

<script>

export default {
  name: 'IndexView',

  methods: {},

  created() {
    this.$emit('light-emit')
    document.body.setAttribute('style', 'background-color: #fff;')
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