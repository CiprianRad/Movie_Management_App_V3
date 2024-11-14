from ro.ubb.movieapp.domain.movieentity import Movie


def test_create_movie():
    movie = Movie(1, "movie title here", "movie description here", "movie genre here" )
    assert (movie.movie_id == 1)
    assert (movie.title == "movie title here")
    assert (movie.description == "movie description here")
    assert (movie.genre == "movie genre here")

def test_get_set_movie():
    movie = Movie(1, "movie title 1", "movie description 1", "movie genre 1")
    movie.movie_id = 2
    assert (movie.movie_id == 2)
    movie.title = "movie title 2"
    assert (movie.title == "movie title 2")
    movie.description = "movie description 2"
    assert (movie.description == "movie description 2")
    movie.genre = "movie genre 2"
    assert (movie.genre == "movie genre 2")
    # movie.title = ''
    # assert (ValueError)
    # movie.movie_id = None
    # assert (ValueError)
    # movie.description = ''
    # assert (ValueError)
    # movie.genre = ''
    # assert (ValueError)

def test_all_movie_entity():
    test_create_movie()
    test_get_set_movie()


if __name__ == "__main__":
    test_all_movie_entity()