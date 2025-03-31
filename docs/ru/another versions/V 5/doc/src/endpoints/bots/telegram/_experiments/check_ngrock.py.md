# Проверка Ngrok

## Обзор

Этот модуль содержит пример кода для отправки POST-запроса к API, предположительно, работающему через Ngrok. Он демонстрирует отправку данных в формате JSON и обработку ответа от сервера.

## Подробней

Этот код предназначен для проверки работоспособности туннеля Ngrok и взаимодействия с API, размещенным локально. Он полезен для тестирования и отладки веб-сервисов, доступных через Ngrok.

## Переменные

- `url` (str): URL API, в данном случае `"127.0.0.1:8443"`.
- `headers` (dict): Заголовки для HTTP-запроса, содержащие токен авторизации и тип контента.
- `data` (dict): Данные, отправляемые в теле POST-запроса в формате JSON.
- `response` (requests.Response): Объект ответа от сервера.

## Функции

### `requests.post`

```python
response = requests.post(url, headers=headers, json=data)
```

**Как работает функция**:

Функция `requests.post` отправляет POST-запрос по указанному URL с заданными заголовками и данными. Затем проверяет статус код ответа. В случае успешного запроса (код 200) выводит сообщение об успехе и JSON-ответ. В случае ошибки выводит код ошибки и текст ответа.

**Параметры**:

- `url` (str): URL, на который отправляется POST-запрос.
- `headers` (dict): Заголовки запроса.
- `json` (dict): Данные для отправки в формате JSON.

**Возвращает**:

- `response` (requests.Response): Объект ответа от сервера.

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
```