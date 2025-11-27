import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
st.title("Przykład Chatbota z Azure OpenAI")
user_input = st.text_input("Ty:", "")
if st.button("Wyślij"):
    if user_input:
        client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
            api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", ""),
        )
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", ""),
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
        )
        content = response.choices[0].message.content
        st.write("AI:")
        st.write(content)
    else:
        st.write("Proszę wpisz wiadomość przed wysłaniem.")
