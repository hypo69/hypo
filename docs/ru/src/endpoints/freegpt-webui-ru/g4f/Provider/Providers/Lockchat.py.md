# Документация модуля Lockchat

## Обзор

Модуль `Lockchat.py` предоставляет реализацию для взаимодействия с сервисом Lockchat, использующим модели GPT (в частности, `gpt-4` и `gpt-3.5-turbo`). Этот модуль позволяет отправлять запросы к API Lockchat и получать ответы в потоковом режиме.

## Подробней

Модуль содержит функцию `_create_completion`, которая отправляет запросы к API Lockchat и обрабатывает ответы. Lockchat используется для получения ответов от языковых моделей, таких как GPT-4 и GPT-3.5-turbo, через их API. В проекте `hypotez` модуль обеспечивает возможность использования Lockchat в качестве одного из провайдеров для получения ответов от языковых моделей. Он поддерживает потоковую передачу данных, что позволяет получать ответы в реальном времени.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, temperature: float = 0.7, **kwargs):
    """ Функция отправляет запрос к API Lockchat и возвращает ответ в потоковом режиме.

    Args:
        model (str): Имя используемой модели (например, 'gpt-4', 'gpt-3.5-turbo').
        messages (list): Список сообщений для отправки в запросе.
        stream (bool): Флаг, указывающий, следует ли возвращать ответ в потоковом режиме.
        temperature (float, optional): Температура для контроля случайности ответов модели. По умолчанию 0.7.
        **kwargs: Дополнительные параметры.

    Returns:
        Generator[str, None, None]: Генератор токенов ответа, если `stream=True`.

    Raises:
        Exception: Если возникает ошибка при запросе к API или обработке ответа.

    Example:
        >>> messages = [{"role": "user", "content": "Hello, how are you?"}]
        >>> for token in _create_completion(model='gpt-3.5-turbo', messages=messages, stream=True):
        ...     print(token, end='')
        I'm doing well, thank you for asking!
    """
```

**Как работает функция**:

1. **Подготовка полезной нагрузки (payload)**:
   - Создается словарь `payload`, содержащий параметры запроса, такие как `temperature`, `messages`, `model` и `stream`.

2. **Настройка заголовков (headers)**:
   - Определяются заголовки `headers`, включающие `user-agent` для имитации запроса от приложения ChatX.

3. **Отправка POST-запроса**:
   - Отправляется POST-запрос к API Lockchat (`http://super.lockchat.app/v1/chat/completions?auth=FnMNPlwZEnGFqvEc9470Vw==`) с использованием библиотеки `requests`. Указываются `json=payload`, `headers=headers` и `stream=True` для потоковой передачи.

4. **Обработка потока токенов**:
   - Функция итерируется по строкам ответа (`response.iter_lines()`).
   - Проверяется наличие ошибки, связанной с отсутствием модели (`b'The model: \`gpt-4\` does not exist'`). Если ошибка обнаружена, функция рекурсивно вызывает себя для повторной попытки.
   - Если в токене содержится `"content"`, то извлекается содержимое токена из JSON-формата, декодируется из UTF-8 и разделяется по строке `'data: '`. Извлекается контент из `token = json.loads(token.decode('utf-8').split('data: ')[1])['choices'][0]['delta'].get('content')`.
   - Если извлеченный контент существует, он возвращается с использованием `yield (token)`.

```
    Подготовка запроса
    │
    ├──► Создание payload (temperature, messages, model, stream)
    │
    ├──► Настройка headers (user-agent)
    │
    Отправка запроса
    │
    ├──► POST запрос к API Lockchat (json=payload, headers=headers, stream=True)
    │
    Обработка ответа
    │
    ├──► Итерация по строкам ответа (response.iter_lines())
    │
    ├──► Проверка на ошибку отсутствия модели
    │   └──► Если ошибка, рекурсивный вызов _create_completion
    │
    ├──► Извлечение содержимого токена из JSON
    │   └──► yield (token)
    │
    Конец
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, how are you?"}]
for token in _create_completion(model='gpt-3.5-turbo', messages=messages, stream=True):
    print(token, end='')
```

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

**Назначение**:

Формирует строку с информацией о поддерживаемых типах параметров функции `_create_completion`.

**Как работает**:

1. **Получение имени файла**:
   - `os.path.basename(__file__)[:-3]` извлекает имя текущего файла (`Lockchat.py`) и удаляет расширение `.py`.

2. **Формирование строки параметров**:
   - `get_type_hints(_create_completion)` возвращает словарь с аннотациями типов для параметров функции `_create_completion`.
   - `_create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]` получает имена параметров функции.
   - Генератор списка `[f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]]` создает список строк, где каждая строка имеет формат `"имя_параметра: тип_параметра"`.
   - `', '.join(...)` объединяет строки списка через запятую и пробел.
   - `f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + '(%s)' % ...` формирует итоговую строку, содержащую имя провайдера и поддерживаемые типы параметров.

**Примеры**:

```python
print(params)
# g4f.Providers.Lockchat supports: (model: str, messages: list, stream: bool, temperature: float)