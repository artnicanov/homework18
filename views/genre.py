from flask_restx import Resource, Namespace

from dao.model.genre import GenreShema
from implemented import genre_service

genre_ns = Namespace('genre')

@genre_ns.route('/')
class GenresView(Resource):
	def get(self):
		g_objects = genre_service.get_all()
		result = GenreShema(many=True).dump(g_objects)
		return result, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
	def get(self, gid):
		g_object = genre_service.get_one(gid)
		result = GenreShema.dump(g_object)
		return result, 200
