# Модуль Gravityengine

## Обзор

Модуль предоставляет реализацию провайдера Gravityengine для использования в G4F (интерфейсе для работы с большими языковыми моделями).
Он позволяет взаимодействовать с API Gravityengine для получения ответов от моделей, таких как `gpt-3.5-turbo-16k` и `gpt-3.5-turbo-0613`. Модуль поддерживает потоковую передачу данных и не требует аутентификации.

## Подробней

Модуль содержит функцию `_create_completion`, которая отправляет запросы к API Gravityengine и возвращает ответы модели.
В модуле также определена переменная `params`, содержащая информацию о поддержке параметров функцией `_create_completion`.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """Создает запрос к API Gravityengine и возвращает ответ модели.

    Args:
        model (str): Имя используемой модели.
        messages (list): Список сообщений для отправки модели.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
        **kwargs: Дополнительные аргументы.

    Yields:
        str: Ответ модели.

    Как работает функция:
    1. Функция формирует заголовки запроса, включая `Content-Type`.
    2. Создает тело запроса `data`, содержащее имя модели, температуру, штраф за присутствие и сообщения.
    3. Отправляет POST-запрос к API Gravityengine (`/api/openai/v1/chat/completions`) с заголовками и телом запроса.
    4. Итерируется по ответу, возвращая содержимое ответа модели.

    ASCII flowchart:
    Запрос к API
    ↓
    Создание заголовков и тела запроса
    ↓
    Отправка POST-запроса
    ↓
    Получение ответа
    ↓
    Извлечение контента из ответа
    ↓
    Возврат контента

    Примеры:
        >>> model = 'gpt-3.5-turbo-16k'
        >>> messages = [{'role': 'user', 'content': 'Hello, world!'}]
        >>> stream = True
        >>> for response in _create_completion(model, messages, stream):
        ...     print(response)
    """
    ...
```

**Параметры**:
- `model` (str): Имя используемой модели.
- `messages` (list): Список сообщений для отправки модели.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `str`: Ответ модели в виде строки.

## Переменные

### `url`
```python
url = 'https://gpt4.gravityengine.cc'
```
URL API Gravityengine.

### `model`
```python
model = ['gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0613']
```
Список поддерживаемых моделей.

### `supports_stream`
```python
supports_stream = True
```
Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.

### `needs_auth`
```python
needs_auth = False
```
Флаг, указывающий, требуется ли аутентификация для доступа к API.

### `params`
```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```
Строка, содержащая информацию о поддержке параметров функцией `_create_completion`. Содержит имя файла без расширения `.py` и типы данных входных параметров.