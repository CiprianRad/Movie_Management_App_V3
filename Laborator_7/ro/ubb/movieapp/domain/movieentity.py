class Movie:
    def __init__(self, movie_id = None, title = None, description = None, genre = None):
        self.__movie_id = movie_id
        self.__title = title
        self.__description = description
        self.__genre = genre

    def __str__(self):
        return f'movie id: {self.__movie_id}, title: {self.__title}, description: {self.__description}, genre: {self.__genre}'

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def genre(self):
        return self.__genre

    @movie_id.setter
    def movie_id(self, movie_id):
        if isinstance(movie_id, int) and movie_id >= 0:
            self.__movie_id = movie_id
        else:
            raise ValueError('Movie id must be a positive integer')

    @title.setter
    def title(self, title):
        if title.strip():
            self.__title = title
        else:
            raise ValueError('Title must be a non-empty string')

    @description.setter
    def description(self, description):
        if description.strip():
            self.__description = description
        else:
            raise ValueError('Description must be a non-empty string')

    @genre.setter
    def genre(self, genre):
        if genre.strip():
            self.__genre = genre
        else:
            raise ValueError('Genre must be a non-empty string')