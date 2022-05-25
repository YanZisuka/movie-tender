<template>
  <div>
    <h1 class="logo">movietender</h1>
    <p class="index-text mt-3">지금,</p>
    <p class="index-text mb-5">어떤 영화를 볼지 고민된다면?</p>
    <button>Signup!</button>
  </div>
</template>

<script>

export default {
  name: 'IndexView',

  methods: {},

  created() {},
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
</style>