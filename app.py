from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config
from setup_db import db
from views.movie import movie_ns
from views.genre import genre_ns
from views.director import director_ns


def register_extentions(app):
	api = Api(app)
	db.init_app(app)
	api.add_namespace(movie_ns)
	api.add_namespace(genre_ns)
	api.add_namespace(director_ns)


def create_app(config_obj):
	app = Flask(__name__)
	app.config.from_object(config_obj)
	register_extentions(app)

app = create_app(Config())

if __name__ == '__main__':
	app.run()
