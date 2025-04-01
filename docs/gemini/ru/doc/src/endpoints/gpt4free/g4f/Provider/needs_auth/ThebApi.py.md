# Модуль ThebApi.py

## Обзор

Модуль `ThebApi.py` предоставляет интерфейс для взаимодействия с API TheB.AI. Он определяет класс `ThebApi`, который наследуется от `OpenaiTemplate` и предназначен для генерации ответов от различных AI-моделей, поддерживаемых TheB.AI. Модуль также содержит словарь `models`, связывающий имена моделей, используемые в коде, с их отображаемыми названиями на платформе TheB.AI.

## Подробней

Модуль предназначен для упрощения взаимодействия с TheB.AI API, предоставляя удобный интерфейс для отправки запросов и получения ответов от различных AI-моделей. Он включает в себя поддержку аутентификации, определение доступных моделей и преобразование сообщений в формат, требуемый API TheB.AI. Этот код используется в проекте для интеграции с сервисом TheB.AI, позволяя пользователям использовать AI-модели, предоставляемые этим сервисом.

## Классы

### `ThebApi`

**Описание**: Класс `ThebApi` предоставляет интерфейс для взаимодействия с API TheB.AI. Он наследуется от `OpenaiTemplate` и предназначен для генерации ответов от различных AI-моделей, поддерживаемых TheB.AI.

**Наследует**:
- `OpenaiTemplate`: Базовый класс для работы с API, совместимыми с OpenAI.

**Атрибуты**:
- `label` (str): Название API ("TheB.AI API").
- `url` (str): URL главной страницы TheB.AI ("https://theb.ai").
- `login_url` (str): URL страницы входа в TheB.AI ("https://beta.theb.ai/home").
- `api_base` (str): Базовый URL API TheB.AI ("https://api.theb.ai/v1").
- `working` (bool): Указывает, что API в настоящее время работает (True).
- `needs_auth` (bool): Указывает, что для доступа к API требуется аутентификация (True).
- `default_model` (str): Модель, используемая по умолчанию ("theb-ai").
- `fallback_models` (list): Список доступных моделей.

**Методы**:
- `create_async_generator`: Асинхронный генератор для создания запросов к API.

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
        """Создает асинхронный генератор для запросов к API TheB.AI.

        Args:
            model (str): Имя используемой модели.
            messages (Messages): Список сообщений для отправки в API.
            temperature (float, optional): Температура генерации. По умолчанию None.
            top_p (float, optional): Top-p вероятность. По умолчанию None.
            **kwargs: Дополнительные параметры.

        Returns:
            CreateResult: Результат создания асинхронного генератора.

        Как работает функция:
        1. Извлекает системные сообщения из списка сообщений и объединяет их в одну строку.
        2. Фильтрует список сообщений, удаляя системные сообщения.
        3. Формирует словарь `data`, содержащий параметры модели, такие как `system_prompt`, `temperature` и `top_p`.
        4. Вызывает метод `create_async_generator` базового класса `OpenaiTemplate`, передавая имя модели, сообщения и сформированный словарь `data`.

        ASCII flowchart:
        [Сообщения] --> Извлечение системных сообщений --> Объединение системных сообщений в строку --> Фильтрация сообщений --> Формирование словаря data --> Вызов create_async_generator базового класса --> [Результат]

        """
        ...
```

**Назначение**: Создает асинхронный генератор для отправки запросов к API TheB.AI.

**Параметры**:
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений для отправки в API.
- `temperature` (float, optional): Температура генерации. По умолчанию `None`.
- `top_p` (float, optional): Top-p вероятность. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `CreateResult`: Результат создания асинхронного генератора.

**Как работает функция**:
 1. **Извлечение системных сообщений**: Функция извлекает все сообщения с ролью "system" из списка `messages` и объединяет их в одну строку `system_message`.
 2. **Фильтрация сообщений**:  Удаляет системные сообщения из списка `messages`, оставляя только сообщения пользователя и ассистента.
 3. **Формирование словаря `data`**: Создаёт словарь `data`, который содержит параметры модели:
    -  `system_prompt`: Объединенные системные сообщения.
    - `temperature`: Температура генерации (если указана).
    - `top_p`: Top-p вероятность (если указана).
 4. **Вызов `super().create_async_generator`**:  Вызывает метод `create_async_generator` базового класса `OpenaiTemplate`, передавая имя модели, сообщения и сформированный словарь `data`. Это позволяет переиспользовать логику базового класса для создания асинхронного генератора.

**ASCII flowchart**:

```
[messages] --> [Извлечение system сообщений] --> [Объединение в system_message] --> [Фильтрация сообщений] --> [Формирование data] --> [super().create_async_generator] --> [Результат]
```
**Примеры**:

```python
# Пример вызова create_async_generator
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]
result = ThebApi.create_async_generator(model="theb-ai", messages=messages, temperature=0.7, top_p=0.9)
```

## Функции

### `models`

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
```

**Назначение**: Словарь, содержащий соответствия между именами моделей, используемыми в коде, и их отображаемыми названиями на платформе TheB.AI.

**Описание**:
- `"theb-ai"`: `"TheB.AI"`
- `"gpt-3.5-turbo"`: `"GPT-3.5"`
- `"gpt-4-turbo"`: `"GPT-4 Turbo"`
- `"gpt-4"`: `"GPT-4"`
- `"claude-3.5-sonnet"`: `"Claude"`
- `"llama-2-7b-chat"`: `"Llama 2 7B"`
- `"llama-2-13b-chat"`: `"Llama 2 13B"`
- `"llama-2-70b-chat"`: `"Llama 2 70B"`
- `"code-llama-7b"`: `"Code Llama 7B"`
- `"code-llama-13b"`: `"Code Llama 13B"`
- `"code-llama-34b"`: `"Code Llama 34B"`
- `"qwen-2-72b"`: `"Qwen"`