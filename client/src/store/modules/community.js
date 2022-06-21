import drf from '@/api/drf'
import router from '@/router'
import axios from 'axios'

export default {

  state: {
    reviews: [],
    review: {},
  },

  getters: {
    reviews: state => state.reviews,
    review: state => state.review,
  },

  mutations: {
    SET_REVIEWS : (state, reviews) => state.reviews = reviews,
    SET_REVIEW : (state, review) => state.review = review,
  },

  actions: {
    fetchReviews({ commit, getters }, cursor = 0){
      axios({
        url : drf.community.reviews(cursor),
        method : 'get',
        headers : getters.authHeader,
      })
        .then(res => commit('SET_REVIEWS', res.data))
        .catch(err => console.error(err.response))
    },

    fetchReview({ commit, getters }, reviewPk){
      axios({
        url : drf.community.review(reviewPk),
        method : 'get',
        headers : getters.authHeader,
      })
        .then(res => commit('SET_REVIEW', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response === 404){
            router.push({ name : 'NotFound404'})
          }})
    },

    createReview({ commit, getters }, review) {
      axios({
        url: drf.community.reviews(),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({ name: 'reviews' })
        })
    },

    updateReview({ commit, getters }, { reviewPk, movie, content }){
      axios({
        url : drf.community.review(reviewPk),
        method : 'put',
        data : { movie, content },
        headers : getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.go()
        })
    },

    deleteReview({ commit, getters }, reviewPk) {
      if (confirm('삭제하시겠습니까?')) {
        axios({
          url: drf.community.review(reviewPk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_REVIEW', {})
            router.go()
          })
          .catch(err => console.error(err.response))
      }
    },
  },
}