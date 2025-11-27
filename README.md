# MailNinja

MailNinja to aplikacja napisana w Pythonie przy użyciu frameworka Streamlit, która wspiera użytkownika w zarządzaniu wiadomościami e-mail. Oferuje funkcjonalności takie jak generowanie skrótów wiadomości, ocenianie priorytetu wiadomości, sugerowanie odpowiedzi oraz wspieranie tworzenia zadań w systemie JIRA.

---

## Kluczowe funkcje

### 1. Generowanie skrótu wiadomości
  - Automatyczne generowanie zwięzłej wersji treści wiadomości e-mail.

### 2. Ocena priorytetu
  - Aplikacja analizuje wiadomość i określa jej priorytet (np. wysoki, średni, niski).

### 3. Sugerowanie odpowiedzi
  - Propozycja odpowiedzi w jednym z predefiniowanych stylów:
    - **Oficjalny**
    - **Profesjonalny**
    - **Koleżeński**
  - Wybór jednej z przygotowanych predefiniowanych treści odpowiedzi:
    - "Zajmę się tym."
    - "Obecnie jestem zajęty."
    - "To temat dla zespołu lub osoby X."

### 4. Generowanie zarysu zadania w JIRA
  - Tworzenie propozycji zadania w systemie JIRA na podstawie treści wiadomości.
  - Możliwość dodania późniejszej integracji z JIRA.

---

## Struktura projektu

Projekt posiada czytelną strukturę, podzieloną na dwa podstawowe części:

- `src/` - Katalog zawierający kod źródłowy aplikacji.
- `tests/` - Katalog zawierający testy sprawdzające poprawność działania aplikacji.

---

## Wymagania

### Technologie
- Python
- Streamlit do interfejsu użytkownika

### Dodatki
- Możliwość rozszerzenia specyfikacji o szczegóły implementacyjne w trakcie rozwoju projektu.
- Przyszłościowa integracja z systemem JIRA.

---

## Instalacja

1. Sklonuj repozytorium:

