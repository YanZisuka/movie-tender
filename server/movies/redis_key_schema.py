def movie_list(user):
    """
    format: `<username>:movie-list
    """
    return f'{user.username}:movie-list'

def movie_detail(movie_pk):
    """
    format: `<movie_pk>:movie
    """
    return f'{movie_pk}:movie'