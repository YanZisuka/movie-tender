<template>
  <div class="search-bar">
    <input
      v-model="inputKeyword"
      @keydown.enter="fetchKeywordReview(inputKeyword)"
      type="text"
      placeholder="리뷰 검색"
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
    padding: 0 1rem;
    height: 2.5rem;
  }
  .search-bar {
    transition: margin 0.5s;
  }
</style>
