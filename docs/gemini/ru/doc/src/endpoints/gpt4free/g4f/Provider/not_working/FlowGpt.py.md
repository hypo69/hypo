# Модуль `FlowGpt.py`

## Обзор

Модуль предоставляет асинхронтный интерфейс для взаимодействия с платформой FlowGPT. Он позволяет генерировать текст с использованием различных моделей, таких как GPT-3.5 Turbo, GPT-4 Turbo, Google Gemini и других. Модуль поддерживает сохранение истории сообщений и использование системных сообщений для управления поведением модели.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с платформой FlowGPT для генерации текста на основе предоставленных сообщений и выбранной модели. Он использует асинхронные запросы для взаимодействия с API FlowGPT и предоставляет результаты в виде асинхронного генератора.

## Классы

### `FlowGpt`

**Описание**: Класс `FlowGpt` предоставляет асинхронный интерфейс для взаимодействия с платформой FlowGPT.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL для взаимодействия с FlowGPT (`https://flowgpt.com/chat`).
- `working` (bool): Указывает, работает ли провайдер (в данном случае `False`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (`True`).
- `default_model` (str): Модель, используемая по умолчанию (`gpt-3.5-turbo`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь с псевдонимами моделей.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от FlowGPT.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    temperature: float = 0.7,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от FlowGPT.

    Args:
        cls (FlowGpt): Класс FlowGpt.
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки в FlowGPT.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        temperature (float, optional): Температура генерации. По умолчанию `0.7`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий ответы от FlowGPT.

    Raises:
        Exception: В случае ошибок при взаимодействии с API FlowGPT.
    """
```

**Назначение**: Создает асинхронный генератор для получения ответов от FlowGPT.

**Параметры**:
- `cls` (FlowGpt): Класс `FlowGpt`.
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений для отправки в FlowGPT.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `temperature` (float, optional): Температура генерации. По умолчанию `0.7`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от FlowGPT.

**Вызывает исключения**:
- `Exception`: В случае ошибок при взаимодействии с API FlowGPT.

**Как работает функция**:

1. **Получение модели**: Извлекает название модели, используя `cls.get_model(model)`, чтобы учесть возможные псевдонимы.
2. **Подготовка заголовков**:
   - Генерирует `timestamp`, `nonce`, `auth` и `signature` для аутентификации запроса.
   - Формирует словарь `headers` с необходимыми HTTP-заголовками, включая сгенерированные значения и User-Agent.
3. **Формирование данных запроса**:
   - Извлекает историю сообщений и системное сообщение из списка `messages`.
   - Если системное сообщение отсутствует, устанавливает его значение по умолчанию.
   - Создает словарь `data` с параметрами запроса, включая модель, вопрос, историю сообщений, системное сообщение и другие параметры.
4. **Отправка запроса и обработка ответа**:
   - Использует `ClientSession` для отправки асинхронного POST-запроса к API FlowGPT (`https://prod-backend-k8s.flowgpt.com/v3/chat-anonymous`).
   - Проверяет статус ответа с помощью `raise_for_status`.
   - Итерируется по чанкам ответа и извлекает текстовые данные, генерируя их через `yield`.

**Внутренние функции**: Отсутствуют

**ASCII flowchart**:

```
    Получение модели
        ↓
    Подготовка заголовков (timestamp, nonce, auth, signature, headers)
        ↓
    Формирование данных запроса (data)
        ↓
    Отправка POST-запроса к API FlowGPT
        ↓
    Проверка статуса ответа
        ↓
    Итерация по чанкам ответа
        |
    Извлечение текстовых данных из JSON
        |
    Генерация данных (yield)
```

**Примеры**:

```python
# Пример вызова функции
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you?"}
]
async def main():
    generator = await FlowGpt.create_async_generator(model="gpt-3.5-turbo", messages=messages)
    async for message in generator:
        print(message)

# Запуск примера
# import asyncio
# asyncio.run(main())
```

```python
# Пример вызова функции с прокси
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you?"}
]
async def main():
    generator = await FlowGpt.create_async_generator(model="gpt-3.5-turbo", messages=messages, proxy="http://your_proxy:8080")
    async for message in generator:
        print(message)

# Запуск примера
# import asyncio
# asyncio.run(main())