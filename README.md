# MailNinja

MailNinja to aplikacja wspierająca zarządzanie wiadomościami e-mail, budowana przy użyciu Streamlit i Flask. Projekt integruje analizę treści wiadomości za pomocą API Azure OpenAI i pozwala na wybór stylu odpowiedzi oraz predefiniowanych opcji.

## Wymagane zależności

Aby uruchomić aplikację, konieczne jest zainstalowanie poniższych pakietów:

### Instalacja zależności

```bash
pip install -r requirements.txt
```

Jeśli nie ma pliku `requirements.txt`, poniżej lista kluczowych pakietów:

```bash
pip install flask streamlit azure-openai pyyaml python-dotenv
```

## Pliki projektu

### `src/mcp_server.py`
- Implementacja logiczna endpointu `/analyze` przy użyciu Flask.
- Interfejs HTTP obsługuje dane wejściowe w formacie JSON (`user_input` i `style`) oraz zwraca odpowiedź zgodnie z wybranym stylem.
- Integruje się z klientem Azure OpenAI.

### `src/ui.py`
- Interaktywny interfejs użytkownika zbudowany na Streamlit.
- Pozwala wklejać treści wiadomości, wybierać styl odpowiedzi oraz przeglądać wyniki analizy (priorytet, podsumowanie, odpowiedzi).
- Umożliwia wybór jednej z trzech predefiniowanych odpowiedzi zdefiniowanych w pliku `styles.yml`.

### `src/azure_openai_client.py`
- Klient integracji z Azure OpenAI API.
- Generuje dynamiczne odpowiedzi na podstawie treści wiadomości oraz wybranego stylu.
- Obsługuje retry logic w przypadku błędów API.

### `src/styles.yml`
- Definicja stylów odpowiedzi w formacie YAML.
- Każdy styl zawiera krótki opis i listę predefiniowanych opcji odpowiedzi, wyświetlanych użytkownikowi.

### `tests/test_mcp.py`
- Testuje endpoint `/analyze` pod kątem poprawności działania.
- Obsługuje scenariusze dla prawidłowych danych wejściowych oraz błędnych przypadków.

### `tests/test_azure_openai_client.py`
- Testuje interakcję klienta `AzureOpenAIClient` z API.
- Waliduje format generowanych odpowiedzi JSON dla różnych scenariuszy.

### `scripts/mcp_curl_test.sh`
- Skrypt demonstracyjny testujący endpoint `/analyze` za pomocą cURL (polecany do szybkiego sprawdzenia działania serwera MCP).

### `.env`
- Plik konfiguracyjny zawierający dane takie jak klucz API oraz endpoint Azure OpenAI.

## Jak uruchomić aplikację

### Uruchom serwer MCP

Uruchom serwer Flask na lokalnym hoście:

```bash
source ./venv/bin/activate
python src/mcp_server.py
```

Serwer dostępny pod `http://127.0.0.1:5000/analyze`.

### Uruchom interfejs użytkownika

Uruchom aplikację Streamlit:

```bash
source ./venv/bin/activate
streamlit run src/ui.py
```

Interfejs użytkownika dostępny pod `http://localhost:8501`. Po wprowadzeniu treści wiadomości i wybraniu stylu, aplikacja zwróci wyniki analizy i umożliwi wybór odpowiedzi.

## Przykłady

- **Priorytet:** 🔴 Wysoki
- **Podsumowanie:** "Wiadomość wymaga pilnej odpowiedzi na temat niedoboru zasobów."
- **Odpowiedź:** "Tak, zajmę się tym." (Profesjonalny styl)

### Dalszy rozwój
Projekt można rozbudować m.in. o:
- Zintegrowanie z zewnętrznymi systemami (np. JIRA).
- Rozszerzenie stylów odpowiedzi.
- Optymalizację wydajności endpointów.