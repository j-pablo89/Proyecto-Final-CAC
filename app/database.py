import pymysql

def conectarMySQL():
    host="juanpablo21.mysql.pythonanywhere-services.com"
    user="juanpablo21"
    clave="admin123456"
    db="juanpablo21$tienda_cac"
    return pymysql.connect(host=host,user=user,password=clave,database=db)

