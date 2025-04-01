# Модуль `ChatgptLogin.py`

## Обзор

Модуль предоставляет класс для взаимодействия с сервисом `chatgptlogin.ac`. Он позволяет отправлять запросы к ChatGPT через API этого сервиса и получать ответы. Модуль включает функции для преобразования сообщений в формат, требуемый API, и получения nonce для заголовков запроса.

## Подробней

Этот модуль используется для обхода ограничений доступа к ChatGPT путем использования сервиса `chatgptlogin.ac`. Он автоматизирует процесс отправки запросов и получения ответов, предоставляя удобный интерфейс для взаимодействия с моделью `gpt-3.5-turbo`.

## Параметры

- `url` (str): URL-адрес сервиса `chatgptlogin.ac`.
- `model` (list): Список поддерживаемых моделей (в данном случае `gpt-3.5-turbo`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (в данном случае `False`).
- `needs_auth` (bool): Указывает, требуется ли аутентификация для доступа к сервису (в данном случае `False`).

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """Создает запрос к API chatgptlogin.ac и возвращает ответ.

    Args:
        model (str): Название используемой модели.
        messages (list): Список сообщений для отправки в запросе.
                         Каждый элемент списка - словарь с ключами 'role' (роль отправителя, например, 'user' или 'assistant')
                         и 'content' (текст сообщения).
        stream (bool): Флаг, указывающий, нужно ли использовать потоковую передачу.
        **kwargs: Дополнительные параметры.

    Returns:
        str: Ответ от API в виде строки.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при отправке запроса.
        re.error: Если возникает ошибка при работе с регулярными выражениями.
        Exception: Если происходит внутренняя ошибка при обработке ответа.
    """
```

**Как работает функция**:
1. Функция `_create_completion` является основной функцией для взаимодействия с API `chatgptlogin.ac`.
2. Внутри функции вызывается `get_nonce` для получения уникального nonce, необходимого для заголовков запроса.
3. Функция `transform` преобразует список сообщений в формат, ожидаемый API.
4. Формируются заголовки запроса, включая полученный nonce.
5. Формируются данные JSON для отправки запроса, включая преобразованные сообщения и параметры модели.
6. Отправляется POST-запрос к API `chatgptlogin.ac` с заголовками и данными JSON.
7. Обрабатывается ответ от API и извлекается текст ответа.

**Внутренние функции**:

#### `get_nonce`

```python
def get_nonce():
    """Получает nonce для заголовков запроса с сайта chatgptlogin.ac.

    Returns:
        str: Nonce, извлеченный из HTML-кода страницы.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при выполнении GET-запроса.
        AttributeError: Если не удается извлечь nonce из HTML-кода.
    """
```

**Как работает функция**:

1.  Функция `get_nonce` отправляет GET-запрос к странице `https://chatgptlogin.ac/use-chatgpt-free/`.
2.  Извлекает JavaScript-файл, содержащий nonce, используя регулярное выражение.
3.  Декодирует base64 строку и извлекает nonce из декодированной строки с помощью регулярного выражения.

#### `transform`

```python
def transform(messages: list) -> list:
    """Преобразует список сообщений в формат, ожидаемый API chatgptlogin.ac.

    Args:
        messages (list): Список сообщений для преобразования.

    Returns:
        list: Список преобразованных сообщений.
    """
```

**Как работает функция**:

1.  Функция `transform` преобразует входящий список сообщений в формат, необходимый для API `chatgptlogin.ac`.
2.  Для каждого сообщения генерируется уникальный идентификатор, добавляется роль и содержимое сообщения, а также форматируется содержимое с использованием HTML-кодирования.

##### `html_encode`

```python
def html_encode(string: str) -> str:
    """Преобразует специальные символы в HTML-сущности.

    Args:
        string (str): Строка для преобразования.

    Returns:
        str: Преобразованная строка с HTML-сущностями.
    """
```

**Как работает функция**:
1.  Функция `html_encode` принимает строку в качестве аргумента и заменяет в ней специальные символы на соответствующие HTML-сущности.
2.  Определяется словарь `table`, содержащий пары "символ": "HTML-сущность".
3.  Выполняется итерация по ключам словаря `table`, и каждый символ заменяется на его HTML-сущность в переданной строке.
4.  Возвращается строка с замененными HTML-сущностями.

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, how are you?"}, {"role": "assistant", "content": "I am fine, thank you."}]
transformed_messages = transform(messages)
print(transformed_messages)
# Expected output:
# [{'id': '...', 'role': 'user', 'content': 'Hello, how are you?', 'who': 'User: ', 'html': 'Hello,&nbsp;how&nbsp;are&nbsp;you?'},
#  {'id': '...', 'role': 'assistant', 'content': 'I am fine, thank you.', 'who': 'AI: ', 'html': 'I&nbsp;am&nbsp;fine,&nbsp;thank&nbsp;you.'}]
```

**Примеры**:

```python
# Пример вызова функции _create_completion
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello!"}]
stream = False
response = _create_completion(model=model, messages=messages, stream=stream)
print(response)
# Expected output: "Hello there! How can I assist you today?"
```

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

Описание:
Строка `params` формирует строку с информацией о поддержке параметров функцией `_create_completion`. Она использует f-строку для создания строки, включающей имя файла модуля и список поддерживаемых параметров с их типами.