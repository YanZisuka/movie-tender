import { Module } from "vuex";

import axios from "axios";
import drf from "@/api/drf";
import router from "@/router";

import { MoviesState, RootState } from "@/types";

const movies: Module<MoviesState, RootState> = {
  // namespaced: true,

  state: {
    movies: [],
    movieDetail: {},
    movieCard: {},
    movieCards: [],
  },

  getters: {
    movies: (state) => state.movies,
    movieDetail: (state) => state.movieDetail,
    movieCard: (state) => state.movieCard,
    movieCards: (state) => state.movieCards,
  },

  mutations: {
    SET_MOVIES: (state, movies) => (state.movies = movies),
    SET_MOVIE_DETAIL: (state, movie) => (state.movieDetail = movie),
    SET_MOVIE_CARD: (state, movie) => (state.movieCard = movie),
    SET_MOVIE_CARDS: (state, movies) => (state.movieCards = movies),
  },

  actions: {
    fetchMovies({ getters, commit }) {
      return axios({
        url: drf.movies.movies(),
        method: "GET",
        headers: getters.authHeader,
      })
        .then((res) => {
          commit("SET_MOVIES", res.data);
        })
        .catch((err) => console.error(err.response));
    },

    fetchMovie({ getters, commit }, moviePk) {
      return axios({
        url: drf.movies.movie(moviePk),
        method: "GET",
        headers: getters.authHeader,
      })
        .then((res) => {
          commit("SET_MOVIE_DETAIL", res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          } else {
            console.error(err.response);
          }
        });
    },

    fetchMovieCard({ getters, commit }) {
      return axios({
        url: drf.movies.moviesWithKeyword(1),
        method: "GET",
        headers: getters.authHeader,
      })
        .then((res) => {
          commit("SET_MOVIE_CARD", res.data[0]);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          } else {
            console.error(err.response);
          }
        });
    },

    fetchMovieCards({ getters, commit }, pickNum) {
      return axios({
        url: drf.movies.moviesWithKeyword(pickNum),
        method: "GET",
        headers: getters.authHeader,
      })
        .then((res) => {
          commit("SET_MOVIE_CARDS", res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          } else {
            console.error(err.response);
          }
        });
    },

    setSurvey({ getters }, selectionResult) {
      axios({
        url: drf.movies.movies(),
        method: "PUT",
        data: {
          survey: selectionResult,
        },
        headers: getters.authHeader,
      })
        .then()
        .catch((err) => console.error(err.response));
    },
  },
};

export default movies;
