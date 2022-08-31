#Comunicação ao banco ACESS via PY

import pyodbc

#Usamos para descobrir o driver do banco antes de tentar a comunicação.
#driver = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper()] 
#print (f'MS-Access Drivers : {driver}')

try:
    dados = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\172.10.20.60\SoapAdmin3.5\Access.mdb;'
    conexao = pyodbc.connect(dados)
    print ("Logado com sucesso")
    cursor = conexao.cursor()
    matricula = str("Definir")

    try:
        cursor.execute('DELETE FROM USERINFO WHERE lastname = ?', (matricula))
        conexao.commit()
        print("Usuário removido com sucesso")
    except pyodbc.Error as e:
        print("Erro ao remover usuários, verifique os dados. erro:", e)
    del conexao

except pyodbc.Error as e:
    print ("error in conection:", e)
