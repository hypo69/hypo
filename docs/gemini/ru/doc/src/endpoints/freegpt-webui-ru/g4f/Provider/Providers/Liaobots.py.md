# Модуль `Liaobots.py`

## Обзор

Модуль предоставляет интерфейс для взаимодействия с провайдером Liaobots, использующим модели GPT-3.5-turbo и GPT-4. Он содержит функции для создания запросов к API Liaobots и получения ответов в потоковом режиме. Модуль требует аутентификации.

## Подробнее

Модуль предназначен для интеграции с сервисом Liaobots и предоставляет функциональность для обмена сообщениями с использованием моделей GPT. Он определяет параметры подключения, заголовки запросов и формат данных для взаимодействия с API Liaobots.

## Переменные

- `url (str)`: URL-адрес сервиса Liaobots (`https://liaobots.com`).
- `model (List[str])`: Список поддерживаемых моделей (`gpt-3.5-turbo`, `gpt-4`).
- `supports_stream (bool)`: Указывает, поддерживает ли провайдер потоковую передачу данных (`True`).
- `needs_auth (bool)`: Указывает, требуется ли аутенентификация (`True`).
- `models (Dict[str, Dict[str, str | int]])`: Словарь с информацией о моделях, включая `id`, `name`, `maxLength` и `tokenLimit`.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает запрос к API Liaobots для генерации завершения текста.

    Args:
        model (str): Идентификатор используемой модели (`gpt-3.5-turbo` или `gpt-4`).
        messages (list): Список сообщений для отправки в API.
        stream (bool): Указывает, использовать ли потоковый режим передачи данных.
        **kwargs: Дополнительные параметры запроса, включая ключ аутентификации (`auth`).

    Returns:
        Generator[str, None, None]: Генератор, возвращающий токены ответа от API Liaobots.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при отправке запроса.

    Как работает функция:
    1. Функция принимает параметры модели, сообщения, флаг потоковой передачи и дополнительные аргументы.
    2. Формируются заголовки запроса, включая `x-auth-code` из `kwargs`.
    3. Создается JSON-структура данных для отправки в API, включающая идентификатор разговора, модель, сообщения, ключ и промпт.
    4. Отправляется POST-запрос к API Liaobots с указанными заголовками и данными.
    5. Функция итерирует по содержимому ответа в чанках размером 2046 байт и декодирует каждый чанк в UTF-8.
    6. Каждый декодированный чанк возвращается как токен через генератор.

    Примеры:
        # Пример вызова функции с минимальными параметрами
        >>> model = 'gpt-3.5-turbo'
        >>> messages = [{'role': 'user', 'content': 'Hello'}]
        >>> stream = True
        >>> auth = 'your_auth_key'
        >>> generator = _create_completion(model, messages, stream, auth=auth)
        >>> for token in generator:
        ...     print(token)
    """
    ...
```

### `params`

```python
params = f\'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: \' + \\\n    \'(%s)\' % \', \'.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

**Описание**: Строка, содержащая информацию о поддержке типов параметров функцией `_create_completion`. Содержит имя файла модуля, а также список типов параметров, поддерживаемых функцией `_create_completion`.

**Как работает**:
1.  Извлекается имя файла текущего модуля с помощью `os.path.basename(__file__)[:-3]`.
2.  Извлекаются аннотации типов для параметров функции `_create_completion` с помощью `get_type_hints(_create_completion)`.
3.  Формируется строка с информацией о поддержке типов параметров.

**Примеры**
```python
# Пример значения переменной params
params = 'g4f.Providers.Liaobots supports: (model: str, messages: list, stream: bool)'