# Модуль Yqcloud.py

## Обзор

Модуль `Yqcloud.py` предоставляет класс для взаимодействия с сервисом Yqcloud для генерации текста. Он определяет функцию `_create_completion`, которая отправляет запросы к API Yqcloud и возвращает сгенерированный текст. Модуль также содержит информацию о поддерживаемых моделях и требованиях аутентификации.

## Подробней

Модуль `Yqcloud.py` предназначен для интеграции с сервисом Yqcloud, который предоставляет API для генерации текста.  Модуль определяет функцию `_create_completion`, которая формирует и отправляет POST-запросы к API `https://api.aichatos.cloud/api/generateStream` с использованием библиотеки `requests`. Функция обрабатывает ответ от API, извлекая токены сгенерированного текста и возвращая их. Модуль также определяет параметры, такие как поддерживаемые модели (`model`) и необходимость аутентификации (`needs_auth`).

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """ Функция отправляет запрос к API Yqcloud и возвращает сгенерированный текст.

    Args:
        model (str): Имя используемой модели.
        messages (list): Список сообщений для отправки в API.
        stream (bool): Флаг, указывающий, нужно ли возвращать результат в потоковом режиме.
        **kwargs: Дополнительные аргументы.

    Returns:
        Generator[str, None, None]: Генератор токенов сгенерированного текста.

    Как работает функция:

    1. Формирование заголовков HTTP-запроса.
    2. Формирование тела запроса в формате JSON, включающего промпт, идентификатор пользователя и другие параметры.
    3. Отправка POST-запроса к API `https://api.aichatos.cloud/api/generateStream` с использованием библиотеки `requests` и включением потоковой передачи данных.
    4. Итерация по содержимому ответа, извлечение токенов сгенерированного текста и возврат их через генератор.

    ASCII Flowchart:

    Запрос к API Yqcloud
    │
    └── Запрос (headers, json_data)
    │
    Ответ от API Yqcloud
    │
    └── Итерация по содержимому ответа (response.iter_content)
    │
    Извлечение токенов
    │
    └── Декодирование токенов (token.decode('utf-8'))
    │
    Возврат токенов (yield)

    Примеры:
    - Вызов с минимальными параметрами:
        _create_completion(model='gpt-3.5-turbo', messages=[{'content': 'Hello'}], stream=True)

    - Вызов с дополнительными параметрами:
        _create_completion(model='gpt-3.5-turbo', messages=[{'content': 'Translate to French: Hello'}], stream=True, temperature=0.7)

    """

    def inner_function():
        """Внутренняя функция не используется.

        Args:
            param (str): Описание параметра `param`.
            param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

        Returns:
            dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

        Raises:
            SomeError: Описание ситуации, в которой возникает исключение `SomeError`.

        ...
        """

        ...

    headers = {
        'authority': 'api.aichatos.cloud',
        'origin': 'https://chat9.yqcloud.top',
        'referer': 'https://chat9.yqcloud.top/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    json_data = {
        'prompt': 'always respond in english | %s' % messages[-1]['content'],
        'userId': f'#/chat/{int(time.time() * 1000)}',
        'network': True,
        'apikey': '',
        'system': '',
        'withoutContext': False,
    }

    response = requests.post('https://api.aichatos.cloud/api/generateStream', headers=headers, json=json_data, stream=True)
    for token in response.iter_content(chunk_size=2046):
        if not b'always respond in english' in token:
            yield (token.decode('utf-8'))
```

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '({0})'.format(', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]]))
```

**Назначение**: Формирует строку с информацией о поддерживаемых параметрах функции `_create_completion`.

**Как работает**:

1.  **`os.path.basename(__file__)[:-3]`**: Извлекает имя текущего файла (`Yqcloud.py`) и удаляет расширение `.py`.
2.  **`_create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]`**: Получает список имен аргументов функции `_create_completion`.
3.  **`get_type_hints(_create_completion)[name].__name__`**: Для каждого аргумента получает его тип из аннотации типов и извлекает имя типа.
4.  **`', '.join(...)`**: Объединяет имена аргументов и их типы в строку, разделенную запятыми.
5.  **`f'g4f.Providers.{...} supports: ({...})'`**: Формирует итоговую строку, включающую имя провайдера (`g4f.Providers.Yqcloud`) и список поддерживаемых параметров с их типами.

**Пример**:

```python
print(params)
# g4f.Providers.Yqcloud supports: (model: str, messages: list, stream: bool, kwargs: dict)