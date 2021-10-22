# Esta archivo va a gestionar la conexion a la base de datos
import pymysql


# Solamente en mi caso en vez de localhost podre mi ip
# en el caso de ustedes va lo siguiente
# host = 'localhost'
# user = 'root'
# password = ''
# db = 'tecsup_employees'
def get_connection_db():
    return pymysql.connect(
        host='192.168.1.4',
        user='root',
        password='mypass123',
        db='tecsup_employees'
    )
