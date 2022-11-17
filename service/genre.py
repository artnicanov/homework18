from dao.genre import GenreDAO

class GenreService:
	def __init__(self, dao: GenreDAO):
		self.dao = dao

	def get_one(self, mid):
		return self.dao.get_one(mid)

	def get_all(self):
		return self.dao.get_all()

	def create(self, genre_d):
		return self.dao.create(genre_d)

	def update(self, genre_d):
		self.dao.update(genre_d)
		return self.dao

	def delete(self, mid):
		self.dao.delete()
