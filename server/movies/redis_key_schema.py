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

def movie_list_with_keywords(user, pick_num):
    """
    format: `<username>:movies-with-kwrds:<pick_num>
    """
    return f'{user.username}:movies-with-kwrds:{pick_num}'
