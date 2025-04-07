# Модуль для проверки ngrok

## Обзор

Этот модуль содержит пример кода для отправки POST-запроса к API, предположительно размещенному на локальном сервере ngrok. Он демонстрирует, как установить заголовки авторизации и отправить данные JSON.

## Подробнее

Этот код используется для тестирования и взаимодействия с API, который может быть временно доступен через ngrok. Он включает в себя отправку данных и обработку ответа от API.

## Функции

### `Отправка POST-запроса`

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

**Назначение**: Отправляет POST-запрос к API и обрабатывает ответ.

**Параметры**:
- `url` (str): URL API, к которому отправляется запрос.
- `headers` (dict): Заголовки запроса, включающие авторизацию и тип контента.
- `data` (dict): Данные, отправляемые в теле запроса в формате JSON.
- `response` (requests.Response): Объект ответа от API.

**Как работает функция**:

1. **Определение URL API**: Устанавливает URL API, к которому будет отправлен POST-запрос.
2. **Определение заголовков**: Устанавливает заголовки, включая токен авторизации и тип контента (application/json).
3. **Определение данных**: Устанавливает данные, которые будут отправлены в теле запроса в формате JSON.
4. **Отправка POST-запроса**: Использует библиотеку `requests` для отправки POST-запроса с указанными URL, заголовками и данными.
5. **Обработка ответа**: Проверяет статус код ответа. Если код 200, выводит сообщение об успехе и JSON-содержимое ответа. В противном случае выводит сообщение об ошибке, статус код и текст ответа.

```
URL_API --> Заголовки --> Данные
|
POST-запрос (requests.post)
|
Ответ (response)
|
Проверка статус кода
|
Успех: Вывод JSON-содержимого
|
Ошибка: Вывод статус кода и текста
```

**Примеры**:

```python
import requests

# Пример 1: Успешный запрос
url = "http://example.com/api"
headers = {"Authorization": "Bearer token", "Content-Type": "application/json"}
data = {"key": "value"}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Успешно:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)
```

```python
import requests

# Пример 2: Неуспешный запрос
url = "http://example.com/api"
headers = {"Authorization": "Bearer token", "Content-Type": "application/json"}
data = {"key": "value"}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Успешно:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)