# Модуль для создания изображений с использованием текстовых подсказок
## Обзор

Этот модуль предназначен для создания изображений на основе текстовых подсказок, используя возможности различных провайдеров изображений, таких как DALL-E 3. Он содержит класс `CreateImagesProvider`, который обрабатывает запросы на создание изображений, встроенные в контент сообщений. Модуль позволяет создавать изображения как синхронно, так и асинхронно, и интегрируется с другими провайдерами для выполнения задач, не связанных с изображениями.

## Подробнее

Модуль `create_images.py` является частью проекта `hypotez` и предоставляет функциональность для генерации изображений на основе текстовых описаний. Он использует класс `CreateImagesProvider`, который оборачивает других провайдеров и добавляет возможность обработки тегов `<img data-prompt="...">` в сообщениях. Когда такой тег обнаружен, модуль извлекает текстовое описание (prompt) и использует его для создания изображения с помощью указанных функций `create_images` (синхронно) или `create_async` (асинхронно). Результат вставляется обратно в сообщение.

Этот модуль важен для создания интерактивных и мультимедийных ответов, где текстовые ответы дополняются сгенерированными изображениями на основе запроса пользователя.

## Классы

### `CreateImagesProvider`

**Описание**:
Класс `CreateImagesProvider` предназначен для обработки запросов на создание изображений на основе текстовых подсказок. Он использует предоставленные функции для создания изображений и интегрируется с другими провайдерами для обработки задач, не связанных с изображениями.

**Принцип работы**:
Класс инициализируется с указанием основного провайдера, функций для синхронного и асинхронного создания изображений, системного сообщения и флага для включения заполнителя изображения в вывод. При получении запроса на создание ответа, класс анализирует сообщения на наличие тегов `<img data-prompt="...">`. Если такой тег найден, он извлекает текстовую подсказку и использует соответствующую функцию (синхронную или асинхронную) для создания изображения. Затем результат вставляется обратно в сообщение.

**Методы**:
- `__init__`
- `create_completion`
- `create_async`

#### `__init__`

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

**Назначение**:
Инициализирует экземпляр класса `CreateImagesProvider`.

**Параметры**:
- `provider` (ProviderType): Базовый провайдер.
- `create_images` (callable): Функция для синхронного создания изображений.
- `create_async` (callable): Функция для асинхронного создания изображений.
- `system_message` (str, optional): Системное сообщение, которое будет добавлено в начало сообщений. По умолчанию используется предопределенное сообщение.
- `include_placeholder` (bool, optional): Флаг, указывающий, нужно ли включать заполнитель изображения в вывод. По умолчанию `True`.

**Как работает метод**:

1. Метод сохраняет ссылки на переданные параметры `provider`, `create_images`, `create_async`, `system_message`, `include_placeholder` в атрибуты экземпляра класса.
2. Устанавливает атрибуты `__name__` и `url` на основе атрибутов базового провайдера.
3. Копирует значения `working` и `supports_stream` из базового провайдера.

**Примеры**:
```python
# Пример инициализации CreateImagesProvider
from ..providers import Openai
from ..providers.response import ImageResponse

def sync_create_images(prompt: str) -> ImageResponse:
    """
    Функция синхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    return ImageResponse(data='image_data', format='png')

async def async_create_images(prompt: str) -> ImageResponse:
    """
    Функция асинхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    return ImageResponse(data='image_data', format='png')

provider = Openai()
image_provider = CreateImagesProvider(provider, sync_create_images, async_create_images)
```

#### `create_completion`

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

**Назначение**:
Создает результат завершения, обрабатывая все запросы на создание изображений, найденные в сообщениях.

**Параметры**:
- `model` (str): Модель, используемая для создания.
- `messages` (Messages): Сообщения для обработки, которые могут содержать подсказки для изображений.
- `stream` (bool, optional): Указывает, следует ли передавать результаты потоком. По умолчанию `False`.
- `**kwargs`: Дополнительные именованные аргументы для провайдера.

**Возвращает**:
- `CreateResult`: Части обработанных сообщений, включая данные изображения, если применимо.

**Как работает функция**:

1.  **Добавление системного сообщения**: Вставляет системное сообщение в начало списка сообщений, чтобы объяснить возможность создания изображений.
2.  **Итерация по чанкам**: Получает чанки из базового провайдера с использованием `self.provider.create_completion`.
3.  **Обработка чанков**:
    *   Если чанк является экземпляром `ImageResponse`, возвращает его.
    *   Если чанк является строкой и содержит `<img data-prompt="...">`:
        *   Накапливает строку в буфере, пока не будет найден закрывающий тег `>`.
        *   Использует регулярное выражение для поиска тега `<img data-prompt="(.*?)">` в буфере.
        *   Если тег найден:
            *   Извлекает заполнитель (placeholder) и подсказку (prompt) из тега.
            *   Разделяет буфер на три части: `start`, `placeholder`, и `append`.
            *   Возвращает `start`, если он не пустой.
            *   Возвращает `placeholder`, если `self.include_placeholder` равен `True`.
            *   Вызывает функцию `self.create_images(prompt)` для создания изображения.
            *   Возвращает части из результата создания изображения.
            *   Возвращает `append`, если он не пустой.
            *   Очищает буфер.
        *   Если тег не найден, возвращает буфер.
    *   Если чанк не содержит тег `<img data-prompt="...">`, возвращает его.

**Внутренние блоки функции**:

*   **Добавление системного сообщения**: Непосредственно изменяет список сообщений.
*   **Обработка и анализ чанков**: Проверяет, является ли текущий чанк типом `ImageResponse`, строкой, и содержит ли он тег `<img data-prompt="...">`.
*   **Извлечение и обработка `prompt`**: Использует регулярное выражение для извлечения содержимого атрибута `data-prompt` из тега `<img>`.
*   **Вызов `create_images`**: Вызывает функцию синхронного создания изображения, если `prompt` найден.
*   **Сборка и возврат результата**: Собирает результаты в нужном порядке и возвращает их.

**Примеры**:

```python
# Пример использования create_completion
from ..providers import Openai
from ..providers.response import ImageResponse

def sync_create_images(prompt: str) -> ImageResponse:
    """
    Функция синхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    return ImageResponse(data='image_data', format='png')

async def async_create_images(prompt: str) -> ImageResponse:
    """
    Функция асинхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    return ImageResponse(data='image_data', format='png')

provider = Openai()
image_provider = CreateImagesProvider(provider, sync_create_images, async_create_images)

messages = [{"role": "user", "content": "Создай изображение: <img data-prompt='cat'>"},
            {"role": "user", "content": "Создай изображение: <img data-prompt='dog'>"}]
model = "gpt-3.5-turbo"
for chunk in image_provider.create_completion(model, messages):
    print(chunk)
```

#### `create_async`

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

**Назначение**:
Асинхронно создает ответ, обрабатывая запросы на создание изображений, найденные в сообщениях.

**Параметры**:
- `model` (str): Модель, используемая для создания.
- `messages` (Messages): Сообщения для обработки, которые могут содержать подсказки для изображений.
- `**kwargs`: Дополнительные именованные аргументы для провайдера.

**Возвращает**:
- `str`: Обработанная строка ответа, включающая асинхронно сгенерированные данные изображения, если применимо.

**Как работает функция**:

1.  **Вставка системного сообщения**: Вставляет системное сообщение в начало списка сообщений, чтобы объяснить возможность создания изображений.
2.  **Получение ответа от базового провайдера**: Асинхронно получает ответ от базового провайдера с использованием `self.provider.create_async`.
3.  **Поиск тегов изображений**: Использует регулярное выражение для поиска всех тегов `<img data-prompt="(.*?)">` в ответе.
4.  **Создание задач для изображений**: Для каждого найденного тега:
    *   Извлекает заполнитель (placeholder) и подсказку (prompt) из тега.
    *   Вызывает асинхронную функцию `self.create_images_async(prompt)` для создания изображения.
    *   Сохраняет заполнители в списке `placeholders`, чтобы избежать дублирования.
5.  **Ожидание завершения задач**: Использует `asyncio.gather` для ожидания завершения всех задач создания изображений.
6.  **Замена заполнителей изображениями**: Заменяет каждый заполнитель соответствующим сгенерированным изображением в ответе.
7.  **Возврат обработанного ответа**: Возвращает строку ответа с вставленными изображениями.

**Внутренние блоки функции**:

*   **Добавление системного сообщения**: Непосредственно изменяет список сообщений.
*   **Асинхронный вызов базового провайдера**: Вызывает `create_async` базового провайдера.
*   **Поиск и извлечение `prompt`**: Использует регулярное выражение для извлечения содержимого атрибута `data-prompt` из тега `<img>`.
*   **Асинхронный вызов `create_images_async`**: Вызывает функцию асинхронного создания изображения для каждого найденного `prompt`.
*   **Сборка и замена результатов**: Ожидает завершения всех асинхронных задач и заменяет заполнители в строке ответа на сгенерированные изображения.

**Примеры**:

```python
# Пример использования create_async
import asyncio
from ..providers import Openai
from ..providers.response import ImageResponse

def sync_create_images(prompt: str) -> ImageResponse:
    """
    Функция синхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    return ImageResponse(data='image_data', format='png')

async def async_create_images(prompt: str) -> ImageResponse:
    """
    Функция асинхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    return ImageResponse(data='image_data', format='png')

async def main():
    provider = Openai()
    image_provider = CreateImagesProvider(provider, sync_create_images, async_create_images)

    messages = [{"role": "user", "content": "Создай изображение: <img data-prompt='cat'>"},
                {"role": "user", "content": "Создай изображение: <img data-prompt='dog'>"}]
    model = "gpt-3.5-turbo"
    result = await image_provider.create_async(model, messages)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

## Функции

В данном модуле нет отдельных функций, кроме методов класса `CreateImagesProvider`. Однако, в примерах выше использовались функции-заглушки `sync_create_images` и `async_create_images`, которые представляют собой функции синхронного и асинхронного создания изображений соответственно.

### `sync_create_images`

```python
def sync_create_images(prompt: str) -> ImageResponse:
    """
    Функция синхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    ...
```

**Назначение**:
Представляет собой заглушку для функции синхронного создания изображений. В реальной реализации должна создавать изображение на основе текстового описания.

**Параметры**:
- `prompt` (str): Текстовое описание для создания изображения.

**Возвращает**:
- `ImageResponse`: Объект `ImageResponse` с сгенерированным изображением. В данном случае возвращает объект с заглушкой данных.

**Как работает функция**:
Функция принимает текстовое описание изображения и возвращает объект `ImageResponse`, содержащий заглушку для данных изображения.

**Примеры**:
```python
# Пример использования sync_create_images
from ..providers.response import ImageResponse

def sync_create_images(prompt: str) -> ImageResponse:
    """
    Функция синхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    return ImageResponse(data='image_data', format='png')

image = sync_create_images("cat")
print(image)
```

### `async_create_images`

```python
async def async_create_images(prompt: str) -> ImageResponse:
    """
    Функция асинхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    ...
```

**Назначение**:
Представляет собой заглушку для функции асинхронного создания изображений. В реальной реализации должна асинхронно создавать изображение на основе текстового описания.

**Параметры**:
- `prompt` (str): Текстовое описание для создания изображения.

**Возвращает**:
- `ImageResponse`: Объект `ImageResponse` с сгенерированным изображением. В данном случае возвращает объект с заглушкой данных.

**Как работает функция**:
Функция принимает текстовое описание изображения и возвращает объект `ImageResponse`, содержащий заглушку для данных изображения.

**Примеры**:
```python
# Пример использования async_create_images
import asyncio
from ..providers.response import ImageResponse

async def async_create_images(prompt: str) -> ImageResponse:
    """
    Функция асинхронного создания изображений (заглушка).
    Args:
        prompt (str): Текстовое описание для создания изображения.

    Returns:
        ImageResponse: Объект ImageResponse с сгенерированным изображением.
    """
    return ImageResponse(data='image_data', format='png')

async def main():
    image = await async_create_images("dog")
    print(image)

if __name__ == "__main__":
    asyncio.run(main())
```