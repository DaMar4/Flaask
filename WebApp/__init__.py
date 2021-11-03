from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object("configuration.DevelopmentConfig")
db = SQLAlchemy(app)

#Importacion de vistas

from WebApp.modules.home.index import index

#Registro de Blueprints


app.register_blueprint(index)

#Creacion de la bd

db.create_all()

