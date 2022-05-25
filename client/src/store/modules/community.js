import drf from '@/api/drf'
import router from '@/router'
import axios from 'axios'
import _ from 'lodash'

export default {

  state: {
    reviews : [],
    review : {},
    // likeCount : {},
    movie : {},
  },

  getters: {
    reviews : state => state.reviews,
    review : state => state.review,
    isAuthor : (state, getters) => {
      return state.review.user.id === getters.currentUser.pk
    },
    isReview: state => !_.isEmpty(state.review),
    // likeCount : state => state.likeCount.like_users_count,
    // isLike : state => state.likeCount.is_like,
    movie : state => state.movie,

  },

  mutations: {
    SET_REVIEWS : (state, reviews) => state.reviews = reviews,
    SET_REVIEW : (state, review) => state.review = review,
    SET_LIKECOUNT : (state, likeCount) => state.likeCount = likeCount,
    SET_REVIEW_COMMENTS: (state, comments) => (state.review.comments = comments),
    SET_MOVIE : (state, movie) => ( state.movie = movie),

  },

  actions: {
    fetchReviews({ commit, getters }){
      axios({
        url : drf.community.reviews(),
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
    // likeReview({ commit, getters }, reviewPk){
    //   axios({
    //     url : drf.community.review(reviewPk),
    //     method : 'post',
    //     headers : getters.authHeader,
    //   })
    //     .then(res=> {
    //       console.log(res.data)
    //       commit('SET_LIKECOUNT', res.data)})
    //     .catch(err => console.error(err.response))
    // },
    createReview({ commit, getters }, review) {
      axios({
        url: drf.community.reviews(),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({name: 'reviewDetail', params: { reviewPk: getters.review.id }})
        })
    },
    updateReview({ commit, getters }, {pk, movie, content}){
      axios({
        url : drf.community.review(pk),
        method : 'put',
        data : { movie, content },
        headers : getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({ name:'reviewDetail', params : {reviewPk : getters.review.id}})
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
            router.push({ name: 'reviews'})
          })
          .catch(err => console.error(err.response))
      }
    },
    createComment({ commit, getters }, { reviewPk, content }) {
      const comment = { content }
      axios({
        url: drf.community.createComment(reviewPk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },
    updateComment({ commit, getters }, { reviewPk, commentPk, content }) {
      const comment = { content }

      axios({
        url: drf.community.comment(reviewPk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteComment({ commit, getters }, { reviewPk, commentPk, content }) {
        content;
        if (confirm('삭제하시겠습니까?')) {
          axios({
            url: drf.community.comment(reviewPk, commentPk),
            method: 'delete',
            data : {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_REVIEW_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },
    fetchMovie({commit, getters }, moviePk){
      axios({
        url : drf.movies.movie(moviePk),
        method : 'get',
        headers : getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)})
        .catch(err => console.error(err.response))
    },
  },
}