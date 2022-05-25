import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default {

  state: {
    movies: [],
    movieDetail: {},
    movieDisplayCard: {},
    movieSelectionCard: {},
    rightMovieCard: {},
  },

  getters: {
    movies: state => state.movies,
    movieDetail: state => state.movieDetail,
    movieDisplayCard: state => state.movieDisplayCard,
    movieSelectionCard: state => state.movieSelectionCard,
    rightMovieCard: state => state.rightMovieCard,
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE_DETAIL: (state, movie) => state.movieDetail = movie,
    SET_MOVIE_DISPLAY_CARD: (state, abstractMovie) => state.movieDisplayCard = abstractMovie,
    SET_MOVIE_SELECTION_CARD: (state, abstractMovie) => state.movieSelectionCard = abstractMovie,
    SET_RIGHT_MOVIE_CARD: (state, abstractMovie) => state.rightMovieCard = abstractMovie,
  },

  actions: {
    fetchMovies({ getters, commit }) {
      axios({
        url: drf.movies.movies(),
        method: 'GET',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIES', res.data)
        })
        .catch(err => console.error(err.response))
    },

    fetchMovie({ getters, commit }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'GET',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_DETAIL', res.data)
        })
        .catch(err => {
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          } else {
            console.error(err.response)
          }
        })
    },

    fetchMovieDisplayCard({ getters, commit }, keywordPk) {
      axios({
        url: drf.movies.movieKeywords(keywordPk),
        method: 'GET',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_DISPLAY_CARD', res.data)
        })
        .catch(err => {
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          } else {
            console.error(err.response)
          }
        })
    },


  },

}