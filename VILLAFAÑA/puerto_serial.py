#CODIGO PARA ARDUINO
import serial
import mysql.connector
import time

#dentro de las '' va el puerto del arduino
ser = serial.Serial( 'COM4', 9600)

coneccion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sm-53"
    )

mi_cursor = coneccion.cursor()
 
while True:
    if ser.in_waiting:
        mensaje = ser.readline().decode('utf-8').rstrip().split(", ")

        query = "INSERT INTO tb_puerto_serial (mensaje) VALUES (%s)"

        mi_cursor.execute(query,mensaje)

        coneccion.commit()

        print(f'Mensaje desde el arduino: {mensaje}')

    else:
        print("Error en la coneccion")

    time.sleep(1)