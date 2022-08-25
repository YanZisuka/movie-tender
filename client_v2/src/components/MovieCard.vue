<template>
  <div class="d-flex flex-column align-items-center card-frame">
    <img class="card-img" :src="movieCard.poster_path" :alt="`${movieCard.title}`">
    <img class="card-shadow mt-5" :src="movieCard.poster_path" alt="card-shadow">
  </div>
</template>

<script>
export default {
  name: 'MovieCard',

  props: {
    movieCard: Object,
  },
}
</script>

<style scoped>
.card-frame {
  background: linear-gradient(#141414 50%, #2d2d2d);
  border-radius: 32px;
  width: 80vh;
  height: 80vh;
  overflow: hidden;
}

.card-img {
  width: 45vh;
}

.card-shadow {
  width: 45vh;
  filter: blur(25px);
  transform: rotate(-180deg) scaleX(-1);
}
</style>