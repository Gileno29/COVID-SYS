import mysql.connector
from mysql.connector import Error


class conexao:

    def __init__(self):
        pass

    def conectar(self):
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1', database='covid', user='root', password='123')

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


#c = conexao()
#executar = c.conectar()

# mySql_Create_Table_Query = """CREATE TABLE Laptop (
#                             Id int(11) NOT NULL,
 #                            Name varchar(250) NOT NULL,
    #                           Price float NOT NULL,
     #                        Purchase_date Date NOT NULL,
      #                       PRIMARY KEY (Id)) """

#cursor = executar.cursor()

#result = cursor.execute(mySql_Create_Table_Query)
