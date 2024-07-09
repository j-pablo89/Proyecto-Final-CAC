import pymysql
from database import conectarMySQL

def loginUsuario(logUsuario, logClave):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        stringSQL = "SELECT * FROM usuarios WHERE usuario = %s and clave = %s"
        cursor.execute(stringSQL,(logUsuario,logClave,))
        usuario = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return usuario

def obtenerProducto():
    conexion = conectarMySQL()
    productos = []
    with conexion.cursor() as cursor:
        stringSQL = "SELECT * FROM productos"
        cursor.execute(stringSQL)
        productos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return productos
    
def obtenerUnProducto(id):
    conexion = conectarMySQL()
    producto = None
    with conexion.cursor() as cursor:
        stringSQL = "SELECT * FROM productos WHERE id=%s"
        cursor.execute(stringSQL,(id,))
        producto = cursor.fetchone()
        conexion.close()
        return producto

def insertarProducto(nombre,descripcion,precio,imagen_url):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        stringSQL = "INSERT INTO productos (nombre,descripcion,precio,imagen_url) VALUES (%s,%s,%s,%s)"
        cursor.execute(stringSQL,(nombre,descripcion,precio,imagen_url))
        result = cursor
        conexion.commit()
        conexion.close()
        return result
