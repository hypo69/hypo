# Модуль для работы с HAR-файлами для получения конфигурации запроса
======================================================================

Модуль содержит функции для чтения, парсинга и генерации конфигураций запросов из HAR-файлов,
используемых для получения необходимых токенов и заголовков для взаимодействия с API.

## Обзор

Этот модуль предоставляет набор функций для извлечения и обработки данных из HAR-файлов,
которые содержат информацию о HTTP-запросах и ответах. Основная цель модуля - автоматизировать
процесс получения необходимых параметров (таких как access_token, proof_token, arkose_token и др.)
для успешного взаимодействия с API, требующими сложной аутентификации и защиты от ботов.

## Подробнее

Модуль предназначен для работы с HAR-файлами, которые содержат записи HTTP-запросов и ответов.
Он используется для извлечения конфигурационных данных, необходимых для выполнения запросов к API,
включая токены доступа, заголовки и куки. Модуль также включает функции для расшифровки и шифрования
данных, необходимых для обхода защиты от ботов.

## Классы

### `RequestConfig`

**Описание**: Класс, представляющий конфигурацию запроса, содержащую различные параметры,
необходимые для выполнения запросов к API.

**Атрибуты**:
- `cookies` (dict): Словарь с куками.
- `headers` (dict): Словарь с заголовками.
- `access_token` (str): Токен доступа.
- `proof_token` (list): Список токенов подтверждения.
- `turnstile_token` (str): Токен Turnstile.
- `arkose_request` (`arkReq`): Объект `arkReq`, содержащий данные для запроса Arkose.
- `arkose_token` (str): Токен Arkose.
- `data_build` (str): Строка, содержащая информацию о сборке данных.

### `arkReq`

**Описание**: Класс, представляющий запрос Arkose, содержащий данные, необходимые для обхода
защиты от ботов.

**Атрибуты**:
- `arkURL` (str): URL для запроса Arkose.
- `arkBx` (str): Зашифрованные данные для запроса Arkose.
- `arkHeader` (dict): Словарь с заголовками для запроса Arkose.
- `arkBody` (dict): Словарь с данными тела запроса Arkose.
- `arkCookies` (dict): Словарь с куками для запроса Arkose.
- `userAgent` (str): User-Agent для запроса Arkose.

## Функции

### `get_har_files`

```python
def get_har_files() -> list[str]:
    """
    Находит все HAR-файлы в директории с куками.

    Args:
        None

    Returns:
        list[str]: Список путей к найденным HAR-файлам.

    Raises:
        NoValidHarFileError: Если директория с куками не читаема или в ней не найдены HAR-файлы.

    Как работает функция:
    1. Проверяет, доступна ли директория с куками для чтения. Если нет, вызывает исключение `NoValidHarFileError`.
    2. Проходит по всем файлам в директории с куками и добавляет пути к HAR-файлам в список `harPath`.
    3. Если список `harPath` пуст, вызывает исключение `NoValidHarFileError`.
    4. Сортирует список `harPath` по времени изменения файла и возвращает его.

    ASCII Flowchart:
    A[Проверка доступности директории с куками]
    |\n
    B[Поиск HAR-файлов в директории]
    |\n
    C[Проверка наличия HAR-файлов]
    |\n
    D[Сортировка HAR-файлов по времени изменения]
    |\n
    E[Возврат списка HAR-файлов]

    Примеры:
        # Предполжим, что в директории есть файл example.har
        >>> get_har_files()
        ['путь/к/example.har']
    """
    ...
```

### `readHAR`

```python
def readHAR(request_config: RequestConfig) -> None:
    """
    Читает HAR-файлы и извлекает из них конфигурационные данные для запроса.

    Args:
        request_config (RequestConfig): Объект конфигурации запроса, который будет заполнен данными из HAR-файлов.

    Returns:
        None

    Raises:
        NoValidHarFileError: Если не найден proof_token в HAR-файлах.

    Как работает функция:
    1. Получает список HAR-файлов с помощью функции `get_har_files`.
    2. Итерируется по списку HAR-файлов.
    3. Для каждого HAR-файла пытается прочитать и распарсить JSON. Если это не удается, переходит к следующему файлу.
    4. Итерируется по записям в HAR-файле и извлекает необходимые данные, такие как `access_token`, `proof_token`, `turnstile_token`, `arkose_request`.
    5. Если не найден `proof_token`, вызывает исключение `NoValidHarFileError`.

    ASCII Flowchart:
    A[Получение списка HAR-файлов]
    |\n
    B[Итерация по HAR-файлам]
    |\n
    C[Чтение и парсинг JSON]
    |\n
    D[Итерация по записям в HAR-файле]
    |\n
    E[Извлечение данных: access_token, proof_token, turnstile_token, arkose_request]
    |\n
    F[Проверка наличия proof_token]
    |\n
    G[Завершение]

    Примеры:
        # Создаем объект RequestConfig и заполняем его данными из HAR-файлов
        >>> request_config = RequestConfig()
        >>> readHAR(request_config)
    """
    ...
```

### `get_headers`

```python
def get_headers(entry: dict) -> dict:
    """
    Извлекает заголовки из записи HAR-файла, приводя их к нижнему регистру.

    Args:
        entry (dict): Запись HAR-файла, содержащая информацию о запросе.

    Returns:
        dict: Словарь с заголовками, приведенными к нижнему регистру.

    Как работает функция:
    1. Извлекает список заголовков из записи HAR-файла.
    2. Преобразует каждый заголовок в нижний регистр и создает словарь, где ключами являются имена заголовков в нижнем регистре, а значениями - их значения.
    3. Исключает заголовки `content-length`, `cookie` и заголовки, начинающиеся с `:`.

    ASCII Flowchart:
    A[Извлечение списка заголовков из записи HAR-файла]
    |\n
    B[Преобразование заголовков к нижнему регистру и создание словаря]
    |\n
    C[Исключение нежелательных заголовков]
    |\n
    D[Возврат словаря заголовков]

    Примеры:
        # Пример записи HAR-файла
        >>> entry = {'request': {'headers': [{'name': 'Content-Type', 'value': 'application/json'}, {'name': 'Cookie', 'value': 'test=123'}]}}
        >>> get_headers(entry)
        {'content-type': 'application/json'}
    """
    ...
```

### `parseHAREntry`

```python
def parseHAREntry(entry: dict) -> arkReq:
    """
    Парсит запись HAR-файла и создает объект `arkReq` с данными для запроса Arkose.

    Args:
        entry (dict): Запись HAR-файла, содержащая информацию о запросе Arkose.

    Returns:
        arkReq: Объект `arkReq`, содержащий данные для запроса Arkose.

    Как работает функция:
    1. Извлекает URL, заголовки, тело запроса и куки из записи HAR-файла.
    2. Создает объект `arkReq` с извлеченными данными.
    3. Расшифровывает данные `bda` из тела запроса с использованием `userAgent` и `x-ark-esync-value` из заголовков.

    ASCII Flowchart:
    A[Извлечение URL, заголовков, тела запроса и куки из записи HAR-файла]
    |\n
    B[Создание объекта `arkReq` с извлеченными данными]
    |\n
    C[Расшифровка данных `bda` из тела запроса]
    |\n
    D[Возврат объекта `arkReq`]

    Примеры:
        # Пример записи HAR-файла для запроса Arkose
        >>> entry = {'request': {'url': 'https://example.com/arkose', 'headers': [{'name': 'X-Ark-Esync-Value', 'value': 'test'}], 'postData': {'params': [{'name': 'bda', 'value': 'test'}]}}}
        >>> parseHAREntry(entry)
        <arkReq object>
    """
    ...
```

### `genArkReq`

```python
def genArkReq(chatArk: arkReq) -> arkReq:
    """
    Генерирует новый запрос Arkose на основе существующего запроса.

    Args:
        chatArk (arkReq): Объект `arkReq`, содержащий данные для запроса Arkose.

    Returns:
        arkReq: Новый объект `arkReq` с обновленными данными для запроса Arkose.

    Raises:
        RuntimeError: Если HAR-файл не валиден.

    Как работает функция:
    1. Создает глубокую копию объекта `chatArk`.
    2. Проверяет, что `tmpArk` и его атрибуты `arkBody` и `arkHeader` не равны `None`. Если это не так, вызывает исключение `RuntimeError`.
    3. Генерирует новые данные `bda` и `bw` с помощью функции `getBDA`.
    4. Кодирует `bda` в base64 и добавляет случайное число `rnd` в тело запроса.
    5. Обновляет заголовок `x-ark-esync-value` значением `bw`.

    ASCII Flowchart:
    A[Создание глубокой копии объекта `chatArk`]
    |\n
    B[Проверка валидности HAR-файла]
    |\n
    C[Генерация новых данных `bda` и `bw`]
    |\n
    D[Кодирование `bda` в base64 и добавление случайного числа `rnd`]
    |\n
    E[Обновление заголовка `x-ark-esync-value`]
    |\n
    F[Возврат нового объекта `arkReq`]

    Примеры:
        # Пример объекта arkReq
        >>> chatArk = arkReq(arkURL='https://example.com/arkose', arkBx='test', arkHeader={'X-Ark-Esync-Value': 'test'}, arkBody={'bda': 'test'}, arkCookies={}, userAgent='test')
        >>> genArkReq(chatArk)
        <arkReq object>
    """
    ...
```

### `sendRequest`

```python
async def sendRequest(tmpArk: arkReq, proxy: str = None) -> str:
    """
    Отправляет запрос Arkose и возвращает токен.

    Args:
        tmpArk (arkReq): Объект `arkReq`, содержащий данные для запроса Arkose.
        proxy (str, optional): Прокси-сервер для отправки запроса. По умолчанию `None`.

    Returns:
        str: Токен Arkose.

    Raises:
        RuntimeError: Если не удалось сгенерировать валидный токен Arkose.

    Как работает функция:
    1. Отправляет POST-запрос на URL `tmpArk.arkURL` с заголовками `tmpArk.arkHeader`, куками `tmpArk.arkCookies` и телом запроса `tmpArk.arkBody`.
    2. Извлекает токен из JSON-ответа.
    3. Проверяет, содержит ли токен подстроку `sup=1|rid=`. Если нет, вызывает исключение `RuntimeError`.

    ASCII Flowchart:
    A[Отправка POST-запроса на URL `tmpArk.arkURL`]
    |\n
    B[Извлечение токена из JSON-ответа]
    |\n
    C[Проверка валидности токена]
    |\n
    D[Возврат токена]

    Примеры:
        # Пример объекта arkReq
        >>> tmpArk = arkReq(arkURL='https://example.com/arkose', arkBx='test', arkHeader={'X-Ark-Esync-Value': 'test'}, arkBody={'bda': 'test'}, arkCookies={}, userAgent='test')
        >>> await sendRequest(tmpArk)
        'arkose_token'
    """
    ...
```

### `getBDA`

```python
def getBDA(arkReq: arkReq) -> tuple[str, str]:
    """
    Генерирует данные `bda` и `bw` для запроса Arkose.

    Args:
        arkReq (arkReq): Объект `arkReq`, содержащий данные для запроса Arkose.

    Returns:
        tuple[str, str]: Кортеж, содержащий зашифрованные данные `bda` и `bw`.

    Как работает функция:
    1. Заменяет значение ключа `"n"` в `bx` на новое значение, полученное с помощью функции `getN`.
    2. Заменяет старый UUID на новый UUID в `bx`.
    3. Генерирует значение `bw` с помощью функций `getBt` и `getBw`.
    4. Шифрует `bx` с использованием `userAgent` и `bw`.

    ASCII Flowchart:
    A[Замена значения ключа `"n"` в `bx`]
    |\n
    B[Замена старого UUID на новый UUID в `bx`]
    |\n
    C[Генерация значения `bw`]
    |\n
    D[Шифрование `bx`]
    |\n
    E[Возврат зашифрованных данных `bda` и `bw`]

    Примеры:
        # Пример объекта arkReq
        >>> arkReq = arkReq(arkURL='https://example.com/arkose', arkBx='test', arkHeader={'X-Ark-Esync-Value': 'test'}, arkBody={'bda': 'test'}, arkCookies={}, userAgent='test')
        >>> getBDA(arkReq)
        ('encrypted_bda', 'bw')
    """
    ...
```

### `getBt`

```python
def getBt() -> int:
    """
    Возвращает текущее время в формате Unix timestamp.

    Args:
        None

    Returns:
        int: Текущее время в формате Unix timestamp.

    Как работает функция:
    1. Получает текущее время с помощью функции `time.time()`.
    2. Преобразует время в целое число.

    ASCII Flowchart:
    A[Получение текущего времени]
    |\n
    B[Преобразование времени в целое число]
    |\n
    C[Возврат времени]

    Примеры:
        # Пример вызова функции
        >>> getBt()
        1678886400
    """
    ...
```

### `getBw`

```python
def getBw(bt: int) -> str:
    """
    Вычисляет значение `bw` на основе времени `bt`.

    Args:
        bt (int): Время в формате Unix timestamp.

    Returns:
        str: Значение `bw`.

    Как работает функция:
    1. Вычисляет остаток от деления `bt` на 21600.
    2. Вычитает остаток из `bt`.
    3. Преобразует результат в строку.

    ASCII Flowchart:
    A[Вычисление остатка от деления `bt` на 21600]
    |\n
    B[Вычитание остатка из `bt`]
    |\n
    C[Преобразование результата в строку]
    |\n
    D[Возврат значения `bw`]

    Примеры:
        # Пример вызова функции
        >>> getBw(1678886400)
        '1678864800'
    """
    ...
```

### `getN`

```python
def getN() -> str:
    """
    Генерирует значение `n` на основе текущего времени.

    Args:
        None

    Returns:
        str: Значение `n`, закодированное в base64.

    Как работает функция:
    1. Получает текущее время в формате Unix timestamp.
    2. Кодирует время в base64.
    3. Преобразует закодированное значение в строку.

    ASCII Flowchart:
    A[Получение текущего времени]
    |\n
    B[Кодирование времени в base64]
    |\n
    C[Преобразование закодированного значения в строку]
    |\n
    D[Возврат значения `n`]

    Примеры:
        # Пример вызова функции
        >>> getN()
        'MTY3ODg4NjQwMA=='
    """
    ...
```

### `get_request_config`

```python
async def get_request_config(request_config: RequestConfig, proxy: str) -> RequestConfig:
    """
    Получает конфигурацию запроса, заполняя объект `RequestConfig` данными из HAR-файлов и Arkose.

    Args:
        request_config (RequestConfig): Объект конфигурации запроса.
        proxy (str): Прокси-сервер для отправки запроса Arkose.

    Returns:
        RequestConfig: Объект конфигурации запроса с заполненными данными.

    Как работает функция:
    1. Проверяет, заполнен ли `proof_token` в `request_config`. Если нет, вызывает функцию `readHAR` для чтения HAR-файлов.
    2. Если `arkose_request` не равен `None`, генерирует и отправляет запрос Arkose с помощью функций `genArkReq` и `sendRequest`.

    ASCII Flowchart:
    A[Проверка наличия `proof_token`]
    |\n
    B[Чтение HAR-файлов (если `proof_token` отсутствует)]
    |\n
    C[Проверка наличия `arkose_request`]
    |\n
    D[Генерация и отправка запроса Arkose (если `arkose_request` присутствует)]
    |\n
    E[Возврат объекта `RequestConfig`]

    Примеры:
        # Пример использования функции
        >>> request_config = RequestConfig()
        >>> await get_request_config(request_config, 'http://proxy.example.com')
        <RequestConfig object>
    """
    ...
```