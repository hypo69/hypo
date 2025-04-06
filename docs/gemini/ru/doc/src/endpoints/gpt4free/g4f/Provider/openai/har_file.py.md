# Модуль для работы с HAR файлами для g4f
=================================================

Модуль содержит функции для чтения, парсинга и обработки HAR (HTTP Archive) файлов, используемых для извлечения необходимой информации для работы с API.
Модуль предназначен для получения конфигурационных данных из HAR файлов, необходимых для аутентификации и авторизации в различных сервисах, таких как OpenAI.

## Обзор

Модуль `har_file.py` предоставляет функциональность для работы с HAR файлами, которые содержат записи HTTP-транзакций. Он используется для извлечения данных аутентификации и конфигурации, таких как токены доступа, proof-токены, turnstile-токены и куки, необходимые для взаимодействия с API OpenAI и другими сервисами. Модуль включает функции для чтения HAR файлов, парсинга записей HAR, дешифрования данных Arkose Labs и генерации новых запросов Arkose Labs.

## Подробней

Этот модуль играет важную роль в процессе автоматизации получения доступа к API, требующим сложных процедур аутентификации и авторизации. Он позволяет извлекать необходимые данные из HAR файлов, которые могут быть получены путем записи HTTP-трафика в браузере.

## Классы

### `RequestConfig`

**Описание**: Класс для хранения конфигурационных данных запроса.

**Атрибуты**:
- `cookies` (dict): Куки для запроса.
- `headers` (dict): Заголовки для запроса.
- `access_token` (str): Токен доступа.
- `proof_token` (list): Proof-токен.
- `turnstile_token` (str): Turnstile-токен.
- `arkose_request` (arkReq): Объект запроса Arkose Labs.
- `arkose_token` (str): Токен Arkose Labs.
- `data_build` (str): Версия сборки данных.

### `arkReq`

**Описание**: Класс для хранения данных, необходимых для запроса Arkose Labs.

**Атрибуты**:
- `arkURL` (str): URL запроса Arkose Labs.
- `arkBx` (str): Зашифрованные данные Arkose Labs.
- `arkHeader` (dict): Заголовки запроса Arkose Labs.
- `arkBody` (dict): Тело запроса Arkose Labs.
- `arkCookies` (dict): Куки для запроса Arkose Labs.
- `userAgent` (str): User-Agent.

## Функции

### `get_har_files`

```python
def get_har_files() -> list[str]:
    """Получает список путей к HAR файлам в директории с куками.

    Returns:
        list[str]: Список путей к HAR файлам.

    Raises:
        NoValidHarFileError: Если директория с куками не читаема или не найдено ни одного HAR файла.
    """
```

**Назначение**: Функция ищет HAR файлы в указанной директории и возвращает список путей к ним.

**Как работает функция**:

1.  **Проверяет доступность директории**:
    *   Проверяет, доступна ли директория с куками для чтения. Если нет, вызывает исключение `NoValidHarFileError`.
2.  **Ищет HAR файлы**:
    *   Проходит по всем файлам в директории с куками и добавляет пути к HAR файлам в список `harPath`.
3.  **Проверяет наличие HAR файлов**:
    *   Если список `harPath` пуст, вызывает исключение `NoValidHarFileError`.
4.  **Сортирует HAR файлы**:
    *   Сортирует список `harPath` по времени модификации файла (от старых к новым).
5.  **Возвращает список HAR файлов**:
    *   Возвращает отсортированный список путей к HAR файлам.

**Примеры**:

```python
try:
    har_files = get_har_files()
    print(f"Найдены HAR файлы: {har_files}")
except NoValidHarFileError as ex:
    print(f"Ошибка: {ex}")
```

### `readHAR`

```python
def readHAR(request_config: RequestConfig) -> None:
    """Читает HAR файлы и извлекает данные конфигурации запроса.

    Args:
        request_config (RequestConfig): Объект конфигурации запроса для заполнения.

    Raises:
        NoValidHarFileError: Если не найден proof_token в HAR файлах.
    """
```

**Назначение**: Функция читает HAR файлы и извлекает из них данные конфигурации запроса, такие как access_token, proof_token, turnstile_token, cookies и headers.

**Как работает функция**:

1.  **Получает список HAR файлов**:
    *   Вызывает функцию `get_har_files()` для получения списка путей к HAR файлам.
2.  **Итерируется по HAR файлам**:
    *   Проходит по каждому пути в списке HAR файлов.
3.  **Читает и парсит HAR файл**:
    *   Открывает HAR файл и пытается распарсить его содержимое как JSON. Если возникает ошибка `json.JSONDecodeError`, переходит к следующему файлу.
4.  **Итерируется по записям HAR**:
    *   Проходит по каждой записи (entry) в HAR файле.
5.  **Извлекает данные из записей**:
    *   Если URL записи соответствует `arkose_url`, вызывает функцию `parseHAREntry()` для парсинга записи Arkose Labs и сохраняет результат в `request_config.arkose_request`.
    *   Если URL записи начинается с `start_url`, пытается извлечь access_token из тела ответа и proof_token, turnstile_token, cookies и headers из заголовков.
6.  **Проверяет наличие proof_token**:
    *   После обработки всех HAR файлов проверяет, был ли найден proof_token. Если нет, вызывает исключение `NoValidHarFileError`.

**Примеры**:

```python
request_config = RequestConfig()
try:
    readHAR(request_config)
    print(f"Access Token: {request_config.access_token}")
    print(f"Proof Token: {request_config.proof_token}")
except NoValidHarFileError as ex:
    print(f"Ошибка: {ex}")
```

### `get_headers`

```python
def get_headers(entry: dict) -> dict:
    """Извлекает заголовки из записи HAR.

    Args:
        entry (dict): Запись HAR.

    Returns:
        dict: Словарь заголовков, приведенных к нижнему регистру.
    """
```

**Назначение**: Функция извлекает заголовки из записи HAR и возвращает их в виде словаря, приводя имена заголовков к нижнему регистру.

**Как работает функция**:

1.  **Извлекает заголовки**:
    *   Проходит по списку заголовков в записи HAR.
2.  **Фильтрует и преобразует заголовки**:
    *   Фильтрует заголовки, исключая `content-length`, `cookie` и заголовки, начинающиеся с `:`.
    *   Приводит имена заголовков к нижнему регистру.
    *   Создает словарь, где ключами являются имена заголовков, а значениями - их значения.
3.  **Возвращает словарь заголовков**:
    *   Возвращает словарь с обработанными заголовками.

**Примеры**:

```python
entry = {
    'request': {
        'headers': [
            {'name': 'Content-Type', 'value': 'application/json'},
            {'name': 'Cookie', 'value': 'sessionid=123'},
            {'name': 'X-Custom-Header', 'value': 'custom_value'}
        ]
    }
}
headers = get_headers(entry)
print(headers)
# Expected output: {'content-type': 'application/json', 'x-custom-header': 'custom_value'}
```

### `parseHAREntry`

```python
def parseHAREntry(entry: dict) -> arkReq:
    """Парсит запись HAR для Arkose Labs и возвращает объект arkReq.

    Args:
        entry (dict): Запись HAR.

    Returns:
        arkReq: Объект arkReq с данными для запроса Arkose Labs.
    """
```

**Назначение**: Функция парсит запись HAR для Arkose Labs, извлекая необходимые данные и возвращая объект `arkReq`.

**Как работает функция**:

1.  **Создает объект `arkReq`**:
    *   Создает экземпляр класса `arkReq` и заполняет его данными из записи HAR, такими как URL, заголовки, тело запроса и куки.
2.  **Извлекает User-Agent**:
    *   Извлекает User-Agent из заголовков.
3.  **Дешифрует данные `bda`**:
    *   Извлекает зашифрованные данные `bda` и `bw` из тела запроса и заголовков.
    *   Дешифрует `bda` с использованием `decrypt()` и сохраняет результат в `arkBx`.
4.  **Возвращает объект `arkReq`**:
    *   Возвращает объект `arkReq` с заполненными данными.

**Примеры**:

```python
entry = {
    'request': {
        'url': 'https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147',
        'headers': [
            {'name': 'User-Agent', 'value': 'Mozilla/5.0'},
            {'name': 'X-Ark-Esync-Value', 'value': 'esync_value'}
        ],
        'postData': {
            'params': [
                {'name': 'bda', 'value': 'encrypted_data'},
                {'name': 'rnd', 'value': '0.123'}
            ]
        },
        'cookies': [
            {'name': 'ark_cookie', 'value': 'cookie_value'}
        ]
    }
}
ark_req = parseHAREntry(entry)
print(ark_req.arkURL)
print(ark_req.arkBx)
```

### `genArkReq`

```python
def genArkReq(chatArk: arkReq) -> arkReq:
    """Генерирует новый запрос Arkose Labs на основе существующего.

    Args:
        chatArk (arkReq): Объект arkReq для генерации нового запроса.

    Returns:
        arkReq: Новый объект arkReq с обновленными данными.

    Raises:
        RuntimeError: Если входной объект arkReq недействителен.
    """
```

**Назначение**: Функция генерирует новый запрос Arkose Labs на основе существующего, обновляя данные `bda`, `rnd` и `x-ark-esync-value`.

**Как работает функция**:

1.  **Создает копию объекта `arkReq`**:
    *   Создает глубокую копию входного объекта `arkReq`.
2.  **Проверяет валидность `arkReq`**:
    *   Проверяет, что скопированный объект `arkReq` и его атрибуты `arkBody` и `arkHeader` не равны `None`. Если какое-либо из этих условий не выполняется, вызывает исключение `RuntimeError`.
3.  **Генерирует новые данные `bda` и `bw`**:
    *   Вызывает функцию `getBDA()` для генерации новых данных `bda` и `bw`.
4.  **Обновляет данные в `arkReq`**:
    *   Обновляет значения `bda`, `rnd` и `x-ark-esync-value` в скопированном объекте `arkReq`.
5.  **Возвращает обновленный объект `arkReq`**:
    *   Возвращает скопированный объект `arkReq` с обновленными данными.

**Примеры**:

```python
chat_ark = arkReq(
    arkURL='https://example.com',
    arkBx='encrypted_data',
    arkHeader={'User-Agent': 'Mozilla/5.0'},
    arkBody={'bda': 'old_bda'},
    arkCookies={},
    userAgent='Mozilla/5.0'
)
try:
    new_ark = genArkReq(chat_ark)
    print(new_ark.arkBody['bda'])
    print(new_ark.arkHeader['x-ark-esync-value'])
except RuntimeError as ex:
    print(f"Ошибка: {ex}")
```

### `sendRequest`

```python
async def sendRequest(tmpArk: arkReq, proxy: str = None) -> str:
    """Отправляет запрос Arkose Labs и возвращает токен.

    Args:
        tmpArk (arkReq): Объект arkReq для отправки запроса.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.

    Returns:
        str: Токен Arkose Labs.

    Raises:
        RuntimeError: Если не удалось сгенерировать валидный токен Arkose Labs.
    """
```

**Назначение**: Асинхронная функция отправляет запрос Arkose Labs и возвращает полученный токен.

**Как работает функция**:

1.  **Отправляет запрос**:
    *   Использует `StreamSession` для отправки POST-запроса на URL Arkose Labs с заголовками, куками и телом запроса из объекта `tmpArk`.
2.  **Получает ответ**:
    *   Получает JSON-ответ от сервера.
3.  **Извлекает токен**:
    *   Извлекает значение токена из поля `token` в JSON-ответе.
4.  **Проверяет валидность токена**:
    *   Проверяет, содержит ли токен подстроку `"sup=1|rid="`. Если нет, вызывает исключение `RuntimeError`.
5.  **Возвращает токен**:
    *   Возвращает полученный токен.

**Примеры**:

```python
import asyncio
async def main():
    tmp_ark = arkReq(
        arkURL='https://example.com',
        arkBx='encrypted_data',
        arkHeader={'User-Agent': 'Mozilla/5.0'},
        arkBody={'bda': 'some_bda'},
        arkCookies={},
        userAgent='Mozilla/5.0'
    )
    try:
        token = await sendRequest(tmp_ark)
        print(f"Получен токен: {token}")
    except RuntimeError as ex:
        print(f"Ошибка: {ex}")

asyncio.run(main())
```

### `getBDA`

```python
def getBDA(arkReq: arkReq) -> tuple[str, str]:
    """Генерирует данные BDA и BW для запроса Arkose Labs.

    Args:
        arkReq (arkReq): Объект arkReq.

    Returns:
        tuple[str, str]: Зашифрованные данные BX и BW.
    """
```

**Назначение**: Функция генерирует данные BDA (Browser Data Analysis) и BW (Browser Width) для запроса Arkose Labs.

**Как работает функция**:

1.  **Извлекает данные `bx`**:
    *   Извлекает зашифрованные данные `bx` из объекта `arkReq`.
2.  **Обновляет значение `n`**:
    *   Заменяет значение ключа `"key":"n","value":"\\S*?"` в данных `bx` на новое значение, полученное с помощью функции `getN()`.
3.  **Обновляет UUID**:
    *   Ищет старый UUID в данных `bx` и заменяет его на новый, сгенерированный с помощью `uuid.uuid4()`.
4.  **Генерирует `bw`**:
    *   Генерирует значение `bw` с помощью функций `getBt()` и `getBw()`.
5.  **Шифрует `bx`**:
    *   Шифрует обновленные данные `bx` с использованием функции `encrypt()` и ключа, состоящего из User-Agent и `bw`.
6.  **Возвращает зашифрованные данные и `bw`**:
    *   Возвращает зашифрованные данные `bx` и значение `bw`.

**Примеры**:

```python
ark_req = arkReq(
    arkURL='https://example.com',
    arkBx='"key":"n","value":"old_value"',
    arkHeader={'User-Agent': 'Mozilla/5.0'},
    arkBody={},
    arkCookies={},
    userAgent='Mozilla/5.0'
)
encrypted_bx, bw = getBDA(ark_req)
print(f"Зашифрованные данные BX: {encrypted_bx}")
print(f"BW: {bw}")
```

### `getBt`

```python
def getBt() -> int:
    """Возвращает текущее время в формате Unix timestamp.

    Returns:
        int: Текущее время в формате Unix timestamp.
    """
```

**Назначение**: Функция возвращает текущее время в формате Unix timestamp.

**Как работает функция**:

1.  **Получает текущее время**:
    *   Использует функцию `time.time()` для получения текущего времени в секундах с плавающей точкой.
2.  **Преобразует в целое число**:
    *   Преобразует полученное значение в целое число, отбрасывая дробную часть.
3.  **Возвращает Unix timestamp**:
    *   Возвращает текущее время в формате Unix timestamp.

**Примеры**:

```python
bt = getBt()
print(f"Текущее время в формате Unix timestamp: {bt}")
```

### `getBw`

```python
def getBw(bt: int) -> str:
    """Вычисляет значение BW на основе времени BT.

    Args:
        bt (int): Время в формате Unix timestamp.

    Returns:
        str: Значение BW.
    """
```

**Назначение**: Функция вычисляет значение BW (Browser Width) на основе времени BT (Browser Time).

**Как работает функция**:

1.  **Вычисляет BW**:
    *   Вычисляет BW как разницу между BT и остатком от деления BT на 21600.
2.  **Преобразует в строку**:
    *   Преобразует полученное значение BW в строку.
3.  **Возвращает BW**:
    *   Возвращает значение BW в виде строки.

**Примеры**:

```python
bt = 1678886400
bw = getBw(bt)
print(f"Значение BW: {bw}")
```

### `getN`

```python
def getN() -> str:
    """Генерирует значение N на основе текущего времени.

    Returns:
        str: Значение N, закодированное в base64.
    """
```

**Назначение**: Функция генерирует значение N на основе текущего времени и кодирует его в base64.

**Как работает функция**:

1.  **Получает текущее время**:
    *   Использует функцию `time.time()` для получения текущего времени в секундах с плавающей точкой.
2.  **Преобразует в строку**:
    *   Преобразует полученное значение в строку.
3.  **Кодирует в base64**:
    *   Кодирует строку с текущим временем в base64.
4.  **Возвращает закодированное значение**:
    *   Возвращает закодированное в base64 значение.

**Примеры**:

```python
n = getN()
print(f"Значение N: {n}")
```

### `get_request_config`

```python
async def get_request_config(request_config: RequestConfig, proxy: str) -> RequestConfig:
    """Получает конфигурацию запроса, читая HAR файлы и генерируя токен Arkose Labs.

    Args:
        request_config (RequestConfig): Объект конфигурации запроса.
        proxy (str): Прокси-сервер для использования.

    Returns:
        RequestConfig: Обновленный объект конфигурации запроса.
    """
```

**Назначение**: Асинхронная функция получает конфигурацию запроса, читая HAR файлы и генерируя токен Arkose Labs.

**Как работает функция**:

1.  **Читает HAR файлы**:
    *   Если `request_config.proof_token` равен `None`, вызывает функцию `readHAR()` для чтения HAR файлов и извлечения данных.
2.  **Генерирует токен Arkose Labs**:
    *   Если `request_config.arkose_request` не равен `None`, вызывает функции `genArkReq()` и `sendRequest()` для генерации нового запроса Arkose Labs и отправки его на сервер. Полученный токен сохраняет в `request_config.arkose_token`.
3.  **Возвращает обновленную конфигурацию**:
    *   Возвращает обновленный объект `request_config`.

**Примеры**:

```python
import asyncio
async def main():
    request_config = RequestConfig()
    proxy = 'http://your_proxy:8080'
    try:
        updated_config = await get_request_config(request_config, proxy)
        print(f"Access Token: {updated_config.access_token}")
        print(f"Arkose Token: {updated_config.arkose_token}")
    except Exception as ex:
        print(f"Ошибка: {ex}")

asyncio.run(main())
```