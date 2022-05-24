import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {

  state: {
    movies: [],
    movieDetail: {},
    movieDisplayCard: {},
    leftMovieCard: {},
    rightMovieCard: {},
  },

  getters: {
    movies: state => state.movies,
    movieDetail: state => state.movieDetail,
    movieDisplayCard: state => state.movieDisplayCard,
    leftMovieCard: state => state.leftMovieCard,
    rightMovieCard: state => state.rightMovieCard,
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE_DETAIL: (state, movie) => state.movieDetail = movie,
    SET_MOVIE_DISPLAY_CARD: (state, abstractMovie) => state.movieDisplayCard = abstractMovie,
    SET_LEFT_MOVIE_CARD: (state, abstractMovie) => state.leftMovieCard = abstractMovie,
    SET_RIGHT_MOVIE_CARD: (state, abstractMovie) => state.rightMovieCard = abstractMovie,
  },

  actions: {},

}