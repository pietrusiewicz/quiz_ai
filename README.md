# Quiz AI

## Opis Projektu
Quiz AI to prosta aplikacja do quizów, którą zasila Flask w Pythonie. Aplikacja umożliwia
tworzenie pytań, dodawanie odpowiedzi oraz sprawdzanie poprawności odpowiedzi przez użytkownika.

## Wymagania
- Python 3.11.4+
- Flask (instalacja: `pip install flask`)
- Edytor tekstowy (excel-like aplikacja albo notatnik)

## Instalacja
1. Sklonuj repozytorium:
   ```sh
   git clone https://github.com/pietrusiewicz/quiz_ai.git
   cd quiz_ai
   ```
2. Utwórz środowisko wirtualne (zalecane):
   ```sh
   python -m venv venv
   source venv/bin/activate  # na Windows użyj `venv\Scripts\activate`
   ```
3. Zainstaluj zależności:
   ```sh
   pip install -r requirements.txt
   ```

## Uruchomienie Aplikacji
1. Upewnij się, że środowisko wirtualne jest aktywowane.
2. Uruchom aplikację:
   ```sh
   python app.py
   ```
Aplikacja powinna być dostępna pod adresem `http://127.0.0.1:5000/`.

## Struktura Projektu
```
quiz_ai/
├── app.py                # Główny plik aplikacji Flask
├── templates/            # Szablony HTML
│   └── index.html        # Strona główna z quizem
├── static/               # Folder dla plików statycznych (CSS, JS)
└── requirements.txt      # Lista zależności
```

## Funkcjonalności
1. **Tworzenie Pytań**: Możesz dodawać pytania do quizu, podając pytanie oraz co najmniej dwie opcje odpowiedzi.
2. **Dodawanie Odpowiedzi**: Każde pytanie może mieć wiele opcji odpowiedzi.
3. **Sprawdzanie Poprawności Odpowiedzi**: Użytkownik podaje odpowiedź na każde pytanie, a aplikacja automatycznie
sprawdza poprawność odpowiedzi.

## Jak Dodawać/Edytować Pytania
1. Przejdź do środkowej części strony.
2. Kliknij przycisk "Dodaj Pytanie" lub podobny.
3. Wypełnij formularz pytaniem oraz odpowiedziami.

## Jak Uruchamiać Testy
1. Upewnij się, że środowisko wirtualne jest aktywowane.
2. Uruchom testy:
   ```sh
   pytest
   ```

## Kontakt
Jeśli masz pytania lub napotkasz problemy, prosimy o kontakt pod adresem email
kacper.pietrusiewicz@o2.pl
