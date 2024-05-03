import streamlit as st
import json
import random

# Cargar el JSON con las respuestas del bot
@st.cache(allow_output_mutation=True)
def cargar_respuestas():
    with open("respuestas.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Función para obtener una respuesta basada en la entrada del usuario
def obtener_respuesta(entrada, data):
    for respuesta in data["respuestas"]:
        if entrada.lower() in respuesta["intentos"]:
            return random.choice(respuesta["respuestas"])
    return "Lo siento, no entendí eso. ¿Podrías repetirlo?"

# Configuración de la aplicación Streamlit
def main():
    st.title("Chatbot Simple")
    st.set_option('deprecation.showfileUploaderEncoding', False) # Configuración de la codificación
    data = cargar_respuestas()
    
    historial = st.session_state.get("historial", [])
    if not historial:
        st.session_state.historial = [{"role": "bot", "message": "Hola, ¿en qué puedo ayudarte?"}]
    
    entrada_usuario = st.text_input("Tú:")
    if entrada_usuario:
        st.session_state.historial.append({"role": "user", "message": entrada_usuario})
        respuesta_bot = obtener_respuesta(entrada_usuario, data)
        st.session_state.historial.append({"role": "bot", "message": respuesta_bot})
    
    for mensaje in st.session_state.historial:
        if mensaje["role"] == "user":
            st.text_input("Tú:", value=mensaje["message"], disabled=True)
        else:
            st.text_area("Bot:", value=mensaje["message"], height=100, disabled=True)

if __name__ == "__main__":
    main()
