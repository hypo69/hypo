# Модуль для демонстрации API-запросов к Copilot

## Обзор

Этот модуль содержит примеры кода, демонстрирующие отправку запросов к API Copilot для получения ответов в режиме реального времени (stream). Он показывает, как отправлять текстовые запросы и обрабатывать ответы, получаемые в формате JSON.

## Подробнее

Этот код является примером использования API Copilot для обмена сообщениями. Он показывает, как отправлять POST-запросы к API и обрабатывать ответы, которые приходят в режиме реального времени (stream). Код использует библиотеку `requests` для отправки HTTP-запросов и модуль `json` для обработки данных в формате JSON. Он генерирует уникальный идентификатор разговора (`conversation_id`) с помощью модуля `uuid`. При получении данных проверяется наличие ошибок, и извлекается полезное содержимое для отображения пользователю.

## Функции

### Отправка запроса и обработка потокового ответа

Основная функциональность модуля заключается в отправке POST-запроса к API Copilot и обработке потокового ответа. Потоковый ответ позволяет получать данные частями, что полезно для длительных разговоров или генерации текста в реальном времени.

```python
import requests
import json
import uuid
```

**Назначение**: Импортирует необходимые библиотеки для выполнения HTTP-запросов, обработки JSON и генерации UUID.

**Как работает функция**:

1.  Импортирует библиотеку `requests` для отправки HTTP-запросов.
2.  Импортирует библиотеку `json` для работы с данными в формате JSON.
3.  Импортирует библиотеку `uuid` для генерации уникальных идентификаторов.

```python
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
```

**Назначение**: Отправляет первый запрос к API Copilot и обрабатывает потоковый ответ.

**Как работает функция**:

1.  **Определение URL**: Задает URL-адрес API, к которому будет отправлен запрос.
2.  **Генерация ID разговора**: Генерирует уникальный идентификатор разговора (`conversation_id`) с использованием `uuid.uuid4()`.
3.  **Формирование тела запроса**: Создает тело запроса в формате JSON, содержащее:
    *   `model`: Модель, используемая для генерации ответа (в данном случае пустая строка).
    *   `provider`: Провайдер, в данном случае `"Copilot"`.
    *   `stream`: Указывает, что ответ должен быть потоковым (`True`).
    *   `messages`: Список сообщений, отправленных пользователем. В данном случае одно сообщение с текстом "Hello, i am Heiner. How are you?".
    *   `conversation_id`: Уникальный идентификатор разговора.
4.  **Отправка POST-запроса**: Отправляет POST-запрос к API с использованием библиотеки `requests`. Указывает, что тело запроса является JSON и что ответ должен быть потоковым (`stream=True`).
5.  **Обработка ответа**:
    *   Проверяет статус ответа с помощью `response.raise_for_status()`. Если статус код не 200, будет вызвано исключение.
    *   Перебирает строки в потоковом ответе с помощью `response.iter_lines()`.
    *   Для каждой строки проверяет, начинается ли она с `b"data: "`.
    *   Если строка начинается с `b"data: "`, пытается декодировать JSON из остальной части строки (начиная с 6-го символа).
    *   Если декодирование JSON прошло успешно, проверяет наличие ошибки в данных. Если ошибка есть, выводит её и прерывает цикл.
    *   Извлекает содержимое сообщения из данных JSON и выводит его на экран.
    *   Обрабатывает исключение `json.JSONDecodeError`, которое может возникнуть, если строка не является корректным JSON.

```python
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

**Назначение**: Отправляет второй запрос к API Copilot и обрабатывает потоковый ответ.

**Как работает функция**:

1.  **Формирование тела запроса**: Создает тело запроса в формате JSON, аналогично предыдущему запросу, но с другим сообщением: "Tell me somethings about my name".
2.  **Отправка POST-запроса**: Отправляет POST-запрос к API с использованием библиотеки `requests`. Указывает, что тело запроса является JSON и что ответ должен быть потоковым (`stream=True`).
3.  **Обработка ответа**:
    *   Проверяет статус ответа с помощью `response.raise_for_status()`. Если статус код не 200, будет вызвано исключение.
    *   Перебирает строки в потоковом ответе с помощью `response.iter_lines()`.
    *   Для каждой строки проверяет, начинается ли она с `b"data: "`.
    *   Если строка начинается с `b"data: "`, пытается декодировать JSON из остальной части строки (начиная с 6-го символа).
    *   Если декодирование JSON прошло успешно, проверяет наличие ошибки в данных. Если ошибка есть, выводит её и прерывает цикл.
    *   Извлекает содержимое сообщения из данных JSON и выводит его на экран.
    *   Обрабатывает исключение `json.JSONDecodeError`, которое может возникнуть, если строка не является корректным JSON.

**Примеры**:

Пример отправки запроса и обработки ответа:

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

```
Этот код отправляет запрос к API Copilot с приветственным сообщением и обрабатывает потоковый ответ, выводя содержимое на экран.

```python
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

Этот код отправляет запрос к API Copilot с просьбой рассказать что-нибудь об имени пользователя и обрабатывает потоковый ответ, выводя содержимое на экран.