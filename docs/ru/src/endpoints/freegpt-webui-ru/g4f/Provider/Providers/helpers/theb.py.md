# Модуль для взаимодействия с chatbot.theb.ai
## Обзор

Модуль предназначен для отправки запросов к API `chatbot.theb.ai` и обработки ответов, полученных в режиме реального времени. Он использует библиотеку `curl_cffi` для выполнения HTTP-запросов и регулярные выражения для извлечения полезной информации из потока данных.

## Подробнее

Модуль отправляет POST-запросы к API `chatbot.theb.ai` с использованием предоставленных заголовков и тела запроса в формате JSON. Ответ обрабатывается по частям (chunk), при этом из каждой части извлекается содержимое, соответствующее определенному шаблону. В случае ошибки при обработке или отправке запроса, модуль пытается повторить операцию.

## Функции

### `format`

```python
def format(chunk):
    """
    Форматирует и выводит часть ответа, полученного от сервера.

    Args:
        chunk (bytes): Часть данных, полученная от сервера.

    Returns:
        None

    Raises:
        Exception: Если не удается извлечь данные из `chunk`.

    Как работает функция:
    Функция `format` принимает на вход часть данных (`chunk`) в виде байтов, пытается извлечь из нее содержимое, используя регулярное выражение, и выводит извлеченное содержимое в консоль. В случае неудачи выводит сообщение об ошибке и возвращается.

    Внутри функции происходят следующие действия и преобразования:
    1.  `Извлечение подстроки`: Попытка извлечения подстроки из `chunk` с использованием регулярного выражения `r'content":"(.*)"},"fin'`.
    2.  `Вывод`: Если подстрока успешно извлечена, она выводится в консоль без добавления новой строки в конце.
    3.  `Обработка исключений`: Если при извлечении подстроки возникает исключение, выводится сообщение об ошибке с содержимым `chunk`.
    """
    try:
        completion_chunk = findall(r'content":"(.*)"},"fin', chunk.decode())[0]
        print(completion_chunk, flush=True, end='')

    except Exception as e:
        print(f'[ERROR] an error occured, retrying... | [[{chunk.decode()}]]', flush=True)
        return
```
## Пример использования

```python
import json
import sys
from re import findall
from curl_cffi import requests

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


while True:
    try:
        response = requests.post('https://chatbot.theb.ai/api/chat-process',
                            headers=headers, json=json_data, content_callback=format, impersonate='chrome110')

        exit(0)

    except Exception as e:
        print('[ERROR] an error occured, retrying... |', e, flush=True)
        continue