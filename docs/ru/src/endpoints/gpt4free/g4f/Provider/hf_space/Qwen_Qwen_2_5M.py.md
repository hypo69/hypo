# Модуль `Qwen_Qwen_2_5M`

## Обзор

Модуль предоставляет асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5M через Hugging Face Space. Он позволяет отправлять запросы к модели и получать ответы в режиме реального времени.

## Подробней

Модуль `Qwen_Qwen_2_5M` использует асинхронные запросы для взаимодействия с API Hugging Face Space, предназначенным для модели Qwen Qwen-2.5M. Он поддерживает потоковую передачу данных, что позволяет получать ответы от модели частями, а не ждать полной генерации ответа. Модуль также поддерживает передачу системных сообщений, но не поддерживает историю сообщений.

## Классы

### `Qwen_Qwen_2_5M`

**Описание**: Класс предоставляет функциональность для взаимодействия с моделью Qwen Qwen-2.5M через Hugging Face Space.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, `"Qwen Qwen-2.5M"`.
- `url` (str): URL Hugging Face Space, `"https://qwen-qwen2-5-1m-demo.hf.space"`.
- `api_endpoint` (str): URL API endpoint, формируется из `url`.
- `working` (bool): Флаг, указывающий, работает ли провайдер, `True`.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных, `True`.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения, `True`.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений, `False`.
- `default_model` (str): Модель по умолчанию, `"qwen-2.5-1m-demo"`.
- `model_aliases` (dict): Алиасы моделей, `{"qwen-2.5-1m": default_model}`.
- `models` (list): Список моделей, формируется из ключей `model_aliases`.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от модели.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    return_conversation: bool = False,
    conversation: JsonConversation = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для получения ответов от модели Qwen Qwen-2.5M.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений для отправки в модель.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        return_conversation (bool, optional): Флаг, указывающий, нужно ли возвращать объект `JsonConversation`. По умолчанию `False`.
        conversation (JsonConversation, optional): Объект `JsonConversation` для поддержания контекста диалога. По умолчанию `None`.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от модели.

    Raises:
        aiohttp.ClientError: Если возникает ошибка при выполнении HTTP-запроса.
        json.JSONDecodeError: Если не удается декодировать JSON-ответ.

    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5M через Hugging Face Space. Генератор отправляет запросы к API и возвращает ответы модели в режиме реального времени.

**Параметры**:
- `model` (str): Название модели, которую нужно использовать.
- `messages` (Messages): Список сообщений, которые нужно отправить модели. Этот список обычно содержит историю разговора.
- `proxy` (str, optional): URL прокси-сервера, если необходимо использовать прокси для подключения к API. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий, нужно ли возвращать объект `JsonConversation` вместе с ответами. По умолчанию `False`.
- `conversation` (JsonConversation, optional): Объект `JsonConversation`, содержащий информацию о текущем разговоре (например, session_hash). По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, которые могут быть переданы в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который возвращает ответы от модели. Ответы могут быть типа `str` (текст ответа) или `Reasoning` (промежуточные размышления модели). Если `return_conversation` установлен в `True`, то первым элементом генератора будет объект `JsonConversation`.

**Вызывает исключения**:
- `aiohttp.ClientError`: Возникает, если происходит ошибка при выполнении HTTP-запроса (например, при подключении к API или при передаче данных).
- `json.JSONDecodeError`: Возникает, если не удается декодировать JSON-ответ, полученный от API.

**Как работает функция**:

1.  **Генерация session_hash**: Если `conversation` не предоставлен, генерируется уникальный `session_hash`.
2.  **Форматирование prompt**: Если `conversation` не предоставлен, формируется `prompt` из списка `messages`. В противном случае извлекается последнее сообщение пользователя.
3.  **Подготовка headers и payload**: Формируются HTTP-заголовки и полезная нагрузка (payload) для отправки запросов к API.
4.  **Отправка запросов**: Выполняются POST-запросы к API для получения данных. Используется `aiohttp.ClientSession` для асинхронных запросов.
5.  **Обработка ответов**: Полученные ответы обрабатываются в цикле. Если ответ содержит данные о генерации (`process_generating`), извлекается текст и возвращается через генератор. Если ответ указывает на завершение (`process_completed`), извлекается окончательный результат и возвращается.
6.  **Обработка ошибок**: В случае ошибки декодирования JSON-ответа, информация об ошибке логируется с использованием модуля `src.logger`.

**Внутренние функции**:

### `generate_session_hash`

```python
def generate_session_hash():
    """Generate a unique session hash."""
    return str(uuid.uuid4()).replace(\'-\', \'\')[:12]
```

**Назначение**: Генерирует уникальный идентификатор сессии (session hash).

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `str`: Уникальный идентификатор сессии в виде строки.

**Как работает функция**:
1.  Генерирует UUID (Universally Unique Identifier) с помощью `uuid.uuid4()`.
2.  Удаляет дефисы из UUID с помощью `replace('-', '')`.
3.  Возвращает первые 12 символов полученной строки с помощью `[:12]`.

**Примеры**:

```
>>> generate_session_hash()
'a1b2c3d4e5f6'
```

**ASCII flowchart**:

```
    generate_session_hash
    │
    uuid.uuid4()  # Генерация UUID
    │
    replace('-', '')  # Удаление дефисов
    │
    [:12]  # Получение первых 12 символов
    │
    return session_hash  # Возврат идентификатора сессии
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator, Optional

from hypotez.src.endpoints.gpt4free.g4f.Provider.hf_space.Qwen_Qwen_2_5M import Qwen_Qwen_2_5M
from hypotez.src.endpoints.gpt4free.g4f.providers.response import JsonConversation

async def main():
    model = "qwen-2.5-1m-demo"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Привет!"},
        {"role": "assistant", "content": "Здравствуйте! Чем могу помочь?"},
        {"role": "user", "content": "Расскажи о себе."}
    ]
    return_conversation = True
    proxy: Optional[str] = None
    conversation: Optional[JsonConversation] = None
    
    generator: AsyncGenerator = Qwen_Qwen_2_5M.create_async_generator(
        model=model,
        messages=messages,
        proxy=proxy,
        return_conversation=return_conversation,
        conversation=conversation
    )
    
    async for item in generator:
        print(item)

if __name__ == "__main__":
    asyncio.run(main())
```

В этом примере создается асинхронный генератор для получения ответов от модели Qwen Qwen-2.5M. Затем в цикле выводятся полученные ответы.

-------------------------------------------------------------------------------------