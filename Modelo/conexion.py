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

#Ejecuta un comando SQL (INSERT, UPDATE, DELETE) y retorna True si se ejecutó correctamente.
def ejecutar_comando(query, params=None):
   
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