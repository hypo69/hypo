# Модуль для взаимодействия с ChatGPT Login через веб-интерфейс

## Обзор

Модуль `ChatgptLogin.py` предназначен для обеспечения взаимодействия с моделью `gpt-3.5-turbo` через веб-интерфейс `chatgptlogin.ac`. Он включает в себя функции для создания запросов к чат-боту, преобразования сообщений и получения ответов. Модуль поддерживает отправку сообщений и получение ответов от AI-ассистента.

## Подробнее

Данный модуль предоставляет способ взаимодействия с моделью `gpt-3.5-turbo` через API веб-сайта `chatgptlogin.ac`. Он использует HTTP-запросы для отправки сообщений и получения ответов, имитируя взаимодействие пользователя с чат-ботом через веб-интерфейс. Это позволяет использовать модель без необходимости прямой аутентификации через API OpenAI.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает запрос к ChatGPT Login и возвращает ответ.

    Args:
        model (str): Название используемой модели (например, "gpt-3.5-turbo").
        messages (list): Список сообщений для отправки в чат-бот.
                        Каждый элемент списка - словарь с ключами 'role' и 'content'.
                        'role' указывает роль (например, 'user' или 'assistant'), а 'content' - текст сообщения.
        stream (bool): Флаг, указывающий на необходимость потоковой передачи данных (не используется в данной реализации).
        **kwargs: Дополнительные параметры (не используются в данной реализации).

    Returns:
        str: Ответ от чат-бота.

    **Как работает функция**:

    1.  **Извлечение nonce**: Функция `get_nonce` отправляет GET-запрос на главную страницу `chatgptlogin.ac` для извлечения nonce, необходимого для последующих POST-запросов.
    2.  **Преобразование сообщений**: Функция `transform` преобразует список сообщений в формат, ожидаемый API, выполняя HTML-кодирование содержимого сообщений.
    3.  **Формирование заголовков и тела запроса**: Формируются заголовки HTTP-запроса, включая nonce, и тело запроса в формате JSON, содержащее параметры запроса и преобразованные сообщения.
    4.  **Отправка POST-запроса**: POST-запрос отправляется на endpoint `chatgptlogin.ac/wp-json/ai-chatbot/v1/chat` с сформированными заголовками и JSON-телом.
    5.  **Обработка ответа**: Полученный ответ в формате JSON извлекается и возвращается в виде текста.

    **Внутренние функции**:

    #### `get_nonce`

    ```python
    def get_nonce():
        """
        Извлекает nonce с главной страницы chatgptlogin.ac.

        Returns:
            str: Значение nonce.

        Raises:
            AttributeError: Если не удается извлечь nonce из ответа.
        """
    ```

    **Назначение**:
    Функция `get_nonce` извлекает одноразовый токен (nonce) с главной страницы веб-сайта `chatgptlogin.ac`.
    Этот токен необходим для аутентификации при отправке запросов к API чат-бота.

    **Как работает функция**:

    1.  **Отправка GET-запроса**: Функция отправляет GET-запрос к `https://chatgptlogin.ac/use-chatgpt-free/`.
    2.  **Извлечение текста ответа**: Извлекается текст ответа из HTTP-ответа.
    3.  **Поиск nonce в тексте**: Используется регулярное выражение для поиска значения nonce в тексте ответа.
        Nonce находится внутри атрибута `src` тега `<script>`.
    4.  **Декодирование Base64**: Часть `src` кодирована в Base64 и декодируется для получения JavaScript кода.
    5.  **Извлечение nonce из JavaScript**: Используется регулярное выражение для поиска значения `restNonce` в декодированном JavaScript коде.
    6.  **Возврат nonce**: Возвращается извлеченное значение nonce.

    **Примеры**:

    ```python
    nonce = get_nonce()
    print(f"Nonce: {nonce}")
    ```

    #### `transform`

    ```python
    def transform(messages: list) -> list:
        """
        Преобразует список сообщений в формат, ожидаемый API.

        Args:
            messages (list): Список сообщений для преобразования.

        Returns:
            list: Список преобразованных сообщений.
        """
    ```

    **Назначение**:
    Функция `transform` преобразует список сообщений в формат, который соответствует требованиям API веб-сайта `chatgptlogin.ac`.
    Она выполняет HTML-кодирование содержимого сообщений и добавляет дополнительную информацию, такую как уникальные идентификаторы и роли.

    **Как работает функция**:

    1.  **Перебор сообщений**: Функция перебирает каждое сообщение в списке `messages`.
    2.  **HTML-кодирование**: Для каждого сообщения вызывается функция `html_encode`, которая заменяет специальные символы HTML-сущностями.
    3.  **Создание нового словаря**: Создается новый словарь для каждого сообщения, включающий:
        *   `id`: Случайный шестнадцатеричный идентификатор.
        *   `role`: Роль сообщения (например, `user` или `assistant`).
        *   `content`: Содержимое сообщения.
        *   `who`: Префикс для отображения роли сообщения.
        *   `html`: HTML-кодированное содержимое сообщения.
    4.  **Возврат списка преобразованных сообщений**: Функция возвращает список словарей, представляющих преобразованные сообщения.

    **Внутренние функции**:

    ##### `html_encode`

    ```python
    def html_encode(string: str) -> str:
        """
        Выполняет HTML-кодирование строки.

        Args:
            string (str): Строка для кодирования.

        Returns:
            str: HTML-кодированная строка.
        """
    ```

    **Назначение**:
    Функция `html_encode` выполняет HTML-кодирование входной строки, заменяя специальные символы HTML-сущностями.
    Это необходимо для корректного отображения текста в HTML-контенте и предотвращения возможных проблем с безопасностью.

    **Как работает функция**:

    1.  **Определение таблицы замен**: Определяется словарь `table`, который содержит соответствия между символами и их HTML-сущностями.
        Например, символ `"` заменяется на `&quot;`.
    2.  **Замена символов**: Функция перебирает символы в таблице замен и заменяет их на соответствующие HTML-сущности в строке.
    3.  **Возврат кодированной строки**: Функция возвращает строку с замененными символами.

    **Примеры**:

    ```python
    encoded_string = html_encode("Hello, world!\"")
    print(f"Encoded string: {encoded_string}")  # Output: Hello, world!&quot;
    ```

    **Примеры**:

    ```python
    messages = [{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there!"}]
    transformed_messages = transform(messages)
    print(transformed_messages)
    ```

    **ASCII-схема работы `_create_completion`**:

    ```
    Начало
    ↓
    Получение nonce (get_nonce)
    ↓
    Преобразование сообщений (transform)
    ↓
    Формирование заголовков и тела запроса
    ↓
    Отправка POST-запроса на chatgptlogin.ac
    ↓
    Извлечение ответа из JSON
    ↓
    Возврат ответа
    Конец
    ```

    **Примеры**:

    ```python
    response = _create_completion(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello!"}], stream=False)
    print(response)
    ```

## Переменные

### `url`

```python
url = 'https://chatgptlogin.ac'
```

URL веб-сайта, используемого для взаимодействия с ChatGPT.

### `model`

```python
model = ['gpt-3.5-turbo']
```

Список поддерживаемых моделей. В данном случае, поддерживается только `gpt-3.5-turbo`.

### `supports_stream`

```python
supports_stream = False
```

Указывает, поддерживает ли провайдер потоковую передачу данных. В данном случае, не поддерживается.

### `needs_auth`

```python
needs_auth = False
```

Указывает, требуется ли аутентификация для использования провайдера. В данном случае, аутентификация не требуется.

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

Строка, содержащая информацию о поддерживаемых параметрах функции `_create_completion`.