# Модуль Aichat

## Обзор

Модуль предоставляет класс для взаимодействия с провайдером Aichat, использующим API `chat-gpt.org`. Он содержит функцию `_create_completion`, которая отправляет запросы к API и возвращает ответы.

## Подробней

Этот модуль предназначен для интеграции с провайдером Aichat, который предоставляет доступ к моделям, подобным `gpt-3.5-turbo`. Модуль включает в себя параметры для настройки HTTP-запросов, таких как заголовки и JSON-данные, необходимые для взаимодействия с API.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает завершение текста на основе предоставленных сообщений, используя API chat-gpt.org.

    Args:
        model (str): Имя используемой модели.
        messages (list): Список сообщений для отправки в API.
        stream (bool): Указывает, нужно ли использовать потоковую передачу.
        **kwargs: Дополнительные параметры.

    Yields:
        str: Сгенерированное сообщение от API.

    Как работает функция:
        1. Формирует базовый текст запроса из предоставленных сообщений, объединяя их в одну строку.
        2. Определяет необходимые заголовки для HTTP-запроса.
        3. Подготавливает JSON-данные для отправки, включая базовый текст, параметры температуры, штрафов присутствия, верхнего значения P и штрафов частоты.
        4. Отправляет POST-запрос к API `chat-gpt.org/api/text`.
        5. Извлекает сгенерированное сообщение из JSON-ответа и возвращает его.

    ASCII Flowchart:

    Сообщения --> Формирование базового текста
         |
         --> Определение заголовков
         |
         --> Подготовка JSON-данных
         |
         --> Отправка POST-запроса (chat-gpt.org/api/text)
         |
         --> Извлечение сообщения из JSON-ответа
         |
         --> Возврат сгенерированного сообщения

    Примеры:
        >>> messages = [{'role': 'user', 'content': 'Hello, how are you?'}]
        >>> generator = _create_completion(model='gpt-3.5-turbo', messages=messages, stream=False)
        >>> for response in generator:
        ...     print(response)
        I am doing well, thank you for asking. How can I assist you today?
    """
    ...
```

## Переменные

### `url`

```python
url = 'https://chat-gpt.org/chat'
```
URL для взаимодействия с `chat-gpt.org`.

### `model`

```python
model = ['gpt-3.5-turbo']
```
Список поддерживаемых моделей.

### `supports_stream`

```python
supports_stream = False
```
Указывает, поддерживается ли потоковая передача.

### `needs_auth`

```python
needs_auth = False
```
Указывает, требуется ли аутентификация.

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```
Строка, формирующая описание поддерживаемых параметров функции `_create_completion` для использования в `g4f`.