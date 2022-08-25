<template>
  <div v-if="isCurrentUser && isMyProfile" class="movie-index">
    <div
      v-if="!isSurvey"
      class="row justify-content-center align-items-center px-3 px-md-5"
    >
      <div class="d-flex flex-column align-items-center col-12 col-md-6">
        <p class="main-text m-0">무비텐더가 {{ profile.nickname }}님이</p>
        <p class="main-text m-0">좋아하실만한 영화를</p>
        <p class="main-text mt-0 mb-4">추천해드릴게요!</p>
        <p class="sub-text m-0">
          두 개의 선택지 중 더 마음에 드는 영화를 골라주시면,
        </p>
        <p class="sub-text mt-0">
          {{ profile.nickname }}님의 취향에 맞는 영화를 추천해드려요.
        </p>
        <div class="w-25">
          <router-link :to="{ name: 'movieSurvey' }">
            <button class="button mt-3 mb-5 mb-md-5">시작하기!</button>
          </router-link>
        </div>
      </div>
      <div class="col-12 col-md-6 d-flex justify-content-center">
        <movie-card :movieCard="movieCard"></movie-card>
      </div>
    </div>

    <div v-else>
      <movie-omakase></movie-omakase>
    </div>
  </div>
</template>

<script>
import _ from "lodash";
import { mapGetters, mapActions } from "vuex";

import MovieCard from "@/components/MovieCard.vue";
import MovieOmakase from "@/components/MovieOmakase.vue";

export default {
  name: "MovieIndexView",

  components: {
    MovieCard,
    MovieOmakase,
  },

  data() {
    return {};
  },

  computed: {
    ...mapGetters(["currentUser", "profile", "movieCard"]),
    isCurrentUser() {
      return !_.isEmpty(this.currentUser);
    },
    isMyProfile() {
      return this.profile.username === this.currentUser.username;
    },
    isSurvey() {
      if (this.profile.survey?.length === 0) {
        return false;
      } else {
        return true;
      }
    },
  },

  methods: {
    ...mapActions([
      "fetchCurrentUser",
      "fetchProfile",
      "fetchMovieCard",
      "fetchMovieCards",
    ]),
  },

  async created() {
    this.$emit("dark-emit");
    document.body.setAttribute("style", "background-color: #171717;");
    this.fetchMovieCards(10);
    this.fetchMovieCard();
    await this.fetchCurrentUser();
    this.fetchProfile(this.currentUser);
  },
};
</script>

<style scoped lang="scss">
.movie-index {
  margin-top: 5vh;
}
.main-text {
  font-size: 2.5rem;
  line-height: 120%;
  font-weight: 700;

  @include xl {
    font-size: 3.75rem;
  }

  color: $whiteColor;
}
.sub-text {
  font-size: 1.2rem;
  line-height: 120%;

  @include xl {
    font-size: 2rem;
  }

  color: $whiteColor;
}
</style>
