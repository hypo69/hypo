# Модуль crypt.py

## Обзор

Модуль `crypt.py` предназначен для обеспечения криптографических функций, необходимых для взаимодействия с API mini_max. В частности, он содержит функции для генерации хешей, создания заголовков и обработки данных, используемых при запросах к API.

## Подробнее

Этот модуль содержит функции для работы с шифрованием и хешированием, что необходимо для обеспечения безопасности и целостности данных при взаимодействии с API mini_max. Он включает в себя функции для генерации MD5 хешей, создания специальных заголовков (`yy_header`) и обработки JSON-данных.

## Классы

### `CallbackResults`

**Описание**: Класс `CallbackResults` используется для хранения результатов обратного вызова (callback), содержащих токен авторизации, путь запроса и временную метку.

**Атрибуты**:

- `token` (str): Токен авторизации. Изначально установлен в `None`.
- `path_and_query` (str): Путь запроса с параметрами. Изначально установлен в `None`.
- `timestamp` (int): Временная метка. Изначально установлен в `None`.

## Функции

### `hash_function`

```python
def hash_function(base_string: str) -> str:
    """
    Mimics the hashFunction using MD5.
    """
    ...
```

**Назначение**: Функция `hash_function` генерирует MD5 хеш из входной строки.

**Параметры**:

- `base_string` (str): Строка, для которой необходимо сгенерировать хеш.

**Возвращает**:

- `str`: MD5 хеш входной строки в шестнадцатеричном формате.

**Как работает функция**:

1. Кодирует входную строку `base_string` в байты, используя кодировку UTF-8.
2. Вычисляет MD5 хеш закодированной строки.
3. Преобразует хеш в шестнадцатеричный формат.

```
base_string --> encode() --> hashlib.md5() --> hexdigest()
```

**Примеры**:

```python
>>> hash_function("test")
'098f6bcd4621d373cade4e832627b4f6'
```

### `generate_yy_header`

```python
def generate_yy_header(has_search_params_path: str, body_to_yy: dict, time: int) -> str:
    """
    Python equivalent of the generateYYHeader function.
    """
    ...
```

**Назначение**: Функция `generate_yy_header` генерирует специальный заголовок `yy_header`, используемый для аутентификации запросов.

**Параметры**:

- `has_search_params_path` (str): Путь с параметрами поиска.
- `body_to_yy` (dict): Словарь с данными тела запроса.
- `time` (int): Временная метка.

**Возвращает**:

- `str`: Сгенерированный заголовок `yy_header`.

**Как работает функция**:

1. Кодирует `has_search_params_path` с использованием `urllib.parse.quote`.
2. Вычисляет хеш от временной метки `time`.
3. Объединяет закодированный путь, тело запроса и хеш временной метки в одну строку.
4. Вычисляет MD5 хеш объединенной строки.

```
has_search_params_path --> quote()
time --> hash_function()
encoded_path, body_to_yy, time_hash --> combine --> hash_function()
```

**Примеры**:

```python
>>> generate_yy_header("/api/chat", {"key": "value"}, 1678886400)
'e38a94bb966a3b0c572d609961bca46d'
```

### `get_body_to_yy`

```python
def get_body_to_yy(l):
    L = l["msgContent"].replace("\\r\\n", "").replace("\\n", "").replace("\\r", "")
    M = hash_function(l["characterID"]) + hash_function(L) + hash_function(l["chatID"])\
        + hash_function("")  # Mimics hashFunction(undefined) in JS

    # print("bodyToYY:", M)
    return M
```

**Назначение**: Функция `get_body_to_yy` формирует строку `bodyToYY` на основе содержимого сообщения и идентификаторов чата и пользователя.

**Параметры**:

- `l` (dict): Словарь, содержащий ключи `"msgContent"`, `"characterID"` и `"chatID"`.

**Возвращает**:

- `str`: Сгенерированная строка `bodyToYY`.

**Как работает функция**:

1. Извлекает `"msgContent"` из входного словаря `l` и удаляет символы переноса строки (`\r\n`, `\n`, `\r`).
2. Вычисляет хеши для `"characterID"`, обработанного `"msgContent"` и `"chatID"`.
3. Конкатенирует полученные хеши вместе с хешем пустой строки.

```
l["msgContent"] --> replace() --> L
l["characterID"] --> hash_function()
L --> hash_function()
l["chatID"] --> hash_function()
"" --> hash_function()
hash1, hash2, hash3, hash4 --> concatenate
```

**Примеры**:

```python
>>> get_body_to_yy({"msgContent": "test message", "characterID": "user123", "chatID": "chat456"})
'хеш_user123хеш_сообщенияхеш_chat456d41d8cd98f00b204e9800998ecf8427e'
```

### `get_body_json`

```python
def get_body_json(s):
    return json.dumps(s, ensure_ascii=True, sort_keys=True)
```

**Назначение**: Функция `get_body_json` преобразует входной словарь в JSON-строку с определенными параметрами.

**Параметры**:

- `s` (dict): Словарь, который необходимо преобразовать в JSON.

**Возвращает**:

- `str`: JSON-представление входного словаря.

**Как работает функция**:

1. Преобразует входной словарь `s` в JSON-строку.
   - `ensure_ascii=True` гарантирует, что все не-ASCII символы будут экранированы.
   - `sort_keys=True` сортирует ключи словаря перед преобразованием в JSON.

```
s --> json.dumps(ensure_ascii=True, sort_keys=True)
```

**Примеры**:

```python
>>> get_body_json({"key": "value", "number": 123})
'{"key": "value", "number": 123}'
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
            const params = {
                device_platform: "web",
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
            };
            [new URLSearchParams(params).toString(), unix]
        """)
        auth_result.path_and_query = f"{API_PATH}?{auth_result.path_and_query}"
    return callback
```

**Назначение**: Функция `get_browser_callback` создает асинхронную функцию обратного вызова, которая извлекает токен авторизации, путь запроса и временную метку из браузера.

**Параметры**:

- `auth_result` (CallbackResults): Объект `CallbackResults`, в котором будут сохранены результаты обратного вызова.

**Возвращает**:

- `callback` (async function): Асинхронная функция обратного вызова.

**Как работает функция**:

1. Определяет внутреннюю асинхронную функцию `callback`, которая принимает объект `page` (вкладку браузера).
2. В цикле ожидает, пока не будет получен токен авторизации из `localStorage` браузера.
3. Извлекает параметры устройства и пользователя из браузера (идентификатор устройства, UUID, имя ОС, имя браузера, количество ядер CPU, язык браузера, платформа браузера, ширина и высота экрана) через JavaScript код, выполняемый в браузере.
4. Формирует строку запроса на основе полученных параметров и добавляет её к `API_PATH`.
5. Сохраняет полученные значения в объект `auth_result`.

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
            const params = {
                device_platform: "web",
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
            };
            [new URLSearchParams(params).toString(), unix]
        """)
        auth_result.path_and_query = f"{API_PATH}?{auth_result.path_and_query}"
```

**Назначение**: Асинхронная функция обратного вызова, которая извлекает токен авторизации, путь запроса и временную метку из браузера.

**Параметры**:

- `page` (Tab): Объект `Tab`, представляющий вкладку браузера.

**Как работает функция**:

1. В цикле ожидает, пока не будет получен токен авторизации из `localStorage` браузера.
2. Извлекает параметры устройства и пользователя из браузера через JavaScript код, выполняемый в браузере.
3. Формирует строку запроса на основе полученных параметров и добавляет её к `API_PATH`.
4. Сохраняет полученные значения в объект `auth_result`.

```
Ждем получения токена из localStorage --> Извлекаем параметры устройства и пользователя через JS --> Формируем строку запроса --> Сохраняем значения в auth_result
```
```
  Начало
  │
  ├───Ждем получения токена из localStorage
  │   │
  │   └───Токен получен?
  │       ├───Да: Продолжаем
  │       └───Нет: Ждем 1 секунду и повторяем
  │
  │
  └───Извлекаем параметры устройства и пользователя через JS
      │
      └───Формируем строку запроса
          │
          └───Сохраняем значения в auth_result
```

**Примеры**:

```python
# Пример использования функции get_browser_callback
auth_result = CallbackResults()
callback_function = get_browser_callback(auth_result)
# Далее callback_function можно использовать с объектом page (вкладкой браузера)