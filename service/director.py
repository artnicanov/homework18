from dao.director import DirectorDAO

class DirectorService:
	def __init__(self, dao: DirectorDAO):
		self.dao = dao

	def get_one(self, mid):
		return self.dao.get_one(mid)

	def get_all(self):
		return self.dao.get_all()

	def create(self, director_d):
		return self.dao.create(director_d)

	def update(self, director_d):
		self.dao.update(director_d)
		return self.dao

	def delete(self, mid):
		self.dao.delete()
