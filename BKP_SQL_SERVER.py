## O script a seguir faz o backp de todos os bancos de dados do sql server que você adicionar.

#importadores
# importamos o dia
import datetime
# Conexão ao banco de dados
import pyodbc 
# Sleep para esperar o sql executar o BKP antes de fechar a conexão, pois estava fechando antes de terminar excluindo o arquivo de BKP
from time import sleep
# Importamos OS para excluir os BKPs existentes.
import os
# Importamos o pathlib
import pathlib
# Importamos o criador de logs
# este PY gera o arquivo e escreve os logs, o arquivo está disponível neste mesmo repositório.
import log

# Resolve o caminho atual
caminho_pasta=pathlib.Path().resolve()

# Cria caminho de log
caminho_log=str(caminho_pasta)+'\LOG_BKP_SQL_'+ str(datetime.datetime.now().strftime("%d-%m-%Y")) +'.txt'

# Inicailiza log
log.criar_log(caminho_log) 

# autenticação 
driver = "{SQL Server Native Client 11.0}"
servidor = "<seu servidor sql>"
usuario = "<usuario do admin remoto>"
senha = "<senha do admin remoto>"

# dados
# Banco de dados geral
# Removemos o arquivo de BKP anterior

dados_geral = (
    "driver="+driver+";"
    "server="+servidor+";"
    "Database=Geral;"
    "UID="+usuario+";"
    "PWD="+senha+";"
)
# Banco de dados das catracas.
dados_catraca = (
    "driver="+driver+";"
    "server="+servidor+";"
    "Database=Catraca;"
    "UID="+usuario+";"
    "PWD="+senha+";"
)

# Execução do BKP no banco geral
# Vamos remover o BKP antigo.
if os.path.exists("//172.10.20.60//bkp_sql//GerenciadorAcessos.bak"):
    os.remove("//172.10.20.60//bkp_sql//GerenciadorAcessos.bak")
    log.registrar_log(caminho_log, 'Arquivo GerenciadorAcessos.bak excluído')
    sleep(5)
conexao_geral = pyodbc.connect(dados_geral)
cursor_geral = conexao_geral.cursor()
conexao_geral.autocommit = True
try:
    cursor_geral.execute("BACKUP DATABASE GerenciadorAcessos TO DISK = 'C:\extencao\BKP_SQL\GerenciadorAcessos.bak'")
    log.registrar_log(caminho_log, 'Backup Banco GerenciadorAcessos realizado')
except pyodbc.Error as erro:
    log.registrar_log(caminho_log, 'Backup Banco GerenciadorAcessos não realizado erro:')
    log.registrar_log(caminho_log,str(erro))
sleep(5)
conexao_geral.close()

# Execução do BKP nas catracas
# Vamos remover o BKP antigo.
if os.path.exists("//172.10.20.60//bkp_sql//TopAcesso.bak"):
    os.remove("//172.10.20.60//bkp_sql//TopAcesso.bak")
    log.registrar_log(caminho_log, 'Arquivo TopAcesso.bak excluído')
    sleep(5)
conexao_catraca = pyodbc.connect(dados_catraca)
cursor_catraca = conexao_catraca.cursor()
conexao_catraca.autocommit = True
try:
    cursor_catraca.execute("BACKUP DATABASE TopAcesso TO DISK = 'C:\extencao\BKP_SQL\TopAcesso.bak'")
    log.registrar_log(caminho_log, 'Backup Banco TopAcesso realizado')
except pyodbc.Error as erro:
    log.registrar_log(caminho_log, 'Backup Banco TopAcesso não realizado erro:')
    log.registrar_log(caminho_log,str(erro))
sleep(5)
conexao_catraca.close()
