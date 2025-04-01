# Модуль для взаимодействия с API Copilot для completions

## Обзор

Этот модуль демонстрирует взаимодействие с API Copilot для получения completions (завершений). Он отправляет POST-запросы к локальному серверу и обрабатывает потоковые ответы, выводя содержимое на консоль.

## Подробнее

Этот код отправляет два запроса к API Copilot, используя библиотеку `requests`. Первый запрос приветствует Copilot, а второй просит рассказать что-нибудь об имени пользователя. Ответы обрабатываются потоково, и извлекаемое содержимое выводится на консоль. Модуль предназначен для демонстрации простого взаимодействия с API Copilot.

## Функции

### Отправка запросов и обработка ответов

```python
import requests
import json
import uuid

url = "http://localhost:1337/v1/chat/completions"

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

**Назначение**: Отправляет запросы к API Copilot и обрабатывает потоковые ответы.

**Параметры**:

- `url` (str): URL-адрес API Copilot.
- `body` (dict): Тело запроса в формате JSON, содержащее информацию о модели, провайдере, флаге потоковой передачи, сообщениях и ID разговора.
- `response` (requests.Response): Объект ответа от сервера.
- `line` (bytes): Каждая строка в потоковом ответе.
- `json_data` (dict): Данные JSON, извлеченные из строки ответа.
- `content` (str): Содержимое сообщения, извлеченное из данных JSON.

**Возвращает**: Ничего. Выводит содержимое ответа на консоль.

**Вызывает исключения**:

- `requests.exceptions.HTTPError`: Если HTTP-запрос завершается с ошибкой.
- `json.JSONDecodeError`: Если не удается декодировать JSON из строки ответа.

**Как работает функция**:

1.  **Инициализация**:
    *   Определяется `url` для запросов к API completions.
    *   Генерируется `conversation_id` с помощью `uuid.uuid4()`.
    *   Создается `body` запроса, содержащий параметры запроса и сообщения.

2.  **Отправка запроса**:
    *   Функция отправляет POST-запрос к `url` с телом `body`, используя библиотеку `requests`. Установлен параметр `stream=True` для потоковой обработки ответа.
    *   Вызывается `response.raise_for_status()`, чтобы проверить, не вернул ли HTTP-запрос код ошибки. Если код ошибки возвращен, вызывается исключение.

3.  **Обработка потокового ответа**:
    *   Функция итерируется по строкам в потоковом ответе с помощью `response.iter_lines()`.
    *   Для каждой строки проверяется, начинается ли она с `b"data: "`.

4.  **Извлечение и обработка данных**:
    *   Если строка начинается с `b"data: "`, функция пытается извлечь JSON-данные из строки, удалив префикс `b"data: "`.
    *   Извлеченные JSON-данные загружаются с помощью `json.loads()`.
    *   Проверяется наличие ключа `"error"` в `json_data`. Если он присутствует, выводится сообщение об ошибке, и цикл прерывается.
    *   Извлекается содержимое сообщения из `json_data`, используя цепочку вызовов `json_data.get("choices", [{"delta": {}}])[0]["delta"].get("content", "")`. Это позволяет получить значение ключа `"content"` из вложенных структур данных.
    *   Если `content` не пустое, оно выводится на консоль с помощью `print(content, end="")`. Параметр `end=""` предотвращает добавление новой строки после каждого выведенного фрагмента содержимого.

5.  **Обработка ошибок JSON**:
    *   Если во время извлечения JSON-данных возникает исключение `json.JSONDecodeError`, оно перехватывается, и выполнение продолжается без вывода сообщения об ошибке.

6.  **Повторение процесса**:
    *   Шаги 2-5 повторяются для второго запроса, который запрашивает информацию об имени пользователя.

```
Блок-схема работы функции:

Начало
  ↓
HTTP Запрос к API completions
  ↓
Получение потокового ответа
  ↓
Перебор строк в потоковом ответе
  ↓
Строка начинается с "data: "?
  ├──→ Да → Извлечение JSON из строки
  │        ↓
  │        Декодирование JSON
  │        ↓
  │        Есть "error" в JSON?
  │        ├──→ Да → Вывод ошибки и прерывание
  │        │        ↓
  │        └──→ Нет → Извлечение "content" из JSON
  │             ↓
  │             "content" не пустое?
  │             ├──→ Да → Вывод "content"
  │             │        ↓
  │             └──→ Нет
  │                  ↓
  └──→ Нет
       ↓
Конец цикла по строкам
  ↓
Конец
```

**Примеры**:

Пример вызова (код не выполняется, только демонстрирует структуру вызова):

```python
import requests
import json
import uuid

# Первая часть запроса
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

# Вторая часть запроса
body = {
    "model": "",
    "provider": "Copilot",
    "stream": True,
    "messages": [
        {"role": "user", "content": "Tell me somethings about my name"}
    ],
    "conversation_id": conversation_id
}