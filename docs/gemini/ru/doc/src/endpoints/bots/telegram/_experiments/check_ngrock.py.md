# Проверка Ngrok

## Обзор

Этот код предназначен для отправки POST-запроса к API, работающему через Ngrok, и обработки ответа. Он включает в себя настройку URL, заголовков авторизации и данных для отправки.

## Подробнее

Код выполняет следующие шаги:
1. **Определение URL**: Указывается URL API, который обычно предоставляется Ngrok. В данном случае это `127.0.0.1:8443`.
2. **Настройка заголовков**: Заголовки включают авторизационный токен и тип контента (JSON).
3. **Подготовка данных**: Данные для отправки в формате JSON.
4. **Отправка запроса**: Используется библиотека `requests` для отправки POST-запроса с указанными заголовками и данными.
5. **Обработка ответа**: Проверяется статус код ответа и выводится соответствующее сообщение об успехе или ошибке.

## Функции

### `requests.post`

```python
response = requests.post(url, headers=headers, json=data)
```

**Описание**: Отправляет POST-запрос на указанный URL с заданными заголовками и данными в формате JSON.

**Параметры**:
- `url` (str): URL для отправки запроса.
- `headers` (dict): Заголовки запроса.
- `json` (dict): Данные для отправки в формате JSON.

**Возвращает**:
- `response` (requests.Response): Объект ответа от сервера.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: В случае проблем с сетевым запросом.

**Примеры**:

```python
import requests

url = "127.0.0.1:8443"
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN",
    "Content-Type": "application/json"
}
data = {
    "key1": "value1",
    "key2": "value2"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Успешно:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)