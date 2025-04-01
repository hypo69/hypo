# Модуль для работы с Copilot API completions

## Обзор

Этот модуль содержит примеры запросов к API Copilot для генерации текста. Он демонстрирует, как отправлять запросы к локальному серверу и обрабатывать потоковые ответы.

## Подробнее

Модуль отправляет два запроса к API `/v1/chat/completions` с использованием библиотеки `requests`. Каждый запрос отправляется с уникальным `conversation_id`, чтобы имитировать беседу. Ответы обрабатываются потоково, и извлекается сгенерированный контент. В случае возникновения ошибок в ответе, информация об ошибке выводится в консоль.

## Функции

### Отправка запроса к API Copilot

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
print()
print()
print()
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

**Как работает функция**:

1.  **Импорт библиотек**: Импортируются библиотеки `requests`, `json` и `uuid`.
2.  **Определение переменных**:
    *   `url`: URL-адрес API-endpoint для запросов.
    *   `conversation_id`: Уникальный идентификатор беседы, генерируемый с помощью `uuid`.
    *   `body`: Тело запроса в формате JSON, включающее:
        *   `model`: Модель для генерации текста (в данном случае пустая строка).
        *   `provider`: Провайдер, используемый для генерации (в данном случае "Copilot").
        *   `stream`: Параметр, указывающий на потоковую передачу данных.
        *   `messages`: Список сообщений в беседе, где каждое сообщение содержит роль (`role`) и контент (`content`).
        *   `conversation_id`: Идентификатор беседы.
3.  **Отправка POST-запроса**: Используется `requests.post` для отправки запроса к API. Параметр `stream=True` указывает на то, что ответ будет получен в потоковом режиме.
4.  **Обработка потокового ответа**:
    *   Цикл `for line in response.iter_lines()`: Итерируется по строкам ответа.
    *   `if line.startswith(b"data: ")`: Проверяется, начинается ли строка с префикса "data: ".
    *   `json_data = json.loads(line[6:])`: Извлекается JSON-данные из строки (после префикса "data: ").
    *   `if json_data.get("error")`: Проверяется наличие ошибки в JSON-данных. Если ошибка присутствует, она выводится в консоль, и цикл прерывается.
    *   `content = json_data.get("choices", [{"delta": {}}])[0]["delta"].get("content", "")`: Извлекается контент из JSON-данных.
    *   `if content`: Если контент присутствует, он выводится в консоль.
    *   Обработка исключений: Если при разборе JSON-данных возникает ошибка (`json.JSONDecodeError`), она игнорируется.
5.  **Повторение процесса**: Шаги 2-4 повторяются для второго запроса, который спрашивает о имени пользователя.

**Примеры**:

Пример запроса:

```python
import uuid
import requests
import json

# URL API
url = "http://localhost:1337/v1/chat/completions"

# Уникальный ID для отслеживания диалога
conversation_id = str(uuid.uuid4())

# Формирование запроса
body = {
    "model": "",
    "provider": "Copilot",
    "stream": True,
    "messages": [
        {"role": "user", "content": "Hello, i am Heiner. How are you?"}
    ],
    "conversation_id": conversation_id
}

# Отправка запроса
response = requests.post(url, json=body, stream=True)
response.raise_for_status()  # Вызов исключения для HTTP ошибок

# Вывод ответа
for line in response.iter_lines():
    if line.startswith(b"data: "):
        try:
            json_data = json.loads(line[6:])  # декодируем JSON из строки ответа
            if json_data.get("error"):
                print(json_data)  # выводим сообщение об ошибке
                break
            content = json_data.get("choices", [{"delta": {}}])[0]["delta"].get("content", "")
            if content:
                print(content, end="")  # печатаем содержимое ответа
        except json.JSONDecodeError:
            pass