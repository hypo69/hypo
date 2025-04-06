# Модуль OpenAssistant

## Обзор

Модуль `OpenAssistant` предоставляет асинхронный генератор для взаимодействия с сервисом Open Assistant. Он позволяет отправлять сообщения и получать ответы от модели `OA_SFT_Llama_30B_6`.

## Подробней

Этот модуль предназначен для интеграции с Open Assistant API через асинхронные запросы. Он использует `aiohttp` для выполнения HTTP-запросов и предоставляет удобный способ для обмена сообщениями с моделью Open Assistant. Модуль поддерживает установку прокси, передачу cookies и настройку параметров генерации текста.

## Классы

### `OpenAssistant`

**Описание**: Класс `OpenAssistant` является асинхронным провайдером генератора для Open Assistant.

**Наследует**: `AsyncGeneratorProvider`

**Атрибуты**:
- `url` (str): URL для взаимодействия с Open Assistant API.
- `needs_auth` (bool): Указывает, требуется ли аутентификация для работы с провайдером.
- `working` (bool): Указывает, находится ли провайдер в рабочем состоянии.
- `model` (str): Название используемой модели Open Assistant.

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        cookies: dict = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для взаимодействия с Open Assistant API.

        Args:
            model (str): Название модели для использования.
            messages (Messages): Список сообщений для отправки в Open Assistant.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            cookies (dict, optional): Словарь с cookies для аутентификации. По умолчанию `None`.
            **kwargs: Дополнительные параметры для настройки генерации текста.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий текст ответа от Open Assistant.

        Raises:
            RuntimeError: Если в ответе от сервера содержится сообщение об ошибке.
            aiohttp.ClientResponseError: Если возникает HTTP-ошибка при запросе.

        Пример:
            >>> async for message in OpenAssistant.create_async_generator(model="OA_SFT_Llama_30B_6", messages=[{"role": "user", "content": "Hello"}], cookies={"session": "test"}):
            ...     print(message)
            Hello
        """
```

**Назначение**: Создает и возвращает асинхронный генератор для получения ответов от Open Assistant.

**Параметры**:
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений для отправки в Open Assistant.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `cookies` (dict, optional): Словарь с cookies для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры для настройки генерации текста.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий текст ответа от Open Assistant.

**Вызывает исключения**:
- `RuntimeError`: Если в ответе от сервера содержится сообщение об ошибке.
- `aiohttp.ClientResponseError`: Если возникает HTTP-ошибка при запросе.

**Как работает функция**:

1. **Инициализация**:
   - Если `cookies` не предоставлены, пытается получить их с `open-assistant.io`.
   - Определяет заголовки User-Agent для HTTP-запросов.

2. **Создание сессии `aiohttp`**:
   - Создает асинхронную сессию `ClientSession` с использованием предоставленных `cookies` и `headers`.

3. **Отправка запроса на создание чата**:
   - Отправляет POST-запрос к `https://open-assistant.io/api/chat` для создания нового чата.
   - Извлекает `chat_id` из ответа.

4. **Отправка сообщения пользователя**:
   - Форматирует список сообщений (`messages`) в строку, используя `format_prompt`.
   - Отправляет POST-запрос к `https://open-assistant.io/api/chat/prompter_message` с `chat_id` и отформатированным сообщением.
   - Извлекает `parent_id` из ответа.

5. **Отправка запроса на генерацию ответа ассистентом**:
   - Отправляет POST-запрос к `https://open-assistant.io/api/chat/assistant_message` с `chat_id`, `parent_id`, названием модели и параметрами генерации (`top_k`, `top_p`, `temperature`, `repetition_penalty`, `max_new_tokens`, `kwargs`).
   - Извлекает `message_id` из ответа.

6. **Получение событий чата**:
   - Отправляет POST-запрос к `https://open-assistant.io/api/chat/events` с `chat_id` и `message_id`.
   - Асинхронно перебирает строки ответа и извлекает текст (`line["text"]`) из событий типа `"token"`.
   - Возвращает текст как часть асинхронного генератора.

7. **Удаление чата**:
   - Отправляет DELETE-запрос к `https://open-assistant.io/api/chat` с `chat_id`.

```ascii
    Начало
     ↓
    Получение/установка cookies
     ↓
    Создание асинхронной сессии
     ↓
    Создание чата (POST /api/chat)
     ↓
    Отправка сообщения пользователя (POST /api/chat/prompter_message)
     ↓
    Генерация ответа ассистентом (POST /api/chat/assistant_message)
     ↓
    Получение событий (POST /api/chat/events)
     │
     ├─> Извлечение текста из событий "token"
     │   │
     │   └─> Выдача текста через yield
     │
     ↓
    Удаление чата (DELETE /api/chat)
     ↓
    Конец
```

**Примеры**:

```python
async for message in OpenAssistant.create_async_generator(model="OA_SFT_Llama_30B_6", messages=[{"role": "user", "content": "Hello"}], cookies={"session": "test"}):
    print(message)
```

```python
async for message in OpenAssistant.create_async_generator(model="OA_SFT_Llama_30B_6", messages=[{"role": "user", "content": "Как дела?"}], proxy="http://proxy.example.com"):
    print(message)
```
```python
async for message in OpenAssistant.create_async_generator(model="OA_SFT_Llama_30B_6", messages=[{"role": "user", "content": "Напиши стихотворение"}], max_new_tokens = 500):
    print(message)