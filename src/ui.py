import streamlit as st
import yaml
from azure_openai_client import AzureOpenAIClient

# Load styles
with open("src/styles.yml", "r") as file:
    styles = yaml.safe_load(file)["styles"]


def display_priority(priority):
    """Wyświetla priorytet wiadomości z odpowiednim emoji."""
    emoji = {
        3: "🚨",  # High priority - urgent
        2: "⚡",  # Medium priority - important
        1: "✅"   # Low priority - can wait
    }
    priority_names = {
        3: "Wysoki",
        2: "Średni",
        1: "Niski"
    }
    return f"{emoji.get(priority, '⚪')} {priority_names.get(priority, 'Nieznany')}"


def initialize_session_state():
    """Ensure the session state has the necessary keys initialized."""
    if "response" not in st.session_state:
        st.session_state["response"] = None


def main():
    initialize_session_state()

    st.title("MailNinja")
    st.header("Wklej treść maila do analizy")

    user_input = st.text_area("Treść maila:", height=200)

    st.header("Wybierz styl odpowiedzi")
    style = st.selectbox("Styl odpowiedzi:", options=[
        style["name"] for style in styles])

    if st.button("Rozpocznij analizę", type="primary", use_container_width=False):
        if user_input:
            selected_style_name = style
            selected_style = next(
                style for style in styles if style["name"] == selected_style_name
            )

            with st.spinner('🔄 Analizuję wiadomość i generuję odpowiedzi...'):
                client = AzureOpenAIClient()
                response = client.get_response(
                    user_input, selected_style["description"])

            if response:
                # Zapisz odpowiedź w pamięci sesji
                st.session_state["response"] = response
            else:
                st.error("Nie udało się uzyskać odpowiedzi od Azure OpenAI.")
        else:
            st.warning(
                "Proszę wprowadź treść maila przed rozpoczęciem analizy.")

    # Pobierz wygenerowaną odpowiedź z pamięci sesji
    response = st.session_state["response"]

    if response:
        st.markdown("""
            <style>
            .analysis-card {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2rem;
                border-radius: 1rem;
                color: white;
                margin: 1rem 0;
            }
            .priority-badge {
                display: inline-block;
                padding: 0.5rem 1rem;
                background: rgba(255, 255, 255, 0.2);
                border-radius: 2rem;
                font-weight: 600;
                margin-bottom: 1rem;
            }
            .summary-text {
                font-size: 1.1rem;
                line-height: 1.6;
                margin-top: 0.5rem;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="analysis-card">
                <strong>⏱️ Priorytet:</strong><br>
                <div class="priority-badge">
                    {display_priority(response.priority)}
                </div>
                <div class="summary-text">
                    <strong>📝 Analiza wiadomości:</strong><br>
                    {response.summary}
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.divider()

        st.subheader("📨 Sugerowane odpowiedzi")

        tabs = st.tabs(
            [f"Odpowiedź {idx + 1}" for idx in range(len(response.responses))])

        for idx, (tab, individual_response) in enumerate(zip(tabs, response.responses)):
            with tab:
                st.markdown("### 💡 Charakterystyka")
                st.info(individual_response.summary)

                st.markdown("### ✉️ Treść odpowiedzi")
                # Use Streamlit's text area for copy functionality
                st.code(body=individual_response.content, height="stretch", wrap_lines=True)


if __name__ == "__main__":
    main()
