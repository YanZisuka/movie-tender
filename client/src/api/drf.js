const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMUNITIES = 'reviews/'
const COMMENTS = 'comments/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + username,
  },
  movies: {
    movies : () => HOST + MOVIES,
    movie : moviePk => HOST + MOVIES + `${moviePk}/`,
    movieOmakase : () => HOST + MOVIES + 'omakase/'
  },
  community : {
    communities : () => HOST + COMMUNITIES,
    review : reviewPk => HOST + COMMUNITIES + `${reviewPk}`,
    likeReview: reviewPk => HOST + COMMUNITIES + `${reviewPk}/` + 'like/',
    comments: reviewPk => HOST + COMMUNITIES + `${reviewPk}/` + COMMENTS,
    comment: (reviewPk, commentPk) =>
      HOST + COMMUNITIES + `${reviewPk}/` + COMMENTS + `${commentPk}/`,
  }
}
