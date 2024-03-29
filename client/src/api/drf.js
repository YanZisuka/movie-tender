const HOST = "https://" + "movietender.link" + "/api/v1/";

const ACCOUNTS = "accounts/";
const MOVIES = "movies/";
const COMMUNITY = "reviews/";
const COMMENTS = "comments/";

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + "login/",
    logout: () => HOST + ACCOUNTS + "logout/",
    signup: () => HOST + ACCOUNTS + "signup/",
    currentUserInfo: () => HOST + ACCOUNTS + "user/",
    profile: (username) => HOST + ACCOUNTS + `profile/${username}/`,
  },
  movies: {
    movies: () => HOST + MOVIES,
    movie: (moviePk) => HOST + MOVIES + `${moviePk}/`,
    rating: (moviePk, username) =>
      HOST + MOVIES + `${moviePk}/` + ACCOUNTS + `${username}/`,
    movieStaff: () => HOST + MOVIES + "staffs/",
    movieGenres: (genreGroup) => HOST + MOVIES + `genres/${genreGroup}/`,
    moviesWithKeyword: (pickNum) => HOST + MOVIES + `keywords/${pickNum}/`,
  },
  community: {
    reviews: () => HOST + COMMUNITY,
    review: (reviewPk) => HOST + COMMUNITY + `${reviewPk}/`,
    createComment: (reviewPk) => HOST + COMMUNITY + `${reviewPk}/` + COMMENTS,
    comment: (reviewPk, commentPk) =>
      HOST + COMMUNITY + `${reviewPk}/` + COMMENTS + `${commentPk}/`,
  },
};
