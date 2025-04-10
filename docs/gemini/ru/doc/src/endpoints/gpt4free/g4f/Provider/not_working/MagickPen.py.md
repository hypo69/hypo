# Модуль `MagickPen`

## Обзор

Модуль `MagickPen` предоставляет асинхронный генератор для взаимодействия с API `MagickPen`. Он позволяет отправлять запросы к API и получать ответы в виде потока данных. Модуль поддерживает стриминг, системные сообщения и историю сообщений.

## Подробнее

Модуль использует библиотеку `aiohttp` для асинхронных HTTP-запросов. Он извлекает необходимые учетные данные API из JavaScript файла на веб-сайте `MagickPen`. Полученные данные используются для формирования заголовков запроса.
В модуле реализована поддержка асинхронной генерации ответов от API, что позволяет обрабатывать большие объемы данных небольшими порциями.

## Классы

### `MagickPen`

**Описание**: Класс `MagickPen` является поставщиком асинхронного генератора и предоставляет методы для взаимодействия с API `MagickPen`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL веб-сайта `MagickPen`.
- `api_endpoint` (str): URL API `MagickPen`.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию.
- `models` (List[str]): Список поддерживаемых моделей.

**Методы**:
- `fetch_api_credentials()`: Извлекает учетные данные API из JavaScript файла.
- `create_async_generator()`: Создает асинхронный генератор для отправки запросов к API.

## Функции

### `fetch_api_credentials`

**Назначение**: Извлекает учетные данные API (`X_API_SECRET`, `signature`, `timestamp`, `nonce`, `secret`) из JavaScript файла на веб-сайте `MagickPen`.

**Как работает функция**:

1. **Определение URL JavaScript файла**: Определяется URL JavaScript файла, содержащего необходимые учетные данные.
2. **Выполнение HTTP-запроса**: Выполняется GET-запрос к JavaScript файлу с использованием `aiohttp`.
3. **Извлечение текста ответа**: Полученный ответ преобразуется в текст.
4. **Поиск учетных данных с использованием регулярных выражений**:
   - Извлекается значение `X-API-Secret` с использованием регулярного выражения.
   - Генерируются значения `timestamp` и `nonce`.
   - Формируется строка `signature_string` и вычисляется ее MD5-хеш.
   - Извлекается значение `secret` с использованием регулярного выражения.
5. **Проверка наличия всех необходимых данных**: Проверяется, что все необходимые учетные данные были успешно извлечены.
6. **Возврат учетных данных**: Если все данные присутствуют, они возвращаются в виде кортежа.
7. **Выброс исключения**: Если какие-либо данные отсутствуют, выбрасывается исключение `Exception` с сообщением об ошибке.

```ascii
    A: Получение URL JavaScript файла
    |
    B: Выполнение GET-запроса к JavaScript файлу
    |
    C: Извлечение текста ответа
    |
    D: Поиск и извлечение X_API_SECRET
    |
    E: Генерация timestamp и nonce
    |
    F: Формирование signature_string и вычисление MD5-хеша
    |
    G: Поиск и извлечение secret
    |
    H: Проверка наличия всех необходимых данных
    |
    I: Возврат учетных данных или выброс исключения
```

**Параметры**:
- Нет параметров.

**Возвращает**:
- `tuple`: Кортеж, содержащий `X_API_SECRET` (str), `signature` (str), `timestamp` (str), `nonce` (str) и `secret` (str).

**Вызывает исключения**:
- `Exception`: Если не удается извлечь все необходимые данные из JavaScript файла.

**Примеры**:

```python
# Пример вызова функции (необходимо запустить в асинхронном контексте)
# X_API_SECRET, signature, timestamp, nonce, secret = await MagickPen.fetch_api_credentials()
# print(f"X_API_SECRET: {X_API_SECRET}, signature: {signature}, timestamp: {timestamp}, nonce: {nonce}, secret: {secret}")
```

### `create_async_generator`

**Назначение**: Создает асинхронный генератор для отправки запросов к API `MagickPen` и получения потоковых ответов.

**Как работает функция**:

1. **Получение модели**: Получает модель из аргументов или использует модель по умолчанию.
2. **Получение учетных данных API**: Вызывает метод `fetch_api_credentials` для получения необходимых учетных данных.
3. **Формирование заголовков запроса**: Формирует заголовки запроса, включая полученные учетные данные.
4. **Формирование тела запроса**: Формирует тело запроса, содержащее промпт, полученный из сообщений.
5. **Выполнение POST-запроса**: Выполняется POST-запрос к API с использованием `aiohttp`.
6. **Обработка потоковых ответов**: Полученные чанки данных декодируются и передаются через генератор.
7. **Обработка ошибок**: В случае ошибки при выполнении запроса, выбрасывается исключение `HTTPError`.

```ascii
    A: Получение модели
    |
    B: Получение учетных данных API
    |
    C: Формирование заголовков запроса
    |
    D: Формирование тела запроса
    |
    E: Выполнение POST-запроса к API
    |
    F: Обработка потоковых ответов
```

**Параметры**:
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки в запросе.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий декодированные чанки данных.

**Вызывает исключения**:
- `HTTPError`: Если при выполнении запроса произошла ошибка.

**Примеры**:

```python
# Пример вызова функции (необходимо запустить в асинхронном контексте)
# messages = [{"role": "user", "content": "Hello, how are you?"}]
# async for chunk in MagickPen.create_async_generator(model="gpt-4o-mini", messages=messages):
#     print(chunk, end="")