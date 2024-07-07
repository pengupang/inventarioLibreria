import mysql.connector
from mysql.connector.fabric.connection import FabricMySQLSet

def conectar():
   #Establece la conxion con la base de datos
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='libreria'
    )
    return conn

#Ejecuta un comando SQL (INSERT, UPDATE, DELETE) y retorna True si se ejecutó correctamente.
def ejecutar_comando(query, params):
   
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

# Ejecuta una consulta SQL (SELECT) y retorna los resultados.
def ejecutar_consulta(query, params=None):
   
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def obtenerAutor():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM autor")
    resultados = cursor.fetchall()
    conn.close()

    return [m[1] for m in resultados]

def obtenerEditorial():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM editorial")
    resultados = cursor.fetchall()
    conn.close()

    return [n[1] for n in resultados]

def comprobarDuplicidad(nomtabla, palabra):
    columna = ''
    if nomtabla == 'libro':
        columna = 'Titulo'
    elif nomtabla == 'autores' or nomtabla == 'editorial' or nomtabla == 'proveedor':
        columna = 'Nombre'
    query = "SELECT {} FROM {} WHERE LOWER({}) = LOWER(\"{}\")".format(columna,nomtabla,columna,palabra)
    print(query)
    resultado = ejecutar_consulta(query)
    if resultado:
        return True
    else:
        return False