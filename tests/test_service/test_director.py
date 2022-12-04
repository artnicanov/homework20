import pytest
from service.director import DirectorService

class TestDirectorService:
	@pytest.fixture(autouse=True)
	def director_service(self, director_dao):
		self.director_service = DirectorService(dao=director_dao)

	def test_get_all(self):
		directors = self.director_service.get_all()
		assert directors is not None
		assert len(directors) > 0

	def test_get_one(self):
		director = self.director_service.get_one(1)
		assert director is not None
		assert director.id is not None
		assert director.name == "Director 1"

	def test_create(self):
		director_test = {"name": "Director 4"}
		director = self.director_service.create(director_test)
		assert  director_test is not  None

	def test_update(self):
		director_test = {"id": 3, "name": "new name"}
		assert self.director_service.update(director_test)

	def test_del(self):
		assert self.director_service.delete(1) is None