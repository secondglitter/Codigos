from nltk.chat.util import Chat, reflections

# Define patrones de expresiones regulares y respuestas
pairs = [
    ["Hola", ["¡Hola!", "Hola, ¿cómo estás?", "¿Cómo puedo ayudarte?"]],
    ["¿Cómo te llamas?", ["Soy un chatbot. ¿Y tú?", "Puedes llamarme ChatBot."]],
    ["Adiós", ["¡Adiós!", "Hasta luego.", "Que tengas un buen día."]],
    # Agrega más patrones y respuestas según sea necesario
]

# Crea un objeto de chat con los pares de patrones y respuestas
chatbot = Chat(pairs, reflections)

# Bucle de conversación
print("¡Bienvenido al chatbot! Escribe 'salir' para terminar.")
while True:
    # Espera el mensaje del usuario
    user_input = input("Usuario: ")
    
    # Salir si el usuario escribe 'salir'
    if user_input.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    # Obtén la respuesta del chatbot para el mensaje del usuario
    response = chatbot.respond(user_input)
    
    # Muestra la respuesta del chatbot
    print("Chatbot:", response)
