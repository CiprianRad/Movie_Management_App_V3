from ro.ubb.movieapp.domain.movieentity import Movie
from ro.ubb.movieapp.operations.movieoperations import MovieOperations

def test_add_movie():
    movie_operations = MovieOperations()
    movie_operations.add_movie(1, 'title 1', 'description 1', 'genre 1')
    assert len(movie_operations.all_movies) == 1
    assert movie_operations.all_movies[0].title == 'title 1'
    assert movie_operations.all_movies[0].description == 'description 1'
    assert movie_operations.all_movies[0].genre == 'genre 1'
    try:
        movie_operations.add_movie(1, 'title 2', 'description 2', 'genre 2')
        assert False
    except ValueError:
        assert True
    try:
        movie_operations.add_movie(3, '', '', '')
        assert False
    except ValueError:
        assert True

def test_remove_movie():
    movie_operations = MovieOperations()
    movie_operations.add_movie(1, 'title 1', 'description 1', 'genre 1')
    movie_operations.add_movie(2, 'title 2', 'description 2', 'genre 2')
    movie_operations.delete_movie(1)
    assert len(movie_operations.all_movies) == 1
    assert movie_operations.all_movies[0].movie_id == 2
    assert movie_operations.all_movies[0].title == 'title 2'
    assert movie_operations.all_movies[0].description == 'description 2'
    assert movie_operations.all_movies[0].genre == 'genre 2'
    try:
        movie_operations.delete_movie(3)
        assert False
    except ValueError:
        assert True

def test_update_movie():
    movie_operations = MovieOperations()
    movie_operations.add_movie(1, 'title 1', 'description 1', 'genre 1')
    movie_operations.add_movie(2, 'title 2', 'description 2', 'genre 2')
    movie_operations.update_movie(1, 'title 3', 'description 3', 'genre 3')
    assert len(movie_operations.all_movies) == 2
    assert movie_operations.all_movies[0].title == 'title 3'
    assert movie_operations.all_movies[0].description == 'description 3'
    assert movie_operations.all_movies[0].genre == 'genre 3'
    try:
        movie_operations.update_movie(4, 'title 1', 'description 1', 'genre 1')
        assert False
    except ValueError:
        assert True

def test_all_movie_operations():
    test_add_movie()
    test_remove_movie()
    test_update_movie()