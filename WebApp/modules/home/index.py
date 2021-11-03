#Modulos Flask
from flask import render_template, abort,request,flash,get_flashed_messages,redirect,url_for
from flask.blueprints import Blueprint
#Modulos usuario
from WebApp.model.model import FormProduct, ProductosTienda
from WebApp import db
index = Blueprint("index",__name__) #varible blue print del INIT
@index.route("/")
@index.route("/producto") #Ruteo con variable blueprint
def main():
    return render_template("index.html")
#Cear productos
@index.route('/registro',methods=['GET','POST'])
def registro():
    form = FormProduct(meta={'csrf':False})
    if form.validate_on_submit():
        producto = ProductosTienda(0,request.form['nombre'],request.form['precio'])
        db.session.add(producto)
        db.session.commit()
        flash("Producto registrado exitosamente")
        return redirect(url_for('index.registro'))
    if form.errors:
        flash(form.errors,"danger")
    return render_template("registro.html",form=form)

#Menu = Leer productos
@index.route("/productos")
@index.route("/show/<int:page>")
def show(page=1):
    return render_template("show.html", productos=ProductosTienda.query.paginate(page,5))
@index.route("/productos/show/<int:id>")
def show_detail(id):
    producto_id=ProductosTienda.query.get_or_404(id)
    return render_template("show_detail.html",id_producto=producto_id)

#Actualizar producto 
@index.route('/actualizar/<int:id>',methods=['GET','POST'])
def actualizar_producto(id):
    form = FormProduct(meta={'csrf':False})
    p = ProductosTienda.query.get_or_404(id)
    if request.method == 'GET':
        form.nombre.data=p.nombre
        form.precio.data=p.precio
    if form.validate_on_submit():
        p.nombre = form.nombre.data
        p.precio = form.precio.data
        db.session.add(p)
        db.session.commit()
        flash("producto editado correctamente")
        return redirect(url_for('index.actualizar_producto',id=p.id_producto))
    if form.errors:
        flash(form.errors,"danger")
    return render_template("editar.html",producto=p,form=form)

#Eliminar Productos
@index.route("/eliminar/<int:id>")
def eliminar_producto(id):
    producto_id=ProductosTienda.query.get_or_404(id)
    db.session.delete(producto_id)
    db.session.commit()
    flash("producto eliminado correctamente")
    return redirect(url_for('index.show'))
