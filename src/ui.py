import streamlit as st
import yaml
from azure_openai_client import AzureOpenAIClient

# Load styles
with open("src/styles.yml", "r") as file:
    styles = yaml.safe_load(file)["styles"]


def display_priority(priority):
    """Wyświetla priorytet wiadomości z odpowiednim emoji."""
    emoji = {
        "wysoki": "🔴",
        "średni": "🟠",
        "niski": "🟢"
    }
    return f"{emoji.get(priority.lower(), '⚪')} {priority.capitalize()}"


def main():
    st.title("MailNinja: Automatyczna Analiza Wiadomości E-mail")

    st.header("Wklej treść maila do analizy")
    user_input = st.text_area("Treść maila:", height=200)

    st.header("Wybierz styl odpowiedzi")
    style = st.selectbox("Styl odpowiedzi:", options=[
                         style["name"] for style in styles])

    if st.button("Rozpocznij analizę"):
        if user_input:
            selected_style_name = style  # Wybrana nazwa stylu z selectbox
            selected_style = next(
                style for style in styles if style["name"] == selected_style_name
            )
            client = AzureOpenAIClient()
            response = client.get_response(
                user_input, selected_style["description"])

            if response:
                priority = response.get("priority", "Brak priorytetu")
                summary = response.get("summary", "Brak podsumowania")
                responses = response.get("responses", [])

                st.subheader("Priorytet wiadomości:")
                st.write(display_priority(priority))
                st.subheader("Podsumowanie wiadomości:")
                st.write(summary)

                st.subheader("Odpowiedzi:")
                for idx, individual_response in enumerate(responses):
                    st.write(f"Odpowiedź {idx + 1}: {individual_response}")
            else:
                st.error("Nie udało się uzyskać odpowiedzi od Azure OpenAI.")
        else:
            st.warning(
                "Proszę wprowadź treść maila przed rozpoczęciem analizy.")


if __name__ == "__main__":
    main()
