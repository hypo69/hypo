# Модуль ThebApi

## Обзор

Модуль `ThebApi` представляет собой класс для взаимодействия с API TheB.AI, предоставляя возможность использовать различные модели для генерации текста. Он наследуется от класса `OpenaiTemplate` и адаптирован для работы с асинхронными генераторами.

## Подробнее

Модуль предназначен для интеграции с платформой TheB.AI, которая предоставляет доступ к различным моделям, таким как GPT-3.5, GPT-4, Claude и Llama. Класс `ThebApi` содержит настройки для аутентификации, базовый URL API и список поддерживаемых моделей.

## Классы

### `ThebApi`

**Описание**: Класс для взаимодействия с API TheB.AI.

**Наследует**:
- `OpenaiTemplate`: Предоставляет базовую функциональность для работы с API, подобными OpenAI.

**Атрибуты**:
- `label` (str): Метка, идентифицирующая API ("TheB.AI API").
- `url` (str): URL главной страницы TheB.AI ("https://theb.ai").
- `login_url` (str): URL страницы для входа в TheB.AI ("https://beta.theb.ai/home").
- `api_base` (str): Базовый URL API TheB.AI ("https://api.theb.ai/v1").
- `working` (bool): Указывает, что API в настоящее время работает (True).
- `needs_auth` (bool): Указывает, требуется ли аутентификация для доступа к API (True).
- `default_model` (str): Модель, используемая по умолчанию ("theb-ai").
- `fallback_models` (list): Список моделей для переключения в случае неудачи.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для выполнения запросов к API TheB.AI.

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
    Создает асинхронный генератор для выполнения запросов к API TheB.AI.

    Args:
        cls (ThebApi): Класс ThebApi.
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        temperature (float, optional): Температура для управления случайностью генерации. По умолчанию None.
        top_p (float, optional): Параметр top_p для управления разнообразием генерации. По умолчанию None.
        **kwargs: Дополнительные аргументы, передаваемые в базовый метод.

    Returns:
        CreateResult: Результат создания асинхронного генератора.

    Как работает функция:
    1. Извлекает системные сообщения из списка сообщений и объединяет их в одну строку.
    2. Фильтрует сообщения, удаляя системные сообщения.
    3. Формирует словарь `data` с параметрами модели, включая `system_prompt`, `temperature` и `top_p`.
    4. Вызывает метод `create_async_generator` родительского класса `OpenaiTemplate`, передавая имя модели, сообщения и дополнительные данные.

    A -- Извлечение системных сообщений
    |
    B -- Фильтрация сообщений
    |
    C -- Формирование данных запроса
    |
    D -- Вызов метода create_async_generator родительского класса
    |
    E

    Примеры:
    >>> ThebApi.create_async_generator(model="theb-ai", messages=[{"role": "user", "content": "Hello"}])
    <async_generator object OpenaiTemplate.create_async_generator at 0x...>

    >>> ThebApi.create_async_generator(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant"}, {"role": "user", "content": "Hello"}], temperature=0.7)
    <async_generator object OpenaiTemplate.create_async_generator at 0x...>
    """
    system_message = "\n".join([message["content"] for message in messages if message["role"] == "system"])
    messages = [message for message in messages if message["role"] != "system"]
    data = {
        "model_params": filter_none(
            system_prompt=system_message,
            temperature=temperature,
            top_p=top_p,
        )
    }
    return super().create_async_generator(model, messages, extra_data=data, **kwargs)
```

## Переменные

- `models` (dict): Словарь, содержащий соответствия между именами моделей и их отображениями в TheB.AI.
  ```python
  models = {
      "theb-ai": "TheB.AI",
      "gpt-3.5-turbo": "GPT-3.5",
      "gpt-4-turbo": "GPT-4 Turbo",
      "gpt-4": "GPT-4",
      "claude-3.5-sonnet": "Claude",
      "llama-2-7b-chat": "Llama 2 7B",
      "llama-2-13b-chat": "Llama 2 13B",
      "llama-2-70b-chat": "Llama 2 70B",
      "code-llama-7b": "Code Llama 7B",
      "code-llama-13b": "Code Llama 13B",
      "code-llama-34b": "Code Llama 34B",
      "qwen-2-72b": "Qwen"
  }