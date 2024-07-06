import pymysql

def conectarMySQL():
    host="186.13.35.55"
    user="administrador"
    clave="Windows123++"
    db="tienda_cac"
    return pymysql.connect(host=host,user=user,password=clave,database=db)

