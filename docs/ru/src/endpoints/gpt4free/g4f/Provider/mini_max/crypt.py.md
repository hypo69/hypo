# Модуль crypt.py

## Обзор

Модуль `crypt.py` предназначен для реализации криптографических функций, используемых в Provider mini_max. Он включает в себя функции для хеширования данных, генерации заголовков и подготовки тела запроса.

## Подробней

Модуль содержит функции для имитации хеш-функций MD5, генерации специальных заголовков `yy_header`, а также подготовки тела запроса в формате JSON для взаимодействия с API. Он также включает функции для получения данных из браузера, такие как токен авторизации и параметры устройства пользователя.
Этот модуль важен для обеспечения безопасности и правильной аутентификации при взаимодействии с API mini_max.

## Классы

### `CallbackResults`

**Описание**: Класс для хранения результатов обратного вызова из браузера, таких как токен, путь запроса и временная метка.

**Атрибуты**:

- `token` (str): Токен авторизации.
- `path_and_query` (str): Путь и параметры запроса.
- `timestamp` (int): Временная метка.

### `__init__`

```python
    def __init__(self):
        self.token: str = None
        self.path_and_query: str = None
        self.timestamp: int = None
```

**Назначение**: Инициализирует экземпляр класса `CallbackResults` с атрибутами `token`, `path_and_query` и `timestamp`, установленными в `None`.

**Параметры**:

- Отсутствуют.

**Возвращает**:

- Отсутствует.

**Как работает функция**:

1.  Инициализирует атрибут `token` значением `None`.
2.  Инициализирует атрибут `path_and_query` значением `None`.
3.  Инициализирует атрибут `timestamp` значением `None`.

**Примеры**:

```python
results = CallbackResults()
print(results.token)  # None
```

## Функции

### `hash_function`

```python
def hash_function(base_string: str) -> str:
    """
    Mimics the hashFunction using MD5.
    """
    return hashlib.md5(base_string.encode()).hexdigest()
```

**Назначение**: Функция `hash_function` имитирует хеш-функцию с использованием алгоритма MD5. Она принимает строку в качестве аргумента, кодирует её в байты и вычисляет MD5 хеш, который затем возвращается в шестнадцатеричном формате.

**Параметры**:

- `base_string` (str): Строка, которую необходимо хешировать.

**Возвращает**:

- `str`: MD5 хеш строки в шестнадцатеричном формате.

**Как работает функция**:

1.  Кодирует входную строку `base_string` в байты с использованием кодировки UTF-8.
2.  Вычисляет MD5 хеш полученных байтов с помощью `hashlib.md5()`.
3.  Преобразует полученный хеш в шестнадцатеричную строку с помощью `.hexdigest()`.
4.  Возвращает полученную шестнадцатеричную строку.

ASCII flowchart:

```
base_string (str)
    ↓
encode('utf-8')
    ↓
MD5 Hash (hashlib.md5)
    ↓
hexdigest()
    ↓
hex_string (str)
```

**Примеры**:

```python
result = hash_function("test_string")
print(result) # Output: 'd8e8fca2dc0f896fd7cb4cb0031ba249'
```

### `generate_yy_header`

```python
def generate_yy_header(has_search_params_path: str, body_to_yy: dict, time: int) -> str:
    """
    Python equivalent of the generateYYHeader function.
    """
    encoded_path = quote(has_search_params_path, "")
    time_hash = hash_function(str(time))
    combined_string = f"{encoded_path}_{body_to_yy}{time_hash}ooui"
    return hash_function(combined_string)
```

**Назначение**: Функция `generate_yy_header` генерирует заголовок `yy_header`, используя предоставленные параметры и хеш-функцию. Этот заголовок используется для аутентификации запросов к API.

**Параметры**:

- `has_search_params_path` (str): Путь с параметрами поиска.
- `body_to_yy` (dict): Словарь с данными тела запроса.
- `time` (int): Временная метка.

**Возвращает**:

- `str`: Сгенерированный заголовок `yy_header`.

**Как работает функция**:

1.  Кодирует `has_search_params_path` с помощью `urllib.parse.quote`.
2.  Вычисляет хеш от временной метки `time` с помощью `hash_function`.
3.  Объединяет закодированный путь, тело запроса и хеш временной метки в одну строку.
4.  Вычисляет хеш от объединенной строки с помощью `hash_function`.
5.  Возвращает полученный хеш.

ASCII flowchart:

```
has_search_params_path (str), body_to_yy (dict), time (int)
    ↓
quote(has_search_params_path)
    ↓
hash_function(str(time))
    ↓
encoded_path + body_to_yy + time_hash + "ooui"
    ↓
hash_function(combined_string)
    ↓
yy_header (str)
```

**Примеры**:

```python
header = generate_yy_header("/api/search", {"key": "value"}, 1678886400)
print(header) # Output: 'some_hash'
```

### `get_body_to_yy`

```python
def get_body_to_yy(l):
    L = l["msgContent"].replace("\\r\\n", "").replace("\\n", "").replace("\\r", "")
    M = hash_function(l["characterID"]) + hash_function(L) + hash_function(l["chatID"])
    M += hash_function("")  # Mimics hashFunction(undefined) in JS
    return M
```

**Назначение**: Функция `get_body_to_yy` подготавливает часть тела запроса для генерации `yy_header`. Она извлекает данные из входного словаря, выполняет необходимые преобразования и хеширует полученные значения.

**Параметры**:

- `l` (dict): Словарь, содержащий данные для формирования тела запроса. Ожидается наличие ключей "msgContent", "characterID" и "chatID".

**Возвращает**:

- `str`: Подготовленная строка для включения в тело запроса.

**Как работает функция**:

1.  Извлекает значение ключа `msgContent` из словаря `l` и удаляет символы переноса строки (`\r\n`, `\n`, `\r`).
2.  Вычисляет хеш от значений `characterID`, очищенного `msgContent` и `chatID` с помощью функции `hash_function`.
3.  Добавляет к полученной строке хеш от пустой строки, имитируя поведение JavaScript.
4.  Возвращает полученную строку.

ASCII flowchart:

```
l (dict)
    ↓
l["msgContent"].replace("\\r\\n", "").replace("\\n", "").replace("\\r", "")
    ↓
hash_function(l["characterID"]) + hash_function(L) + hash_function(l["chatID"]) + hash_function("")
    ↓
body_to_yy (str)
```

**Примеры**:

```python
body = get_body_to_yy({"msgContent": "test\nmessage", "characterID": "123", "chatID": "456"})
print(body) # Output: 'some_hash'
```

### `get_body_json`

```python
def get_body_json(s):
    return json.dumps(s, ensure_ascii=True, sort_keys=True)
```

**Назначение**: Функция `get_body_json` преобразует входной словарь в JSON-строку с обеспечением кодировки ASCII и сортировкой ключей.

**Параметры**:

- `s` (dict): Словарь, который необходимо преобразовать в JSON.

**Возвращает**:

- `str`: JSON-строка, представляющая входной словарь.

**Как работает функция**:

1.  Использует `json.dumps` для преобразования словаря `s` в JSON-строку.
2.  Устанавливает `ensure_ascii=True`, чтобы все не-ASCII символы были экранированы.
3.  Устанавливает `sort_keys=True`, чтобы ключи в JSON были отсортированы.
4.  Возвращает полученную JSON-строку.

ASCII flowchart:

```
s (dict)
    ↓
json.dumps(s, ensure_ascii=True, sort_keys=True)
    ↓
json_string (str)
```

**Примеры**:

```python
json_data = get_body_json({"key": "value", "another_key": 123})
print(json_data) # Output: '{"another_key": 123, "key": "value"}'
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
            const browser_platform = `${navigator.platform || "unknown"}`;\n            const screen_width = window.screen.width || "unknown";
            const screen_height = window.screen.height || "unknown";
            const unix = Date.now(); // Current Unix timestamp in milliseconds
            const params = {\n                device_platform: "web",\n                biz_id: 2,\n                app_id: 3001,\n                version_code: 22201,\n                lang: "en",\n                uuid,\n                device_id,\n                os_name,\n                browser_name,\n                cpu_core_num,\n                browser_language,\n                browser_platform,\n                screen_width,\n                screen_height,\n                unix\n            };\n            [new URLSearchParams(params).toString(), unix]\n        """)
        auth_result.path_and_query = f"{API_PATH}?{auth_result.path_and_query}"
    return callback
```

**Назначение**: Функция `get_browser_callback` создает асинхронную функцию обратного вызова, которая используется для получения данных из браузера, таких как токен авторизации, параметры устройства и временная метка.

**Параметры**:

- `auth_result` (CallbackResults): Объект класса `CallbackResults`, в котором будут сохранены результаты обратного вызова.

**Возвращает**:

- `callback` (async function): Асинхронная функция обратного вызова, которая принимает объект `page: Tab` и выполняет извлечение данных из браузера.

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
                const browser_platform = `${navigator.platform || "unknown"}`;\n                const screen_width = window.screen.width || "unknown";
                const screen_height = window.screen.height || "unknown";
                const unix = Date.now(); // Current Unix timestamp in milliseconds
                const params = {\n                    device_platform: "web",\n                    biz_id: 2,\n                    app_id: 3001,\n                    version_code: 22201,\n                    lang: "en",\n                    uuid,\n                    device_id,\n                    os_name,\n                    browser_name,\n                    cpu_core_num,\n                    browser_language,\n                    browser_platform,\n                    screen_width,\n                    screen_height,\n                    unix\n                };\n                [new URLSearchParams(params).toString(), unix]\n            """)
            auth_result.path_and_query = f"{API_PATH}?{auth_result.path_and_query}"
```

**Назначение**: Асинхронная функция обратного вызова, которая извлекает токен авторизации, параметры запроса и временную метку из браузера.

**Параметры**:

- `page` (Tab): Объект, представляющий вкладку браузера, из которой необходимо извлечь данные.

**Как работает функция**:

1.  В цикле ожидает, пока не будет получен токен авторизации из `localStorage` браузера.
2.  Извлекает параметры устройства, такие как ID устройства, UUID, имя ОС, имя браузера, количество ядер CPU, язык браузера, платформа браузера, ширина и высота экрана.
3.  Формирует параметры запроса на основе извлеченных данных.
4.  Получает временную метку Unix.
5.  Сохраняет путь и параметры запроса в объекте `auth_result`.
6.  Добавляет `API_PATH` к пути запроса.

ASCII flowchart:

```
auth_result (CallbackResults), page (Tab)
    ↓
while not auth_result.token:
    ↓
auth_result.token = await page.evaluate("localStorage.getItem('_token')")
    ↓
Extract device parameters from browser
    ↓
Create URLSearchParams from device parameters
    ↓
auth_result.path_and_query, auth_result.timestamp
    ↓
auth_result.path_and_query = f"{API_PATH}?{auth_result.path_and_query}"
```

**Примеры**:

```python
auth_result = CallbackResults()
callback = get_browser_callback(auth_result)
# Пример вызова callback функции (требуется интеграция с webdriver)
# await callback(page)