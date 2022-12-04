import pytest
from service.movie import MovieService

class TestMovieService:
	@pytest.fixture(autouse=True)
	def movie_service(self, movie_dao):
		self.movie_service = MovieService(dao=movie_dao)

	def test_get_all(self):
		movies = self.movie_service.get_all()
		assert movies is not None
		assert len(movies) > 0

	def test_get_one(self):
		movie = self.movie_service.get_one(1)
		assert movie is not None
		assert movie.id is not None
		assert movie.title == "Movie 1"

	def test_create(self):
		movie_test = {"title": "Movie 4"}
		movie = self.movie_service.create(movie_test)
		assert  movie_test is not  None

	def test_update(self):
		movie_test = {"id": 3, "title": "new title"}
		assert self.movie_service.update(movie_test)

	def test_del(self):
		assert self.movie_service.delete(1) is None