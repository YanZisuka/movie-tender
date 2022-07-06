def movies():
    """
    format: `movies
    """
    return f'movies'

def movies_for_user(user):
    """
    format: `<username>:movies
    """
    return f'{user.username}:movies'

def movie_detail(movie_pk):
    """
    format: `<movie_pk>:movie
    """
    return f'{movie_pk}:movie'
