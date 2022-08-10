from class_info import *

import mysql.connector
class Fabric:
    def __init__(self):
        self.con = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'q1w2e3',
            database = 'cafeteria'

        )
        self.curs = self.con.cursor()
        self.nomEmpr = []
        


    def cadastro_fabric(self,nomEmp):
        print("|■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■|")
        sql_command = f'insert into fabricante (nomeFabri) values ("{nomEmp}")' 
        self.nomEmpr.append(nomEmp)
        self.curs.execute(sql_command)
        self.con.commit()
        print('Empresa cadastrada com Sucesso!!!')
        print("|■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■|")
        
        
        
