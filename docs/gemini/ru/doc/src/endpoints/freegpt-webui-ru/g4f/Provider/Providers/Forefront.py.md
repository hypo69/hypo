# Модуль для работы с Forefront API

## Обзор

Модуль предоставляет интерфейс для взаимодействия с API Forefront для генерации текста на основе предоставленных сообщений. Он поддерживает потоковую передачу ответов и использует модель `gpt-3.5-turbo`.

## Подробней

Модуль содержит функцию `_create_completion`, которая отправляет запрос к API Forefront и возвращает сгенерированный текст.  Для отправки запросов используется библиотека `requests`. `Forefront` может быть использован для интеграции в различные приложения, требующие генерации текста, такие как чат-боты или системы автоматического ответа.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """ Функция отправляет запрос к API Forefront и генерирует текст на основе предоставленных сообщений.

    Args:
        model (str): Модель для использования (в данном случае 'gpt-3.5-turbo').
        messages (list): Список сообщений для отправки в API.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу ответов.
        **kwargs: Дополнительные аргументы.

    Yields:
        str: Части сгенерированного текста при потоковой передаче.

    Как работает функция:
    1. Формирует JSON-данные для отправки в API Forefront.
    2. Отправляет POST-запрос на указанный URL с потоковой передачей.
    3. Итерируется по строкам ответа, извлекая полезные данные (токены).
    4. Преобразует токены из JSON и извлекает текст из поля 'delta'.
    5. Генерирует текст по мере поступления токенов.

    ASII flowchart:

    JSON_данные --> POST-запрос --> API Forefront --> Ответ (поток) --> Извлечение токенов --> Генерация текста

    Примеры:
        >>> messages = [{"role": "user", "content": "Hello, how are you?"}]
        >>> for token in _create_completion(model='gpt-3.5-turbo', messages=messages, stream=True):
        ...     print(token, end='')
        I am doing well, thank you for asking. How can I assist you today?
    """
    ...
```

**Параметры**:

-   `model` (str): Модель для использования. В данном случае, всегда `'gpt-3.5-turbo'`.
-   `messages` (list): Список сообщений, где каждое сообщение - словарь с ключами `'role'` и `'content'`.
-   `stream` (bool): Флаг, указывающий, использовать ли потоковую передачу. Если `True`, функция возвращает генератор.
-   `**kwargs`: Дополнительные параметры, которые могут быть переданы в API.

**Возвращает**:

-   `Generator[str, None, None]`: Генератор, выдающий части сгенерированного текста, если `stream=True`.

**Как работает функция**:

1.  **Формирование JSON-данных**: Создается словарь `json_data`, содержащий параметры запроса, включая текст сообщения, идентификаторы, модель и предыдущие сообщения.
2.  **Отправка POST-запроса**: Отправляется POST-запрос к API Forefront по адресу `'https://streaming.tenant-forefront-default.knative.chi.coreweave.com/free-chat'` с использованием библиотеки `requests`. Устанавливается потоковый режим (`stream=True`).
3.  **Обработка потока данных**: Функция итерируется по строкам ответа, полученного от API. Каждая строка представляет собой JSON-объект, содержащий часть сгенерированного текста.
4.  **Извлечение токенов**: Из каждой строки извлекается JSON-объект, содержащий токен (`delta`).
5.  **Генерация текста**: Из токена извлекается текст и генерируется с использованием `yield`.

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, how are you?"}]
for token in _create_completion(model='gpt-3.5-turbo', messages=messages, stream=True):
    print(token, end='')
```

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '({})'.format(', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]]))
```

Описание:
Строка `params` формируется для предоставления информации о поддержке параметров функцией `_create_completion`.

**Как работает**:

1.  `os.path.basename(__file__)[:-3]`: Извлекает имя текущего файла (без расширения `.py`).
2.  `get_type_hints(_create_completion)`: Получает аннотации типов для параметров функции `_create_completion`.
3.  `_create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]`: Извлекает имена параметров функции `_create_completion`.
4.  Генерируется строка, содержащая имена параметров и их типы.

```