# Модуль для работы с провайдером Dynaspark
## Обзор

Модуль предоставляет класс `Dynaspark`, который является асинхронным генераторным провайдером для взаимодействия с сервисом Dynaspark. Dynaspark используется для генерации ответов на основе предоставленных сообщений и изображений, используя различные модели, включая Gemini.

## Подробней

Модуль `Dynaspark` предназначен для интеграции с сервисом Dynaspark через асинхронные запросы. Он поддерживает отправку текстовых сообщений и изображений, а также выбор различных моделей для генерации ответов. Класс `Dynaspark` наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что обеспечивает возможность стриминга ответов и управления моделями. Расположение файла в структуре проекта указывает на то, что он является одним из провайдеров для работы с различными AI-моделями в рамках проекта `hypotez`.

## Классы

### `Dynaspark`

**Описание**: Класс `Dynaspark` предоставляет интерфейс для взаимодействия с сервисом Dynaspark. Он позволяет генерировать ответы на основе текстовых сообщений и изображений, используя различные модели, включая Gemini.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает поддержку асинхронной генерации ответов.
- `ProviderModelMixin`: Предоставляет функциональность для управления моделями.

**Атрибуты**:
- `url` (str): URL сервиса Dynaspark.
- `login_url` (str | None): URL для логина (в данном случае `None`).
- `api_endpoint` (str): URL для отправки запросов на генерацию ответов.
- `working` (bool): Флаг, указывающий на работоспособность провайдера (в данном случае `True`).
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (в данном случае `False`).
- `use_nodriver` (bool): Флаг, указывающий на использование без драйвера (в данном случае `True`).
- `supports_stream` (bool): Флаг, указывающий на поддержку стриминга ответов (в данном случае `True`).
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений (в данном случае `False`).
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений (в данном случае `False`).
- `default_model` (str): Модель, используемая по умолчанию (`gemini-1.5-flash`).
- `default_vision_model` (str): Модель для обработки изображений, используемая по умолчанию (`gemini-1.5-flash`).
- `vision_models` (List[str]): Список поддерживаемых моделей для обработки изображений.
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь с псевдонимами моделей.

**Методы**:
- `create_async_generator`: Асинхронный генератор для создания запросов к Dynaspark и получения ответов.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    media: MediaListType = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с Dynaspark.

    Args:
        cls (Type[Dynaspark]): Ссылка на класс `Dynaspark`.
        model (str): Модель для генерации ответа.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от Dynaspark.
    """
```

**Назначение**: Создание асинхронного генератора для отправки запросов в Dynaspark и получения ответов.

**Параметры**:
- `cls` (Type[Dynaspark]): Ссылка на класс `Dynaspark`.
- `model` (str): Модель, используемая для генерации ответа.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `media` (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от Dynaspark.

**Как работает функция**:

1. **Подготовка заголовков**: Функция определяет заголовки HTTP-запроса, включая `user-agent`, `origin` и другие необходимые параметры.
2. **Создание асинхронной сессии**: Создается асинхронная сессия `ClientSession` с заданными заголовками.
3. **Формирование данных формы**: Создается объект `FormData` для отправки данных, включая пользовательский ввод, выбранную модель и, если есть, медиафайлы.
4. **Отправка запроса**: Отправляется POST-запрос на `api_endpoint` с данными формы и прокси-сервером, если он указан.
5. **Обработка ответа**: Полученный ответ преобразуется в JSON и извлекается поле `response`, которое возвращается как результат работы генератора.

**ASCII flowchart**:

```
    Начало
     ↓
  Подготовка заголовков
     ↓
  Создание асинхронной сессии
     ↓
  Формирование данных формы
     ↓
  Отправка POST-запроса
     ↓
  Обработка ответа
     ↓
    Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
messages = [{"role": "user", "content": "Hello, how are you?"}]
async for response in Dynaspark.create_async_generator(model="gemini-1.5-flash", messages=messages):
    print(response)
```
```python
# Пример использования create_async_generator с медиафайлом
messages = [{"role": "user", "content": "Describe this image."}]
media = [("image.jpg", b"image data")]
async for response in Dynaspark.create_async_generator(model="gemini-1.5-flash", messages=messages, media=media):
    print(response)
```