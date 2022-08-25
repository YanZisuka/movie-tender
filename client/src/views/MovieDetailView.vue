<template>
  <div
    v-if="isMovie"
    class="row justify-content-center align-items-center px-3 p-lg-5 detail-box"
  >
    <div class="col-12 col-xl-6 text-start mb-5">
      <h1 class="movie-title text-fff">{{ movieDetail.title }}</h1>
      <div class="movie-subtitle text-fff mb-4">
        <h2>
          {{ releaseDate }}
        </h2>
        <h2>
          {{ genres }}
        </h2>
        <h2>
          {{ runtime }}
        </h2>
      </div>
      <a
        v-if="isProvider"
        :href="provider.url"
        target="_blank"
        class="d-inline-block text-decoration-none"
      >
        <button
          class="btn-provider d-flex justify-content-start align-items-center text-fff"
        >
          <img
            v-if="provider.name === 'Netflix'"
            :src="netflixLogo"
            alt="netflix-logo"
          />
          <img
            v-if="provider.name === 'Disney+'"
            :src="disneyPlusLogo"
            alt="disney-plus-logo"
          />
          <img
            v-if="provider.name === 'wavve'"
            :src="wavveLogo"
            alt="wavve-logo"
          />
          <img
            v-if="provider.name === 'Watcha'"
            :src="watchaLogo"
            alt="watcha-logo"
          />
          <img
            v-if="provider.name === 'Apple TV+'"
            :src="appleTvPlusLogo"
            alt="apple-tv-plus-logo"
          />
          <span>
            {{ provider.name }}
          </span>
        </button>
      </a>
    </div>

    <div class="col-12 col-xl-6">
      <movie-info :movieDetail="movieDetail" :profile="profile"></movie-info>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import MovieInfo from "@/components/MovieInfo.vue";

export default {
  name: "MovieDetailView",

  components: {
    MovieInfo,
  },

  data() {
    return {
      netflixLogo:
        "https://image.tmdb.org/t/p/original/t2yyOv40HZeVlLjYsCsPHnWLk4W.jpg",
      disneyPlusLogo:
        "https://image.tmdb.org/t/p/original/7rwgEs15tFwyR9NPQ5vpzxTj19Q.jpg",
      watchaLogo: require("@/assets/watcha.png"),
      wavveLogo:
        "https://image.tmdb.org/t/p/original/2ioan5BX5L9tz4fIGU93blTeFhv.jpg",
      appleTvPlusLogo:
        "https://image.tmdb.org/t/p/original/6uhKBfmtzFqOcLousHwZuzcrScK.jpg",
    };
  },

  computed: {
    ...mapGetters(["currentUser", "profile", "movieDetail"]),
    moviePk() {
      return parseInt(this.$route.params.moviePk);
    },
    isMovie() {
      return this.movieDetail.id === this.moviePk;
    },
    isProvider() {
      return this.movieDetail._providers?.length !== 0;
    },
    runtime() {
      const hh = parseInt(this.movieDetail.runtime / 60);
      const mm = this.movieDetail.runtime % 60;

      if (hh && mm) {
        return `${hh}시간 ${mm}분`;
      } else if (hh && !mm) {
        return `${hh}시간`;
      } else {
        return `${mm}분`;
      }
    },
    releaseDate() {
      return `${this.movieDetail.release_date?.replaceAll("-", "/")} (KR)`;
    },
    genres() {
      const genres = this.movieDetail._genres.join(" · ");
      return genres.trim();
    },
    provider() {
      if (this.isProvider) {
        const providerArray = this.movieDetail._providers[0].split("::");
        if (
          providerArray[0] === "Disney Plus" ||
          providerArray[0] === "Apple TV Plus"
        ) {
          providerArray[0] = providerArray[0].replace(" Plus", "+");
        }
        return {
          name: providerArray[0],
          url: providerArray[1],
        };
      } else {
        return {};
      }
    },
  },

  methods: {
    ...mapActions(["fetchCurrentUser", "fetchProfile", "fetchMovie"]),
    getTextColorByBackgroundColor(hexColor) {
      const c = hexColor.replace("#", "");
      const rgb = parseInt(c, 16);
      const r = (rgb >> 16) & 0xff;
      const g = (rgb >> 8) & 0xff;
      const b = (rgb >> 0) & 0xff;

      const luma = 0.2126 * r + 0.7152 * g + 0.0722 * b;

      return luma < 127.5 ? "white" : "black";
    },
    getBackgroundImageColor() {
      document.createElement("canvas");
    },
  },

  async created() {
    this.$emit("dark-emit");
    document.body.style.backgroundColor = `#171717`;
    await this.fetchCurrentUser();
    this.fetchProfile(this.currentUser);
    await this.fetchMovie(this.moviePk);
    document.body.style.backgroundImage = `url(${this.movieDetail.poster_path})`;
    document.body.style.backgroundSize = `cover`;
  },

  beforeDestroy() {
    document.body.style.backgroundImage = ``;
  },
};
</script>

<style scoped lang="scss">
.detail-box {
  min-height: calc(100vh - 85px);
}
.movie-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 2rem;
  color: $adaptiveGrey100;

  @include lg {
    font-size: 4.5rem;
    margin-bottom: 1rem;
  }
}
.movie-subtitle {
  font-size: 1.2rem;
  font-weight: normal;
  display: flex;
  flex-wrap: wrap;

  h2 {
    border: 2px solid $adaptiveGrey900;
    background-color: $adaptiveGrey900;
    padding: 0.3rem 0.5rem;
    border-radius: 4px;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    color: $adaptiveGrey100;
  }
}
.btn-provider {
  background-color: $blackColor;
  color: $whiteColor;
  font-size: 1rem;
  font-weight: 700;
  width: 10rem;
  height: 3.5rem;
  border: 0;
  border-radius: 4px;

  img {
    width: 3rem;
    border-radius: 4px;
  }
  span {
    width: 100%;
  }
}
</style>
