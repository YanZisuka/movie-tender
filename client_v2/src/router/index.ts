import { createWebHistory, createRouter } from "vue-router";

import IndexView from "@/views/IndexView.vue";

import MovieIndexView from "@/views/MovieIndexView.vue";
import MovieDetailView from "@/views/MovieDetailView.vue";
import MovieSurveyView from "@/views/MovieSurveyView.vue";

import ReviewListView from "@/views/ReviewListView.vue";

import LogoutView from "@/views/LogoutView.vue";
import ProfileView from "@/views/ProfileView.vue";
import NotFound404 from "@/views/NotFound404.vue";

const routes = [
  {
    path: "/",
    name: "index",
    component: IndexView,
  },
  {
    path: "/logout",
    name: "logout",
    component: LogoutView,
  },
  {
    path: "/profile/:username",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/movies",
    name: "movies",
    component: MovieIndexView,
  },
  {
    path: "/movies/survey",
    name: "movieSurvey",
    component: MovieSurveyView,
  },
  {
    path: "/movies/:moviePk",
    name: "movie",
    component: MovieDetailView,
  },
  {
    path: "/reviews",
    name: "reviews",
    component: ReviewListView,
  },
  {
    path: "/404",
    name: "NotFound404",
    component: NotFound404,
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/404",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
