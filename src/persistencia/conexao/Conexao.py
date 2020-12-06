import mysql.connector
from mysql.connector import Error


class Conexao:

    def __init__(self):
        pass

    def conectar(self):
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1', database='siscovid', user='root', password='123')

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Conectado ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database()")
                record = cursor.fetchone()
                print("vocẽ está conectado ao database: ", record)

                return connection
        except Error as e:
            print("=============================")
            print("Erro ao conectar ao Mysql ", e)

# finally:
#    if(connection.is_connected()):
#        cursor.close()
#        connection.close
#       print("Mysql connection is closed")
