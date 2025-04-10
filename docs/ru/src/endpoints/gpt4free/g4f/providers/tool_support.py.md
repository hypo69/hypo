# Модуль поддержки инструментов

## Обзор

Модуль `tool_support.py` предоставляет класс `ToolSupportProvider`, который предназначен для поддержки интеграции инструментов (tools) в запросы к моделям генерации текста, таким как GPT-4. Это позволяет модели использовать внешние функции и возвращать результаты в структурированном формате, например, JSON.

## Подробнее

Этот модуль служит мостом между моделями и внешними инструментами, обеспечивая стандартизированный способ вызова и обработки ответов от этих инструментов. Он поддерживает асинхронные запросы и предоставляет функциональность для форматирования запросов и фильтрации ответов.

## Классы

### `ToolSupportProvider`

**Описание**: Класс `ToolSupportProvider` является асинхронным провайдером, который обеспечивает поддержку использования инструментов с моделями.

**Наследует**: `AsyncGeneratorProvider`

**Атрибуты**:
- `working` (bool): Указывает, работает ли провайдер. Всегда `True`.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с моделью с использованием инструментов.

## Функции

### `create_async_generator`

```python
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        stream: bool = True,
        media: MediaListType = None,
        tools: list[str] = None,
        response_format: dict = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для взаимодействия с моделью с использованием инструментов.

        Args:
            model (str): Имя модели для использования. Может включать имя провайдера через `:`.
            messages (Messages): Список сообщений для отправки в модель.
            stream (bool, optional): Флаг, указывающий, использовать ли потоковую передачу. По умолчанию `True`.
            media (MediaListType, optional): Список медиафайлов для отправки в модель. По умолчанию `None`.
            tools (list[str], optional): Список инструментов для использования с моделью. По умолчанию `None`.
            response_format (dict, optional): Формат ответа, например, `{"type": "json"}`. По умолчанию `None`.
            **kwargs: Дополнительные аргументы, передаваемые провайдеру.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий части ответа модели.

        Raises:
            ValueError: Если передано больше одного инструмента.

        """
```

**Назначение**: Функция `create_async_generator` создает и возвращает асинхронный генератор, который позволяет взаимодействовать с заданной моделью, используя предоставленные инструменты. Она отвечает за подготовку запроса, отправку его в модель и обработку потоковых ответов.

**Параметры**:
- `cls`: Ссылка на класс `ToolSupportProvider`.
- `model` (str): Имя модели для использования. Может включать имя провайдера через `:`.
- `messages` (Messages): Список сообщений для отправки в модель.
- `stream` (bool, optional): Флаг, указывающий, использовать ли потоковую передачу. По умолчанию `True`.
- `media` (MediaListType, optional): Список медиафайлов для отправки в модель. По умолчанию `None`.
- `tools` (list[str], optional): Список инструментов для использования с моделью. По умолчанию `None`.
- `response_format` (dict, optional): Формат ответа, например, `{"type": "json"}`. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, передаваемые провайдеру.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий части ответа модели.

**Вызывает исключения**:
- `ValueError`: Если передано больше одного инструмента.

**Как работает функция**:

1.  **Разделение модели и провайдера**: Если в имени модели присутствует `:`, функция разделяет строку на имя провайдера и имя модели.
2.  **Получение модели и провайдера**: Используется функция `get_model_and_provider` для получения экземпляра модели и провайдера на основе предоставленных имени модели и провайдера.
3.  **Обработка инструментов**:
    *   Проверяется, что передан только один инструмент. Если передано больше одного инструмента, вызывается исключение `ValueError`.
    *   Если `response_format` не указан, устанавливается значение по умолчанию `{"type": "json"}`.
    *   Извлекаются свойства параметров инструмента и формируется сообщение для модели с инструкциями по форматированию ответа в JSON.
4.  **Асинхронная генерация**:
    *   Вызывается асинхронный генератор `provider.get_async_create_function()` для получения потоковых ответов от модели.
    *   Обрабатываются различные типы чанков (части ответа):
        *   `str`: Добавляется в список `chunks`.
        *   `Usage`: Передается вызывающей стороне.
        *   `FinishReason`: Указывает на завершение генерации.
        *   Другие типы чанков немедленно передаются вызывающей стороне.
5.  **Обработка результатов**:
    *   Если не было информации об использовании (`Usage`), создается и передается объект `Usage` на основе длины собранных чанков.
    *   Если использовались инструменты, формируется объект `ToolCalls` с именем функции и аргументами, извлеченными из `chunks` с использованием `filter_json`.
    *   Собранные чанки (`chunks`) передаются вызывающей стороне.
    *   Если был получен `FinishReason`, он передается вызывающей стороне.

**ASCII flowchart функции**:

```
    Начало
      ↓
    Проверка наличия ':' в model
      ↓
    Получение model и provider
      ↓
    Проверка tools
      ↓
    Формирование messages для tools
      ↓
    Асинхронная генерация chunks
      ↓
    Обработка chunks
      ↓
    Обработка Usage
      ↓
    Обработка ToolCalls
      ↓
    Передача chunks
      ↓
    Передача FinishReason
      ↓
    Конец
```

**Примеры**:

Пример 1: Использование модели с указанием провайдера и инструмента:

```python
model = "openai:gpt-4"
messages = [{"role": "user", "content": "Напиши функцию на Python, которая складывает два числа."}]
tools = [{"function": {"name": "add", "parameters": {"properties": {"a": {"type": "number"}, "b": {"type": "number"}}}}}]

async for chunk in ToolSupportProvider.create_async_generator(model=model, messages=messages, tools=tools):
    print(chunk)
```

Пример 2: Использование модели с потоковой передачей и медиафайлами:

```python
model = "gemini"
messages = [{"role": "user", "content": "Опиши изображение."}]
media = [{"type": "image_url", "source_url": "https://example.com/image.jpg"}]

async for chunk in ToolSupportProvider.create_async_generator(model=model, messages=messages, media=media):
    print(chunk)
```