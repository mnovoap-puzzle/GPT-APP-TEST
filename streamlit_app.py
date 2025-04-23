import streamlit as st
import openai
import os
# ✅ Set up Streamlit page (must be first Streamlit command)
st.set_page_config(page_title="ChatGPT in Streamlit", layout="centered")

# ✅ Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# 🚀 Title and description
st.title("🤖 ChatGPT Assistant")
st.markdown("Ask anything, and ChatGPT will reply right here in your browser.")

# 💬 User input
user_input = st.text_area("Type your question here:")

# 📤 Submit button
if st.button("Send") and user_input.strip():
    with st.spinner("Waiting for ChatGPT to respond..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # You can switch to "gpt-4" if you have access
                messages=[
                    {"role": "system", "content": "You are a helpful and concise assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response['choices'][0]['message']['content']
            st.markdown("**ChatGPT’s reply:**")
            st.success(reply)
        except Exception as e:
            st.error(f"Error communicating with ChatGPT: {e}")