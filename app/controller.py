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
    try:
        with conexion.cursor() as cursor:
            stringSQL = "SELECT * FROM productos WHERE idproductos=%s"
            cursor.execute(stringSQL, (id,))
            producto = cursor.fetchone()
    finally:
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


def updateProducto(nombre, descripcion, precio, imagen_url, id_producto):
    try:
        conexion = conectarMySQL()
        with conexion.cursor() as cursor:
            print(nombre, descripcion, precio, imagen_url, id_producto)
            stringSQL = "UPDATE productos SET descripcion = %s, nombre = %s, precio = %s, imagen_url = %s WHERE idproductos = %s;"
            cursor.execute(stringSQL, (descripcion, nombre, precio, imagen_url, id_producto))
            conexion.commit()
            conexion.close()
            return "Producto actualizado correctamente"
    except Exception as e:
        print("Error al actualizar producto:", e) 
        return "Error al actualizar producto"


def deleteProducto(id_producto):
    try:
        conexion = conectarMySQL()
        with conexion.cursor() as cursor:
            stringSQL = "DELETE FROM productos WHERE idproductos = %s;"
            cursor.execute(stringSQL, (id_producto))
            conexion.commit()
            conexion.close()
            return "Producto eliminado correctamente"
    except Exception as e:
        print("Error al borrar el producto:", e) 
        return "Error al borrar producto"