# Модуль `Yqcloud.py`

## Обзор

Модуль предназначен для взаимодействия с Yqcloud API для генерации текста. Он предоставляет функцию `_create_completion`, которая отправляет запросы к API и возвращает сгенерированный текст. Модуль поддерживает потоковую передачу данных и не требует аутентификации.

## Подробней

Этот модуль предоставляет интерфейс к API Yqcloud, который используется для генерации текста на основе предоставленных сообщений. Он отправляет POST-запросы к `https://api.aichatos.cloud/api/generateStream` и обрабатывает ответы в потоковом режиме. Модуль предназначен для интеграции с другими частями проекта `hypotez`, где требуется генерация текста с использованием Yqcloud API.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает запрос к Yqcloud API для генерации текста на основе предоставленных сообщений.

    Args:
        model (str): Идентификатор модели для генерации текста.
        messages (list): Список сообщений для генерации текста.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
        **kwargs: Дополнительные параметры.

    Yields:
        str: Сгенерированный текст.

    Как работает функция:
    1. Формирует заголовки запроса, включая `authority`, `origin`, `referer` и `user-agent`.
    2. Создает JSON-данные для запроса, включая `prompt`, `userId`, `network`, `apikey` и `withoutContext`.
       - `prompt` формируется как "always respond in english | %s", где %s - последнее сообщение из `messages`.
       - `userId` генерируется на основе текущего времени.
    3. Отправляет POST-запрос к `https://api.aichatos.cloud/api/generateStream` с использованием `requests.post`.
    4. Итерируется по содержимому ответа в потоковом режиме с помощью `response.iter_content(chunk_size=2046)`.
    5. Для каждого полученного токена проверяет, содержит ли он `b'always respond in english'`.
       - Если не содержит, декодирует токен в UTF-8 и возвращает его.

    Примеры:
        Пример вызова функции:
        _create_completion(model='gpt-3.5-turbo', messages=[{'content': 'Hello, how are you?'}], stream=True)
    """
```

**ASCII Flowchart функции `_create_completion`**:

```
A [Формирование заголовков запроса]
│
B [Создание JSON-данных для запроса]
│
C [Отправка POST-запроса к API]
│
D [Итерация по содержимому ответа в потоковом режиме]
│
E [Проверка наличия 'always respond in english' в токене]
│
F [Декодирование токена в UTF-8 и возврат]
```

**Параметры**
- `model` (str): Идентификатор модели для генерации текста.
- `messages` (list): Список сообщений для генерации текста.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `str`: Сгенерированный текст.

**Внутренние функции**: Нет

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '({0})'.format(', '.join(['{0}: {1}'.format(name, get_type_hints(_create_completion)[name].__name__) for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]]))
```

**Назначение**: Формирует строку с информацией о поддержке параметров функцией `_create_completion`.

**Как работает переменная**:

1.  **Извлечение имени файла**: `os.path.basename(__file__)[:-3]` извлекает имя текущего файла (например, `"Yqcloud.py"`) и удаляет последние три символа (".py"), чтобы получить имя модуля (например, `"Yqcloud"`).
2.  **Формирование списка параметров**:
    *   `_create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]` получает имена всех аргументов функции `_create_completion`.
    *   `get_type_hints(_create_completion)` возвращает словарь, содержащий аннотации типов для аргументов функции `_create_completion`.
    *   `['{0}: {1}'.format(name, get_type_hints(_create_completion)[name].__name__) for name in ...]` создает список строк, где каждая строка имеет формат `"имя_параметра: тип_параметра"`.
3.  **Объединение параметров в строку**: `', '.join([...])` объединяет все элементы списка в одну строку, разделяя их запятой и пробелом.
4.  **Формирование итоговой строки**: `'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ({0})'.format(...)` формирует итоговую строку, которая содержит имя модуля и список поддерживаемых параметров с их типами.

**Примеры**:

В результате работы этого кода может быть сформирована следующая строка:

```
'g4f.Providers.Yqcloud supports: (model: str, messages: list, stream: bool, kwargs: Dict)'