import mysql.connector

def conectar():
   #Establece la conxion con la base de datos
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='libreria'
    )
    return conn



