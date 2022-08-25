const HOST = "http://localhost:8000/api/v1/";

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
    profile: (username: string) => HOST + ACCOUNTS + `profile/${username}/`,
  },
  movies: {
    movies: () => HOST + MOVIES,
    movie: (moviePk: number) => HOST + MOVIES + `${moviePk}/`,
    rating: (moviePk: number, username: string) =>
      HOST + MOVIES + `${moviePk}/` + ACCOUNTS + `${username}/`,
    movieStaff: () => HOST + MOVIES + "staffs/",
    movieGenres: (genreGroup: string) =>
      HOST + MOVIES + `genres/${genreGroup}/`,
    moviesWithKeyword: (pickNum: number) =>
      HOST + MOVIES + `keywords/${pickNum}/`,
  },
  community: {
    reviews: () => HOST + COMMUNITY,
    review: (reviewPk: number) => HOST + COMMUNITY + `${reviewPk}/`,
    createComment: (reviewPk: number) =>
      HOST + COMMUNITY + `${reviewPk}/` + COMMENTS,
    comment: (reviewPk: number, commentPk: number) =>
      HOST + COMMUNITY + `${reviewPk}/` + COMMENTS + `${commentPk}/`,
  },
};
