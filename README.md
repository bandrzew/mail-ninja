# MailNinja

MailNinja to aplikacja wspierająca zarządzanie wiadomościami e-mail, budowana przy użyciu Streamlit i Flask. Projekt integruje analizę treści wiadomości za pomocą API Azure OpenAI i pozwala na wybór stylu odpowiedzi oraz predefiniowanych opcji.

## Wymagane zależności

Aby uruchomić aplikację, konieczne jest zainstalowanie poniższych pakietów:

### Instalacja zależności

```bash
pip install -r requirements.txt
```

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