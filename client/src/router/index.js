import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieIndexView from '@/views/MovieIndexView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MovieSelectGenreView from '@/views/MovieSelectGenreView'
import MovieSelectKeywordView from '@/views/MovieSelectKeywordView'
import MovieOmakaseView from '@/views/MovieOmakaseView'

import ReviewListView from '@/views/ReviewListView'
import ReviewNewView from '@/views/ReviewNewView'
import ReviewDetailView from '@/views/ReviewDetailView'
import ReviewEditView from '@/views/ReviewEditView'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/movies',
    name: 'movies',
    component:  MovieIndexView,
  },
  {
    path: '/movies/:movie_pk',
    name: 'movie',
    component:  MovieDetailView,
  },
  {
    path: '/movies/:genre_group',
    name: 'movieGenre',
    component:  MovieSelectGenreView,
  },
  {
    path: '/movies/:keyword',
    name: 'movieKeyword',
    component: MovieSelectKeywordView,
  },
  {
    path: '/movies/omakase',
    name: 'movieOmakase',
    component:  MovieOmakaseView,
  },
  {
    path: '/community',
    name: 'reviews',
    component:  ReviewListView,
  },
  {
    path: '/community/new',
    name: 'reviewNew',
    component:  ReviewNewView,
  },
  {
    path: '/community/:review_pk',
    name: 'review',
    component:  ReviewDetailView,
  },
  {
    path: '/community/:review_pk/edit',
    name: 'reviewEdit',
    component:  ReviewEditView,
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
