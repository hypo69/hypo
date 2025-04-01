# Модуль `DeepseekAI_JanusPro7b`

## Обзор

Модуль `DeepseekAI_JanusPro7b` предоставляет асинхронный интерфейс для взаимодействия с моделью Janus-Pro-7B от DeepseekAI, размещенной на Hugging Face Spaces. Он поддерживает как текстовые запросы, так и генерацию изображений, а также потоковую передачу ответов.

## Подробней

Модуль предназначен для использования в проекте `hypotez` для обеспечения функциональности генерации текста и изображений с использованием модели DeepseekAI Janus-Pro-7B. Он включает в себя функции для форматирования запросов, обработки изображений, установления соединения с API Hugging Face Spaces и обработки потоковых ответов.

## Классы

### `DeepseekAI_JanusPro7b`

**Описание**: Класс `DeepseekAI_JanusPro7b` реализует асинхронный интерфейс для взаимодействия с моделью Janus-Pro-7B от DeepseekAI. Он наследует от `AsyncGeneratorProvider` и `ProviderModelMixin`, предоставляя методы для отправки запросов к API и обработки ответов.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, "DeepseekAI Janus-Pro-7B".
- `space` (str): Название пространства на Hugging Face, "deepseek-ai/Janus-Pro-7B".
- `url` (str): URL пространства на Hugging Face.
- `api_url` (str): URL API для взаимодействия с моделью.
- `referer` (str): Referer заголовок для HTTP-запросов.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Поддерживает ли потоковую передачу ответов.
- `supports_system_message` (bool): Поддерживает ли системные сообщения.
- `supports_message_history` (bool): Поддерживает ли историю сообщений.
- `default_model` (str): Модель по умолчанию, "janus-pro-7b".
- `default_image_model` (str): Модель для генерации изображений по умолчанию, "janus-pro-7b-image".
- `default_vision_model` (str): Модель для обработки изображений по умолчанию, совпадает с `default_model`.
- `image_models` (list): Список моделей для генерации изображений.
- `vision_models` (list): Список моделей для обработки изображений.
- `models` (list): Объединенный список моделей для генерации и обработки изображений.

**Методы**:
- `run()`: Выполняет HTTP-запрос к API.
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от API.

### `DeepseekAI_JanusPro7b.run`

```python
@classmethod
def run(cls, method: str, session: StreamSession, prompt: str, conversation: JsonConversation, image: dict = None, seed: int = 0):
    """
    Выполняет HTTP-запрос к API.

    Args:
        method (str): HTTP-метод ("post" или "image").
        session (StreamSession): Асинхронная сессия для выполнения запросов.
        prompt (str): Текст запроса.
        conversation (JsonConversation): Объект, содержащий информацию о текущем диалоге.
        image (dict, optional): Данные изображения для запроса. По умолчанию `None`.
        seed (int): Зерно для генерации случайных чисел.

    Returns:
        StreamResponse: Объект ответа от API.
    """
    ...
```

### `DeepseekAI_JanusPro7b.create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    media: MediaListType = None,
    prompt: str = None,
    proxy: str = None,
    cookies: Cookies = None,
    api_key: str = None,
    zerogpu_uuid: str = "[object Object]",
    return_conversation: bool = False,
    conversation: JsonConversation = None,
    seed: int = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от API.

    Args:
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для формирования запроса.
        media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
        prompt (str, optional): Текст запроса. По умолчанию `None`.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        cookies (Cookies, optional): HTTP-куки. По умолчанию `None`.
        api_key (str, optional): API-ключ. По умолчанию `None`.
        zerogpu_uuid (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
        return_conversation (bool, optional): Возвращать ли объект диалога. По умолчанию `False`.
        conversation (JsonConversation, optional): Объект, содержащий информацию о текущем диалоге. По умолчанию `None`.
        seed (int, optional): Зерно для генерации случайных чисел. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Yields:
        AsyncResult: Асинхронный результат, содержащий ответы от API.
    """
    ...
```

## Функции

### `get_zerogpu_token`

```python
async def get_zerogpu_token(space: str, session: StreamSession, conversation: JsonConversation, cookies: Cookies = None):
    """
    Получает токен ZeroGPU для доступа к API.

    Args:
        space (str): Название пространства на Hugging Face.
        session (StreamSession): Асинхронная сессия для выполнения запросов.
        conversation (JsonConversation): Объект, содержащий информацию о текущем диалоге.
        cookies (Cookies, optional): HTTP-куки. По умолчанию `None`.

    Returns:
        tuple[str, str]: Кортеж, содержащий UUID и токен ZeroGPU.
    """
    ...
```

**Как работает функция**:

1. **Инициализация**:
   - Устанавливает `zerogpu_uuid` в `None`, если `conversation` is `None`, иначе берет значение `zerogpu_uuid` из атрибута `conversation`. Если атрибут не определен, то  `zerogpu_uuid`  тоже будет `None`.
   - Устанавливает `zerogpu_token` в значение по умолчанию `"[object Object]"`.

2. **Получение Cookies**:
   - Если `cookies` не переданы, то пытается получить их с домена `"huggingface.co"` с помощью функции `get_cookies`.
   - Если получение `cookies` завершилось неудачей, устанавливает `cookies` в `None`.

3. **Получение zerogpu_uuid (если отсутствует)**:
   - Если `zerogpu_uuid` is `None`, то выполняет GET-запрос к странице пространства Hugging Face (`f"https://huggingface.co/spaces/{space}"`) для извлечения `token` и `sessionUuid` из HTML-кода страницы с использованием регулярных выражений.
   - Если удается извлечь `token` и `sessionUuid`, то они присваиваются переменным `zerogpu_token` и `zerogpu_uuid` соответственно.

4. **Обновление токена (если есть Cookies)**:
   - Если `cookies` были получены, вычисляет время истечения срока действия токена (текущее UTC-время + 10 минут) и кодирует его в формат, пригодный для использования в URL.
   - Отправляет GET-запрос к API Hugging Face (`f"https://huggingface.co/api/spaces/{space}/jwt?expiration={encoded_dt}&include_pro_status=true"`) для получения нового токена.
   - Если запрос успешен и ответ содержит поле `"token"`, то `zerogpu_token` обновляется значением из ответа.

5. **Возврат результата**:
   - Возвращает кортеж, содержащий `zerogpu_uuid` и `zerogpu_token`.

**ASCII Flowchart**:

```
Начало
↓
Установка zerogpu_uuid и zerogpu_token по умолчанию
↓
Получение Cookies (если не переданы)
↓
zerogpu_uuid is None?
├──→ Да → GET-запрос к странице пространства для извлечения token и sessionUuid
│   │       ↓
│   │       Извлечение token и sessionUuid (если найдены)
│   │
└──→ Нет
↓
Cookies есть?
├──→ Да → Вычисление времени истечения срока действия и кодирование
│   │       ↓
│   │       GET-запрос к API для обновления токена
│   │       ↓
│   │       Обновление zerogpu_token (если получен новый токен)
│   │
└──→ Нет
↓
Возврат zerogpu_uuid и zerogpu_token
Конец
```

**Примеры**:

```python
# Пример вызова функции get_zerogpu_token
import asyncio
from aiohttp import ClientSession
from src.providers.response import JsonConversation

async def main():
    space = "deepseek-ai/Janus-Pro-7B"
    async with ClientSession() as session:
        conversation = JsonConversation(session_hash="test_session")
        zerogpu_uuid, zerogpu_token = await get_zerogpu_token(space, session, conversation)
        print(f"zerogpu_uuid: {zerogpu_uuid}")
        print(f"zerogpu_token: {zerogpu_token}")

if __name__ == "__main__":
    asyncio.run(main())