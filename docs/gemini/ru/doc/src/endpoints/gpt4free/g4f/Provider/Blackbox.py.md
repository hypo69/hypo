# Модуль Blackbox

## Обзор

Модуль `Blackbox` предоставляет класс `Blackbox`, который является асинхронным провайдером для взаимодействия с API Blackbox AI. Он поддерживает различные модели, включая модели для генерации текста и изображений, а также предоставляет механизмы для управления сессиями и проверки авторизации.

## Подробней

Модуль предназначен для интеграции с сервисом Blackbox AI, предоставляя удобный интерфейс для отправки запросов и получения ответов. Он включает в себя поддержку различных моделей, управление сессиями, проверку премиум-доступа и обработку изображений.

## Классы

### `Conversation`

**Описание**: Класс `Conversation` представляет собой структуру данных для хранения информации о текущем разговоре с Blackbox AI.

**Наследует**:

- `JsonConversation`: Расширяет класс `JsonConversation`, предоставляя функциональность для работы с JSON-форматом данных в контексте разговора.

**Атрибуты**:

- `validated_value` (str): Строка, содержащая проверенное значение, используемое для аутентификации или валидации запросов.
- `chat_id` (str): Уникальный идентификатор чата, используемый для отслеживания и управления разговором.
- `message_history` (Messages): Список сообщений, составляющих историю разговора.
- `model` (str): Модель, используемая в разговоре.

**Методы**:

- `__init__(self, model: str)`:
    - **Описание**: Конструктор класса `Conversation`.
    - **Параметры**:
        - `model` (str): Модель, используемая в разговоре.
    - **Как работает функция**:
        1. Инициализирует атрибут `model` экземпляра класса.

### `Blackbox`

**Описание**: Класс `Blackbox` предоставляет асинхронный интерфейс для взаимодействия с API Blackbox AI.

**Наследует**:

- `AsyncGeneratorProvider`: Расширяет класс `AsyncGeneratorProvider`, предоставляя функциональность для асинхронной генерации данных.
- `ProviderModelMixin`: Расширяет класс `ProviderModelMixin`, предоставляя функциональность для работы с моделями провайдера.

**Атрибуты**:

- `label` (str): Метка провайдера (Blackbox AI).
- `url` (str): URL главной страницы Blackbox AI.
- `api_endpoint` (str): URL API для чата Blackbox AI.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `default_model` (str): Модель, используемая по умолчанию ("blackboxai").
- `default_vision_model` (str): Модель для работы с изображениями по умолчанию.
- `default_image_model` (str): Модель для генерации изображений по умолчанию ('flux').
- `fallback_models` (list): Список моделей, используемых в случае отсутствия авторизации.
- `image_models` (list): Список моделей для работы с изображениями.
- `vision_models` (list): Список моделей для анализа изображений.
- `userSelectedModel` (list): Список моделей, выбранных пользователем.
- `agentMode` (dict): Конфигурация режимов агента для различных моделей.
- `trendingAgentMode` (dict): Конфигурация популярных режимов агента.
- `_all_models` (list): Полный список всех моделей (для авторизованных пользователей).
- `models` (list): Список моделей, доступных для использования (инициализируется `fallback_models`).
- `model_aliases` (dict): Словарь псевдонимов моделей.

**Методы**:

- `generate_session(cls, id_length: int = 21, days_ahead: int = 365) -> dict`
- `fetch_validated(cls, url: str = "https://www.blackbox.ai", force_refresh: bool = False) -> Optional[str]`
- `generate_id(cls, length: int = 7) -> str`
- `get_models(cls) -> list`
- `_check_premium_access(cls) -> bool`
- `generate_session(cls, id_length: int = 21, days_ahead: int = 365) -> dict`
- `fetch_validated(cls, url: str = "https://www.blackbox.ai", force_refresh: bool = False) -> Optional[str]`
- `generate_id(cls, length: int = 7) -> str`
- `async create_async_generator(...) -> AsyncResult`

## Функции

### `generate_session`

```python
    @classmethod
    def generate_session(cls, id_length: int = 21, days_ahead: int = 365) -> dict:
        """
        Generate a dynamic session with proper ID and expiry format.
        
        Args:
            id_length: Length of the numeric ID (default: 21)
            days_ahead: Number of days ahead for expiry (default: 365)
        
        Returns:
            dict: A session dictionary with user information and expiry
        """
        # Generate numeric ID
        numeric_id = ''.join(random.choice('0123456789') for _ in range(id_length))
        
        # Generate future expiry date
        future_date = datetime.now() + timedelta(days=days_ahead)
        expiry = future_date.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        
        # Decode the encoded email
        encoded_email = "Z2lzZWxlQGJsYWNrYm94LmFp"  # Base64 encoded email
        email = base64.b64decode(encoded_email).decode('utf-8')
        
        # Generate random image ID for the new URL format
        chars = string.ascii_letters + string.digits + "-"
        random_img_id = ''.join(random.choice(chars) for _ in range(48))
        image_url = f"https://lh3.googleusercontent.com/a/ACg8oc{random_img_id}=s96-c"
        
        return {
            "user": {
                "name": "BLACKBOX AI", 
                "email": email, 
                "image": image_url, 
                "id": numeric_id
            }, 
            "expires": expiry
        }
```

**Назначение**: Генерация динамической сессии с правильным идентификатором и форматом срока действия.

**Параметры**:

- `id_length` (int): Длина числового идентификатора (по умолчанию: 21).
- `days_ahead` (int): Количество дней до истечения срока действия (по умолчанию: 365).

**Возвращает**:

- `dict`: Словарь сессии с информацией о пользователе и сроке действия.

**Как работает функция**:

1. **Генерация числового идентификатора**:
   - Генерируется случайный числовой идентификатор указанной длины (`id_length`).

2. **Генерация даты истечения срока действия**:
   - Вычисляется дата истечения срока действия на основе текущей даты и количества дней (`days_ahead`).
   - Дата форматируется в строку в формате `YYYY-MM-DDTHH:MM:SS.fffZ`.

3. **Декодирование закодированной электронной почты**:
   - Закодированная строка электронной почты ("Z2lzZWxlQGJsYWNrYm94LmFp") декодируется из Base64 в UTF-8.

4. **Генерация случайного идентификатора изображения**:
   - Генерируется случайный идентификатор изображения для нового формата URL.

5. **Формирование словаря сессии**:
   - Формируется словарь, содержащий информацию о пользователе (имя, электронная почта, URL изображения, идентификатор) и сроке действия сессии.

```
    Генерация ID сессии
    │
    ├── Генерация числового ID
    │   │
    │   └── Генерация случайного числа длиной id_length
    │
    └── Генерация даты истечения сессии
        │
        ├── Вычисление даты истечения (текущая дата + days_ahead)
        │   │
        │   └── Форматирование даты в строку
        │
        └── Декодирование email
            │
            └── Декодирование email из base64
            │
            └── Генерация Image URL
                │
                └── Вычисление случайного id для image_url
                │
                └──  Формирование словаря сессии
```

**Примеры**:

```python
session_data = Blackbox.generate_session(id_length=25, days_ahead=400)
print(session_data)
# {'user': {'name': 'BLACKBOX AI', 'email': 'gisele@blackbox.ai', 'image': 'https://lh3.googleusercontent.com/a/ACg8oc...=s96-c', 'id': '...'}, 'expires': '...'}
```

---

### `fetch_validated`

```python
    @classmethod
    async def fetch_validated(cls, url: str = "https://www.blackbox.ai", force_refresh: bool = False) -> Optional[str]:
        cache_file = Path(get_cookies_dir()) / 'blackbox.json'
        
        if not force_refresh and cache_file.exists():
            try:
                with open(cache_file, 'r') as f:
                    data = json.load(f)
                    if data.get('validated_value'):
                        return data['validated_value']
            except Exception as e:
                debug.log(f"Blackbox: Error reading cache: {e}")
        
        js_file_pattern = r'static/chunks/\d{4}-[a-fA-F0-9]+\.js'
        uuid_pattern = r'["\']([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})["\']'

        def is_valid_context(text: str) -> bool:
            return any(char + '=' in text for char in 'abcdefghijklmnopqrstuvwxyz')

        async with ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status != 200:
                        return None

                    page_content = await response.text()
                    js_files = re.findall(js_file_pattern, page_content)

                for js_file in js_files:
                    js_url = f"{url}/_next/{js_file}"
                    async with session.get(js_url) as js_response:
                        if js_response.status == 200:
                            js_content = await js_response.text()
                            for match in re.finditer(uuid_pattern, js_content):
                                start = max(0, match.start() - 10)
                                end = min(len(js_content), match.end() + 10)
                                context = js_content[start:end]

                                if is_valid_context(context):
                                    validated_value = match.group(1)
                                    
                                    cache_file.parent.mkdir(exist_ok=True)
                                    try:
                                        with open(cache_file, 'w') as f:
                                            json.dump({'validated_value': validated_value}, f)
                                    except Exception as e:
                                        debug.log(f"Blackbox: Error writing cache: {e}")
                                        
                                    return validated_value

            except Exception as e:
                debug.log(f"Blackbox: Error retrieving validated_value: {e}")

        return None
```

**Назначение**: Получение проверенного значения из кэша или с веб-страницы.

**Параметры**:

- `url` (str): URL для получения данных (по умолчанию: "https://www.blackbox.ai").
- `force_refresh` (bool): Флаг, указывающий на необходимость принудительного обновления кэша (по умолчанию: `False`).

**Возвращает**:

- `Optional[str]`: Проверенное значение или `None` в случае ошибки.

**Как работает функция**:

1. **Проверка кэша**:
   - Проверяет наличие кэшированного файла `blackbox.json` в директории cookies.
   - Если файл существует и `force_refresh` равен `False`, пытается прочитать проверенное значение из файла.
   - В случае успеха возвращает значение из кэша.
   - В случае ошибки чтения кэша логирует ошибку.

2. **Поиск значения на веб-странице**:
   - Если кэш не найден или `force_refresh` равен `True`, выполняет следующие действия:
     - Формирует регулярные выражения для поиска JS-файлов и UUID на веб-странице.
     - Загружает содержимое веб-страницы по указанному URL.
     - Извлекает список JS-файлов из содержимого страницы.
     - Для каждого JS-файла:
       - Загружает содержимое JS-файла.
       - Ищет UUID в содержимом JS-файла.
       - Проверяет контекст найденного UUID на валидность.
       - Если контекст валиден, сохраняет UUID в кэш и возвращает его.

3. **Обработка ошибок**:
   - В случае ошибок при загрузке веб-страницы или JS-файлов логирует ошибки.

```
    Получение validated_value
    │
    ├── Проверка кэша (blackbox.json)
    │   │
    │   └── Чтение validated_value из кэша (если есть и не force_refresh)
    │   │
    │   └── Возврат validated_value из кэша
    │
    └── Получение validated_value с веб-страницы
        │
        ├── Загрузка содержимого веб-страницы
        │   │
        │   └── Поиск JS-файлов на странице
        │
        └── Для каждого JS-файла
            │
            ├── Загрузка содержимого JS-файла
            │   │
            │   └── Поиск UUID в JS-файле
            │   │
            │   └── Проверка контекста UUID на валидность
            │   │
            │   └── Сохранение UUID в кэш
            │   │
            │   └── Возврат validated_value
            │
            └── Обработка ошибок
```

**Примеры**:

```python
validated_value = await Blackbox.fetch_validated(force_refresh=True)
if validated_value:
    print(f"Validated value: {validated_value}")
else:
    print("Failed to fetch validated value.")
# Validated value: 123e4567-e89b-12d3-a456-426614174000
```

---

### `generate_id`

```python
    @classmethod
    def generate_id(cls, length: int = 7) -> str:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
```

**Назначение**: Генерация случайного идентификатора указанной длины.

**Параметры**:

- `length` (int): Длина идентификатора (по умолчанию: 7).

**Возвращает**:

- `str`: Случайный идентификатор.

**Как работает функция**:

1. **Определение набора символов**:
   - Определяется набор символов, включающий буквы ASCII и цифры.

2. **Генерация идентификатора**:
   - Генерируется случайный идентификатор путем выбора случайных символов из определенного набора указанное количество раз (`length`).

```
    Генерация ID
    │
    ├── Определение набора символов (буквы ASCII + цифры)
    │
    └── Генерация случайного ID
        │
        └── Выбор случайных символов из набора length раз
        │
        └── Объединение символов в строку
```

**Примеры**:

```python
random_id = Blackbox.generate_id(length=10)
print(random_id)
# 4a9b2c1d5e
```

---

### `get_models`

```python
    @classmethod
    def get_models(cls) -> list:
        """
        Returns a list of available models based on authorization status.
        Authorized users get the full list of models.
        Unauthorized users only get fallback_models.
        """
        # Check if there are valid session data in HAR files
        has_premium_access = cls._check_premium_access()
        
        if has_premium_access:
            # For authorized users - all models
            debug.log(f"Blackbox: Returning full model list with {len(cls._all_models)} models")
            return cls._all_models
        else:
            # For demo accounts - only free models
            debug.log(f"Blackbox: Returning free model list with {len(cls.fallback_models)} models")
            return cls.fallback_models
```

**Назначение**: Получение списка доступных моделей в зависимости от статуса авторизации пользователя.

**Возвращает**:

- `list`: Список доступных моделей.

**Как работает функция**:

1. **Проверка премиум-доступа**:
   - Вызывается метод `_check_premium_access()` для определения, имеет ли пользователь премиум-доступ.

2. **Формирование списка моделей**:
   - Если пользователь имеет премиум-доступ, возвращается полный список моделей (`cls._all_models`).
   - Если пользователь не имеет премиум-доступа, возвращается список fallback-моделей (`cls.fallback_models`).

```
    Получение списка моделей
    │
    ├── Проверка премиум-доступа
    │   │
    │   └── Вызов _check_premium_access()
    │
    └── Формирование списка моделей
        │
        ├── Если премиум-доступ:
        │   │
        │   └── Возврат _all_models
        │
        └── Иначе:
            │
            └── Возврат fallback_models
```

**Примеры**:

```python
models = Blackbox.get_models()
print(models)
# ['blackboxai', 'gpt-4o-mini', ...]
```

---

### `_check_premium_access`

```python
    @classmethod
    def _check_premium_access(cls) -> bool:
        """
        Checks for an authorized session in HAR files.
        Returns True if a valid session is found that differs from the demo.
        """
        try:
            har_dir = get_cookies_dir()
            if not os.access(har_dir, os.R_OK):
                return False
                
            for root, _, files in os.walk(har_dir):
                for file in files:
                    if file.endswith(".har"):
                        try:
                            with open(os.path.join(root, file), 'rb') as f:
                                har_data = json.load(f)
                                
                            for entry in har_data['log']['entries']