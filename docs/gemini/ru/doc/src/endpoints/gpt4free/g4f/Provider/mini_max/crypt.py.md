# Модуль crypt.py

## Обзор

Модуль `crypt.py` предназначен для обеспечения криптографических функций, необходимых для взаимодействия с API mini_max. Он включает в себя функции для генерации хешей, формирования заголовков и тел запросов, а также получения параметров обратного вызова через браузер.

## Подробнее

Этот модуль содержит функции, которые имитируют криптографические процессы, используемые в JavaScript коде для обеспечения совместимости и безопасности при взаимодействии с API. Он включает в себя функции для вычисления MD5 хешей, генерации специальных заголовков и форматирования тел запросов. Также модуль предоставляет механизм для получения токена аутентификации и других параметров из браузера с использованием асинхронных функций.

## Классы

### `CallbackResults`

**Описание**: Класс для хранения результатов обратного вызова, полученных из браузера.

**Атрибуты**:
- `token` (str): Токен аутентификации.
- `path_and_query` (str): Путь и параметры запроса.
- `timestamp` (int): Временная метка.

## Функции

### `hash_function`

```python
def hash_function(base_string: str) -> str:
    """
    Mimics the hashFunction using MD5.
    """
    ...
```

**Назначение**: Генерирует MD5 хеш из переданной строки.

**Параметры**:
- `base_string` (str): Строка для хеширования.

**Возвращает**:
- `str`: MD5 хеш в шестнадцатеричном формате.

**Как работает функция**:
1. Принимает строку `base_string` в качестве аргумента.
2. Кодирует строку в байты, используя кодировку UTF-8.
3. Вычисляет MD5 хеш от полученных байтов.
4. Возвращает хеш в виде строки шестнадцатеричных цифр.

**ASCII flowchart**:

```
A[Строка]
|
B[Кодирование в байты]
|
C[MD5 хеширование]
|
D[Преобразование в hex]
|
E[Возврат хеша]
```

**Примеры**:

```python
hash_function("test_string")
```

### `generate_yy_header`

```python
def generate_yy_header(has_search_params_path: str, body_to_yy: dict, time: int) -> str:
    """
    Python equivalent of the generateYYHeader function.
    """
    ...
```

**Назначение**: Генерирует заголовок `yy` на основе пути с параметрами поиска, тела запроса и временной метки.

**Параметры**:
- `has_search_params_path` (str): Путь с параметрами поиска.
- `body_to_yy` (dict): Тело запроса в виде словаря.
- `time` (int): Временная метка.

**Возвращает**:
- `str`: Сгенерированный заголовок `yy`.

**Как работает функция**:

1.  **Кодирование пути**: Кодирует путь `has_search_params_path` с использованием `urllib.parse.quote`.
2.  **Хеширование времени**: Вычисляет хеш от временной метки `time` с использованием `hash_function`.
3.  **Объединение строк**: Конкатенирует закодированный путь, тело запроса `body_to_yy` и хеш времени.
4.  **Хеширование объединенной строки**: Вычисляет хеш от объединенной строки.
5.  **Возврат хеша**: Возвращает полученный хеш.

**ASCII flowchart**:

```
A[Путь с параметрами, тело запроса, время]
|
B[Кодирование пути]
|
C[Хеширование времени]
|
D[Объединение строк]
|
E[Хеширование объединенной строки]
|
F[Возврат хеша заголовка]
```

**Примеры**:

```python
generate_yy_header("/v4/api/chat/msg", {"key": "value"}, 1678886400)
```

### `get_body_to_yy`

```python
def get_body_to_yy(l):
    L = l["msgContent"].replace("\\r\\n", "").replace("\\n", "").replace("\\r", "")
    M = hash_function(l["characterID"]) + hash_function(L) + hash_function(l["chatID"])
    M += hash_function("")  # Mimics hashFunction(undefined) in JS

    # print("bodyToYY:", M)
    return M
```

**Назначение**: Формирует строку `bodyToYY` на основе содержимого сообщения, идентификаторов персонажа и чата.

**Параметры**:
- `l` (dict): Словарь, содержащий ключи `"msgContent"`, `"characterID"` и `"chatID"`.

**Возвращает**:
- `str`: Сформированная строка `bodyToYY`.

**Как работает функция**:

1.  **Очистка содержимого сообщения**: Удаляет символы перевода строки и возврата каретки из содержимого сообщения `"msgContent"`.
2.  **Хеширование идентификаторов**: Вычисляет хеши от идентификаторов персонажа `"characterID"` и чата `"chatID"`.
3.  **Объединение хешей**: Конкатенирует хеши идентификаторов и хеш очищенного содержимого сообщения.
4.  **Добавление хеша пустой строки**: Добавляет хеш пустой строки для имитации поведения JavaScript.
5.  **Возврат строки**: Возвращает полученную строку.

**ASCII flowchart**:

```
A[Словарь с данными]
|
B[Очистка msgContent]
|
C[Хеширование characterID]
|
D[Хеширование msgContent]
|
E[Хеширование chatID]
|
F[Объединение хешей]
|
G[Добавление хеша пустой строки]
|
H[Возврат строки bodyToYY]
```

**Примеры**:

```python
data = {"msgContent": "Hello\\r\\nWorld", "characterID": "char123", "chatID": "chat456"}
get_body_to_yy(data)
```

### `get_body_json`

```python
def get_body_json(s):
    return json.dumps(s, ensure_ascii=True, sort_keys=True)
```

**Назначение**: Преобразует словарь в JSON-строку, обеспечивая ASCII-совместимость и сортировку ключей.

**Параметры**:
- `s` (dict): Словарь для преобразования в JSON.

**Возвращает**:
- `str`: JSON-строка.

**Как работает функция**:

1.  **Преобразование в JSON**: Преобразует словарь `s` в JSON-строку с использованием `json.dumps`.
2.  **Обеспечение ASCII**: Устанавливает `ensure_ascii=True` для кодирования не-ASCII символов.
3.  **Сортировка ключей**: Устанавливает `sort_keys=True` для сортировки ключей в JSON-строке.
4.  **Возврат JSON**: Возвращает полученную JSON-строку.

**ASCII flowchart**:

```
A[Словарь]
|
B[Преобразование в JSON]
|
C[Обеспечение ASCII]
|
D[Сортировка ключей]
|
E[Возврат JSON строки]
```

**Примеры**:

```python
data = {"key1": "value1", "key2": "value2"}
get_body_json(data)
```

### `get_browser_callback`

```python
async def get_browser_callback(auth_result: CallbackResults):
    async def callback(page: Tab):
        while not auth_result.token:
            auth_result.token = await page.evaluate("localStorage.getItem(\'_token\')")
            if not auth_result.token:
                await asyncio.sleep(1)
        (auth_result.path_and_query, auth_result.timestamp) = await page.evaluate("""
            const device_id = localStorage.getItem("USER_HARD_WARE_INFO");
            const uuid = localStorage.getItem("UNIQUE_USER_ID");
            const os_name = navigator.userAgentData?.platform || navigator.platform || "Unknown";
            const browser_name = (() => {
                const userAgent = navigator.userAgent.toLowerCase();
                if (userAgent.includes("chrome") && !userAgent.includes("edg")) return "chrome";
                if (userAgent.includes("edg")) return "edge";
                if (userAgent.includes("firefox")) return "firefox";
                if (userAgent.includes("safari") && !userAgent.includes("chrome")) return "safari";
                return "unknown";
            })();
            const cpu_core_num = navigator.hardwareConcurrency || 8;
            const browser_language = navigator.language || "unknown";
            const browser_platform = `${navigator.platform || "unknown"}`;\
            const screen_width = window.screen.width || "unknown";
            const screen_height = window.screen.height || "unknown";
            const unix = Date.now(); // Current Unix timestamp in milliseconds
            const params = {\n                device_platform: "web",
                biz_id: 2,
                app_id: 3001,
                version_code: 22201,
                lang: "en",
                uuid,
                device_id,
                os_name,
                browser_name,
                cpu_core_num,
                browser_language,
                browser_platform,
                screen_width,
                screen_height,
                unix
            };\n            [new URLSearchParams(params).toString(), unix]\n        """)
        auth_result.path_and_query = f"{API_PATH}?{auth_result.path_and_query}"
    return callback
```

**Назначение**: Возвращает асинхронную функцию обратного вызова для получения токена аутентификации и параметров запроса из браузера.

**Параметры**:
- `auth_result` (CallbackResults): Объект `CallbackResults` для хранения полученных данных.

**Возвращает**:
- `Callable[[Tab], Awaitable[None]]`: Асинхронная функция обратного вызова, принимающая объект `Tab`.

**Как работает функция**:

1.  **Определение внутренней функции `callback`**: Определяет асинхронную функцию `callback`, которая будет выполняться в браузере.
2.  **Получение токена**: В цикле ожидает получения токена из `localStorage` браузера.
3.  **Получение параметров запроса**: Извлекает параметры запроса, такие как `device_id`, `uuid`, `os_name`, `browser_name`, `cpu_core_num`, `browser_language`, `browser_platform`, `screen_width`, `screen_height` и текущую метку времени Unix, из `localStorage` и `navigator` браузера.
4.  **Формирование пути запроса**: Формирует путь запроса, добавляя полученные параметры к `API_PATH`.
5.  **Сохранение результатов**: Сохраняет полученный токен, путь запроса и временную метку в объекте `auth_result`.
6.  **Возврат функции обратного вызова**: Возвращает функцию `callback`.

**Внутренние функции**:

### `callback`
```python
async def callback(page: Tab):
        while not auth_result.token:
            auth_result.token = await page.evaluate("localStorage.getItem(\'_token\')")
            if not auth_result.token:
                await asyncio.sleep(1)
        (auth_result.path_and_query, auth_result.timestamp) = await page.evaluate("""
            const device_id = localStorage.getItem("USER_HARD_WARE_INFO");
            const uuid = localStorage.getItem("UNIQUE_USER_ID");
            const os_name = navigator.userAgentData?.platform || navigator.platform || "Unknown";
            const browser_name = (() => {
                const userAgent = navigator.userAgent.toLowerCase();
                if (userAgent.includes("chrome") && !userAgent.includes("edg")) return "chrome";
                if (userAgent.includes("edg")) return "edge";
                if (userAgent.includes("firefox")) return "firefox";
                if (userAgent.includes("safari") && !userAgent.includes("chrome")) return "safari";
                return "unknown";
            })();
            const cpu_core_num = navigator.hardwareConcurrency || 8;
            const browser_language = navigator.language || "unknown";
            const browser_platform = `${navigator.platform || "unknown"}`;\
            const screen_width = window.screen.width || "unknown";
            const screen_height = window.screen.height || "unknown";
            const unix = Date.now(); // Current Unix timestamp in milliseconds
            const params = {\n                device_platform: "web",
                biz_id: 2,
                app_id: 3001,
                version_code: 22201,
                lang: "en",
                uuid,
                device_id,
                os_name,
                browser_name,
                cpu_core_num,
                browser_language,
                browser_platform,
                screen_width,
                screen_height,
                unix
            };\n            [new URLSearchParams(params).toString(), unix]\n        """)
        auth_result.path_and_query = f"{API_PATH}?{auth_result.path_and_query}"
```

**Назначение**: Асинхронная функция обратного вызова для получения токена аутентификации и параметров запроса из браузера.

**Параметры**:
- `page` (Tab): Объект `Tab`, представляющий вкладку браузера.

**Как работает функция**:

1.  **Получение токена**: В цикле ожидает получения токена из `localStorage` браузера.
2.  **Получение параметров запроса**: Извлекает параметры запроса, такие как `device_id`, `uuid`, `os_name`, `browser_name`, `cpu_core_num`, `browser_language`, `browser_platform`, `screen_width`, `screen_height` и текущую метку времени Unix, из `localStorage` и `navigator` браузера.
3.  **Формирование пути запроса**: Формирует путь запроса, добавляя полученные параметры к `API_PATH`.
4.  **Сохранение результатов**: Сохраняет полученный токен, путь запроса и временную метку в объекте `auth_result`.

**ASCII flowchart**:

```
A[Вкладка браузера]
|
B[Ожидание получения токена]
|
C[Извлечение параметров запроса]
|
D[Формирование пути запроса]
|
E[Сохранение результатов]
```

**Примеры**:

```python
auth_result = CallbackResults()
callback_func = get_browser_callback(auth_result)
# Assume 'page' is an instance of Tab (from playwright or similar)
# await callback_func(page)
```
```
auth_result = CallbackResults()
get_browser_callback(auth_result)