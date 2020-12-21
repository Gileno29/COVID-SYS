import os
import time
import datetime

DB_HOST = 'localhost'
DB_USER = 'gileno'
DB_USER_PASSWORD = '123'
#DB_NAME = '/backup/dbnames.txt'
# Se você tiver varias databases listadas em um arquivo, descomente a linha acima e substitua o caminho do diretório.
DB_NAME = 'siscovid'
DIRETORIO_BACKUP = '/home/gileno/backup/'

# Pegar hora para botar como nome pra pasta
DATETIME = time.strftime('%d%m%Y-%H%M')

DIRETORIO_BACKUP_HOJE = DIRETORIO_BACKUP + DATETIME

# Checando se a pasta já existe
print("Criando pasta de backup")
if not os.path.exists(DIRETORIO_BACKUP_HOJE):
    os.makedirs(DIRETORIO_BACKUP_HOJE)

# checagem de database unica ou múltipla
print("checando arquivo de databases.")
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print("O arquivo de dbs foi encontrado...")
    print("Começando o backup de todos os bancos listados... " + DB_NAME)
else:
    print("O arquivo de dbs não foi encontrado...")
    print("Começando o backup " + DB_NAME)
    multi = 0

# Comecando o processo de backup.
if multi:
    in_file = open(DB_NAME, "r")
    flength = len(in_file.readlines())
    in_file.close()
    p = 1
    dbfile = open(DB_NAME, "r")

    while p <= flength:
        db = dbfile.readline()   # lendo nome da database do arquivo
        db = db[:-1]         # deletar linha extra
        dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + \
            " " + db + " > " + DIRETORIO_BACKUP_HOJE + "/" + db + ".sql"
        os.system(dumpcmd)
        p = p + 1
    dbfile.close()
else:
    db = DB_NAME
    dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + \
        " " + db + " > " + DIRETORIO_BACKUP_HOJE + "/" + db + ".sql"
    os.system(dumpcmd)

print("Backup completo")
print("Seu backup foi criado em '" + DIRETORIO_BACKUP_HOJE + "' diretorio")
