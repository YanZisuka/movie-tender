<template>
  <div
    class="omakase row flex-column justify-content-center align-items-center"
  >
    <div class="col-6 d-flex flex-column">
      <div class="d-flex justify-content-between align-items-center">
        <p class="omakase-text text-start m-0">
          {{ profile.nickname }}님이 좋아하실 영화들이에요!
        </p>
        <router-link :to="{ name: 'movieSurvey' }">
          <button class="btn-survey m-0">다시하기 ＞</button>
        </router-link>
      </div>

      <hr class="mb-4" />

      <omakase-item
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      ></omakase-item>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import OmakaseItem from "@/components/OmakaseItem.vue";

export default {
  name: "MovieOmakase",

  components: {
    OmakaseItem,
  },

  data() {
    return {};
  },

  computed: {
    ...mapGetters(["profile", "movies"]),
  },

  methods: {
    ...mapActions(["fetchMovies"]),
  },

  created() {
    this.fetchMovies();
  },
};
</script>

<style scoped lang="scss">
hr {
  color: $whiteColor;
}
.btn-survey {
  background-color: transparent;
  border: 0;
  color: $mainBadgeColor;
  font-weight: 700;
}
.omakase {
  margin: 3rem 5rem;
}
.omakase-text {
  font-size: 2rem;
  font-weight: 700;
  line-height: 150%;
  color: $whiteColor;
}
.omakase a {
  width: fit-content;
  padding: 0;
}
</style>
