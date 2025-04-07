# Модуль для взаимодействия с Phind API
=================================================

Модуль предназначен для отправки запросов к API Phind и обработки ответов. Он использует библиотеку `curl_cffi` для выполнения HTTP-запросов и предназначен для получения ответов на вопросы, заданные в запросе.

## Обзор

Этот модуль отправляет запросы к API Phind и обрабатывает потоковые ответы. Он принимает параметры запроса из аргументов командной строки, формирует JSON-данные и заголовки, необходимые для запроса, и выводит полученные данные в консоль.

## Подробней

Модуль `phind.py` является частью проекта `hypotez` и служит для интеграции с поисковой системой Phind, специализирующейся на ответах на технические вопросы. Он формирует запросы к API `www.phind.com` и отображает результаты поиска. 

## Функции

### `output`

```python
def output(chunk):
    """Функция обработки чанков данных, получаемых от API Phind.

    Args:
        chunk (bytes): Часть данных, полученная от API.

    Returns:
        None

    Raises:
        json.decoder.JSONDecodeError: Если возникает ошибка при декодировании JSON.
    """
```

**Назначение**: Обрабатывает чанки данных, поступающие от API Phind, удаляя метаданные и форматируя вывод.

**Параметры**:
- `chunk` (bytes): Часть данных, полученная от API в виде байтовой строки.

**Возвращает**:
- `None`: Функция ничего не возвращает, а выводит обработанные данные в консоль.

**Вызывает исключения**:
- `json.decoder.JSONDecodeError`: Возникает, если при попытке декодировать JSON происходит ошибка.

**Как работает функция**:

1.  **Проверка на метаданные**: Проверяет, содержит ли чанк байтовую строку `b'PHIND_METADATA'`. Если да, функция завершает выполнение, чтобы избежать вывода метаданных.
2.  **Коррекция чанка**: Исправляет некорректные последовательности данных, такие как `b'data:  \\r\\ndata: \\r\\ndata: \\r\\n\\r\\n'`, заменяя их на `b'data:  \\n\\r\\n\\r\\n'`.
3.  **Декодирование чанка**: Декодирует чанк из байтовой строки в обычную строку.
4.  **Замена строк**: Заменяет специфические строки, такие как `'data: \\r\\n\\r\\ndata: '` на `'data: \\n'`, `'\\r\\ndata: \\r\\ndata: \\r\\n\\r\\n'` на `'\\n\\r\\n\\r\\n'` и `'data: '` на `''`, а также удаляет `'\\r\\n\\r\\n'`.
5.  **Вывод чанка**: Выводит обработанный чанк в консоль с немедленной очисткой буфера (`flush=True`) и без добавления новой строки в конце (`end = ''`).
6.  **Обработка ошибок JSON**: Перехватывает исключение `json.decoder.JSONDecodeError`, которое может возникнуть при попытке декодировать JSON, и игнорирует его.

**ASCII flowchart**:

```
    A [Проверка на метаданные]
    |
    B [Коррекция чанка]
    |
    C [Декодирование чанка]
    |
    D [Замена строк]
    |
    E [Вывод чанка]
    |
    F [Обработка ошибок JSON]
```

**Примеры**:

1.  Чанк с метаданными:

```python
chunk = b'PHIND_METADATA: some metadata'
output(chunk)  # Ничего не выводится
```

2.  Корректный чанк данных:

```python
chunk = b'data:  Example data\\r\\n\\r\\n'
output(chunk)  # Выводит " Example data"
```

3.  Чанк с ошибкой JSON:

```python
chunk = b'data:  {\\r\\n"key": "value"\\r\\n'
output(chunk)  # Выводит "{\\r\\n"key": "value"\\r\\n"
```

## Основной код

В основном коде выполняются следующие действия:

1.  **Чтение конфигурации**: Читает конфигурацию из аргументов командной строки.
2.  **Формирование данных JSON**: Формирует JSON-данные для запроса на основе полученной конфигурации.
3.  **Определение заголовков**: Определяет заголовки, необходимые для запроса.
4.  **Цикл запросов**: В цикле отправляет POST-запросы к API Phind и обрабатывает ответы с использованием функции `output`. В случае ошибки повторяет попытку.

**Примеры**:

Пример запуска модуля из командной строки:

```bash
python phind.py '{"messages": [{"content": "What is the capital of France?"}], "model": "gpt-4"}'
```

```python
import sys
import json
import datetime
import urllib.parse

from curl_cffi import requests

config = json.loads(sys.argv[1])
prompt = config['messages'][-1]['content']

skill = 'expert' if config['model'] == 'gpt-4' else 'intermediate'

json_data = json.dumps({
    'question': prompt,
    'options': {
        'skill': skill,
        'date': datetime.datetime.now().strftime('%d/%m/%Y'),
        'language': 'en',
        'detailed': True,
        'creative': True,
        'customLinks': []}}, separators=(',', ':'))

headers = {
    'Content-Type': 'application/json',
    'Pragma': 'no-cache',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Sec-Fetch-Mode': 'cors',
    'Content-Length': str(len(json_data)),
    'Origin': 'https://www.phind.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Referer': f'https://www.phind.com/search?q={urllib.parse.quote(prompt)}&source=searchbox',
    'Connection': 'keep-alive',
    'Host': 'www.phind.com',
    'Sec-Fetch-Dest': 'empty'
}

def output(chunk):
    """Функция обработки чанков данных, получаемых от API Phind.

    Args:
        chunk (bytes): Часть данных, полученная от API.

    Returns:
        None

    Raises:
        json.decoder.JSONDecodeError: Если возникает ошибка при декодировании JSON.
    """
    try:
        if b'PHIND_METADATA' in chunk:
            return
        
        if chunk == b'data:  \\r\\ndata: \\r\\ndata: \\r\\n\\r\\n':
            chunk = b'data:  \\n\\r\\n\\r\\n'

        chunk = chunk.decode()

        chunk = chunk.replace('data: \\r\\n\\r\\ndata: ', 'data: \\n')
        chunk = chunk.replace('\\r\\ndata: \\r\\ndata: \\r\\n\\r\\n', '\\n\\r\\n\\r\\n')
        chunk = chunk.replace('data: ', '').replace('\\r\\n\\r\\n', '')

        print(chunk, flush=True, end = '')
        
    except json.decoder.JSONDecodeError:
        pass

while True:
    try:
        response = requests.post('https://www.phind.com/api/infer/answer',
                         headers=headers, data=json_data, content_callback=output, timeout=999999, impersonate='safari15_5')
        
        exit(0)
    
    except Exception as e:
        print('an error occured, retrying... |', e, flush=True)
        continue