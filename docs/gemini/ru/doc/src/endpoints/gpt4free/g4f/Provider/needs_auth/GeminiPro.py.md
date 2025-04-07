# Модуль для работы с Google Gemini API (GeminiPro)

## Обзор

Модуль `GeminiPro.py` предоставляет асинхронный интерфейс для взаимодействия с API Google Gemini, включая поддержку потоковой передачи данных, мультимодальных запросов (текст и изображения) и использования инструментов (tools). Этот модуль предназначен для интеграции с другими частями проекта `hypotez`, требующими функциональности обработки естественного языка и генерации контента на основе моделей Gemini. Он поддерживает различные модели, включая `gemini-1.5-pro`, `gemini-2.0-flash-exp`, `gemini-pro` и другие.

## Подробнее

Модуль обеспечивает асинхронное взаимодействие с API Google Gemini, поддерживая как потоковую передачу данных, так и отправку мультимодальных запросов (текст и изображения). Он также предоставляет возможность использовать инструменты (tools) для расширения функциональности модели.

Расположение файла в структуре проекта указывает на его роль как одного из провайдеров (источников) для получения ответов от языковых моделей. Он находится в подкаталоге `needs_auth`, что говорит о необходимости авторизации для использования этого провайдера.

## Классы

### `GeminiPro`

**Описание**: Класс `GeminiPro` реализует асинхронного провайдера для Google Gemini API.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Добавляет методы для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера ("Google Gemini API").
- `url` (str): URL главной страницы Google AI.
- `login_url` (str): URL для получения API-ключа.
- `api_base` (str): Базовый URL API Gemini.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений.
- `needs_auth` (bool): Флаг, указывающий на необходимость авторизации.
- `default_model` (str): Модель, используемая по умолчанию ("gemini-1.5-pro").
- `default_vision_model` (str): Модель для обработки изображений, используемая по умолчанию.
- `fallback_models` (list[str]): Список запасных моделей.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `get_models`: Возвращает список доступных моделей Gemini.
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с API Gemini.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, api_key: str = None, api_base: str = api_base) -> list[str]:
    """
    Возвращает список доступных моделей Gemini.

    Args:
        api_key (str, optional): API-ключ для Google Gemini. Defaults to None.
        api_base (str, optional): Базовый URL API. Defaults to api_base.

    Returns:
        list[str]: Список доступных моделей.

    Raises:
        MissingAuthError: Если `api_key` недействителен.
    """
```

**Назначение**: Получает список доступных моделей Gemini API. Если список моделей уже был получен ранее, возвращает закэшированный результат. В случае ошибки при получении списка моделей возвращает список запасных моделей.

**Параметры**:
- `api_key` (str, optional): API-ключ для доступа к Google Gemini API. Если не указан, используется `fallback_models`. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL API Gemini. По умолчанию использует атрибут класса `api_base`.

**Возвращает**:
- `list[str]`: Список доступных моделей Gemini API.

**Вызывает исключения**:
- `MissingAuthError`: Если предоставлен недействительный `api_key`.

**Как работает функция**:

1. **Проверка кэша**: Сначала проверяет, были ли уже получены модели ранее (хранятся в `cls.models`). Если да, возвращает закэшированный список.
2. **Формирование URL**: Если модели не закэшированы, формирует URL для запроса списка моделей, используя `api_base` и `api_key`.
3. **Выполнение запроса**: Отправляет GET-запрос к API для получения списка моделей.
4. **Обработка ответа**:
   - В случае успешного ответа (код 200):
     - Извлекает имена моделей из JSON-ответа.
     - Фильтрует модели, оставляя только те, которые поддерживают метод `generateContent`.
     - Сортирует список моделей.
     - Сохраняет список моделей в `cls.models` для последующего кэширования.
   - В случае ошибки:
     - Логирует ошибку с использованием `debug.error(e)`.
     - Если предоставлен `api_key`, вызывает исключение `MissingAuthError` с сообщением о недействительном API-ключе.
     - Возвращает `fallback_models`.
5. **Возврат результата**: Возвращает список доступных моделей.

**Внутренние логические блоки**:

```
Проверка кэша --> Формирование URL --> Выполнение запроса --> Обработка ответа --> Возврат результата
```

**Примеры**:

```python
# Пример получения списка моделей с API-ключом
models = GeminiPro.get_models(api_key="YOUR_API_KEY")
print(models)

# Пример получения списка моделей без API-ключа (используются fallback_models)
models = GeminiPro.get_models()
print(models)
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool = False,
    proxy: str = None,
    api_key: str = None,
    api_base: str = api_base,
    use_auth_header: bool = False,
    media: MediaListType = None,
    tools: Optional[list] = None,
    connector: BaseConnector = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API Gemini.

    Args:
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для отправки в API.
        stream (bool, optional): Флаг для включения потоковой передачи данных. Defaults to False.
        proxy (str, optional): URL прокси-сервера. Defaults to None.
        api_key (str, optional): API-ключ для Google Gemini. Defaults to None.
        api_base (str, optional): Базовый URL API. Defaults to api_base.
        use_auth_header (bool, optional): Использовать заголовок авторизации. Defaults to False.
        media (MediaListType, optional): Список медиафайлов для отправки. Defaults to None.
        tools (Optional[list], optional): Список инструментов для использования. Defaults to None.
        connector (BaseConnector, optional): Aiohttp connector. Defaults to None.
        **kwargs: Дополнительные параметры для конфигурации генерации.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от API Gemini.

    Raises:
        MissingAuthError: Если отсутствует `api_key`.
        RuntimeError: Если при выполнении запроса возникла ошибка.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API Google Gemini. Этот генератор позволяет отправлять запросы к API и получать ответы в асинхронном режиме, поддерживая потоковую передачу данных, мультимодальные запросы (текст и изображения) и использование инструментов.

**Параметры**:
- `model` (str): Имя используемой модели Gemini.
- `messages` (Messages): Список сообщений для отправки в API. Каждое сообщение содержит роль (`user`, `assistant`, `system`) и контент.
- `stream` (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `False`.
- `proxy` (str, optional): URL прокси-сервера для выполнения запросов. По умолчанию `None`.
- `api_key` (str, optional): API-ключ для аутентификации в Google Gemini API. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL API Gemini. По умолчанию использует атрибут класса `api_base`.
- `use_auth_header` (bool, optional): Флаг, указывающий, передавать ли API-ключ в заголовке `Authorization` (Bearer token). По умолчанию `False`.
- `media` (MediaListType, optional): Список медиафайлов (изображений) для отправки вместе с запросом. По умолчанию `None`.
- `tools` (Optional[list], optional): Список инструментов (function calling) для использования в запросе. Каждый инструмент содержит описание функции и её параметров. По умолчанию `None`.
- `connector` (BaseConnector, optional): Пользовательский коннектор aiohttp для управления соединением. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры конфигурации для генерации контента, такие как `stop`, `temperature`, `max_tokens`, `top_p`, `top_k`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает ответы от API Gemini. В случае потоковой передачи данных, генератор выдает части ответа по мере их поступления.

**Вызывает исключения**:
- `MissingAuthError`: Если не предоставлен `api_key`.
- `RuntimeError`: Если при выполнении запроса к API произошла ошибка (например, неверный формат ответа, ошибка на стороне сервера).

**Как работает функция**:

1. **Проверка аутентификации**: Проверяет, предоставлен ли `api_key`. Если нет, вызывает исключение `MissingAuthError`.
2. **Получение имени модели**: Вызывает `cls.get_model` для получения имени модели, используя предоставленный `model`, `api_key` и `api_base`.
3. **Формирование заголовков и параметров запроса**:
   - Если `use_auth_header` равен `True`, формирует заголовок `Authorization` с API-ключом.
   - Иначе, добавляет `api_key` в параметры запроса.
4. **Определение метода и URL**: Определяет метод API (`streamGenerateContent` для потоковой передачи, `generateContent` для обычного запроса) и формирует URL запроса.
5. **Формирование данных запроса**:
   - Преобразует список сообщений (`messages`) в формат, ожидаемый API Gemini. Сообщения с ролью `assistant` преобразуются в роль `model`. Системные сообщения исключаются из основного тела запроса, но используются для формирования `system_instruction`.
   - Добавляет медиафайлы (`media`) в запрос, если они предоставлены. Медиафайлы кодируются в Base64 и добавляются в последнюю часть сообщения пользователя.
   - Добавляет параметры конфигурации генерации (`generationConfig`) из `kwargs`, такие как `stopSequences`, `temperature`, `maxOutputTokens`, `topP`, `topK`.
   - Добавляет инструменты (`tools`) в запрос, если они предоставлены. Инструменты описывают функции, которые модель может вызывать.
   - Формирует `system_instruction` из системных сообщений, если они есть.
6. **Выполнение асинхронного запроса**:
   - Использует `aiohttp.ClientSession` для выполнения POST-запроса к API.
   - Обрабатывает ответ:
     - В случае ошибки (не 200 OK), извлекает сообщение об ошибке из JSON-ответа и вызывает исключение `RuntimeError`.
     - В случае потоковой передачи данных (`stream=True`):
       - Читает ответ по частям (chunks).
       - Собирает строки JSON из chunks.
       - Извлекает текст из каждой части ответа и выдает его через `yield`.
       - Извлекает информацию об использовании токенов (`usageMetadata`) и выдает объект `Usage`.
       - Обрабатывает ошибки при чтении chunks и вызывает исключение `RuntimeError`.
     - В случае обычного запроса (`stream=False`):
       - Извлекает текст ответа из JSON-ответа и выдает его через `yield`.
       - Если `candidate["finishReason"] == "STOP"` выдает просто текст
       - Иначе выдает `candidate["finishReason"] + \' \' + candidate["safetyRatings"]`
7. **Закрытие сессии**: После завершения запроса, `aiohttp.ClientSession` автоматически закрывается.

**Внутренние функции**:

Функция не содержит внутренних функций.

**Внутренние логические блоки**:

```
Проверка аутентификации --> Получение имени модели --> Формирование заголовков и параметров -->
Определение метода и URL --> Формирование данных запроса --> Выполнение асинхронного запроса -->
Обработка ответа (потоковая или обычная) --> Закрытие сессии
```

**Примеры**:

```python
# Пример использования асинхронного генератора для получения ответа
async def main():
    messages = [
        {"role": "user", "content": "Напиши небольшое стихотворение о природе."}
    ]
    async for response in GeminiPro.create_async_generator(
        model="gemini-1.5-pro",
        messages=messages,
        api_key="YOUR_API_KEY",
        stream=True
    ):
        print(response, end="")

# Пример использования асинхронного генератора с media (добавьте путь к изображению)
async def main():
    messages = [
        {"role": "user", "content": "Опиши что изображено на картинке"}
    ]
    media = [("path_to_image.jpg", "image.jpg")]
    async for response in GeminiPro.create_async_generator(
        model="gemini-1.5-pro",
        messages=messages,
        api_key="YOUR_API_KEY",
        media=media,
        stream=False
    ):
        print(response, end="")

# Пример использования инструментов
async def main():
    tools = [{
        "function": {
            "name": "get_current_weather",
            "description": "Получает текущую погоду в заданном месте",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Город и страна, например: Москва, Россия"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Единица измерения температуры"
                    }
                },
                "required": ["location"]
            }
        }
    }]
    messages = [
        {"role": "user", "content": "Какая погода в Москве?"}
    ]
    async for response in GeminiPro.create_async_generator(
        model="gemini-1.5-pro",
        messages=messages,
        api_key="YOUR_API_KEY",
        tools=tools,
        stream=False
    ):
        print(response, end="")
```