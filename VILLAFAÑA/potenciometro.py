#Codigo para que mande la informacion al arduino IDE y a la base de datos

import serial
import time
import mysql.connector

ser = serial.Serial('COM4', 9600)
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="potenciometro"
)

cursor = conexion.cursor()

def enviar_valor_arduino(valor):
    ser.write(valor.encode())
    print(f"Enviado valor al Arduino: {valor}")

while True:
    if ser.in_waiting:
        mensaje = ser.readline().decode('utf-8').rstrip()
        partes = mensaje.split('=')
        if len(partes) == 2:
            clave, valor = partes
            query = "INSERT INTO valores (mensaje, valor) VALUES (%s, %s)"
            cursor.execute(query, (clave, valor))
            conexion.commit()
            print(f"Mensaje desde el Arduino - Clave: {clave}, Valor: {valor}")

            valor_a_enviar = valor
            enviar_valor_arduino(valor_a_enviar)

        else:
            print(f"Error en el formato del mensaje: {mensaje}")
    else:
        print("Error en la conexión")

    time.sleep(2)