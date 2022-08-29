<template>
  <div class="movie-info">
    <iframe
      v-if="videoPath"
      class="movie-info-video"
      :src="videoPath"
      frameborder="0"
      allowfullscreen
    ></iframe>

    <div class="text-start">
      <p class="mt-5 mb-3 overview-title text-white">개요</p>
      <span class="overview-content text-white">{{
        overview | strUnescape
      }}</span>

      <hr class="mt-5 mb-3 text-white" />

      <div class="row justify-content-between">
        <div class="col-6">
          <p class="info-title text-secondary">평균 평점</p>
          <p class="info-content text-white mb-4">
            <i class="fa-solid fa-star"></i> {{ voteAverage }}
          </p>

          <p class="info-title text-secondary">나의 평점</p>
          <div class="star-rating info-content d-flex justify-content-center">
            <input
              type="radio"
              id="5-stars"
              name="rating"
              value="5"
              v-model="rating"
            />
            <label for="5-stars" class="star"
              ><i @click="setRating(5)" class="fa-solid fa-star"></i
            ></label>
            <input
              type="radio"
              id="4-stars"
              name="rating"
              value="4"
              v-model="rating"
            />
            <label for="4-stars" class="star"
              ><i @click="setRating(4)" class="fa-solid fa-star"></i
            ></label>
            <input
              type="radio"
              id="3-stars"
              name="rating"
              value="3"
              v-model="rating"
            />
            <label for="3-stars" class="star"
              ><i @click="setRating(3)" class="fa-solid fa-star"></i
            ></label>
            <input
              type="radio"
              id="2-stars"
              name="rating"
              value="2"
              v-model="rating"
            />
            <label for="2-stars" class="star"
              ><i @click="setRating(2)" class="fa-solid fa-star"></i
            ></label>
            <input
              type="radio"
              id="1-stars"
              name="rating"
              value="1"
              v-model="rating"
            />
            <label for="1-stars" class="star"
              ><i @click="setRating(1)" class="fa-solid fa-star"></i
            ></label>
          </div>
        </div>

        <div class="col-6 text-end">
          <p class="info-title text-secondary mb-2">출연진</p>
          <ul class="info-content text-white p-0 mb-4">
            <li v-for="actor in credits" :key="actor.id">{{ actor.name }}</li>
          </ul>
        </div>

        <!-- <div class="col-12 col-lg-2">
          <p class="info-title text-secondary">리뷰쓰기</p>
          <div @click="showModal = true" class="btn-review">
            <p class="info-content text-white mb-4">
              <i class="fa-solid fa-feather-pointed"></i>
            </p>
          </div>
        </div> -->
      </div>
    </div>

    <!-- modal component -->
    <modal-detail :show="showModal">
      <div slot="body" class="modal-body d-flex flex-column">
        <button
          class="btn align-self-end mt-2 me-2"
          @click="showModal = !showModal"
        >
          <i class="fa-solid fa-xmark"></i>
        </button>
        <review-form-modal :movieDetail="movieDetail"></review-form-modal>
      </div>
    </modal-detail>
  </div>
</template>

<script>
import drf from "@/api/drf";
import axios from "axios";

import { mapGetters } from "vuex";
import ModalDetail from "@/components/ModalDetail.vue";
import ReviewFormModal from "@/components/ReviewFormModal.vue";

export default {
  name: "MovieInfo",

  components: {
    ModalDetail,
    ReviewFormModal,
  },

  props: {
    movieDetail: Object,
    profile: Object,
  },

  data() {
    return {
      showModal: false,
      rating: 0,
    };
  },

  computed: {
    ...mapGetters(["authHeader"]),
    voteAverage() {
      return this.movieDetail.vote_average.toFixed(1);
    },
    overview() {
      return this.movieDetail.overview.replaceAll("\\n", "\n");
    },
    videoPath() {
      const key = this.movieDetail.video_path.split("=");
      if (key[key.length - 1]) {
        return `https://www.youtube.com/embed/${key[key.length - 1]}`;
      } else {
        return "";
      }
    },
    credits() {
      return this.movieDetail.credits.filter((actor) => {
        return (
          actor.role === "Actor" && this.movieDetail.credits.indexOf(actor) < 4
        );
      });
    },
  },

  methods: {
    getRating() {
      axios({
        url: drf.movies.rating(this.movieDetail.id, this.profile.username),
        method: "GET",
        headers: this.authHeader,
      })
        .then((res) => {
          this.rating = res.data.rating;
        })
        .catch((err) => console.error(err.response));
    },
    setRating(rating) {
      axios({
        url: drf.movies.movie(this.movieDetail.id),
        method: "POST",
        data: {
          rating: rating,
        },
        headers: this.authHeader,
      })
        .then()
        .catch((err) => console.error(err.response));
    },
  },

  created() {
    this.getRating();
  },
};
</script>

<style scoped lang="scss">
.movie-info {
  background-color: $darkColor;
  border-radius: 8px;
  padding: 2rem;
  width: 100%;
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.movie-info-video {
  width: 100%;
  height: 30vh;

  @include lg {
    height: 60vh;
  }
}
.overview-title {
  font-size: 2rem;
  line-height: 44px;
  font-weight: 600;
}
.overview-content {
  font-size: 1rem;
}
.info-title {
  font-size: 1rem;
  line-height: 19px;
}
.info-content {
  font-size: 2rem;

  li {
    font-size: 1rem;
    line-height: 150%;
  }
  input {
    display: flex;
    justify-content: center;
  }
}
.btn-review {
  display: inline-block;
}
.btn-review:hover {
  cursor: pointer;
}
.modal-body {
  display: inline-block;
  background: $whiteColor;
  /* border: 2px solid var(--black); */
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  border-radius: 16px;
}

/* 별점 */
.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 3rem;
  justify-content: space-around;
  padding: 0 0 0 0.5em;
  text-align: center;
  width: 5em;

  & :checked ~ label {
    -webkit-text-fill-color: $whiteColor;
  }
  input {
    display: none;
  }
  label {
    -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
    -webkit-text-stroke-width: 2px;
    -webkit-text-stroke-color: $adaptiveGrey800;
    cursor: pointer;

    &:hover,
    &:hover ~ label {
      -webkit-text-fill-color: $adaptiveGrey400;
    }
  }
}
</style>
