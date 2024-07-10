from flask import Flask, render_template, request, redirect, url_for, session
from controller import *
from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/imagenes')
app.secret_key = os.urandom(20)

@app.route("/")
def index():
    title = 'Home'
    return render_template("index.html", title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        inputUsuario = request.form.get('inputUsuario')
        inputClave = request.form.get('inputClave')
        result = loginUsuario(inputUsuario, inputClave)

        if result:
            session['logged_in'] = True
            session['username'] = inputUsuario
            return redirect("/")
        else:
            error = 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo'
            return render_template('login.html', error=error)
    else:
        return render_template("login.html", error=None)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('usuario', None)
    return redirect("/")

@app.route('/servicios')
def paginaServicios():
    title = 'Servicios'
    return render_template("servicios.html",title=title)

@app.route('/quienesomos')
def paginaQuienesSomos():
    title = 'Staff'
    return render_template("quienesomos.html",title=title)

@app.route('/notimascotas')
def paginaNotiMascotas():
    title = 'Noti Mascotas'
    return render_template("notimascotas.html",title=title)

@app.route('/tienda')
def paginaTienda():
    title = 'Tienda'
    productos = obtenerProducto()
    return render_template("tienda.html", title=title, productos=productos)

@app.route('/contacto')
def paginaContacto():
    title = 'Contacto'
    return render_template("contacto.html", title=title)

@app.route('/error404')
def paginaError404():
    title = 'Error 404'
    return render_template("error404.html",title=title)

@app.route('/administrador')
def paginaAdministrador():
    title = 'Administrador Tienda'
    productos = obtenerProducto()
    return render_template("administrador.html", title=title, productos=productos)

@app.route('/nuevoProducto', methods=['GET'])
def nuevoProducto():
    title = 'Nuevo Producto'
    return render_template("nuevoProducto.html",title=title)


@app.route('/insertarProducto', methods=['POST'])
def cargarProducto():
    nombreProducto = request.form.get('nombre')
    descripcionProducto = request.form.get('descripcion')
    precioProducto = request.form.get('precio')
    imagenProducto = request.files.get('imagen')
    if imagenProducto:
        filename = secure_filename(imagenProducto.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        img = Image.open(imagenProducto)
        img = img.resize((300,300))
        img.save(filepath)

        imagen_url = url_for('static', filename=f'imagenes/{filename}')

        result = insertarProducto(nombreProducto,descripcionProducto,precioProducto,imagen_url)
        print(result)
        return redirect("/administrador")
    
    return "Error al guardar el producto"


@app.route('/editarProducto/<string:id>', methods=['GET','POST'])  
def editarProducto(id):
    title = 'Editar Producto'
    producto = obtenerUnProducto(id)
    if producto:
        print(request.method)
        if request.method == 'POST':
            nombreProducto = request.form.get('nombre')
            descripcionProducto = request.form.get('descripcion')
            precioProducto = request.form.get('precio')
            imagenProducto = request.files.get('imagen')
            if imagenProducto:
                filename = secure_filename(imagenProducto.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                img = Image.open(imagenProducto)
                img = img.resize((300,300))
                img.save(filepath)

                imagen_url = url_for('static', filename=f'imagenes/{filename}')
            else:
                imagen_url = ""
            result = updateProducto(nombreProducto, descripcionProducto, precioProducto, imagen_url, id)
            return redirect('/administrador')   
        else:
            return render_template("editarProducto.html", title=title, producto=producto)
    else:
       return redirect('/error404')   
      


@app.route('/eliminarProducto/<string:id>')  
def eliminarProducto(id):
    producto = obtenerUnProducto(id)
    if producto:
        result = deleteProducto(id)
        print(result)
        return redirect('/administrador')   
    else:
       return redirect('/error404')   
