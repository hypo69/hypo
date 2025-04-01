# Модуль для создания изображений на основе текстовых запросов
## Обзор

Модуль `create_images.py` предназначен для интеграции функциональности генерации изображений в систему обработки текстовых сообщений. Он содержит класс `CreateImagesProvider`, который расширяет возможности базового провайдера, позволяя обрабатывать запросы на создание изображений, встроенные в текстовые сообщения. Модуль использует регулярные выражения для поиска специальных тегов `<img data-prompt="...">`, содержащих текстовые подсказки для генерации изображений.

## Подробней

Этот модуль позволяет динамически создавать изображения на основе текстовых запросов, извлеченных из сообщений. Он использует два подхода к созданию изображений: синхронный и асинхронный, что позволяет интегрировать его в различные типы приложений.

Класс `CreateImagesProvider` принимает базового провайдера и две функции для создания изображений (синхронную и асинхронную) в качестве аргументов. Это позволяет использовать различные API и модели для генерации изображений.

Основная логика работы модуля заключается в поиске в сообщениях специальных тегов `<img data-prompt="...">`, извлечении текстовой подсказки из атрибута `data-prompt` и использовании предоставленных функций для создания изображений на основе этой подсказки.

## Классы

### `CreateImagesProvider`

**Описание**: Провайдер для создания изображений на основе текстовых запросов.

**Наследует**:
- `BaseProvider`: Базовый класс для всех провайдеров.

**Атрибуты**:
- `provider` (ProviderType): Базовый провайдер, который обрабатывает задачи, не связанные с изображениями.
- `create_images` (callable): Функция для синхронного создания изображений.
- `create_images_async` (callable): Функция для асинхронного создания изображений.
- `system_message` (str): Системное сообщение, объясняющее возможности создания изображений.
- `include_placeholder` (bool): Флаг, определяющий, следует ли включать заполнитель изображения в вывод.
- `__name__` (str): Имя провайдера.
- `url` (str): URL провайдера.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу.

**Методы**:
- `__init__`: Инициализирует `CreateImagesProvider`.
- `create_completion`: Создает результат завершения, обрабатывая любые запросы на создание изображений, найденные в сообщениях.
- `create_async`: Асинхронно создает ответ, обрабатывая любые запросы на создание изображений, найденные в сообщениях.

### `__init__`

```python
def __init__(
        self,
        provider: ProviderType,
        create_images: callable,
        create_async: callable,
        system_message: str = system_message,
        include_placeholder: bool = True
    ) -> None:
        """
        Initializes the CreateImagesProvider.

        Args:
            provider (ProviderType): The underlying provider.
            create_images (callable): Function to create images synchronously.
            create_async (callable): Function to create images asynchronously.
            system_message (str, optional): System message to be prefixed to messages. Defaults to a predefined message.
            include_placeholder (bool, optional): Whether to include image placeholders in the output. Defaults to True.
        """
        ...
```

**Назначение**: Инициализирует экземпляр класса `CreateImagesProvider`.

**Параметры**:
- `provider` (ProviderType): Базовый провайдер, который будет использоваться для обработки не связанных с изображениями задач.
- `create_images` (callable): Функция, используемая для синхронного создания изображений.
- `create_async` (callable): Функция, используемая для асинхронного создания изображений.
- `system_message` (str, optional): Системное сообщение, которое будет добавлено в начало сообщений. По умолчанию используется предопределенное сообщение `system_message`.
- `include_placeholder` (bool, optional): Определяет, следует ли включать заполнитель изображения в вывод. По умолчанию `True`.

**Как работает функция**:
1.  Сохраняет переданные аргументы в качестве атрибутов экземпляра класса.

### `create_completion`

```python
def create_completion(
        self,
        model: str,
        messages: Messages,
        stream: bool = False,
        **kwargs
    ) -> CreateResult:
        """
        Creates a completion result, processing any image creation prompts found within the messages.

        Args:
            model (str): The model to use for creation.
            messages (Messages): The messages to process, which may contain image prompts.
            stream (bool, optional): Indicates whether to stream the results. Defaults to False.
            **kwargs: Additional keywordarguments for the provider.

        Yields:
            CreateResult: Yields chunks of the processed messages, including image data if applicable.

        Note:
            This method processes messages to detect image creation prompts. When such a prompt is found, 
            it calls the synchronous image creation function and includes the resulting image in the output.
        """
        ...
```

**Назначение**: Создает результат завершения, обрабатывая запросы на создание изображений, найденные в сообщениях.

**Параметры**:
- `model` (str): Модель, используемая для создания.
- `messages` (Messages): Сообщения для обработки, которые могут содержать запросы на создание изображений.
- `stream` (bool, optional): Указывает, следует ли передавать результаты потоком. По умолчанию `False`.
- `**kwargs`: Дополнительные именованные аргументы для провайдера.

**Возвращает**:
- `CreateResult`: Части обработанных сообщений, включая данные изображения, если это применимо.

**Как работает функция**:

1.  Добавляет системное сообщение в начало списка сообщений, чтобы объяснить возможности создания изображений.
2.  Итерируется по частям результата, полученного от базового провайдера.
3.  Если текущая часть является экземпляром `ImageResponse`, она передается дальше.
4.  Если текущая часть является строкой и содержит `<img data-prompt="...">`, извлекается подсказка для создания изображения.
5.  Вызывается синхронная функция создания изображения `self.create_images` с извлеченной подсказкой.
6.  Результат создания изображения передается дальше.

```
Сообщения -> Вставить системное сообщение
     ↓
     → Итерировать по частям результата от базового провайдера
     ↓
     Проверить тип части: ImageResponse или строка с "<"
     ↓
     Если ImageResponse:
     |   ↓
     |   Передать часть дальше
     |
     Если строка с "<":
     ↓
     Извлечь подсказку для создания изображения
     ↓
     Вызвать self.create_images(prompt)
     ↓
     Передать результат создания изображения дальше
```

**Примеры**:

Пример вызова функции `create_completion`:

```python
provider = CreateImagesProvider(provider=..., create_images=..., create_async=...)
model = "dall-e-3"
messages = [{"role": "user", "content": "Создай изображение: <img data-prompt='красивый пейзаж'>"},
            {"role": "assistant", "content": "Вот результат:"}]
stream = False
result = provider.create_completion(model=model, messages=messages, stream=stream)
```

### `create_async`

```python
async def create_async(
        self,
        model: str,
        messages: Messages,
        **kwargs
    ) -> str:
        """
        Asynchronously creates a response, processing any image creation prompts found within the messages.

        Args:
            model (str): The model to use for creation.
            messages (Messages): The messages to process, which may contain image prompts.
            **kwargs: Additional keyword arguments for the provider.

        Returns:
            str: The processed response string, including asynchronously generated image data if applicable.

        Note:
            This method processes messages to detect image creation prompts. When such a prompt is found, 
            it calls the asynchronous image creation function and includes the resulting image in the output.
        """
        ...
```

**Назначение**: Асинхронно создает ответ, обрабатывая запросы на создание изображений, найденные в сообщениях.

**Параметры**:
- `model` (str): Модель, используемая для создания.
- `messages` (Messages): Сообщения для обработки, которые могут содержать запросы на создание изображений.
- `**kwargs`: Дополнительные именованные аргументы для провайдера.

**Возвращает**:
- `str`: Обработанная строка ответа, включающая асинхронно сгенерированные данные изображения, если это применимо.

**Как работает функция**:

1.  Добавляет системное сообщение в начало списка сообщений, чтобы объяснить возможности создания изображений.
2.  Вызывает асинхронную функцию создания `self.provider.create_async` для получения ответа от базового провайдера.
3.  Ищет в ответе теги `<img data-prompt="...">` с использованием регулярного выражения.
4.  Извлекает подсказки для создания изображений из найденных тегов.
5.  Вызывает асинхронную функцию создания изображения `self.create_images_async` для каждой подсказки.
6.  Заменяет теги `<img data-prompt="...">` в ответе на результаты создания изображений.

```
Сообщения -> Вставить системное сообщение
     ↓
     → Вызвать асинхронную функцию создания self.provider.create_async
     ↓
     Найти теги <img data-prompt="...">
     ↓
     Извлечь подсказки для создания изображений
     ↓
     Вызвать асинхронную функцию создания изображения self.create_images_async для каждой подсказки
     ↓
     Заменить теги <img data-prompt="..."> на результаты создания изображений
     ↓
     Вернуть обработанную строку ответа
```

**Примеры**:

Пример вызова функции `create_async`:

```python
provider = CreateImagesProvider(provider=..., create_images=..., create_async=...)
model = "dall-e-3"
messages = [{"role": "user", "content": "Создай изображение: <img data-prompt='красивый пейзаж'>"},
            {"role": "assistant", "content": "Вот результат:"}]
result = await provider.create_async(model=model, messages=messages)