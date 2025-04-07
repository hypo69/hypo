# Модуль `ThebApi`

## Обзор

Модуль `ThebApi` представляет собой реализацию API для взаимодействия с сервисом TheB.AI. Он наследуется от класса `OpenaiTemplate` и предоставляет функциональность для создания асинхронных генераторов текста на основе моделей, поддерживаемых TheB.AI. Модуль предназначен для использования в проектах, требующих интеграции с TheB.AI для генерации текста.

## Подробнее

Модуль содержит определения моделей, поддерживаемых TheB.AI, а также класс `ThebApi`, который реализует логику взаимодействия с API TheB.AI. Класс `ThebApi` определяет URL для логина и базовый URL API, а также предоставляет метод `create_async_generator` для создания асинхронных генераторов текста.

## Переменные

- `models (dict)`: Словарь, содержащий соответствия между идентификаторами моделей, используемыми в коде, и их отображаемыми именами на платформе TheB.AI. Например, `"theb-ai": "TheB.AI"`.
- `login_url (str)`: URL-адрес страницы входа для аутентификации на платформе TheB.AI.
- `api_base (str)`: Базовый URL-адрес API TheB.AI для выполнения запросов.

## Классы

### `ThebApi`

**Описание**: Класс `ThebApi` предоставляет интерфейс для взаимодействия с API TheB.AI. Он наследуется от класса `OpenaiTemplate` и переопределяет некоторые его методы для адаптации к особенностям API TheB.AI.

**Наследует**:
- `OpenaiTemplate`: Класс, предоставляющий общую функциональность для работы с API, подобными OpenAI.

**Атрибуты**:
- `label (str)`: Метка, идентифицирующая провайдера TheB.AI API.
- `url (str)`: URL-адрес веб-сайта TheB.AI.
- `login_url (str)`: URL-адрес страницы логина TheB.AI.
- `api_base (str)`: Базовый URL-адрес API TheB.AI.
- `working (bool)`: Флаг, указывающий на работоспособность API.
- `needs_auth (bool)`: Флаг, указывающий на необходимость аутентификации для работы с API.
- `default_model (str)`: Модель, используемая по умолчанию, если не указана другая.
- `fallback_models (list)`: Список моделей, которые могут быть использованы в качестве запасных, если основная модель недоступна.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор текста на основе API TheB.AI.

## Функции

### `create_async_generator`

```python
@classmethod
def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    temperature: float = None,
    top_p: float = None,
    **kwargs
) -> CreateResult:
    """
    Создает асинхронный генератор текста на основе API TheB.AI.

    Args:
        model (str): Идентификатор модели, которую необходимо использовать.
        messages (Messages): Список сообщений, которые необходимо передать модели.
        temperature (float, optional): Параметр temperature, определяющий случайность генерации. По умолчанию `None`.
        top_p (float, optional): Параметр top_p, определяющий ядро выборки. По умолчанию `None`.
        **kwargs: Дополнительные аргументы, которые могут быть переданы в API.

    Returns:
        CreateResult: Результат создания асинхронного генератора.

    Как работает функция:
    1. Извлекает системные сообщения из списка сообщений.
    2. Формирует словарь `data` с параметрами запроса, включая `system_prompt`, `temperature` и `top_p`.
    3. Вызывает метод `create_async_generator` родительского класса `OpenaiTemplate` для создания генератора.

    Внутренние функции:
    - Отсутствуют

    ASCII flowchart:

    Сообщения ->  Извлечь системные сообщения (system_message)
    |
    Сообщения ->  Оставить только сообщения пользователя (messages)
    |
    system_message, temperature, top_p -> Сформировать словарь данных (data)
    |
    model, messages, data, kwargs -> Вызвать create_async_generator родительского класса

    """
```

**Назначение**: Создает асинхронный генератор текста, используя API TheB.AI.

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Идентификатор модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `temperature` (float, optional): Температура для контроля случайности вывода. По умолчанию `None`.
- `top_p` (float, optional): Top P для контроля разнообразия вывода. По умолчанию `None`.
- `**kwargs`: Дополнительные ключевые аргументы.

**Возвращает**:
- `CreateResult`: Результат создания асинхронного генератора.

**Как работает функция**:

1. **Извлечение системных сообщений**: Функция извлекает системные сообщения из входного списка сообщений, объединяя их в одну строку `system_message`.
2. **Фильтрация сообщений**: Оставляет в списке `messages` только те сообщения, которые не являются системными (то есть сообщения пользователя).
3. **Формирование данных запроса**: Создает словарь `data`, который содержит параметры запроса к API, такие как `system_prompt`, `temperature` и `top_p`.  `filter_none` удаляет параметры со значением `None`.
4. **Вызов родительского метода**: Вызывает метод `create_async_generator` родительского класса `OpenaiTemplate`, передавая ему модель, сообщения и сформированные данные запроса.

```
Сообщения --1--> Извлечение системных сообщений (system_message)
    |
    ↓
Сообщения --2--> Фильтрация сообщений (messages)
    |
    ↓
system_message, temperature, top_p --3--> Формирование данных запроса (data)
    |
    ↓
model, messages, data, kwargs --4--> Вызов create_async_generator родительского класса
    |
    ↓
   CreateResult
```

**Примеры**:

```python
# Пример вызова функции create_async_generator
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]
result = ThebApi.create_async_generator(model="theb-ai", messages=messages, temperature=0.7)
print(result)
```
```python
# Пример вызова функции create_async_generator с указанием temperature и top_p
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of Germany?"}
]
result = ThebApi.create_async_generator(model="gpt-4", messages=messages, temperature=0.9, top_p=0.8)
print(result)
```
```python
# Пример вызова функции create_async_generator без системного сообщения
messages = [
    {"role": "user", "content": "Tell me a joke."}
]
result = ThebApi.create_async_generator(model="llama-2-7b-chat", messages=messages)
print(result)
```