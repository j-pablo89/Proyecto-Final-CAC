import pymysql, os
from app import controller, database
from app import app
# Otras importaciones necesarias


def conectarMySQL():
    # host="186.13.35.55"
    # user="administrador"
    # clave="Windows123++"
    # db="tienda_cac"
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    clave = os.getenv('DB_PASSWORD')
    db = os.getenv('DB_NAME')
    return pymysql.connect(host=host,user=user,password=clave,database=db)

