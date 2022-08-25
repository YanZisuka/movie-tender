<template>
  <div class="search-bar d-flex align-items-center">
    <i class="fa-solid fa-magnifying-glass"></i>
    <input
      v-model="inputKeyword"
      @keydown.enter="fetchKeywordReview(inputKeyword)"
      type="text"
      placeholder="리뷰 검색"
    />
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "SearchBar",
  data() {
    return {
      inputKeyword: "",
    };
  },
  methods: {
    ...mapActions(["fetchKeywordReview"]),
  },
};
</script>
<style scoped>
i {
  color: #ccc;
}

.search-bar input {
  border: 0;
  padding: 0 1rem;
  height: 2.5rem;
}

.search-bar {
  border: 2px solid var(--border);
  border-radius: 8px;
  padding: 0 1rem;
}
</style>
