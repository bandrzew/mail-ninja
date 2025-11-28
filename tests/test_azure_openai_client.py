import sys
import os

# Ustawienie ścieżki do folderu src:
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
print("PYTHONPATH ustawiony na src:", sys.path)

from azure_openai_client import AzureOpenAIClient


def test_get_response_integration():
    """Test rzeczywistej integracji z Azure OpenAI."""
    client = AzureOpenAIClient()

    user_input = "Hello, how can I help you?"
    response = client.get_response(user_input, "Formalny")

    assert response is not None
    assert isinstance(response, dict)
    assert "priority" in response
    assert "summary" in response
    assert "responses" in response
