# Модуль `grock.py`

## Обзор

Модуль предоставляет класс `XAI` для взаимодействия с API x.ai, позволяя отправлять запросы на завершение чата как в обычном, так и в потоковом режимах.

## Оглавление

1. [Классы](#классы)
    - [`XAI`](#xai)
2. [Функции](#функции)
    - [`_send_request`](#_send_request)
    - [`chat_completion`](#chat_completion)
    - [`stream_chat_completion`](#stream_chat_completion)

## Классы

### `XAI`

**Описание**: Класс для взаимодействия с API x.ai.

**Методы**:
- `__init__`: Инициализирует класс XAI с заданным API-ключом.
- `_send_request`: Отправляет запрос к API x.ai.
- `chat_completion`: Выполняет запрос на завершение чата.
- `stream_chat_completion`: Выполняет запрос на завершение чата с потоковой передачей.

#### `__init__`
```python
    def __init__(self, api_key):
        """
        Инициализация класса XAI.

        :param api_key: Ключ API для аутентификации.
        """
```
**Описание**: Инициализирует класс `XAI`, устанавливая API-ключ, базовый URL и заголовки для запросов.

**Параметры**:
- `api_key` (str): Ключ API для аутентификации.

## Функции

### `_send_request`

```python
    def _send_request(self, method, endpoint, data=None):
        """
        Отправка запроса к API x.ai.

        :param method: Метод HTTP (GET, POST, PUT, DELETE).
        :param endpoint: Конечная точка API.
        :param data: Данные для отправки в теле запроса (для POST и PUT).
        :return: Ответ от API.
        """
```

**Описание**: Отправляет запрос к API x.ai с указанным методом, конечной точкой и данными.

**Параметры**:
- `method` (str): Метод HTTP (GET, POST, PUT, DELETE).
- `endpoint` (str): Конечная точка API.
- `data` (Optional[dict]): Данные для отправки в теле запроса (для POST и PUT). По умолчанию `None`.

**Возвращает**:
- `dict`: Ответ от API в формате JSON.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если статус ответа не 2xx.

### `chat_completion`

```python
    def chat_completion(self, messages, model="grok-beta", stream=False, temperature=0):
        """
        Запрос на завершение чата.

        :param messages: Список сообщений для чата.
        :param model: Модель для использования.
        :param stream: Флаг для включения потоковой передачи.
        :param temperature: Температура для генерации ответа.
        :return: Ответ от API.
        """
```

**Описание**: Отправляет запрос на завершение чата к API x.ai.

**Параметры**:
- `messages` (list): Список сообщений для чата.
- `model` (str): Модель для использования. По умолчанию "grok-beta".
- `stream` (bool): Флаг для включения потоковой передачи. По умолчанию `False`.
- `temperature` (int): Температура для генерации ответа. По умолчанию 0.

**Возвращает**:
- `dict`: Ответ от API в формате JSON.

### `stream_chat_completion`

```python
    def stream_chat_completion(self, messages, model="grok-beta", temperature=0):
        """
        Запрос на завершение чата с потоковой передачей.

        :param messages: Список сообщений для чата.
        :param model: Модель для использования.
        :param temperature: Температура для генерации ответа.
        :return: Поток ответов от API.
        """
```

**Описание**: Отправляет запрос на завершение чата с потоковой передачей к API x.ai.

**Параметры**:
- `messages` (list): Список сообщений для чата.
- `model` (str): Модель для использования. По умолчанию "grok-beta".
- `temperature` (int): Температура для генерации ответа. По умолчанию 0.

**Возвращает**:
- `Iterable[str]`: Поток ответов от API в виде строк.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если статус ответа не 2xx.