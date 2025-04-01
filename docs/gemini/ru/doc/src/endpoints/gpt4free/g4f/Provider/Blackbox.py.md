# Модуль Blackbox.py

## Обзор

Модуль `Blackbox.py` предоставляет реализацию асинхронного провайдера для взаимодействия с сервисом Blackbox AI. Он включает в себя функциональность для генерации сессий, получения валидированных значений, управления моделями (включая модели изображений и агентов), а также для создания асинхронных генераторов для обработки сообщений и изображений.

## Подробнее

Модуль предназначен для интеграции с API Blackbox AI, обеспечивая поддержку различных моделей и режимов работы, включая агентов и генерацию изображений. Он также включает механизмы для проверки премиум-доступа на основе данных HAR-файлов. Модуль активно использует кэширование для повышения эффективности и предоставляет гибкие возможности для настройки сессий и управления моделями.

## Классы

### `Conversation`

**Описание**: Класс `Conversation` представляет собой структуру данных для хранения информации о текущем разговоре с Blackbox AI. Он расширяет класс `JsonConversation` и содержит атрибуты для хранения идентификатора чата, истории сообщений и валидированного значения.

**Наследует**:

- `JsonConversation`: Предоставляет базовую структуру для управления разговорами в формате JSON.

**Атрибуты**:

- `validated_value` (str, optional): Валидированное значение для текущего разговора.
- `chat_id` (str, optional): Идентификатор текущего чата.
- `message_history` (Messages, optional): История сообщений в текущем чате.
- `model` (str): Модель, используемая в текущем разговоре.

**Методы**:

- `__init__(model: str)`: Инициализирует новый объект разговора с указанной моделью.

### `Blackbox`

**Описание**: Класс `Blackbox` предоставляет асинхронный генератор для взаимодействия с API Blackbox AI. Он поддерживает различные модели, включая модели изображений и агентов, и предоставляет функциональность для генерации сессий, получения валидированных значений и проверки премиум-доступа.

**Наследует**:

- `AsyncGeneratorProvider`: Обеспечивает базовую структуру для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для управления моделями.

**Атрибуты**:

- `label` (str): Метка провайдера ("Blackbox AI").
- `url` (str): URL сервиса Blackbox AI ("https://www.blackbox.ai").
- `api_endpoint` (str): URL API Blackbox AI ("https://www.blackbox.ai/api/chat").
- `working` (bool): Указывает, работает ли провайдер (True).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу (True).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (True).
- `default_model` (str): Модель, используемая по умолчанию ("blackboxai").
- `default_vision_model` (str): Модель для обработки изображений по умолчанию (default_model).
- `default_image_model` (str): Модель генерации изображений по умолчанию ('flux').
- `fallback_models` (list): Список бесплатных моделей, используемых по умолчанию.
- `image_models` (list): Список моделей для генерации изображений.
- `vision_models` (list): Список моделей для обработки изображений.
- `userSelectedModel` (list): Список моделей, выбранных пользователем.
- `agentMode` (dict): Конфигурации для режима агента.
- `trendingAgentMode` (dict): Конфигурации для популярных режимов агента.
- `_all_models` (list): Полный список всех моделей (для авторизованных пользователей).
- `models` (list): Список моделей, инициализированных с использованием fallback_models.
- `model_aliases` (dict): Псевдонимы моделей для удобства использования.

**Методы**:

- `generate_session(id_length: int = 21, days_ahead: int = 365) -> dict`: Генерирует динамическую сессию с правильным ID и форматом истечения срока действия.
- `fetch_validated(url: str = "https://www.blackbox.ai", force_refresh: bool = False) -> Optional[str]`: Получает валидированное значение из кэша или с веб-сайта Blackbox AI.
- `generate_id(length: int = 7) -> str`: Генерирует случайный идентификатор указанной длины.
- `get_models() -> list`: Возвращает список доступных моделей в зависимости от статуса авторизации.
- `_check_premium_access() -> bool`: Проверяет наличие авторизованной сессии в HAR-файлах.
- `create_async_generator(model: str, messages: Messages, prompt: str = None, proxy: str = None, media: MediaListType = None, top_p: float = None, temperature: float = None, max_tokens: int = None, conversation: Conversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с API Blackbox AI.

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

**Назначение**: Генерирует динамическую сессию с правильным ID и форматом истечения срока действия для Blackbox AI.

**Параметры**:

- `id_length` (int, optional): Длина числового ID. По умолчанию 21.
- `days_ahead` (int, optional): Количество дней до истечения срока действия. По умолчанию 365.

**Возвращает**:

- `dict`: Словарь, содержащий информацию о пользователе и сроке действия сессии.

**Как работает функция**:

1.  **Генерация числового ID**: Функция генерирует числовой ID заданной длины, выбирая случайные цифры.
2.  **Генерация даты истечения срока действия**: Вычисляет дату истечения срока действия на основе текущей даты и заданного количества дней.
3.  **Декодирование закодированной электронной почты**: Декодирует base64-закодированный email.
4.  **Генерация случайного ID изображения**: Генерирует случайный ID изображения для нового формата URL.
5.  **Формирование словаря сессии**: Собирает все сгенерированные данные в словарь, который содержит информацию о пользователе (имя, email, URL изображения, ID) и сроке действия сессии.

**ASCII Flowchart**:

```
    Генерация числового ID (numeric_id)
    │
    └──> Генерация даты истечения срока действия (expiry)
    │
    └──> Декодирование email (email)
    │
    └──> Генерация случайного ID изображения (random_img_id) и формирование URL изображения (image_url)
    │
    └──> Формирование словаря сессии с информацией о пользователе и сроке действия
```

**Примеры**:

```python
session = Blackbox.generate_session()
print(session)
# {'user': {'name': 'BLACKBOX AI', 'email': 'gisele@blackbox.ai', 'image': 'https://lh3.googleusercontent.com/a/ACg8oc...=s96-c', 'id': '...'}, 'expires': '2024-07-06T14:22:12.345Z'}

session = Blackbox.generate_session(id_length=10, days_ahead=100)
print(session)
# {'user': {'name': 'BLACKBOX AI', 'email': 'gisele@blackbox.ai', 'image': 'https://lh3.googleusercontent.com/a/ACg8oc...=s96-c', 'id': '...'}, 'expires': '2024-01-27T14:22:12.345Z'}
```

### `fetch_validated`

```python
    @classmethod
    async def fetch_validated(cls, url: str = "https://www.blackbox.ai", force_refresh: bool = False) -> Optional[str]:
        """
        fetch_validated
        """
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

**Назначение**: Получает валидированное значение из кэша или с веб-сайта Blackbox AI.

**Параметры**:

- `url` (str, optional): URL для получения валидированного значения. По умолчанию "https://www.blackbox.ai".
- `force_refresh` (bool, optional): Флаг, указывающий на необходимость принудительного обновления кэша. По умолчанию False.

**Возвращает**:

- `Optional[str]`: Валидированное значение или None в случае ошибки.

**Как работает функция**:

1.  **Проверка кэша**: Функция проверяет наличие кэшированного значения в файле `blackbox.json`. Если значение найдено и `force_refresh` равен False, функция возвращает кэшированное значение.
2.  **Поиск JavaScript файлов**: Если кэш не найден или требуется принудительное обновление, функция загружает содержимое веб-страницы и ищет ссылки на JavaScript файлы, соответствующие определенному шаблону.
3.  **Извлечение UUID**: Функция загружает содержимое каждого найденного JavaScript файла и ищет UUID (Universally Unique Identifier), соответствующие определенному шаблону.
4.  **Валидация контекста**: Функция проверяет контекст каждого найденного UUID, чтобы убедиться, что он является валидным.
5.  **Кэширование значения**: Если валидированное значение найдено, функция сохраняет его в кэш-файл.

**Внутренние функции**:

- `is_valid_context(text: str) -> bool`:
    - **Назначение**: Проверяет, является ли контекст валидным.
    - **Параметры**:
        - `text` (str): Проверяемый текст.
    - **Возвращает**:
        - `bool`: True, если контекст валиден, иначе False.
    - **Как работает функция**:
        - Функция проверяет, содержит ли текст хотя бы один символ из алфавита (a-z) с последующим символом "=".

**ASCII Flowchart**:

```
    Проверка кэша (cache_file.exists())
    │
    └──> Чтение из кэша (чтение validated_value из файла)
    │   │
    │   └──> Возврат значения из кэша
    │
    └──> Запрос веб-страницы (session.get(url))
    │
    └──> Поиск JS файлов (re.findall(js_file_pattern, page_content))
    │
    └──> Для каждого JS файла:
    │   │
    │   └──> Запрос JS файла (session.get(js_url))
    │   │
    │   └──> Поиск UUID (re.finditer(uuid_pattern, js_content))
    │   │
    │   └──> Для каждого UUID:
    │       │
    │       └──> Валидация контекста (is_valid_context(context))
    │       │
    │       └──> Кэширование значения (сохранение validated_value в файл)
    │       │
    │       └──> Возврат validated_value
    │
    └──> Возврат None (если не найдено)
```

**Примеры**:

```python
validated_value = await Blackbox.fetch_validated()
print(validated_value)
# 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

validated_value = await Blackbox.fetch_validated(force_refresh=True)
print(validated_value)
# 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
```

### `generate_id`

```python
    @classmethod
    def generate_id(cls, length: int = 7) -> str:
        """
        generate_id
        """
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
```

**Назначение**: Генерирует случайный идентификатор указанной длины.

**Параметры**:

- `length` (int, optional): Длина генерируемого идентификатора. По умолчанию 7.

**Возвращает**:

- `str`: Случайный идентификатор.

**Как работает функция**:

1.  **Определение набора символов**: Функция определяет набор символов, из которых будет состоять идентификатор (буквы и цифры).
2.  **Генерация идентификатора**: Функция генерирует случайный идентификатор заданной длины, выбирая случайные символы из определенного набора.

**ASCII Flowchart**:

```
    Определение набора символов (chars)
    │
    └──> Генерация идентификатора (случайный выбор символов)
    │
    └──> Возврат идентификатора
```

**Примеры**:

```python
id = Blackbox.generate_id()
print(id)
# 'aBc1De2'

id = Blackbox.generate_id(length=10)
print(id)
# 'fGh3Ij4Kl5'
```

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

**Назначение**: Возвращает список доступных моделей в зависимости от статуса авторизации пользователя.

**Параметры**:

- Нет

**Возвращает**:

- `list`: Список доступных моделей.

**Как работает функция**:

1.  **Проверка премиум-доступа**: Функция проверяет наличие премиум-доступа у пользователя, используя метод `_check_premium_access`.
2.  **Возврат списка моделей**: Если у пользователя есть премиум-доступ, функция возвращает полный список моделей (`_all_models`). В противном случае функция возвращает список бесплатных моделей (`fallback_models`).

**ASCII Flowchart**:

```
    Проверка премиум-доступа (_check_premium_access())
    │
    └──> Если премиум-доступ:
    │   │
    │   └──> Возврат полного списка моделей (_all_models)
    │
    └──> Иначе:
    │   │
    │   └──> Возврат списка бесплатных моделей (fallback_models)
```

**Примеры**:

```python
models = Blackbox.get_models()
print(models)
# ['blackboxai', 'gpt-4o-mini', 'GPT-4o', ...]
```

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
                                
                            for entry in har_data['log']['entries']:
                                # Only check requests to blackbox API
                                if 'blackbox.ai/api' in entry['request']['url']:
                                    if 'response' in entry and 'content' in entry['response']:
                                        content = entry['response']['content']
                                        if ('text' in content and 
                                            isinstance(content['text'], str) and 
                                            '"user"' in content['text'] and 
                                            '"email"' in content['text']):
                                            
                                            try:
                                                # Process request text
                                                text = content['text'].strip()
                                                if text.startswith('{') and text.endswith('}'):
                                                    text = text.replace('\\"', '"')
                                                    session_data = json.loads(text)
                                                    
                                                    # Check if this is a valid session
                                                    if (isinstance(session_data, dict) and 
                                                        'user' in session_data and 
                                                        'email' in session_data['user']):
                                                        
                                                        # Check if this is not a demo session
                                                        demo_session = cls.generate_session()
                                                        if (session_data['user'].get('email') != 
                                                            demo_session['user'].get('email')):
                                                            # This is not a demo session, so user has premium access
                                                            return True
                                            except:
                                                pass
                        except:
                            pass
            return False
        except Exception as e:
            debug.log(f"Blackbox: Error checking premium access: {e}")
            return False
```

**Назначение**: Проверяет наличие авторизованной сессии в HAR-файлах.

**Параметры**:

- Нет

**Возвращает**:

- `bool`: True, если найдена валидная сессия, отличающаяся от демонстрационной, иначе False.

**Как работает функция**:

1.  **Получение директории HAR-файлов**: Функция получает путь к директории, где хранятся HAR-файлы.
2.  **Проверка доступа к директории**: Проверяет, есть ли у процесса права на чтение директории. Если нет, возвращает False.
3.  **Перебор HAR-файлов**: Функция перебирает все HAR-файлы в указанной директории.
4.  **Анализ HAR-файлов**: Для каждого HAR-файла функция пытается извлечь информацию о сессии из HTTP-ответов, фильтруя запросы к API Blackbox.
5.  **Проверка данных сессии**: Функция проверяет, является ли найденная сессия валидной и отличается ли она от демонстрационной сессии, сгенерированной с помощью `generate_session`.
6.  **Возврат результата**: Если найдена валидная сессия, отличающаяся от демонстрационной, функция возвращает True, иначе False.

**ASCII Flowchart**:

```
    Получение директории HAR-файлов (get_cookies_dir())
    │
    └──> Проверка доступа к директории (os.access(har_dir, os.R_OK))
    │
    └──> Перебор HAR-файлов (os.walk(har_dir))
    │
    └──> Для каждого HAR-файла:
    │   │
    │   └──> Чтение данных из HAR-файла (json.load(f))
    │   │
    │   └──> Перебор записей в HAR-файле (har_data['log']['entries'])
    │   │
    │   └──> Для каждой записи:
    │       │
    │       └──> Проверка URL запроса ( 'blackbox.ai/api' in entry['request']['url'])
    │       │
    │       └──> Извлечение данных сессии из ответа
    │       │
    │       └──> Проверка валидности сессии (наличие 'user' и 'email')
    │       │
    │       └──> Сравнение с демонстрационной сессией (session_data['user'].get('email') != demo_session['user'].get('email'))
    │       │
    │       └──> Если сессия валидна и отличается от демонстрационной:
    │           │
    │           └──> Возврат True
    │
    └──> Если валидная сессия не найдена:
    │
    └──> Возврат False
```

**Примеры**:

```python
has_premium_access = Blackbox._check_premium_access()
print(has_premium_access)
# True или False в зависимости от наличия премиум-доступа
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        prompt: str = None,
        proxy: str = None,
        media: MediaListType = None,
        top_p: float = None,
        temperature: float = None,
        max_tokens: int = None,
        conversation: Conversation = None,
        return_conversation: bool = False,
        **kwargs
    ) -> AsyncResult:      
        model = cls.get_model(model)
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.blackbox.ai',
            'referer': 'https://www.blackbox.ai/',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
        
        async with ClientSession(headers=headers) as session:
            if conversation is None or not hasattr(conversation, "chat_id"):
                conversation = Conversation(model)
                conversation.validated_value = await cls.fetch_validated()
                conversation.chat_id = cls.generate_id()
                conversation.message_history = []

            current_messages = []
            for i, msg in enumerate(messages):
                msg_id = conversation.chat_id if i == 0 and msg["role"] == "user" else cls.generate_id()
                current_msg = {
                    "id": msg_id,
                    "content": msg["content"],
                    "role": msg["role"]
                }
                current_messages.append(current_msg)

            if media is not None:
                current_messages[-1]['data'] = {
                    "imagesData": [
                        {
                            "filePath": f"/{image_name}",
                            "contents": to_data_uri(image)
                        }
                        for image, image_name in merge_media(media, messages)
                    ],
                    "fileText": "",
                    "title": ""
                }

            # Try to get session data from HAR files
            session_data = cls.generate_session()  # Default fallback
            session_found = False

            # Look for HAR session data
            har_dir = get_cookies_dir()
            if os.access(har_dir, os.R_OK):
                for root, _, files in os.walk(har_dir):
                    for file in files:
                        if file.endswith(".har"):
                            try:
                                with open(os.path.join(root, file), 'rb') as f:
                                    har_data = json.load(f)
                                    
                                for entry in har_data['log']['entries']:
                                    # Only look at blackbox API responses
                                    if 'blackbox.ai/api' in entry['request']['url']:
                                        # Look for a response that has the right structure
                                        if 'response' in entry and 'content' in entry['response']:
                                            content = entry['response']['content']
                                            # Look for both regular and Google auth session formats
                                            if ('text' in content and 
                                                isinstance(content['text'], str) and 
                                                '"user"' in content['text'] and 
                                                '"email"' in content['text'] and
                                                '"expires"' in content['text']):
                                                
                                                try:
                                                    # Remove any HTML or other non-JSON content
                                                    text = content['text'].strip()
                                                    if text.startswith('{') and text.endswith('}'):
                                                        # Replace escaped quotes
                                                        text = text.replace('\\"', '"')
                                                        har_session = json.loads(text)
                                                        
                                                        # Check if this is a valid session object (supports both regular and Google auth)
                                                        if (isinstance(har_session, dict) and 
                                                            'user' in har_session and 
                                                            'email' in har_session['user'] and
                                                            'expires' in har_session):
                                                            
                                                            file_path = os.path.join(root, file)
                                                            debug.log(f"Blackbox: Found session in HAR file")
                                                            
                                                            session_data = har_session
                                                            session_found = True
                                                            break
                                                except json.JSONDecodeError as e:
                                                    # Only print error for entries that truly look like session data
                                                    if ('"user"' in content['text'] and 
                                                        '"email"' in content['text']):
                                                        debug.log(f"Blackbox: Error parsing likely session data: {e}")
                                        
                                    if session_found:
                                        break
                                        
                            except Exception as e:
                                debug.log(f"Blackbox: Error reading HAR file: {e}")
                            
                            if session_found:
                                break
                                
                    if session_found:
                        break

            data = {
                "messages": current_messages,
                "agentMode": cls.agentMode.get(model, {}) if model in cls.agentMode else {},
                "id": conversation.chat_id,
                "previewToken": None,
                "userId": None,
                "codeModelMode": True,
                "trendingAgentMode": cls.trendingAgentMode.get(model, {}) if model in cls.trendingAgentMode else {},
                "isMicMode": False,
                "userSystemPrompt": None,
                "maxTokens": max_tokens,
                "playgroundTopP": top_p,
                "playgroundTemperature": temperature,
                "isChromeExt": False,
                "githubToken": "",
                "clickedAnswer2": False,
                "clickedAnswer3": False,
                "clickedForceWebSearch": False,
                "visitFromDelta": False,
                "isMemoryEnabled": False,
                "mobileClient": False,
                "userSelectedModel": model if model in cls.userSelectedModel else None,
                "validated": conversation.validated_value,
                "imageGenerationMode": model == cls.default_image_model,
                "webSearchModePrompt": False,
                "deepSearchMode": False,
                "domains": None,
                "vscodeClient": False,
                "codeInterpreterMode": False,
                "customProfile": {
                    "name": "",
                    "occupation": "",
                    "traits": [],
                    "additionalInfo": "",
                    "enableNewChats": False
                },
                "session": session_data if session_data else cls.generate_session(),
                "isPremium": True, 
                "subscriptionCache": None,
                "beastMode": False,
                "webSearchMode": False
            }

            # Add debugging before making the API call
            if isinstance(session_data, dict) and 'user' in session_data:
                # Генеруємо демо-сесію для порівняння
                demo_session = cls.generate_session()
                is_demo = False
                
                if demo_session and isinstance(demo_session, dict) and 'user' in demo_session:
                    if session_data['user'].get('email') == demo_session['user'].get('email'):
                        is_demo = True
                
                if is_demo:
                    debug.log(f"Blackbox: Making API request with built-in Developer Premium Account")
                else:
                    user_email = session_data['user'].get('email', 'unknown')
                    debug.log(f"Blackbox: Making API request with HAR session email: {user_email}")
                
            # Continue with the API request and async generator behavior
            async with session.post(cls.api_endpoint, json=data, proxy=proxy) as response:
                await raise_for_status(response)
                
                # Collect the full response
                full_response = []
                async for chunk in response.content.iter_any():
                    if chunk:
                        chunk_text = chunk.decode()
                        full_response.append(chunk_text)
                        # Only yield chunks for non-image models
                        if model != cls.default_image_model:
                            yield chunk_text
                
                full_response_text = ''.join(full_response)
                
                # For image models, check for image markdown
                if model == cls.default_image_model:
                    image_url_match = re.search(r'!\\[.*?\\]\\((.*?)\\)\', full_response_text)
                    if image_url_match:
                        image_url = image_url_match.group(1)
                        yield ImageResponse(images=[image_url], alt=format_image_prompt(messages, prompt))
                        return
                
                # Handle conversation history once, in one place
                if return_conversation:
                    conversation.message_history.append({"role": "assistant", "content": full_response_text})
                    yield conversation
                # For image models that didn't produce an image, fall back to text response
                elif model == cls.default_image_model:
                    yield full_response_text
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API Blackbox AI.

**Параметры**:

- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `prompt` (str, optional): Дополнительный промпт. По умолчанию None.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию None.
- `media` (MediaListType, optional): Список медиафайлов для отправки. По умолчанию None.
- `top_p` (float, optional): Значение top_p. По умолчанию None.
- `temperature` (float, optional): Значение temperature. По умолчанию None.
- `max_tokens` (int, optional): Максимальное количество