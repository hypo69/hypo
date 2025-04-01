# Модуль для работы с Blackbox AI
======================================

Модуль `Blackbox.py` предоставляет интерфейс для взаимодействия с сервисом Blackbox AI.
Он включает в себя функции для создания сессий, получения моделей, проверки премиум-доступа и создания асинхронных генераторов для обмена сообщениями с использованием различных моделей Blackbox AI.
Модуль поддерживает как текстовые, так и графические модели, а также интеграцию с HAR-файлами для сохранения и восстановления сессий.

## Обзор

Модуль предназначен для интеграции с платформой Blackbox AI, предоставляя возможности для создания сессий, получения списка доступных моделей (включая проверку премиум-доступа), а также обмена сообщениями с использованием асинхронных генераторов.
Поддерживаются как текстовые, так и графические модели, а также интеграция с HAR-файлами для сохранения и восстановления сессий.

## Подробнее

Этот модуль является ключевым компонентом для обеспечения взаимодействия с Blackbox AI в проекте `hypotez`.
Он реализует функциональность, необходимую для аутентификации, выбора моделей и отправки запросов к API Blackbox AI.
Модуль также содержит логику для обработки ответов от API, включая поддержку потоковой передачи данных и обработки изображений.

## Классы

### `Conversation`

**Описание**: Класс `Conversation` предназначен для хранения информации о текущем разговоре с Blackbox AI.

**Принцип работы**:
Класс `Conversation` наследуется от `JsonConversation` и предназначен для хранения состояния разговора, включая историю сообщений, идентификатор чата и модель, используемую в разговоре.
Он позволяет сохранять контекст беседы между запросами к API.

**Атрибуты**:
- `validated_value` (str): Валидированное значение, используемое для аутентификации.
- `chat_id` (str): Идентификатор чата.
- `message_history` (Messages): Список сообщений в истории разговора.
- `model` (str): Модель, используемая в разговоре.

**Методы**:
- `__init__(self, model: str)`: Конструктор класса.

     **Назначение**: Инициализирует экземпляр класса `Conversation`.

     **Параметры**:
     - `model` (str): Модель, используемая в разговоре.

     **Как работает функция**:
     1. Конструктор принимает параметр `model`, который определяет модель, используемую в разговоре.
     2. Устанавливает значение атрибута `model` экземпляра класса равным переданному значению.

### `Blackbox`

**Описание**: Класс `Blackbox` предоставляет методы для взаимодействия с API Blackbox AI.

**Принцип работы**:
Класс `Blackbox` наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin` и предоставляет методы для создания сессий, получения моделей, проверки премиум-доступа и создания асинхронных генераторов для обмена сообщениями с использованием различных моделей Blackbox AI.
Он поддерживает как текстовые, так и графические модели, а также интеграцию с HAR-файлами для сохранения и восстановления сессий.

**Атрибуты**:

- `label` (str): Метка провайдера, "Blackbox AI".
- `url` (str): URL сайта Blackbox AI, "https://www.blackbox.ai".
- `api_endpoint` (str): URL API Blackbox AI, "https://www.blackbox.ai/api/chat".
- `working` (bool): Флаг, указывающий, работает ли провайдер, `True`.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу, `True`.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения, `True`.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений, `True`.
- `default_model` (str): Модель, используемая по умолчанию, `"blackboxai"`.
- `default_vision_model` (str): Модель для работы с изображениями, `"blackboxai"`.
- `default_image_model` (str): Модель для генерации изображений, `'flux'`.
- `fallback_models` (list): Список бесплатных моделей.
- `image_models` (list): Список моделей для работы с изображениями.
- `vision_models` (list): Список моделей для анализа изображений.
- `userSelectedModel` (list): Список моделей, выбранных пользователем.
- `agentMode` (dict): Конфигурации для различных моделей в режиме агента.
- `trendingAgentMode` (dict): Конфигурации для популярных моделей в режиме агента.
- `_all_models` (list): Полный список моделей, доступных для авторизованных пользователей.
- `models` (list): Список моделей, используемых по умолчанию (совпадает с `fallback_models`).
- `model_aliases` (dict): Псевдонимы моделей.

**Методы**:

- `generate_session(cls, id_length: int = 21, days_ahead: int = 365) -> dict`
- `fetch_validated(cls, url: str = "https://www.blackbox.ai", force_refresh: bool = False) -> Optional[str]`
- `generate_id(cls, length: int = 7) -> str`
- `get_models(cls) -> list`
- `_check_premium_access(cls) -> bool`
- `create_async_generator(...) -> AsyncResult`

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
```

**Назначение**: Генерирует динамическую сессию с правильным идентификатором и форматом срока действия.

**Параметры**:
- `id_length` (int, optional): Длина числового идентификатора. По умолчанию 21.
- `days_ahead` (int, optional): Количество дней до истечения срока действия. По умолчанию 365.

**Возвращает**:
- `dict`: Словарь сессии с информацией о пользователе и сроком действия.

**Как работает функция**:

1. **Генерация числового идентификатора**: Создается числовой идентификатор заданной длины, используя случайный выбор из цифр.
2. **Генерация даты истечения срока действия**: Вычисляется дата истечения срока действия на основе текущей даты и заданного количества дней.
3. **Декодирование закодированной электронной почты**: Декодируется base64-закодированный email.
4. **Генерация случайного идентификатора изображения**: Создается случайный идентификатор изображения для нового формата URL.
5. **Создание словаря сессии**: Формируется словарь, содержащий информацию о пользователе (имя, email, URL изображения, идентификатор) и срок действия сессии.

**Примеры**:

```python
session = Blackbox.generate_session()
print(session)
# {'user': {'name': 'BLACKBOX AI', 'email': 'gisele@blackbox.ai', 'image': 'https://lh3.googleusercontent.com/a/ACg8oc...=s96-c', 'id': '...'}, 'expires': '...'}
```

### `fetch_validated`

```python
@classmethod
async def fetch_validated(cls, url: str = "https://www.blackbox.ai", force_refresh: bool = False) -> Optional[str]:
    """
    Args:
        url (str, optional): URL для получения данных. По умолчанию "https://www.blackbox.ai".
        force_refresh (bool, optional): Флаг для принудительного обновления кэша. По умолчанию False.

    Returns:
        Optional[str]: Валидированное значение или None в случае ошибки.
    """
```

**Назначение**: Извлекает валидированное значение с веб-страницы Blackbox AI.

**Параметры**:
- `url` (str, optional): URL для получения данных. По умолчанию "https://www.blackbox.ai".
- `force_refresh` (bool, optional): Флаг для принудительного обновления кэша. По умолчанию `False`.

**Возвращает**:
- `Optional[str]`: Валидированное значение или `None` в случае ошибки.

**Как работает функция**:

1. **Проверка кэша**: Проверяет, существует ли файл кэша и содержит ли он валидированное значение. Если да, возвращает его.
2. **Поиск JS-файлов**: Использует регулярное выражение для поиска JS-файлов на веб-странице.
3. **Извлечение UUID**: В каждом JS-файле ищет UUID, который соответствует определенному контексту.
4. **Кэширование значения**: Если UUID найден, сохраняет его в файл кэша.

**Примеры**:

```python
validated_value = await Blackbox.fetch_validated()
if validated_value:
    print(f"Валидированное значение: {validated_value}")
else:
    print("Не удалось получить валидированное значение.")
```

**Внутренние функции**:

- `is_valid_context(text: str) -> bool`:

     **Назначение**: Проверяет, является ли контекст валидным.

     **Параметры**:
     - `text` (str): Текст для проверки.

     **Возвращает**:
     - `bool`: `True`, если контекст валиден, иначе `False`.

     **Как работает функция**:
     1. Проверяет, содержит ли текст символы, за которыми следует знак равенства.

### `generate_id`

```python
@classmethod
def generate_id(cls, length: int = 7) -> str:
    """
    Args:
        length (int, optional): Длина генерируемого идентификатора. По умолчанию 7.

    Returns:
        str: Сгенерированный идентификатор.
    """
```

**Назначение**: Генерирует случайный идентификатор заданной длины.

**Параметры**:
- `length` (int, optional): Длина генерируемого идентификатора. По умолчанию 7.

**Возвращает**:
- `str`: Сгенерированный идентификатор.

**Как работает функция**:

1. **Определение набора символов**: Определяет набор символов, из которых будет состоять идентификатор (буквы и цифры).
2. **Генерация идентификатора**: Генерирует строку случайных символов из определенного набора заданной длины.

**Примеры**:

```python
id = Blackbox.generate_id()
print(id)  # Пример: "aB3cD5e"
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
```

**Назначение**: Возвращает список доступных моделей в зависимости от статуса авторизации пользователя.

**Возвращает**:
- `list`: Список доступных моделей.

**Как работает функция**:

1. **Проверка премиум-доступа**: Проверяет наличие премиум-доступа у пользователя.
2. **Возврат списка моделей**: Если у пользователя есть премиум-доступ, возвращает полный список моделей. В противном случае возвращает список бесплатных моделей.

**Примеры**:

```python
models = Blackbox.get_models()
print(models)
# Пример для авторизованных пользователей: ['blackboxai', 'gpt-4o', ...]
# Пример для неавторизованных пользователей: ['blackboxai', 'blackboxai-pro', ...]
```

### `_check_premium_access`

```python
@classmethod
def _check_premium_access(cls) -> bool:
    """
    Checks for an authorized session in HAR files.
    Returns True if a valid session is found that differs from the demo.
    """
```

**Назначение**: Проверяет наличие авторизованной сессии в HAR-файлах.

**Возвращает**:
- `bool`: `True`, если найдена валидная сессия, отличающаяся от демонстрационной, иначе `False`.

**Как работает функция**:

1. **Проверка доступа к каталогу HAR**: Проверяет наличие доступа на чтение к каталогу с HAR-файлами.
2. **Обход HAR-файлов**: Обходит все HAR-файлы в каталоге.
3. **Анализ HAR-данных**: Анализирует HAR-данные в поисках информации о сессии Blackbox AI.
4. **Проверка сессии**: Проверяет, является ли найденная сессия валидной и отличается ли она от демонстрационной.

**Примеры**:

```python
has_premium_access = Blackbox._check_premium_access()
if has_premium_access:
    print("У пользователя есть премиум-доступ.")
else:
    print("У пользователя нет премиум-доступа.")
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
    """
    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        prompt (str, optional): Дополнительный промпт. По умолчанию None.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию None.
        media (MediaListType, optional): Список медиа-файлов для отправки. По умолчанию None.
        top_p (float, optional): Параметр top_p. По умолчанию None.
        temperature (float, optional): Параметр temperature. По умолчанию None.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию None.
        conversation (Conversation, optional): Объект Conversation для продолжения разговора. По умолчанию None.
        return_conversation (bool, optional): Флаг для возврата объекта Conversation. По умолчанию False.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответа.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API Blackbox AI.

**Параметры**:
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `prompt` (str, optional): Дополнительный промпт. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `media` (MediaListType, optional): Список медиа-файлов для отправки. По умолчанию `None`.
- `top_p` (float, optional): Параметр `top_p`. По умолчанию `None`.
- `temperature` (float, optional): Параметр `temperature`. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию `None`.
- `conversation` (Conversation, optional): Объект `Conversation` для продолжения разговора. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг для возврата объекта `Conversation`. По умолчанию `False`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответа.

**Как работает функция**:

1. **Выбор модели**: Получает модель для использования.
2. **Создание или использование объекта `Conversation`**: Если объект `Conversation` не передан, создает новый.
3. **Формирование сообщений**: Формирует список сообщений для отправки.
4. **Добавление медиа-файлов**: Если переданы медиа-файлы, добавляет их в сообщение.
5. **Получение данных сессии**: Получает данные сессии из HAR-файлов или генерирует новую сессию.
6. **Формирование данных для запроса**: Формирует словарь данных для отправки в API Blackbox AI.
7. **Отправка запроса**: Отправляет POST-запрос к API Blackbox AI.
8. **Обработка ответа**: Обрабатывает ответ от API Blackbox AI и возвращает асинхронный генератор для получения данных.

**Примеры**:

```python
messages = [{"role": "user", "content": "Привет!"}]
async for chunk in Blackbox.create_async_generator(model="blackboxai", messages=messages):
    print(chunk, end="")
```
```python
messages = [{"role": "user", "content": "Нарисуй кота!"}]
async for chunk in Blackbox.create_async_generator(model="flux", messages=messages):
    print(chunk, end="")
```
```python
messages = [{"role": "user", "content": "What is the capital of France?"}]
async for chunk in Blackbox.create_async_generator(model="GPT-4o", messages=messages):
    print(chunk, end="")
```
```python
messages = [{"role": "user", "content": "Write a python script that prints numbers from 1 to 10"}]
async for chunk in Blackbox.create_async_generator(model="Python Agent", messages=messages):
    print(chunk, end="")
```
```python
from pathlib import Path
messages = [{"role": "user", "content": "Describe the image"}]
image_path = Path("./path/to/image.jpg")
async for chunk in Blackbox.create_async_generator(model="Gemini-PRO", messages=messages, media = [image_path]):
    print(chunk, end="")
```

```python
from pathlib import Path
messages = [{"role": "user", "content": "Describe the image"}]
image_path = Path("./path/to/image.jpg")
async for chunk in Blackbox.create_async_generator(model="Gemini Agent", messages=messages, media = [image_path]):
    print(chunk, end="")