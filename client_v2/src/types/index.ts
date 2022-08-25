export type RootState = {};
export type AccountsState = {
  token: string;
  currentUser: User;
  profile: User;
  authError: string | null;
  showAccountModal: boolean;
};
export type CommunityState = {
  reviews: Array<Review>;
  review: Review;
};
export type MoviesState = {
  movies: Array<Movie>;
  movieDetail: Movie;
  movieCard: Movie;
  movieCards: Array<Movie>;
};
export type User = {};
export type Review = {};
export type Movie = {};
