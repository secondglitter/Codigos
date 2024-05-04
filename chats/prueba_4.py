import streamlit as st
import json
import random
import time

# Carga el JSON
with open('respuestas.json', encoding='utf-8') as f:
    json_data = json.load(f)

def get_response(user_input):
    # Recorre las respuestas definidas en el JSON
    for respuesta in json_data["respuestas"]:
        # Verifica si el input del usuario coincide con alguno de los intentos en el tema actual
        if user_input in respuesta["intentos"]:
            # Retorna una respuesta aleatoria del tema actual
            return random.choice(respuesta["respuestas"])
    # Si no hay coincidencias, retorna None
    return None

st.title("Chat bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "first_message" not in st.session_state:
    st.session_state.first_message = True
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # Si el último mensaje es del asistente, hacer que la ventana de Streamlit se desplace hacia abajo
        if message["role"] == "assistant":
            st.markdown('<div style="visibility: hidden;">.</div>', unsafe_allow_html=True)
        
if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿En qué puedo ayudarte?")
        
    st.session_state.messages.append({"role": "assistant", "content" : "Hola, ¿En qué puedo ayudarte?"})
    st.session_state.first_message = False
    
if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Simular un retraso de 3 segundos antes de obtener la respuesta del bot
    time.sleep(1)
    
    # Obtiene la respuesta del bot
    response = get_response(prompt)
    if response:
        with st.chat_message("assistant"):
            st.markdown(f'{response}')
            # Hacer que la ventana de Streamlit se desplace hacia abajo después de la respuesta del bot
            st.markdown('<div style="visibility: hidden;">.</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        with st.chat_message("assistant"):
            st.markdown("Lo siento, no entendí tu pregunta.")
            # Hacer que la ventana de Streamlit se desplace hacia abajo después de la respuesta del bot
            st.markdown('<div style="visibility: hidden;">.</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": "Lo siento, no entendí tu pregunta."})
