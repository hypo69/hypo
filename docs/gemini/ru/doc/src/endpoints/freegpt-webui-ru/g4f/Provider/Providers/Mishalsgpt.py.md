# Модуль Mishalsgpt

## Обзор

Модуль `Mishalsgpt` предоставляет интерфейс для взаимодействия с сервисом Mishalsgpt для генерации текста на основе моделей GPT. Он включает функцию для создания запросов к API и обработки ответов в потоковом режиме.

## Подробней

Этот модуль предназначен для использования в проекте `hypotez` для обеспечения доступа к моделям GPT через API Mishalsgpt. Он поддерживает потоковую передачу ответов, что позволяет получать результаты генерации текста в реальном времени.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """Создает запрос к API Mishalsgpt для генерации текста.

    Args:
        model (str): Идентификатор используемой модели GPT.
        messages (list): Список сообщений для отправки в запросе.
        stream (bool): Флаг, указывающий, следует ли использовать потоковый режим.
        **kwargs: Дополнительные параметры запроса.

    Returns:
        Generator[str, None, None]: Генератор, возвращающий части сгенерированного текста.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при отправке запроса.
        json.JSONDecodeError: Если не удается декодировать JSON-ответ.

    Как работает функция:
    1. Функция `_create_completion` отправляет запрос к API Mishalsgpt для генерации текста на основе предоставленных параметров.
    2. Формирует заголовок запроса `headers` с указанием типа контента `application/json`.
    3. Создает тело запроса `data`, включающее идентификатор модели `model`, температуру `temperature` и список сообщений `messages`.
    4. Отправляет `POST`-запрос на URL-адрес `url + '/api/openai/v1/chat/completions'` с использованием библиотеки `requests`.
    5. Если запрос выполнен успешно, функция извлекает сгенерированный текст из JSON-ответа и возвращает его в виде генератора.

    Внутри функции происходят следующие действия и преобразования:
    A. Формирование заголовков запроса: Создание словаря `headers`, включающего `Content-Type`.
    |
    B. Создание тела запроса: Создание словаря `data` с параметрами `model`, `temperature` и `messages`.
    |
    C. Отправка POST-запроса: Отправка запроса к API Mishalsgpt с использованием библиотеки `requests`.
    |
    D. Извлечение сгенерированного текста: Извлечение текста из JSON-ответа и возвращение его в виде генератора.

    Примеры:
    Пример вызова функции с различными параметрами:
    >>> model_id = 'gpt-3.5-turbo'
    >>> messages_list = [{'role': 'user', 'content': 'Напиши короткий рассказ.'}]
    >>> stream_mode = True
    >>> generator = _create_completion(model=model_id, messages=messages_list, stream=stream_mode)
    >>> for text_part in generator:
    ...     print(text_part)
    """
```

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '({0})'.format(', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]]))
```

`params` - это строка, содержащая информацию о поддерживаемых параметрах функцией `_create_completion`. Она формируется путем извлечения имен параметров и их типов из аннотаций типов функции `_create_completion`.