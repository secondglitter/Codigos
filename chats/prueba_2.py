import json
import random

def cargar_respuestas():
    with open("chats/respuestas.json", "r", encoding="utf-8") as file:
        return json.load(file)

def manejar_respuesta_invalida():
    mensajes_error = ["Lo siento, no comprendo eso.", "No estoy seguro de entender. ¿Podrías explicar más?", "Parece que estoy teniendo dificultades para entender. ¿Podrías reformular tu pregunta?"]
    print(random.choice(mensajes_error))

def chat():
    # Cargar respuestas desde el archivo JSON
    respuestas = cargar_respuestas()["respuestas"]

    # Saludo inicial
    print("¡Hola! Soy ChatGPT, un chatbot basado en el modelo de lenguaje GPT-3.5 de OpenAI. ¿En qué puedo ayudarte hoy?")

    # Bucle de conversación
    while True:
        # Obtener la entrada del usuario
        mensaje_usuario = input("Tú: ").capitalize()

        # Salir si el usuario escribe 'Adiós'
        if mensaje_usuario == "Adiós":
            print(random.choice(respuestas["Adiós"]))
            break

        # Buscar una respuesta adecuada
        if mensaje_usuario in respuestas:
            print(random.choice(respuestas[mensaje_usuario]))
        else:
            manejar_respuesta_invalida()

# Iniciar el chat
if __name__ == "__main__":
    chat()
