import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "09090909",
    database = "carreras",
    port = "3306"
)

def test_1():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Sistemas")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)

#test_1()