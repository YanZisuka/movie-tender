<template>
  <div>
    <nav class="d-flex justify-content-between align-items-center sticky-top p-3">
      <div>
        <img src="@/assets/logo.png" alt="logo">
      </div>
      <div>
        <router-link :to="{ name: 'index' }" class="mx-4">Home</router-link>
        <router-link :to="{ name: 'movies' }" class="mx-4">Omakase</router-link>
        <router-link :to="{ name: 'reviews' }" class="mx-4">Community</router-link>
      </div>
    </nav>
  </div>
</template>

<script>
export default {

}
</script>

<style>
img {
  width: 3rem;
}
</style>