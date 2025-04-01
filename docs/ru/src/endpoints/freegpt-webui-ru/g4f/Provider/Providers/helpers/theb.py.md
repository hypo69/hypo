# Модуль взаимодействия с chatbot.theb.ai

## Обзор

Модуль предназначен для взаимодействия с API `chatbot.theb.ai` с целью получения ответов на заданные запросы. Он отправляет POST-запросы к API и обрабатывает получаемые ответы.

## Подробней

Этот модуль используется для отправки запросов к `chatbot.theb.ai` и получения ответов в режиме реального времени. Модуль принимает запрос пользователя, формирует JSON-запрос и отправляет его к API. Полученные данные обрабатываются в режиме потока (chunked) с использованием функции обратного вызова `format`.

## Функции

### `format`

```python
def format(chunk):
    """
    Обрабатывает полученный чанк данных из ответа сервера, извлекая и выводя полезную информацию.

    Args:
        chunk (bytes): Часть данных, полученная от сервера.

    Raises:
        Exception: Если возникает ошибка при обработке данных.

    Внутренние функции:
        Отсутствуют

    Как работает функция:
    1. Пытается извлечь содержимое из чанка, используя регулярное выражение `r'content":"(.*)"},"fin'`.
    2. Выводит извлеченное содержимое в стандартный поток вывода, не добавляя символ новой строки в конце.
    3. Если происходит ошибка, выводит сообщение об ошибке, содержащее необработанные данные чанка.

    ASCII flowchart:

    Начало --> Извлечение_содержимого --> Вывод_содержимого --> Конец
                |
                Ошибка --> Вывод_сообщения_об_ошибке --> Конец

    Примеры:
        В данном коде не предусмотрены отдельные примеры вызова, так как функция `format` вызывается как callback
        при получении данных от сервера в функции `requests.post`.
    """
```

## Код

```python
import json
import sys
from re import findall
from curl_cffi import requests
from src.logger import logger

config = json.loads(sys.argv[1])
prompt = config['messages'][-1]['content']

headers = {
    'authority': 'chatbot.theb.ai',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
    'content-type': 'application/json',
    'origin': 'https://chatbot.theb.ai',
    'referer': 'https://chatbot.theb.ai/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

json_data = {
    'prompt': prompt,
    'options': {}
}

def format(chunk: bytes):
    """
    Обрабатывает полученный чанк данных из ответа сервера, извлекая и выводя полезную информацию.

    Args:
        chunk (bytes): Часть данных, полученная от сервера.

    Raises:
        Exception: Если возникает ошибка при обработке данных.
    """
    try:
        completion_chunk = findall(r'content":"(.*)"},"fin', chunk.decode())[0]
        print(completion_chunk, flush=True, end='')

    except Exception as ex:
        print(f'[ERROR] an error occurred, retrying... | [[{chunk.decode()}]]', flush=True)
        logger.error('Ошибка при обработке данных', ex, exc_info=True)
        return

while True:
    try:
        response = requests.post(
            'https://chatbot.theb.ai/api/chat-process',
            headers=headers,
            json=json_data,
            content_callback=format,
            impersonate='chrome110'
        )

        exit(0)

    except Exception as ex:
        print('[ERROR] an error occurred, retrying... |', ex, flush=True)
        logger.error('Ошибка при отправке запроса', ex, exc_info=True)
        continue
```

**Параметры**:
- `config` (dict): Словарь, содержащий конфигурационные данные, загруженные из аргументов командной строки.
- `prompt` (str): Текст запроса, извлеченный из конфигурации.
- `headers` (dict): Словарь, содержащий заголовки HTTP-запроса.
- `json_data` (dict): Словарь, содержащий данные JSON для отправки в теле запроса.
```

### Основной цикл обработки запросов
```python
while True:
    """
    Бесконечный цикл для отправки запросов к API и обработки ответов.

    Внутренние функции:
        Отсутствуют

    Как работает цикл:
    1. Отправляет POST-запрос к API `chatbot.theb.ai/api/chat-process` с заданными заголовками и данными.
       Использует функцию `format` для обработки данных, получаемых в реальном времени.
    2. Если запрос выполнен успешно, завершает программу с кодом 0.
    3. Если происходит ошибка, выводит сообщение об ошибке и повторяет попытку.

    ASCII flowchart:

    Начало --> Отправка_запроса --> Успех? --> Завершение
                                   |
                                   Нет --> Обработка_ошибки --> Повтор

    Примеры:
        В данном коде не предусмотрены отдельные примеры вызова, так как цикл выполняется непрерывно до успешного завершения
        или принудительной остановки.
    """
```
**Как работает код**:
1. **Инициализация**:
   - Загружает конфигурацию из аргументов командной строки, используя `json.loads(sys.argv[1])`.
   - Извлекает текст запроса (`prompt`) из конфигурации.
   - Определяет заголовки (`headers`) для HTTP-запроса, включая `User-Agent`, `Content-Type` и другие.
   - Формирует JSON-данные (`json_data`) для отправки в теле запроса.

2. **Функция `format(chunk)`**:
   - Используется как callback-функция для обработки данных, получаемых от сервера в режиме реального времени.
   - Пытается извлечь содержимое ответа (`completion_chunk`) из каждого чанка данных, используя регулярное выражение.
   - Выводит извлеченное содержимое в стандартный поток вывода.
   - В случае ошибки выводит сообщение об ошибке.

3. **Основной цикл `while True`**:
   - Отправляет POST-запрос к API `chatbot.theb.ai/api/chat-process`, используя библиотеку `curl_cffi`.
   - Указывает `content_callback=format` для обработки данных в режиме реального времени.
   - В случае успешного выполнения запроса завершает программу с кодом 0 (`exit(0)`).
   - В случае ошибки выводит сообщение об ошибке и повторяет попытку.
```