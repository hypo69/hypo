# Модуль `gemini.py`

## Обзор

Модуль `gemini.py` представляет собой веб-сервис на основе Flask, который предоставляет API для взаимодействия с моделью Google Gemini AI. Он принимает текстовый запрос от клиента и возвращает ответ сгенерированный моделью.

## Оглавление

- [Функции](#Функции)
    - [`ask`](#ask)

## Функции

### `ask`

**Описание**: Функция обрабатывает POST-запросы к эндпоинту `/ask`. Она получает текстовый запрос от клиента, отправляет его в модель Google Gemini AI и возвращает сгенерированный ответ.

**Параметры**:
- `request` (flask.Request): Объект запроса Flask, содержащий данные от клиента.

**Возвращает**:
- `flask.Response`: JSON-ответ, содержащий либо ответ модели в поле `reply`, либо сообщение об ошибке в поле `error`.
    - В случае успеха: `{"reply": "сгенерированный ответ"}`
    - В случае ошибки: `{"error": "сообщение об ошибке"}`

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время обработки запроса к модели Google Gemini AI.

```python
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        reply = ai_model.ask(prompt)
        return jsonify({"reply": reply})
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
```