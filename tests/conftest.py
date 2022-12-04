from unittest.mock import MagicMock
import pytest

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from setup_db import db

@pytest.fixture()
def director_dao():
	director_dao = DirectorDAO(db.session)
	# данные для тестов
	director_1 = Director(id=1, name="Director 1")
	director_2 = Director(id=2, name="Director 2")
	director_3 = Director(id=3, name="Director 3")

	directors = {1: director_1, 2: director_2, 3: director_3}  # словарь чтобы протестировать метод get_all
	director_dao.get_one = MagicMock(return_value=director_1)  # в этом моке проверяем получение одного режиссера из списка
	director_dao.get_all = MagicMock(return_value=directors.values())  # в этом моке проверяем получени всего списка режиссеров
	director_dao.create = MagicMock(return_value=director_1)  # мок для создание режисера
	director_dao.delete = MagicMock()  # мок для удаления режисера
	director_dao.update = MagicMock()  # мок для обновления режисера

	return director_dao

@pytest.fixture()
def genre_dao():
	genre_dao = GenreDAO(db.session)
	# данные для тестов
	genre_1 = Genre(id=1, name="Genre 1")
	genre_2 = Genre(id=2, name="Genre 2")
	genre_3 = Genre(id=3, name="Genre 3")

	genres = {1: genre_1, 2: genre_2, 3: genre_3}
	genre_dao.get_one = MagicMock(return_value=genre_1)
	genre_dao.get_all = MagicMock(return_value=genres.values())
	genre_dao.create = MagicMock(return_value=genre_1)
	genre_dao.delete = MagicMock()
	genre_dao.update = MagicMock()

	return genre_dao

@pytest.fixture()
def movie_dao():
	movie_dao = MovieDAO(db.session)
	# данные для тестов
	movie_1 = Movie(id=1, title="Movie 1", description="description", trailer="link", year=2000, rating=8, genre_id=1,director_id=1)
	movie_2 = Movie(id=2, title="Movie 2", description="description", trailer="link", year=2000, rating=8, genre_id=1,director_id=1)
	movie_3 = Movie(id=3, title="Movie 3", description="description", trailer="link", year=2000, rating=8, genre_id=1,director_id=1)

	movies = {1: movie_1, 2: movie_2, 3: movie_3}
	movie_dao.get_one = MagicMock(return_value=movie_1)
	movie_dao.get_all = MagicMock(return_value=movies.values())
	movie_dao.create = MagicMock(return_value=movie_1)
	movie_dao.delete = MagicMock()
	movie_dao.update = MagicMock()

	return movie_dao