import json
import random

# Cargar el JSON con las respuestas del bot
def cargar_respuestas():
    with open("respuestas.json", "r") as file:
        return json.load(file)

# Función para obtener una respuesta basada en la entrada del usuario
def obtener_respuesta(entrada, data):
    for respuesta in data["respuestas"]:
        if entrada.lower() in respuesta["intentos"]:
            return random.choice(respuesta["respuestas"])
    return "Lo siento, no entendí eso. ¿Podrías repetirlo?"

# Loop principal del chatbot
def main():
    data = cargar_respuestas()
    while True:
        entrada_usuario = input("Tú: ")
        respuesta_bot = obtener_respuesta(entrada_usuario, data)
        print("Bot:", respuesta_bot)

if __name__ == "__main__":
    main()
