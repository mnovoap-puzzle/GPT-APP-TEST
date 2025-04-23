import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


import openai
import os

# Configura tu clave API aquí o como variable de entorno
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# Título y descripción
st.set_page_config(page_title="ChatGPT en Streamlit", layout="centered")
st.title("🤖 ChatGPT Assistant")
st.markdown("Hazle preguntas a ChatGPT directamente desde esta app.")

# Input del usuario
user_input = st.text_area("Escribe tu pregunta aquí:")

# Botón de enviar
if st.button("Enviar") and user_input.strip():
    with st.spinner("Esperando respuesta de ChatGPT..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # O "gpt-4" si tienes acceso
                messages=[
                    {"role": "system", "content": "Eres un asistente útil y conciso."},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response['choices'][0]['message']['content']
            st.markdown("**Respuesta de ChatGPT:**")
            st.success(reply)
        except Exception as e:
            st.error(f"Error al contactar con ChatGPT: {e}")
