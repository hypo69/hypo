# Документация модуля `grock.py`

## Оглавление
1. [Обзор](#обзор)
2. [Классы](#классы)
    - [XAI](#xai)
3. [Функции](#функции)
    - [`_send_request`](#_send_request)
    - [`chat_completion`](#chat_completion)
    - [`stream_chat_completion`](#stream_chat_completion)

## Обзор

Модуль `grock.py` предоставляет класс `XAI` для взаимодействия с API x.ai. Этот класс позволяет отправлять запросы на завершение чата, как в обычном режиме, так и с потоковой передачей ответов.

## Классы

### `XAI`

**Описание**: Класс для взаимодействия с API x.ai.

**Методы**:
- `__init__`: Инициализирует класс `XAI` с заданным API-ключом.
- `_send_request`: Отправляет запрос к API x.ai.
- `chat_completion`: Запрашивает завершение чата (непотоковый режим).
- `stream_chat_completion`: Запрашивает завершение чата с потоковой передачей.

#### `__init__`
```python
def __init__(self, api_key):
    """
    Инициализация класса XAI.

    Args:
        api_key (str): Ключ API для аутентификации.
    """
```
**Описание**: Инициализирует объект `XAI` с заданным ключом API и базовым URL.

**Параметры**:
- `api_key` (str): API-ключ для аутентификации.

#### `_send_request`
```python
def _send_request(self, method, endpoint, data=None):
    """
    Отправка запроса к API x.ai.

    Args:
        method (str): Метод HTTP (GET, POST, PUT, DELETE).
        endpoint (str): Конечная точка API.
        data (Optional[dict], optional): Данные для отправки в теле запроса (для POST и PUT). По умолчанию None.

    Returns:
        dict: Ответ от API.

    Raises:
        requests.exceptions.HTTPError: Вызывает исключение, если статус ответа не 2xx.
    """
```
**Описание**: Отправляет HTTP-запрос к API x.ai.

**Параметры**:
- `method` (str): HTTP-метод запроса (например, "GET", "POST").
- `endpoint` (str): Конечная точка API.
- `data` (Optional[dict], optional): Данные запроса в формате JSON. По умолчанию `None`.

**Возвращает**:
- `dict`: Ответ от API в формате JSON.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если статус ответа не 2xx.

## Функции

### `chat_completion`

```python
def chat_completion(self, messages, model="grok-beta", stream=False, temperature=0):
    """
    Запрос на завершение чата.

    Args:
        messages (list[dict]): Список сообщений для чата.
        model (str, optional): Модель для использования. По умолчанию "grok-beta".
        stream (bool, optional): Флаг для включения потоковой передачи. По умолчанию False.
        temperature (float, optional): Температура для генерации ответа. По умолчанию 0.

    Returns:
        dict: Ответ от API.
    """
```

**Описание**: Запрашивает завершение чата с указанными параметрами.

**Параметры**:
- `messages` (list[dict]): Список сообщений для чата.
- `model` (str, optional): Имя модели для использования. По умолчанию `"grok-beta"`.
- `stream` (bool, optional): Включает потоковую передачу, если `True`. По умолчанию `False`.
- `temperature` (float, optional): Температура для генерации ответов. По умолчанию `0`.

**Возвращает**:
- `dict`: Ответ от API.

### `stream_chat_completion`

```python
def stream_chat_completion(self, messages, model="grok-beta", temperature=0):
    """
    Запрос на завершение чата с потоковой передачей.

    Args:
        messages (list[dict]): Список сообщений для чата.
        model (str, optional): Модель для использования. По умолчанию "grok-beta".
        temperature (float, optional): Температура для генерации ответа. По умолчанию 0.

    Returns:
        Iterable[str]: Поток ответов от API.
    
    Raises:
        requests.exceptions.HTTPError: Вызывает исключение, если статус ответа не 2xx.
    """
```

**Описание**: Запрашивает завершение чата с потоковой передачей ответов.

**Параметры**:
- `messages` (list[dict]): Список сообщений для чата.
- `model` (str, optional): Имя модели для использования. По умолчанию `"grok-beta"`.
- `temperature` (float, optional): Температура для генерации ответов. По умолчанию `0`.

**Возвращает**:
- `Iterable[str]`: Итератор, возвращающий строки JSON-ответов от API.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если статус ответа не 2xx.