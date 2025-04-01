# Модуль Qwen_Qwen_2_5_Max
## Обзор

Модуль `Qwen_Qwen_2_5_Max` представляет собой асинхронный провайдер для взаимодействия с моделью Qwen Qwen-2.5-Max через API Hugging Face Space. Он обеспечивает генерацию текста на основе предоставленных сообщений, поддерживая потоковую передачу ответов и работу с системными сообщениями.

## Подробнее

Этот модуль позволяет использовать модель Qwen Qwen-2.5-Max для генерации текста, поддерживая как обычные запросы, так и потоковую передачу ответов. Он включает в себя механизмы для формирования запросов, отправки их к API Hugging Face Space и обработки полученных ответов. Модуль также поддерживает использование прокси-серверов для обеспечения доступа к API.

## Классы

### `Qwen_Qwen_2_5_Max`

**Описание**: Класс `Qwen_Qwen_2_5_Max` реализует асинхронный провайдер для модели Qwen Qwen-2.5-Max.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера (значение: `"Qwen Qwen-2.5-Max"`).
- `url` (str): URL Hugging Face Space (значение: `"https://qwen-qwen2-5-max-demo.hf.space"`).
- `api_endpoint` (str): URL API для присоединения к очереди (значение: `"https://qwen-qwen2-5-max-demo.hf.space/gradio_api/queue/join?"`).
- `working` (bool): Указывает, работает ли провайдер (значение: `True`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу (значение: `True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (значение: `True`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (значение: `False`).
- `default_model` (str): Модель по умолчанию (значение: `"qwen-qwen2-5-max"`).
- `model_aliases` (dict): Псевдонимы моделей (значение: `{"qwen-2-5-max": default_model}`).
- `models` (list): Список поддерживаемых моделей (значение: список ключей из `model_aliases`).

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
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от модели Qwen Qwen-2.5-Max.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений для отправки модели.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий фрагменты текста ответа.

    Raises:
        aiohttp.ClientError: Если возникает ошибка при выполнении HTTP-запроса.
        json.JSONDecodeError: Если не удается декодировать JSON-ответ.

    Внутренние функции:
        generate_session_hash: Генерирует уникальный идентификатор сессии.
    """
    ...
```

**Назначение**: Создает асинхронный генератор для получения ответов от модели Qwen Qwen-2.5-Max.

**Параметры**:
- `cls`: Ссылка на класс `Qwen_Qwen_2_5_Max`.
- `model` (str): Название модели.
- `messages` (Messages): Список сообщений для отправки модели.
- `proxy` (str, optional): Адрес прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий фрагменты текста ответа.

**Вызывает исключения**:
- `aiohttp.ClientError`: Если возникает ошибка при выполнении HTTP-запроса.
- `json.JSONDecodeError`: Если не удается декодировать JSON-ответ.

**Внутренние функции**:
- `generate_session_hash`: Генерирует уникальный идентификатор сессии.

#### `generate_session_hash`

```python
def generate_session_hash():
    """Generate a unique session hash."""
    return str(uuid.uuid4()).replace(\'-\', \'\')[:8] + str(uuid.uuid4()).replace(\'-\', \'\')[:4]
```

**Назначение**: Генерирует уникальный идентификатор сессии.

**Параметры**:
- Нет.

**Возвращает**:
- `str`: Уникальный идентификатор сессии.

**Как работает функция**:

1.  Функция `create_async_generator` генерирует уникальный идентификатор сессии, используя функцию `generate_session_hash`.
2.  Формирует заголовки и полезную нагрузку для отправки запроса на присоединение к очереди API.
3.  Отправляет POST-запрос к API для присоединения к очереди и получает идентификатор события.
4.  Формирует заголовки и параметры для запроса потока данных.
5.  Отправляет GET-запрос к API для получения потока данных и обрабатывает каждый фрагмент ответа.
6.  Извлекает и очищает фрагменты текста из JSON-ответов, выдавая их через генератор.
7.  Завершает работу после получения полного ответа.

**ASCII flowchart**:

```
    Начало
    |
    V
    Генерация session_hash
    |
    V
    Формирование запроса на подключение
    |
    V
    Отправка POST запроса -> Получение event_id
    |
    V
    Формирование запроса на получение данных
    |
    V
    Отправка GET запроса -> Получение потока данных
    |
    V
    Обработка JSON данных
    |
    V
    Извлечение и очистка текстовых фрагментов
    |
    V
    Выдача фрагментов через yield
    |
    V
    Конец (после завершения потока)
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict

async def main():
    model_name = "qwen-2-5-max"
    messages: List[Dict[str, str]] = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]

    generator = Qwen_Qwen_2_5_Max.create_async_generator(model=model_name, messages=messages)
    
    try:
        async for fragment in await generator:
            print(fragment, end="")
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    asyncio.run(main())