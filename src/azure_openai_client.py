import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from models import MessageResponse


class AzureOpenAIClient:
    def __init__(self):
        load_dotenv()
        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
            api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", ""),
        )
        self.model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")

    def get_response(self, user_input, style_description):
        """Get structured response using Pydantic model"""
        try:
            prompt = (
                "Zwięźle podsumuj poniższą wiadomość, określ jej priorytet i wygeneruj trzy różne odpowiedzi różniące się treścią, "
                "każda ze swoim podsumowaniem.\n"
                f"Styl odpowiedzi: {style_description}\n"
                f"Treść wiadomości: {user_input}\n"
                "Priorytet powinien być: 'niski', 'średni' lub 'wysoki'."
            )

            response = self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format=MessageResponse,
            )

            return response.choices[0].message.parsed

        except Exception as e:
            print(f"Error in getting response: {e}")
            return None
