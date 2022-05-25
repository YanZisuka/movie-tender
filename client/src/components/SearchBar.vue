<template>
  <div class="search-bar">
    <input
      v-model="inputKeyword"
      @keydown.enter="fetchKeywordReview(inputKeyword)"
      type="text"
      placeholder="Search Movie..."
    />
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default{
  name : 'SearchBar',
  data() {
      return {
          inputKeyword : '',
      }
  },
  methods : {
      ...mapActions(['fetchKeywordReview'])
  }

}
</script>
<style>
  .search-bar > input {
    padding: 0.5rem;
    font-size: 2rem;
  }
  .search-bar {
    transition: margin 0.5s;
  }
</style>
