# Модуль для проверки ngrok

## Обзор

Модуль содержит пример кода для отправки POST-запроса к API, предположительно, развернутому через ngrok. Код демонстрирует отправку данных в формате JSON и обработку ответа от API.

## Подробнее

Этот код используется для тестирования и взаимодействия с API, доступным через ngrok. Он может быть полезен для отладки и проверки работоспособности API в процессе разработки.

## Функции

### Отправка POST-запроса и обработка ответа

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

**Назначение**: Отправляет POST-запрос к API и обрабатывает полученный ответ.

**Параметры**:
- Нет явных параметров, но используются переменные:
    - `url` (str): URL API, к которому отправляется запрос.
    - `headers` (dict): Заголовки запроса, включая токен авторизации и тип контента.
    - `data` (dict): Данные, отправляемые в теле запроса в формате JSON.
    - `response` (requests.Response): Объект ответа от сервера.

**Возвращает**:
- Нет явного возвращаемого значения. Функция печатает результат выполнения запроса в консоль.

**Вызывает исключения**:
- Не обрабатывает исключения напрямую, но может возникнуть `requests.exceptions.RequestException` при проблемах с отправкой запроса.

**Как работает функция**:

1.  **Определение переменных:**
    - `url` - определяет URL API, к которому будет отправлен запрос.
    - `headers` - определяет заголовки запроса, включая авторизационный токен и тип контента (JSON).
    - `data` - определяет данные, которые будут отправлены в теле запроса в формате JSON.

2.  **Отправка POST-запроса:**
    - Используется библиотека `requests` для отправки POST-запроса по указанному `url` с заданными `headers` и `data`.
    - Результат запроса сохраняется в переменной `response`.

3.  **Обработка ответа:**
    - Проверяется статус код ответа (`response.status_code`).
    - Если статус код равен 200 (успешно), то печатается сообщение "Успешно:" и JSON-ответ (`response.json()`).
    - Если статус код отличается от 200, то печатается сообщение "Ошибка:", статус код и текст ошибки (`response.text`).

```mermaid
graph TD
    A[Определение URL, заголовков и данных] --> B{Отправка POST-запроса};
    B -- Успешно (status_code == 200) --> C[Печать "Успешно" и JSON-ответа];
    B -- Ошибка (status_code != 200) --> D[Печать "Ошибка", status_code и текста ошибки];
    C --> E[Конец];
    D --> E;
```

**Примеры**:

1.  Успешный запрос:

```python
import requests

url = "http://example.com/api"
headers = {
    "Authorization": "Bearer valid_token",
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

2.  Неудачный запрос (неверный URL):

```python
import requests

url = "invalid_url"
headers = {
    "Authorization": "Bearer valid_token",
    "Content-Type": "application/json"
}
data = {
    "key1": "value1",
    "key2": "value2"
}

try:
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Успешно:", response.json())
    else:
        print("Ошибка:", response.status_code, response.text)
except requests.exceptions.RequestException as ex:
    print(f"Ошибка подключения: {ex}")