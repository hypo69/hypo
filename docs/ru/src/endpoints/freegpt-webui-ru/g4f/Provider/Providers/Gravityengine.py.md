# Модуль для работы с провайдером Gravityengine
## Обзор

Модуль предоставляет интерфейс для взаимодействия с сервисом Gravityengine через их API для создания завершений чата. Он поддерживает потоковую передачу данных и работает с моделями, такими как 'gpt-3.5-turbo-16k' и 'gpt-3.5-turbo-0613'.

## Подробнее

Этот модуль предназначен для интеграции с Gravityengine, позволяя отправлять запросы на генерацию текста и получать ответы в потоковом режиме. Он определяет функцию `_create_completion`, которая формирует и отправляет запросы к API Gravityengine.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """Функция для создания запроса к Gravityengine API для получения завершения чата.

    Args:
        model (str): Идентификатор используемой модели.
        messages (list): Список сообщений для передачи в запросе.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу.
        **kwargs: Дополнительные параметры запроса.

    Returns:
        Generator[str, None, None]: Генератор, возвращающий содержимое ответа от API Gravityengine.

    Raises:
        Exception: Если возникает ошибка при запросе к API.

    """
```

**Назначение**:
Функция `_create_completion` отвечает за отправку запроса к API Gravityengine и получение ответа.

**Параметры**:
- `model` (str): Идентификатор модели, которую необходимо использовать для генерации завершения.
- `messages` (list): Список сообщений, составляющих контекст запроса.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковый режим передачи данных.
- `**kwargs`: Дополнительные именованные аргументы, которые могут быть переданы в API Gravityengine.

**Возвращает**:
- `Generator[str, None, None]`: Генератор, который выдает содержимое ответа от API Gravityengine.

**Как работает функция**:

1.  **Формирование заголовков**: Функция создает заголовки запроса, указывая тип контента как `application/json`.

2.  **Формирование данных запроса**: Создается словарь `data`, включающий модель, температуру, штраф за присутствие и сообщения.

3.  **Отправка POST-запроса**: Используется библиотека `requests` для отправки POST-запроса к API Gravityengine. В запросе указываются URL, заголовки, данные и флаг потоковой передачи.

4.  **Обработка ответа**: Функция ожидает JSON-ответ от API и извлекает содержимое первого сообщения из списка `choices`.

5.  **Генерация результата**: Функция возвращает генератор, который выдает извлеченное содержимое сообщения.

**ASCII Flowchart**:

```
FormHeaders  -> FormData
FormData   -> SendPostRequest
SendPostRequest -> ReceiveJsonResponse
ReceiveJsonResponse -> ExtractContent
ExtractContent -> YieldContent
```

**Примеры**:

```python
# Пример вызова функции
model = "gpt-3.5-turbo-16k"
messages = [{"role": "user", "content": "Hello, how are you?"}]
stream = True

# Создание генератора
response_generator = _create_completion(model=model, messages=messages, stream=stream)

# Получение данных из генератора
for chunk in response_generator:
    print(chunk)
```

## Переменные

### `url`
```python
url = 'https://gpt4.gravityengine.cc'
```

URL-адрес API Gravityengine. Используется для отправки запросов.

### `model`
```python
model = ['gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0613']
```

Список поддерживаемых моделей для использования с API Gravityengine.

### `supports_stream`
```python
supports_stream = True
```

Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.

### `needs_auth`
```python
needs_auth = False
```

Флаг, указывающий, требуется ли аутентификация для работы с провайдером.

### `params`
```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

Строка, содержащая информацию о поддерживаемых параметрах функции `_create_completion`.