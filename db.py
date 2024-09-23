import pymysql

host = "awsdatabase14.cd8ayis6yy2f.us-east-2.rds.amazonaws.com"
user = "AWSHarris15"
passw = "AWSAnathema14"
db_name = "AWSdatabase14"

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db_name
        )
        print("Conexión exitosa a la Base de Datos")
        return connection
    except Exception as err:
        print("Error", err)
        return None

def insert(codigo, nombre, apellido, actividad, horainicio, horafinal):
    try:
        instruction = "INSERT INTO users VALUES ("+codigo+", '"+nombre+"', '"+apellido+"', '"+actividad+"', '"+horainicio+"', '"+horafinal+"');"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print("Usuario Agregado")
    except Exception as err:
        print("Error", err)
        return None