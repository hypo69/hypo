# Документация для модуля `check_ngrock.py`

## Обзор

Данный модуль содержит пример кода для отправки POST-запроса к API и обработки ответа. Используется библиотека `requests` для выполнения HTTP-запросов.

## Подробней

Этот код демонстрирует, как можно отправить POST-запрос к указанному URL (`127.0.0.1:8443`) с использованием библиотеки `requests`. В коде определены заголовки, включающие токен авторизации, и данные, которые будут отправлены в формате JSON. После отправки запроса обрабатывается ответ: в случае успешного запроса (код 200) выводится JSON-ответ, иначе выводится код ошибки и текст ответа.

## Функции

### Отправка POST-запроса

```python
import requests

# URL API
url = "127.0.0.1:8443"

# Заголовки
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN",
    "Content-Type": "application/json"
}

# Данные для отправки
data = {
    "key1": "value1",
    "key2": "value2"
}

# Отправка POST-запроса
response = requests.post(url, headers=headers, json=data)

# Обработка ответа
if response.status_code == 200:
    print("Успешно:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)
```

**Описание**: Пример отправки POST-запроса к API и обработки ответа.

**Параметры**:
- `url` (str): URL API для отправки запроса.
- `headers` (dict): Заголовки запроса, включающие токен авторизации и тип контента.
- `data` (dict): Данные для отправки в формате JSON.
- `response` (requests.Response): Объект ответа от сервера.

**Возвращает**:
- `None`: Функция ничего не возвращает явно, но выводит результаты в консоль.

**Примеры**:

Пример успешного запроса:

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
# Успешно: {'message': 'Data received successfully'}
```

Пример неуспешного запроса:

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
# Ошибка: 404 Not Found
```