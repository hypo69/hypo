# Модуль `gemini.py`

## Обзор

Модуль `gemini.py` представляет собой FastAPI приложение, которое предоставляет API для взаимодействия с моделью Google Generative AI. Приложение принимает запросы с приглашением (prompt) и возвращает ответ от модели.

## Импорты

```
import header 
from flask import Flask, request, jsonify
from src.ai.google_generativeai.generative_ai import GoogleGenerativeAI
```

## Переменные

```
MODE = 'development'
```

## Классы

### `GoogleGenerativeAI`

**Описание**:  Класс `GoogleGenerativeAI` представляет собой обертку для доступа к модели Google Generative AI.

**Методы**:
- `ask(prompt)`: Запрашивает ответ от модели на заданный prompt.


## Функции

### `ask`

**Описание**: Обрабатывает входящий запрос и возвращает ответ от модели.

**Параметры**:
- `data` (dict): Словарь, содержащий данные запроса, полученные из `request.get_json()`.
- `prompt` (str): Приглашение (prompt) для модели.

**Возвращает**:
- `jsonify({"reply": reply})` (dict): Ответ в формате JSON, содержащий полученный ответ модели (reply). Возвращает код 200.
- `jsonify({"error": "No prompt provided"}), 400` (dict):  Возвращает ошибку 400, если prompt не предоставлен.
- `jsonify({"error": str(e)}), 500` (dict):  Возвращает ошибку 500, если произошла ошибка во время выполнения запроса.

**Вызывает исключения**:
- `Exception`: Любое исключение, которое может возникнуть во время взаимодействия с моделью Google Generative AI. Обработка ошибок осуществляется блоком `try...except`.


## Точка входа

```python
if __name__ == '__main__':
    app.run(debug=True)
```

**Описание**: Запускает приложение Flask в отладочном режиме (debug=True), что позволяет быстро исправлять ошибки и отображать отладочную информацию.
