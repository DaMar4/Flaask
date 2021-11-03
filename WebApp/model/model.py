from WebApp import db
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import DecimalField
from decimal import Decimal
from wtforms.validators import InputRequired,NumberRange
class ProductosTienda(db.Model):
    __tablename__='stocktienda'
    id_producto=db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(255))
    precio = db.Column(db.Float)
    def __init__(self, id_producto,nombre,precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
    def __repr__(self):
        return '<ProductosTienda %r>' % self.nombre

class FormProduct(FlaskForm):
    nombre = StringField('nombre',validators=[InputRequired()])
    precio = DecimalField('precio',validators=[InputRequired(),NumberRange(min=Decimal(0.0))])