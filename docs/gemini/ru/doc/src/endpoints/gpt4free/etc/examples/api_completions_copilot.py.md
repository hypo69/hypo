# Модуль для тестирования API Copilot

## Обзор

Данный модуль предназначен для тестирования API Copilot, в частности, отправки запросов к эндпоинту `/v1/chat/completions` и обработки потоковых ответов. Он демонстрирует, как отправлять сообщения и получать ответы от Copilot.

## Подробнее

Модуль отправляет POST-запросы к API Copilot и обрабатывает потоковые ответы, выводя полученные данные в консоль.  Он инициализирует conversation_id и отправляет несколько сообщений для поддержания диалога.
## Функции

### Отправка запроса к API Copilot и обработка ответа

```python
import requests
import json
import uuid

url = "http://localhost:1337/v1/chat/completions"
conversation_id = str(uuid.uuid4())
body = {
    "model": "",
    "provider": "Copilot",
    "stream": True,
    "messages": [
        {"role": "user", "content": "Hello, i am Heiner. How are you?"}
    ],
    "conversation_id": conversation_id
}
response = requests.post(url, json=body, stream=True)
response.raise_for_status()
for line in response.iter_lines():
    if line.startswith(b"data: "):
        try:
            json_data = json.loads(line[6:])
            if json_data.get("error"):
                print(json_data)
                break
            content = json_data.get("choices", [{"delta": {}}])[0]["delta"].get("content", "")
            if content:
                print(content, end="")
        except json.JSONDecodeError:
            pass

body = {
    "model": "",
    "provider": "Copilot",
    "stream": True,
    "messages": [
        {"role": "user", "content": "Tell me somethings about my name"}
    ],
    "conversation_id": conversation_id
}
response = requests.post(url, json=body, stream=True)
response.raise_for_status()
for line in response.iter_lines():
    if line.startswith(b"data: "):
        try:
            json_data = json.loads(line[6:])
            if json_data.get("error"):
                print(json_data)
                break
            content = json_data.get("choices", [{"delta": {}}])[0]["delta"].get("content", "")
            if content:
                print(content, end="")
        except json.JSONDecodeError:
            pass
```

**Назначение**: Отправляет запросы к API Copilot и обрабатывает ответы.

**Параметры**:

- Нет явных параметров, но используются переменные `url`, `conversation_id` и `body` для формирования запроса.

**Как работает функция**:

1.  **Инициализация**:
    *   Устанавливает URL эндпоинта API Copilot: `url = "http://localhost:1337/v1/chat/completions"`.
    *   Генерирует уникальный идентификатор для conversation_id.

2.  **Отправка первого запроса**:
    *   Формирует тело запроса `body` с сообщением "Hello, i am Heiner. How are you?".
    *   Отправляет POST-запрос к API с указанным телом и потоковой передачей данных (`stream=True`).

3.  **Обработка потокового ответа**:
    *   Итерируется по каждой строке в ответе.
    *   Проверяет, начинается ли строка с `b"data: "`.
    *   Пытается распарсить JSON-данные из строки.
    *   Проверяет наличие поля "error" в JSON-данных и, если оно есть, выводит сообщение об ошибке и прерывает цикл.
    *   Извлекает содержимое ответа из поля "content" и выводит его в консоль.
    *   Обрабатывает исключение `json.JSONDecodeError`, если не удается распарсить JSON.

4.  **Отправка второго запроса**:
    *   Формирует тело запроса `body` с сообщением "Tell me somethings about my name".
    *   Отправляет POST-запрос к API с указанным телом и потоковой передачей данных (`stream=True`).

5.  **Обработка потокового ответа (повторно)**:
    *   Повторяет шаги обработки потокового ответа, как и для первого запроса.

```
Инициализация URL и conversation_id
↓
Формирование тела первого запроса (Приветствие)
↓
Отправка POST-запроса (Приветствие)
↓
Обработка потокового ответа:
    → Проверка начала строки с "data: "
    ↓
    → Попытка распарсинга JSON
    ↓
    → Проверка наличия ошибки в JSON
    ↓
    → Извлечение и вывод содержимого
↓
Формирование тела второго запроса (Информация об имени)
↓
Отправка POST-запроса (Информация об имени)
↓
Обработка потокового ответа (повторно):
    → Проверка начала строки с "data: "
    ↓
    → Попытка распарсинга JSON
    ↓
    → Проверка наличия ошибки в JSON
    ↓
    → Извлечение и вывод содержимого
```

**Примеры**:

```python
import requests
import json
import uuid

# URL эндпоинта API
url = "http://localhost:1337/v1/chat/completions"

# Генерация conversation_id
conversation_id = str(uuid.uuid4())

# Тело запроса для приветствия
body_hello = {
    "model": "",
    "provider": "Copilot",
    "stream": True,
    "messages": [
        {"role": "user", "content": "Hello, i am Heiner. How are you?"}
    ],
    "conversation_id": conversation_id
}

# Тело запроса для информации об имени
body_name = {
    "model": "",
    "provider": "Copilot",
    "stream": True,
    "messages": [
        {"role": "user", "content": "Tell me somethings about my name"}
    ],
    "conversation_id": conversation_id
}

# Отправка запроса и обработка ответа для приветствия
response_hello = requests.post(url, json=body_hello, stream=True)
response_hello.raise_for_status()
print("Response to Hello:")
for line in response_hello.iter_lines():
    if line.startswith(b"data: "):
        try:
            json_data = json.loads(line[6:])
            if json_data.get("error"):
                print(json_data)
                break
            content = json_data.get("choices", [{"delta": {}}])[0]["delta"].get("content", "")
            if content:
                print(content, end="")
        except json.JSONDecodeError:
            pass
print("\n")

# Отправка запроса и обработка ответа для информации об имени
response_name = requests.post(url, json=body_name, stream=True)
response_name.raise_for_status()
print("Response to Name:")
for line in response_name.iter_lines():
    if line.startswith(b"data: "):
        try:
            json_data = json.loads(line[6:])
            if json_data.get("error"):
                print(json_data)
                break
            content = json_data.get("choices", [{"delta": {}}])[0]["delta"].get("content", "")
            if content:
                print(content, end="")
        except json.JSONDecodeError:
            pass
print("\n")