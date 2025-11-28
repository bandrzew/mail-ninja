import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

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
        attempt = 0
        max_attempts = 3

        while attempt < max_attempts:
            try:
                prompt = (
                    f"Podsumuj poniższą wiadomość, określ jej priorytet i wygeneruj trzy różne odpowiedzi w formie JSON:\n"
                    f"Styl odpowiedzi: {style_description}\n"
                    f"Treść wiadomości: {user_input}\n"
                    "Format odpowiedzi:\n"
                    '{"priority": "<niski/średni/wysoki>", "summary": "<podsumowanie>", "responses": ["<odpowiedź_1>", "<odpowiedź_2>", "<odpowiedź_3>"]}'
                )

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
                content = response.choices[0].message.content

                try:
                    return json.loads(content)
                except json.JSONDecodeError:
                    print(f"Invalid JSON response: {content}")
                    attempt += 1
                    continue
            except Exception as e:
                print(f"Error in getting response: {e}")
                attempt += 1

                return None
