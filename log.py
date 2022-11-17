## O script PY abaixo cria e escreve as informações no seu arquivo de LOG

# importamos datetime para registrar o dia e hora.
import datetime
# Importamos OS para verificar se o arquivo existe.
import os

# Cria o arquvio de log
def criar_log(arquivo):
        arquivo_log=open(arquivo,'w')
        hoje=datetime.date.today()
        arquivo_log.writelines('Inicializando Aplicacao em ' + str(hoje)+'\n')
        arquivo_log.close

# Escreve no arquivo de log.
def registrar_log(arquivo, registro):
    if(os.path.isfile(arquivo)):
        agora = datetime.datetime.now() 
        arquivo_log=open(arquivo,'a+',-1, "utf-8")
        arquivo_log.writelines((str(agora)+": "+str(registro))+'\n')
        arquivo_log.close()
        return(0)
    else:
        return("Arquivo não encontrado")
