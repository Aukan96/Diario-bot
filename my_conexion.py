#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import mysql.connector
'''
base de datos: diario_bot
tabla: usuarios
    columnas: 
    usuario, clave Primaria varchar(100)
    apellido	varchar(50)
    genero	varchar(10)
    password	varchar(30

'''

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '1234root' 
DB_NAME = 'diario_bot' 

def run_query(query):

    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 

    conn = MySQLdb.connect(*datos) 
    cursor = conn.cursor()          
    cursor.execute(query) 
    if query.startswith('SELECT'):
        date = cursor.fetchall() 
        for i in date:
            data = i[0]
    elif query.startswith('INSERT'):
        data = "registrado" 
    elif query.startswith('CREATE'):
        data='tabla registrada'
    else:             
        data = None  

    conn.commit() 
    cursor.close()                 
    conn.close() 
 
    return data
