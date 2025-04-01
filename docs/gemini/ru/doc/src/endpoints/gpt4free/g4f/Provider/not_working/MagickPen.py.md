# Модуль MagickPen

## Обзор

Модуль `MagickPen` предоставляет асинхронный интерфейс для взаимодействия с API MagickPen. Он позволяет генерировать текст на основе предоставленных сообщений, используя асинхронные генераторы для потоковой передачи результатов.

## Подробней

Модуль предназначен для интеграции с сервисом MagickPen, предоставляющим API для генерации текста. Он включает в себя функциональность для получения необходимых API-ключей и подписей, а также для отправки запросов к API и получения результатов в режиме реального времени. Этот модуль использует асинхронные запросы для обеспечения неблокирующей работы.

## Классы

### `MagickPen`

**Описание**: Класс `MagickPen` является асинхронным провайдером и расширяет возможности `AsyncGeneratorProvider` и `ProviderModelMixin`. Он предназначен для взаимодействия с API MagickPen.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных провайдеров, генерирующих данные.
- `ProviderModelMixin`: Обеспечивает поддержку выбора и управления моделями, используемыми провайдером.

**Атрибуты**:
- `url` (str): URL веб-сайта MagickPen (`"https://magickpen.com"`).
- `api_endpoint` (str): URL API-endpoint MagickPen (`"https://api.magickpen.com/ask"`).
- `working` (bool): Указывает, работает ли провайдер (`False`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (`True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (`True`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`True`).
- `default_model` (str): Модель, используемая по умолчанию (`'gpt-4o-mini'`).
- `models` (list): Список поддерживаемых моделей (`['gpt-4o-mini']`).

**Методы**:
- `fetch_api_credentials()`: Асинхронный метод для получения учетных данных API.
- `create_async_generator()`: Асинхронный метод для создания асинхронного генератора для запросов к API.

## Функции

### `fetch_api_credentials`

```python
    @classmethod
    async def fetch_api_credentials(cls) -> tuple:
        """
        Получает необходимые учетные данные API для взаимодействия с MagickPen.

        Args:
            cls (MagickPen): Ссылка на класс `MagickPen`.

        Returns:
            tuple: Кортеж, содержащий X_API_SECRET, signature, timestamp, nonce и secret.

        Raises:
            Exception: Если не удается извлечь все необходимые данные из JavaScript-файла.
        """
        ...
```

**Назначение**:
Извлекает учетные данные API, необходимые для аутентификации и авторизации запросов к API MagickPen.

**Как работает функция**:

1. **Определение URL JavaScript-файла**:
   - URL JavaScript-файла, содержащего необходимые ключи, определяется как `url = "https://magickpen.com/_nuxt/bf709a9ce19f14e18116.js"`.

2. **Загрузка содержимого JavaScript-файла**:
   - Функция выполняет GET-запрос к указанному URL, используя `aiohttp.ClientSession`.
   - Содержимое ответа извлекается в виде текста: `text = await response.text()`.

3. **Извлечение `X_API_SECRET`**:
   - Используется регулярное выражение `r'"X-API-Secret":"(\\w+)"'` для поиска значения `X-API-Secret` в тексте.
   - Если значение найдено, оно присваивается переменной `X_API_SECRET`.

4. **Создание `timestamp` и `nonce`**:
   - Текущее время в миллисекундах используется для создания `timestamp`: `timestamp = str(int(time.time() * 1000))`.
   - Случайное число используется для создания `nonce`: `nonce = str(random.random())`.

5. **Создание `signature`**:
   - Формируется список `s` из фиксированной строки `"TGDBU9zCgM"`, `timestamp` и `nonce`.
   - Список сортируется, элементы объединяются в строку `signature_string`.
   - Вычисляется MD5-хеш строки `signature_string`, который присваивается переменной `signature`.

6. **Извлечение `secret`**:
   - Используется регулярное выражение `r'secret:"(\\w+)"'` для поиска значения `secret` в тексте.
   - Если значение найдено, оно присваивается переменной `secret`.

7. **Проверка наличия всех необходимых данных**:
   - Проверяется, что все переменные (`X_API_SECRET`, `timestamp`, `nonce`, `secret`) содержат значения.
   - Если все данные присутствуют, функция возвращает их в виде кортежа.

8. **Выброс исключения в случае отсутствия данных**:
   - Если хотя бы одна из переменных не содержит значения, функция выбрасывает исключение `Exception` с сообщением об ошибке.

**ASCII flowchart**:

```
A: Загрузка содержимого JavaScript-файла
|
B: Извлечение X_API_SECRET
|
C: Создание timestamp и nonce
|
D: Создание signature
|
E: Извлечение secret
|
F: Проверка наличия всех данных
|
G: Возврат данных
```

**Примеры**:

```python
# Пример вызова функции (предположительно внутри класса MagickPen)
try:
    X_API_SECRET, signature, timestamp, nonce, secret = await MagickPen.fetch_api_credentials()
    print(f"X_API_SECRET: {X_API_SECRET}")
    print(f"Signature: {signature}")
    print(f"Timestamp: {timestamp}")
    print(f"Nonce: {nonce}")
    print(f"Secret: {secret}")
except Exception as ex:
    print(f"Ошибка: {ex}")
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для запросов к API MagickPen.

        Args:
            cls (MagickPen): Ссылка на класс `MagickPen`.
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий результаты от API.
        """
        ...
```

**Назначение**:
Создает асинхронный генератор для отправки запросов к API MagickPen и получения результатов в реальном времени.

**Параметры**:
- `cls` (MagickPen): Ссылка на класс `MagickPen`.
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий результаты от API.

**Как работает функция**:

1. **Получение модели**:
   - Вызывает метод `cls.get_model(model)` для получения информации о модели.

2. **Получение учетных данных API**:
   - Вызывает асинхронный метод `cls.fetch_api_credentials()` для получения необходимых учетных данных API (X_API_SECRET, signature, timestamp, nonce, secret).

3. **Формирование заголовков запроса**:
   - Создает словарь `headers` с необходимыми HTTP-заголовками, включая полученные учетные данные.

4. **Создание асинхронной сессии**:
   - Использует `aiohttp.ClientSession` для создания асинхронной сессии с заданными заголовками.

5. **Формирование запроса**:
   - Форматирует список сообщений `messages` в строку `prompt` с использованием функции `format_prompt(messages)`.
   - Создает словарь `payload` с данными запроса, включая `query` (сформированный prompt) и `turnstileResponse`.

6. **Отправка POST-запроса к API**:
   - Отправляет асинхронный POST-запрос к `cls.api_endpoint` с использованием `session.post()`.
   - Включает `payload` в формате JSON и использует прокси-сервер, если он указан.

7. **Обработка ответа**:
   - Проверяет статус ответа с помощью `response.raise_for_status()`, чтобы убедиться, что запрос выполнен успешно.

8. **Генерация данных из ответа**:
   - Асинхронно итерирует по частям (chunks) содержимого ответа (`response.content`).
   - Декодирует каждую часть в строку (`chunk.decode()`) и передает её в генератор с помощью `yield`.

**ASCII flowchart**:

```
A: Получение модели
|
B: Получение учетных данных API
|
C: Формирование заголовков запроса
|
D: Создание асинхронной сессии
|
E: Формирование запроса
|
F: Отправка POST-запроса к API
|
G: Обработка ответа
|
H: Генерация данных из ответа
```

**Примеры**:

```python
# Пример вызова функции (предположительно внутри класса MagickPen)
messages = [{"role": "user", "content": "Hello, how are you?"}]
try:
    async for chunk in MagickPen.create_async_generator(model='gpt-4o-mini', messages=messages):
        print(chunk, end="")
except Exception as ex:
    print(f"Ошибка: {ex}")