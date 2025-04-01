# Модуль `you.py` для работы с провайдером You.com

## Обзор

Модуль `you.py` предназначен для взаимодействия с API You.com с целью получения ответов на запросы. Он содержит функции для преобразования формата сообщений и отправки запросов к API.

## Подробней

Этот модуль используется для интеграции с провайдером You.com в проекте `hypotez`. Он преобразует входящие сообщения в формат, требуемый API You.com, отправляет запрос и обрабатывает полученные данные. Модуль включает обработку ошибок и повторные попытки в случае сбоев.

## Функции

### `transform`

```python
def transform(messages: list) -> list:
    """Преобразует список сообщений в формат, необходимый для API You.com.

    Args:
        messages (list): Список сообщений, где каждое сообщение представляет собой словарь с ключами 'role' и 'content'.

    Returns:
        list: Список словарей, где каждый словарь содержит ключи 'question' и 'answer', представляющие вопрос и ответ соответственно.

    Как работает функция:
    -----------------------
    Функция итерируется по списку сообщений и преобразует их в формат, подходящий для API You.com.
    Она обрабатывает сообщения с ролями 'user', 'assistant' и 'system', формируя структуру данных,
    состоящую из вопросов и ответов.

    ASCII flowchart:
    ----------------
    Начало --> Проверка роли сообщения
    |
    --- Роль = 'user' --> Извлечение вопроса
    |   |
    |   --- Проверка следующего сообщения --> Роль = 'assistant' --> Извлечение ответа
    |       |   |
    |       |   --- Добавление вопроса и ответа в результат
    |       |
    --- Роль = 'assistant' --> Добавление ответа в результат с пустым вопросом
    |
    --- Роль = 'system' --> Добавление вопроса в результат с пустым ответом
    |
    Конец

    Примеры:
    ---------
    >>> transform([{'role': 'user', 'content': 'Привет'}, {'role': 'assistant', 'content': 'Здравствуйте'}])
    [{'question': 'Привет', 'answer': 'Здравствуйте'}]

    >>> transform([{'role': 'user', 'content': 'Как дела?'}, {'role': 'assistant', 'content': 'Все хорошо'}, {'role': 'system', 'content': 'Важное сообщение'}])
    [{'question': 'Как дела?', 'answer': 'Все хорошо'}, {'question': 'Важное сообщение', 'answer': ''}]
    """
    ...
```
**Назначение**: Преобразует список сообщений в формат, необходимый для API You.com.

**Параметры**:
- `messages` (list): Список сообщений, где каждое сообщение представляет собой словарь с ключами `role` и `content`.

**Возвращает**:
- `list`: Список словарей, где каждый словарь содержит ключи `question` и `answer`, представляющие вопрос и ответ соответственно.

**Как работает функция**:
 1. Функция итерируется по списку сообщений и преобразует их в формат, подходящий для API You.com.
 2. Она обрабатывает сообщения с ролями `user`, `assistant` и `system`, формируя структуру данных, состоящую из вопросов и ответов.

```
Начало --> Проверка роли сообщения
|
--- Роль = 'user' --> Извлечение вопроса
|   |
|   --- Проверка следующего сообщения --> Роль = 'assistant' --> Извлечение ответа
|       |   |
|       |   --- Добавление вопроса и ответа в результат
|       |
--- Роль = 'assistant' --> Добавление ответа в результат с пустым вопросом
|
--- Роль = 'system' --> Добавление вопроса в результат с пустым ответом
|
Конец
```
**Примеры**:
```python
>>> transform([{'role': 'user', 'content': 'Привет'}, {'role': 'assistant', 'content': 'Здравствуйте'}])
[{'question': 'Привет', 'answer': 'Здравствуйте'}]

>>> transform([{'role': 'user', 'content': 'Как дела?'}, {'role': 'assistant', 'content': 'Все хорошо'}, {'role': 'system', 'content': 'Важное сообщение'}])
[{'question': 'Как дела?', 'answer': 'Все хорошо'}, {'question': 'Важное сообщение', 'answer': ''}]
```

### `output`

```python
def output(chunk):
    """Обрабатывает чанк данных, полученный от API You.com, и выводит токен чата.

    Args:
        chunk (bytes): Часть данных, полученная от API.

    Как работает функция:
    -----------------------
    Функция проверяет, содержит ли чанк данных строку `"youChatToken"`.
    Если строка найдена, функция извлекает JSON из чанка, декодирует его и выводит значение
    ключа `'youChatToken'` в консоль.

    ASCII flowchart:
    ----------------
    Начало --> Проверка наличия '"youChatToken"' в чанке
    |
    --- Найдено --> Извлечение JSON из чанка --> Декодирование JSON --> Вывод youChatToken
    |
    Конец

    """
    ...
```

**Назначение**: Обрабатывает чанк данных, полученный от API You.com, и выводит токен чата.

**Параметры**:
- `chunk` (bytes): Часть данных, полученная от API.

**Как работает функция**:

 1. Функция проверяет, содержит ли чанк данных строку `"youChatToken"`.
 2. Если строка найдена, функция извлекает JSON из чанка, декодирует его и выводит значение ключа `'youChatToken'` в консоль.

```
Начало --> Проверка наличия '"youChatToken"' в чанке
|
--- Найдено --> Извлечение JSON из чанка --> Декодирование JSON --> Вывод youChatToken
|
Конец
```

## Переменные

- `config`: Конфигурация, загруженная из аргументов командной строки.
- `messages`: Список сообщений из конфигурации.
- `prompt`: Последнее сообщение пользователя.
- `headers`: Заголовки HTTP-запроса.
- `params`: Параметры запроса, закодированные в URL-формате.

```python
import sys
import json
import urllib.parse

from curl_cffi import requests

config = json.loads(sys.argv[1]) #  Конфигурация, загруженная из аргументов командной строки.
messages = config['messages'] # Список сообщений из конфигурации.
prompt = '' # Последнее сообщение пользователя.

headers = { # Заголовки HTTP-запроса.
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Sec-Fetch-Mode': 'navigate',
    'Host': 'you.com',
    'Origin': 'https://you.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Referer': 'https://you.com/api/streamingSearch?q=nice&safeSearch=Moderate&onShoppingPage=false&mkt=&responseFilter=WebPages,Translations,TimeZone,Computation,RelatedSearches&domain=youchat&queryTraceId=7a6671f8-5881-404d-8ea3-c3f8301f85ba&chat=%5B%7B%22question%22%3A%22hi%22%2C%22answer%22%3A%22Hello!%20How%20can%20I%20assist%20you%20today%3F%22%7D%5D&chatId=7a6671f8-5881-404d-8ea3-c3f8301f85ba&__cf_chl_tk=ex2bw6vn5vbLsUm8J5rDYUC0Bjzc1XZqka6vUl6765A-1684108495-0-gaNycGzNDtA',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Priority': 'u=0, i',
}

if messages[-1]['role'] == 'user':
    prompt = messages[-1]['content']
    messages = messages[:-1]

params = urllib.parse.urlencode({ # Параметры запроса, закодированные в URL-формате.
    'q': prompt,
    'domain': 'youchat',
    'chat': transform(messages)
})