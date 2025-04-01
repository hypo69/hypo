# Модуль для работы с RubiksAI
===========================

Модуль предоставляет класс `RubiksAI`, который используется для взаимодействия с API RubiksAI для генерации текста с использованием различных моделей, таких как gpt-4o и llama-3.

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [RubiksAI](#rubiksai)
        - [Методы](#методы-1)
            - [generate_mid](#generate_mid)
            - [create_referer](#create_referer)
            - [create_async_generator](#create_async_generator)

## Обзор

Модуль содержит класс `RubiksAI`, который наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`. Этот класс предоставляет методы для асинхронной генерации текста с использованием различных моделей, предоставляемых RubiksAI. Он поддерживает потоковую передачу, системные сообщения и историю сообщений.

## Подробнее

Этот модуль предназначен для интеграции с API RubiksAI, позволяя пользователям генерировать текст на основе различных моделей. Он предоставляет методы для создания запросов к API, обработки ответов и предоставления результатов в виде асинхронного генератора.

## Классы

### `RubiksAI`

**Описание**: Класс для взаимодействия с API RubiksAI для генерации текста.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает поддержку асинхронной генерации.
- `ProviderModelMixin`: Предоставляет методы для управления моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("Rubiks AI").
- `url` (str): URL провайдера ("https://rubiks.ai").
- `api_endpoint` (str): URL API ("https://rubiks.ai/search/api/").
- `working` (bool): Указывает, работает ли провайдер (True).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу (True).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (True).
- `default_model` (str): Модель по умолчанию ('gpt-4o-mini').
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Словарь псевдонимов моделей.

#### Методы

- `generate_mid`
- `create_referer`
- `create_async_generator`

#### `generate_mid`

```python
@staticmethod
def generate_mid() -> str:
    """
    Generates a 'mid' string following the pattern:
    6 characters - 4 characters - 4 characters - 4 characters - 12 characters
    Example: 0r7v7b-quw4-kdy3-rvdu-ekief6xbuuq4
    """
    ...
```

**Назначение**: Генерирует строку `mid` в формате `6 символов - 4 символа - 4 символа - 4 символа - 12 символов`.

**Как работает функция**:
1. Создает пять частей строки:
   - Первая часть: 6 случайных символов (буквы в нижнем регистре и цифры).
   - Вторая часть: 4 случайных символа (буквы в нижнем регистре и цифры).
   - Третья часть: 4 случайных символа (буквы в нижнем регистре и цифры).
   - Четвертая часть: 4 случайных символа (буквы в нижнем регистре и цифры).
   - Пятая часть: 12 случайных символов (буквы в нижнем регистре и цифры).
2. Объединяет эти пять частей через дефис `-`.
3. Возвращает полученную строку.

```
Создание частей строки с случайными символами
│
├─> Объединение частей через дефис
│
└─> Возврат строки 'mid'
```

**Примеры**:
```python
>>> RubiksAI.generate_mid()
'a1b2c3-d4e5-f6g7-h8i9-j0k1l2m3n4o5'
```

#### `create_referer`

```python
@staticmethod
def create_referer(q: str, mid: str, model: str = '') -> str:
    """
    Creates a Referer URL with dynamic q and mid values, using urlencode for safe parameter encoding.
    """
    ...
```

**Назначение**: Создает URL Referer с динамическими значениями `q` (query) и `mid`, используя `urlencode` для безопасного кодирования параметров.

**Параметры**:
- `q` (str): Значение параметра запроса.
- `mid` (str): Значение параметра `mid`.
- `model` (str, optional): Значение параметра модели. По умолчанию ''.

**Возвращает**:
- `str`: Сформированный URL Referer.

**Как работает функция**:
1. Создает словарь параметров, содержащий `q`, `model` и `mid`.
2. Кодирует параметры URL с помощью `urllib.parse.urlencode` для безопасной передачи.
3. Формирует строку URL, объединяя базовый URL (`https://rubiks.ai/search/?`) и закодированные параметры.
4. Возвращает полученный URL.

```
Создание словаря параметров
│
├─> Кодирование параметров URL
│
└─> Формирование URL Referer
```

**Примеры**:
```python
>>> RubiksAI.create_referer(q='test', mid='12345')
'https://rubiks.ai/search/?q=test&model=&mid=12345'
```

#### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    web_search: bool = False,
    temperature: float = 0.6,
    **kwargs
) -> AsyncResult:
    """
    Creates an asynchronous generator that sends requests to the Rubiks AI API and yields the response.

    Parameters:
    - model (str): The model to use in the request.
    - messages (Messages): The messages to send as a prompt.
    - proxy (str, optional): Proxy URL, if needed.
    - web_search (bool, optional): Indicates whether to include search sources in the response. Defaults to False.
    """
    ...
```

**Назначение**: Создает асинхронный генератор, отправляющий запросы к API Rubiks AI и выдающий ответы.

**Параметры**:
- `model` (str): Модель для использования в запросе.
- `messages` (Messages): Сообщения для отправки в качестве запроса.
- `proxy` (str, optional): URL прокси, если необходимо.
- `web_search` (bool, optional): Указывает, следует ли включать источники поиска в Интернете в ответ. По умолчанию `False`.
- `temperature` (float, optional): Температура модели. По умолчанию `0.6`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от API.

**Как работает функция**:

1.  **Инициализация**:
    *   Определяется модель, которая будет использоваться, с помощью `cls.get_model(model)`.
    *   Генерируется уникальный идентификатор `mid_value` с помощью `cls.generate_mid()`.
    *   Создается URL `referer` с использованием сгенерированного идентификатора и последнего сообщения пользователя.

2.  **Формирование данных запроса**:
    *   Создается словарь `data`, содержащий сообщения, модель, флаг веб-поиска, флаг потоковой передачи и температуру.

3.  **Формирование заголовков запроса**:
    *   Создается словарь `headers` с необходимыми заголовками, включая `Referer`, сгенерированный ранее.

4.  **Отправка запроса и обработка ответа**:
    *   Используется асинхронная сессия `aiohttp` для отправки `POST` запроса к API Rubiks AI.
    *   Проверяется статус ответа с помощью `raise_for_status(response)`.
    *   Асинхронно итерируется по каждой строке в содержимом ответа.
    *   Декодируется каждая строка, удаляются пробелы в начале и конце.
    *   Пропускаются строки, не начинающиеся с `data: `.
    *   Извлекаются данные из строки после префикса `data: `.
    *   Если данные равны `[DONE]` или `{"done": ""}`, цикл прерывается.
    *   Пытается распарсить данные JSON. В случае ошибки парсинга JSON, строка пропускается.

5.  **Обработка данных JSON**:
    *   Если в JSON данных есть ключи `url` и `title` и включен `web_search`, данные добавляются в список `sources`.
    *   Если в JSON данных есть ключ `choices`, извлекается содержимое из каждого элемента `delta` и передается в генератор с помощью `yield`.

6.  **Обработка источников веб-поиска**:
    *   После завершения обработки всех строк ответа, если включен `web_search` и список `sources` не пуст, данные о источниках передаются в генератор с помощью `yield Sources(sources)`.

```
Определение модели и создание идентификатора
│
├─> Формирование данных запроса
│
├─> Формирование заголовков запроса
│
├─> Отправка запроса к API Rubiks AI
│
├─> Обработка ответа:
│   ├─> Чтение и декодирование строк
│   ├─> Проверка на завершение
│   ├─> Парсинг JSON
│   ├─> Извлечение данных и передача в генератор
│
└─> Обработка источников веб-поиска (если включено)
```

**Примеры**:
```python
async def example():
    model = 'gpt-4o-mini'
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    async for response in RubiksAI.create_async_generator(model=model, messages=messages):
        print(response, end='')

import asyncio
asyncio.run(example())
```
```python
async def example_with_web_search():
    model = 'gpt-4o-mini'
    messages = [{"role": "user", "content": "What is the capital of France?"}]
    async for response in RubiksAI.create_async_generator(model=model, messages=messages, web_search=True):
        print(response, end='')

import asyncio
asyncio.run(example_with_web_search())