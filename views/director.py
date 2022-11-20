from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('director')

@director_ns.route('/')
class DirectorsView(Resource):
	def get(self):
		d_objects = director_service.get_all()
		result = DirectorSchema(many=True).dump(d_objects)
		return result, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
	def get(self, did):
		d_object = director_service.get_one(did)
		result = DirectorSchema().dump(d_object)
		return result, 200
