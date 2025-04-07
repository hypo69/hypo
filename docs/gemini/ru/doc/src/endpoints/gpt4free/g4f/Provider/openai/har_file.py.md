# Модуль для работы с HAR-файлами OpenAI
==============================================

Модуль предназначен для обработки HAR-файлов, содержащих информацию о запросах и ответах, связанных с сервисами OpenAI.
Он включает в себя функции для чтения, парсинга и генерации запросов Arkose Labs, которые используются для обхода защиты от ботов.

## Обзор

Этот модуль предназначен для извлечения и обработки данных из HAR-файлов, которые обычно содержат HTTP-запросы и ответы. В контексте взаимодействия с OpenAI, HAR-файлы могут содержать важную информацию, такую как токены доступа, proof-токены и данные, необходимые для генерации запросов Arkose Labs. Модуль предоставляет инструменты для парсинга этих файлов, извлечения нужной информации и создания новых запросов Arkose Labs на основе извлеченных данных.

## Подробнее

Модуль содержит классы и функции, необходимые для работы с HAR-файлами. Основные этапы работы модуля включают:

1.  Поиск HAR-файлов в указанной директории.
2.  Чтение и парсинг HAR-файлов.
3.  Извлечение токенов доступа, proof-токенов и других необходимых данных.
4.  Создание и отправка запросов Arkose Labs для получения токенов, необходимых для обхода защиты от ботов.

## Классы

### `RequestConfig`

**Описание**: Класс, содержащий конфигурацию запроса, включая cookies, заголовки, токены доступа и информацию для запросов Arkose Labs.

**Атрибуты**:

*   `cookies` (dict): Словарь с cookies.
*   `headers` (dict): Словарь с заголовками запроса.
*   `access_token` (str): Токен доступа.
*   `proof_token` (list): Proof-токен.
*   `turnstile_token` (str): Turnstile-токен.
*   `arkose_request` (arkReq): Объект `arkReq`, содержащий информацию для запроса Arkose Labs.
*   `arkose_token` (str): Токен Arkose Labs.
*   `data_build` (str): Строка, представляющая версию сборки данных.

### `arkReq`

**Описание**: Класс, представляющий запрос Arkose Labs.

**Атрибуты**:

*   `arkURL` (str): URL для запроса Arkose Labs.
*   `arkBx` (str): Зашифрованное значение для запроса Arkose Labs.
*   `arkHeader` (dict): Заголовки запроса Arkose Labs.
*   `arkBody` (dict): Тело запроса Arkose Labs.
*   `arkCookies` (dict): Cookies для запроса Arkose Labs.
*   `userAgent` (str): User-Agent для запроса Arkose Labs.

## Функции

### `get_har_files`

```python
def get_har_files() -> list[str]:
    """
    Поиск HAR-файлов в директории с cookies.

    Returns:
        list[str]: Список путей к найденным HAR-файлам.

    Raises:
        NoValidHarFileError: Если директория с cookies не читаема или в ней не найдены HAR-файлы.
    """
```

**Назначение**: Функция ищет HAR-файлы в указанной директории и возвращает список путей к найденным файлам.

**Как работает функция**:

1.  Проверяет, доступна ли директория с cookies для чтения. Если нет, вызывает исключение `NoValidHarFileError`.
2.  Проходит по всем файлам в директории и ее поддиректориях.
3.  Если файл имеет расширение ".har", добавляет его путь в список.
4.  Если список пуст, вызывает исключение `NoValidHarFileError`.
5.  Сортирует список HAR-файлов по времени последнего изменения и возвращает его.

```
    Проверка доступности директории cookies
    │
    └── Поиск HAR-файлов в директории cookies
        │
        └── Добавление пути к HAR-файлу в список
            │
            └── Проверка, найдены ли HAR-файлы
                │
                └── Сортировка HAR-файлов по времени изменения
                    │
                    └── Возврат списка HAR-файлов
```

**Примеры**:

```python
try:
    har_files = get_har_files()
    print(f"Найденные HAR-файлы: {har_files}")
except NoValidHarFileError as ex:
    print(f"Ошибка: {ex}")
```

### `readHAR`

```python
def readHAR(request_config: RequestConfig) -> None:
    """
    Чтение и парсинг HAR-файлов для извлечения конфигурации запроса.

    Args:
        request_config (RequestConfig): Объект `RequestConfig` для хранения извлеченной конфигурации.

    Raises:
        NoValidHarFileError: Если не найден proof_token в .har файлах.
    """
```

**Назначение**: Функция читает HAR-файлы и извлекает из них конфигурацию запроса, такую как токены доступа, proof-токены и данные для запросов Arkose Labs.

**Параметры**:

*   `request_config` (RequestConfig): Объект `RequestConfig`, в который будут записаны извлеченные данные.

**Как работает функция**:

1.  Получает список HAR-файлов с помощью функции `get_har_files`.
2.  Перебирает HAR-файлы в списке.
3.  Читает содержимое каждого HAR-файла и пытается распарсить его как JSON. Если файл не является корректным JSON, переходит к следующему файлу.
4.  Перебирает записи в HAR-файле.
5.  Если URL записи соответствует URL для запроса Arkose Labs, парсит запись с помощью функции `parseHAREntry` и сохраняет результат в `request_config.arkose_request`.
6.  Если URL записи начинается с URL сервиса OpenAI, пытается извлечь токен доступа, proof-токен и turnstile-токен из заголовков и содержимого записи.
7.  Сохраняет извлеченные данные в объект `request_config`.
8.  Если после обработки всех HAR-файлов не найден proof-токен, вызывает исключение `NoValidHarFileError`.

```
    Получение списка HAR-файлов
    │
    └── Перебор HAR-файлов
        │
        └── Чтение и парсинг HAR-файла
            │
            └── Перебор записей в HAR-файле
                │
                ├── URL соответствует запросу Arkose Labs?
                │   └── Парсинг записи Arkose Labs
                │
                ├── URL начинается с URL сервиса OpenAI?
                │   └── Извлечение токена доступа, proof-токена и turnstile-токена
                │
                └── Сохранение извлеченных данных в request_config
                    │
                    └── Проверка, найден ли proof-токен
                        │
                        └── Вызов исключения, если proof-токен не найден
```

**Примеры**:

```python
request_config = RequestConfig()
try:
    readHAR(request_config)
    print(f"Токен доступа: {request_config.access_token}")
    print(f"Proof-токен: {request_config.proof_token}")
except NoValidHarFileError as ex:
    print(f"Ошибка: {ex}")
```

### `get_headers`

```python
def get_headers(entry: dict) -> dict:
    """
    Извлечение заголовков из записи HAR-файла.

    Args:
        entry (dict): Запись HAR-файла.

    Returns:
        dict: Словарь с заголовками, приведенными к нижнему регистру.
    """
```

**Назначение**: Функция извлекает заголовки из записи HAR-файла и возвращает их в виде словаря, приводя имена заголовков к нижнему регистру.

**Параметры**:

*   `entry` (dict): Запись HAR-файла.

**Возвращает**:

*   `dict`: Словарь с заголовками, где ключи - имена заголовков в нижнем регистре, а значения - значения заголовков.

**Как работает функция**:

1.  Перебирает заголовки в записи HAR-файла.
2.  Приводит имя каждого заголовка к нижнему регистру.
3.  Исключает заголовки "content-length" и "cookie", а также заголовки, начинающиеся с ":".
4.  Сохраняет заголовок и его значение в словаре.
5.  Возвращает словарь с заголовками.

```
    Перебор заголовков в записи HAR-файла
    │
    └── Приведение имени заголовка к нижнему регистру
        │
        └── Исключение нежелательных заголовков
            │
            └── Сохранение заголовка и его значения в словаре
                │
                └── Возврат словаря с заголовками
```

**Примеры**:

```python
entry = {
    'request': {
        'headers': [
            {'name': 'Content-Type', 'value': 'application/json'},
            {'name': 'Cookie', 'value': 'test=123'}
        ]
    }
}
headers = get_headers(entry)
print(headers)  # Вывод: {'content-type': 'application/json'}
```

### `parseHAREntry`

```python
def parseHAREntry(entry: dict) -> arkReq:
    """
    Парсинг записи HAR-файла для извлечения данных запроса Arkose Labs.

    Args:
        entry (dict): Запись HAR-файла.

    Returns:
        arkReq: Объект `arkReq`, содержащий данные запроса Arkose Labs.
    """
```

**Назначение**: Функция парсит запись HAR-файла и извлекает из нее данные, необходимые для создания запроса Arkose Labs.

**Параметры**:

*   `entry` (dict): Запись HAR-файла.

**Возвращает**:

*   `arkReq`: Объект `arkReq`, содержащий URL, заголовки, тело и cookies запроса Arkose Labs.

**Как работает функция**:

1.  Извлекает URL, заголовки, тело и cookies из записи HAR-файла.
2.  Создает объект `arkReq` с извлеченными данными.
3.  Извлекает значение "bda" из тела запроса и "x-ark-esync-value" из заголовков.
4.  Расшифровывает значение "bda" с помощью функции `decrypt` и сохраняет результат в `tmpArk.arkBx`.
5.  Возвращает объект `arkReq`.

```
    Извлечение URL, заголовков, тела и cookies из записи HAR-файла
    │
    └── Создание объекта arkReq
        │
        └── Извлечение значений "bda" и "x-ark-esync-value"
            │
            └── Расшифровка значения "bda"
                │
                └── Возврат объекта arkReq
```

**Примеры**:

```python
entry = {
    'request': {
        'url': 'https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147',
        'headers': [
            {'name': 'X-Ark-Esync-Value', 'value': 'test_bw'},
            {'name': 'User-Agent', 'value': 'test_user_agent'}
        ],
        'postData': {
            'params': [
                {'name': 'bda', 'value': 'test_bda'},
                {'name': 'rnd', 'value': '123'}
            ]
        },
        'cookies': [
            {'name': 'test_cookie', 'value': 'test_value'}
        ]
    }
}
ark_req = parseHAREntry(entry)
print(f"URL: {ark_req.arkURL}")
print(f"Cookies: {ark_req.arkCookies}")
```

### `genArkReq`

```python
def genArkReq(chatArk: arkReq) -> arkReq:
    """
    Генерация запроса Arkose Labs на основе существующего запроса.

    Args:
        chatArk (arkReq): Объект `arkReq`, представляющий существующий запрос Arkose Labs.

    Returns:
        arkReq: Объект `arkReq`, представляющий сгенерированный запрос Arkose Labs.

    Raises:
        RuntimeError: Если .har файл не валидный.
    """
```

**Назначение**: Функция генерирует новый запрос Arkose Labs на основе существующего запроса, заменяя некоторые параметры и перешифровывая данные.

**Параметры**:

*   `chatArk` (arkReq): Объект `arkReq`, представляющий существующий запрос Arkose Labs.

**Возвращает**:

*   `arkReq`: Объект `arkReq`, представляющий сгенерированный запрос Arkose Labs.

**Как работает функция**:

1.  Создает глубокую копию объекта `chatArk`.
2.  Проверяет, что объект `tmpArk` и его поля `arkBody` и `arkHeader` не равны `None`. Если какое-либо из этих условий не выполняется, вызывает исключение `RuntimeError`.
3.  Генерирует новые значения для параметров "bda" и "x-ark-esync-value" с помощью функции `getBDA`.
4.  Заменяет старые значения параметров "bda" и "x-ark-esync-value" в объекте `tmpArk` новыми значениями.
5.  Добавляет параметр "rnd" в тело запроса со случайным значением.
6.  Возвращает объект `tmpArk`.

```
    Создание глубокой копии объекта chatArk
    │
    └── Проверка валидности объекта tmpArk
        │
        └── Генерация новых значений для параметров "bda" и "x-ark-esync-value"
            │
            └── Замена старых значений параметров новыми значениями
                │
                └── Добавление параметра "rnd"
                    │
                    └── Возврат объекта tmpArk
```

**Примеры**:

```python
# Пример использования genArkReq
chat_ark = arkReq(
    arkURL="https://example.com/arkose",
    arkBx="encrypted_data",
    arkHeader={"header1": "value1"},
    arkBody={"param1": "value1"},
    arkCookies={"cookie1": "value1"},
    userAgent="test_agent"
)

try:
    new_ark = genArkReq(chat_ark)
    print(f"New arkose body: {new_ark.arkBody}")
    print(f"New arkose header: {new_ark.arkHeader}")
except RuntimeError as ex:
    print(f"Error: {ex}")
```

### `sendRequest`

```python
async def sendRequest(tmpArk: arkReq, proxy: str = None) -> str:
    """
    Отправка запроса Arkose Labs и получение токена.

    Args:
        tmpArk (arkReq): Объект `arkReq`, представляющий запрос Arkose Labs.
        proxy (str, optional): Прокси-сервер для отправки запроса. По умолчанию `None`.

    Returns:
        str: Токен Arkose Labs.

    Raises:
        RuntimeError: Если не удалось сгенерировать валидный токен Arkose Labs.
    """
```

**Назначение**: Функция отправляет запрос Arkose Labs и получает токен, необходимый для обхода защиты от ботов.

**Параметры**:

*   `tmpArk` (arkReq): Объект `arkReq`, представляющий запрос Arkose Labs.
*   `proxy` (str, optional): Прокси-сервер для отправки запроса. По умолчанию `None`.

**Возвращает**:

*   `str`: Токен Arkose Labs.

**Как работает функция**:

1.  Создает асинхронную сессию с использованием библиотеки `StreamSession`.
2.  Отправляет POST-запрос на URL, указанный в `tmpArk.arkURL`, с использованием заголовков, cookies и тела запроса, указанных в `tmpArk`.
3.  Получает JSON-ответ от сервера.
4.  Извлекает значение поля "token" из JSON-ответа.
5.  Проверяет, содержит ли токен подстроку "sup=1|rid=". Если нет, вызывает исключение `RuntimeError`.
6.  Возвращает токен.

```
    Создание асинхронной сессии
    │
    └── Отправка POST-запроса
        │
        └── Получение JSON-ответа
            │
            └── Извлечение токена
                │
                └── Проверка валидности токена
                    │
                    └── Возврат токена
```

**Примеры**:

```python
# Пример использования sendRequest
tmp_ark = arkReq(
    arkURL="https://example.com/arkose",
    arkBx="encrypted_data",
    arkHeader={"header1": "value1"},
    arkBody={"param1": "value1"},
    arkCookies={"cookie1": "value1"},
    userAgent="test_agent"
)

async def main():
    try:
        arkose_token = await sendRequest(tmp_ark, proxy="http://proxy.example.com")
        print(f"Arkose token: {arkose_token}")
    except RuntimeError as ex:
        print(f"Error: {ex}")

# Запуск асинхронной функции
import asyncio
asyncio.run(main())
```

### `getBDA`

```python
def getBDA(arkReq: arkReq) -> tuple[str, str]:
    """
    Генерация значений BDA и BW для запроса Arkose Labs.

    Args:
        arkReq (arkReq): Объект `arkReq`, представляющий запрос Arkose Labs.

    Returns:
        tuple[str, str]: Кортеж, содержащий зашифрованное значение BX и значение BW.
    """
```

**Назначение**: Функция генерирует значения BDA (Body Data) и BW (Body Watermark) для запроса Arkose Labs.

**Параметры**:

*   `arkReq` (arkReq): Объект `arkReq`, содержащий данные запроса Arkose Labs.

**Возвращает**:

*   `tuple[str, str]`: Кортеж, содержащий зашифрованное значение BX и значение BW.

**Как работает функция**:

1.  Извлекает значение BX из объекта `arkReq`.
2.  Заменяет в BX значение ключа "n" на новое значение, полученное с помощью функции `getN`.
3.  Ищет в BX старый UUID и заменяет его новым UUID.
4.  Генерирует значение BW с помощью функций `getBt` и `getBw`.
5.  Шифрует BX с использованием User-Agent и BW с помощью функции `encrypt`.
6.  Возвращает зашифрованное значение BX и значение BW.

```
    Извлечение значения BX
    │
    └── Замена значения ключа "n"
        │
        └── Замена старого UUID новым UUID
            │
            └── Генерация значения BW
                │
                └── Шифрование значения BX
                    │
                    └── Возврат зашифрованного значения BX и значения BW
```

**Примеры**:

```python
# Пример использования getBDA
ark_req = arkReq(
    arkURL="https://example.com/arkose",
    arkBx='"key":"n","value":"old_value"',
    arkHeader={"x-ark-esync-value": "old_bw"},
    arkBody={"param1": "value1"},
    arkCookies={"cookie1": "value1"},
    userAgent="test_agent"
)

encrypted_bx, bw = getBDA(ark_req)
print(f"Encrypted BX: {encrypted_bx}")
print(f"BW: {bw}")
```

### `getBt`

```python
def getBt() -> int:
    """
    Получение текущего времени в формате Unix timestamp.

    Returns:
        int: Текущее время в формате Unix timestamp.
    """
```

**Назначение**: Функция возвращает текущее время в формате Unix timestamp.

**Возвращает**:

*   `int`: Текущее время в формате Unix timestamp.

**Как работает функция**:

1.  Получает текущее время с помощью функции `time.time()`.
2.  Преобразует текущее время в целое число.
3.  Возвращает текущее время в формате Unix timestamp.

```
    Получение текущего времени
    │
    └── Преобразование времени в целое число
        │
        └── Возврат времени в формате Unix timestamp
```

**Примеры**:

```python
# Пример использования getBt
bt = getBt()
print(f"Current time: {bt}")
```

### `getBw`

```python
def getBw(bt: int) -> str:
    """
    Генерация значения BW на основе времени.

    Args:
        bt (int): Время в формате Unix timestamp.

    Returns:
        str: Значение BW.
    """
```

**Назначение**: Функция генерирует значение BW (Body Watermark) на основе времени в формате Unix timestamp.

**Параметры**:

*   `bt` (int): Время в формате Unix timestamp.

**Возвращает**:

*   `str`: Значение BW.

**Как работает функция**:

1.  Вычисляет остаток от деления времени на 21600.
2.  Вычитает остаток из времени.
3.  Преобразует результат в строку.
4.  Возвращает строку.

```
    Вычисление остатка от деления времени на 21600
    │
    └── Вычитание остатка из времени
        │
        └── Преобразование результата в строку
            │
            └── Возврат строки
```

**Примеры**:

```python
# Пример использования getBw
bt = 1678886400
bw = getBw(bt)
print(f"BW: {bw}")
```

### `getN`

```python
def getN() -> str:
    """
    Генерация значения N на основе текущего времени.

    Returns:
        str: Значение N, закодированное в Base64.
    """
```

**Назначение**: Функция генерирует значение N на основе текущего времени и кодирует его в Base64.

**Возвращает**:

*   `str`: Значение N, закодированное в Base64.

**Как работает функция**:

1.  Получает текущее время в формате Unix timestamp.
2.  Преобразует время в строку.
3.  Кодирует строку в Base64.
4.  Декодирует Base64 в строку UTF-8.
5.  Возвращает строку.

```
    Получение текущего времени
    │
    └── Преобразование времени в строку
        │
        └── Кодирование строки в Base64
            │
            └── Декодирование Base64 в строку UTF-8
                │
                └── Возврат строки
```

**Примеры**:

```python
# Пример использования getN
n = getN()
print(f"N: {n}")
```

### `get_request_config`

```python
async def get_request_config(request_config: RequestConfig, proxy: str) -> RequestConfig:
    """
    Получение конфигурации запроса, включая токен Arkose Labs.

    Args:
        request_config (RequestConfig): Объект `RequestConfig` для хранения конфигурации.
        proxy (str): Прокси-сервер для отправки запроса.

    Returns:
        RequestConfig: Объект `RequestConfig` с заполненной конфигурацией.
    """
```

**Назначение**: Функция получает конфигурацию запроса, включая токен Arkose Labs, и сохраняет ее в объекте `RequestConfig`.

**Параметры**:

*   `request_config` (RequestConfig): Объект `RequestConfig`, в который будет записана конфигурация.
*   `proxy` (str): Прокси-сервер для отправки запроса.

**Возвращает**:

*   `RequestConfig`: Объект `RequestConfig` с заполненной конфигурацией.

**Как работает функция**:

1.  Проверяет, установлен ли proof-токен в объекте `request_config`. Если нет, читает HAR-файлы с помощью функции `readHAR`.
2.  Проверяет, установлен ли запрос Arkose Labs в объекте `request_config`. Если да, генерирует и отправляет запрос Arkose Labs с помощью функций `genArkReq` и `sendRequest` и сохраняет полученный токен в `request_config.arkose_token`.
3.  Возвращает объект `request_config`.

```
    Проверка, установлен ли proof-токен
    │
    └── Чтение HAR-файлов, если proof-токен не установлен
        │
        └── Проверка, установлен ли запрос Arkose Labs
            │
            └── Генерация и отправка запроса Arkose Labs, если запрос установлен
                │
                └── Сохранение токена Arkose Labs
                    │
                    └── Возврат объекта request_config
```

**Примеры**:

```python
# Пример использования get_request_config
request_config = RequestConfig()

async def main():
    updated_config = await get_request_config(request_config, proxy="http://proxy.example.com")
    print(f"Access Token: {updated_config.access_token}")
    print(f"Arkose Token: {updated_config.arkose_token}")

# Запуск асинхронной функции
import asyncio
asyncio.run(main())