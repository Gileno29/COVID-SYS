import MySQLdb
con = MySQLdb.connect(host="ServidorMysql",
                      user="UsuarioMysql", passwd="SuaSenha", db="SeuDb")
con.select_db('banco de dados')
