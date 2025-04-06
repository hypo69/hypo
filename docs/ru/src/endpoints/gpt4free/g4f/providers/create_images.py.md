# Модуль для создания изображений на основе текстовых запросов
## Обзор

Модуль `create_images.py` предназначен для создания изображений на основе текстовых запросов, используя функциональность DALL-E 3 или аналогичных генераторов изображений. Он предоставляет класс `CreateImagesProvider`, который обрабатывает запросы на создание изображений, встроенные в текстовые сообщения.

## Подробней

Модуль позволяет интегрировать процесс генерации изображений непосредственно в текстовое взаимодействие с AI-моделями. Он использует специальные теги `<img data-prompt="keywords for the image">` для указания запросов на генерацию изображений. При обнаружении такого тега, модуль вызывает соответствующие функции для создания изображений (синхронные или асинхронные) и вставляет результаты в текст ответа.

Расположение модуля `hypotez/src/endpoints/gpt4free/g4f/providers/create_images.py` указывает, что он является частью системы для работы с различными провайдерами AI-сервисов, в частности, для интеграции с GPT4Free.

## Классы

### `CreateImagesProvider`

**Описание**: Класс `CreateImagesProvider` предназначен для обработки запросов на создание изображений на основе текстовых подсказок. Он использует предоставленные функции создания изображений и интегрирует их в процесс обработки сообщений.

**Принцип работы**:
Класс получает на вход другого провайдера, который отвечает за обработку текста, а также две функции: для синхронного и асинхронного создания изображений. Когда в тексте сообщения обнаруживается тег `<img data-prompt="...">`, класс вызывает соответствующую функцию создания изображений и вставляет результат в ответ.

**Наследует**:
- `BaseProvider`: Базовый класс для провайдеров, предоставляющий общую функциональность.

**Атрибуты**:
- `provider` (ProviderType): Провайдер, обрабатывающий остальные задачи, не связанные с генерацией изображений.
- `create_images` (callable): Функция для синхронного создания изображений.
- `create_images_async` (callable): Функция для асинхронного создания изображений.
- `system_message` (str): Системное сообщение, объясняющее возможность генерации изображений.
- `include_placeholder` (bool): Флаг, определяющий, нужно ли включать placeholder изображения в вывод.
- `__name__` (str): Имя провайдера.
- `url` (str): URL провайдера.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу.

**Методы**:
- `__init__`: Инициализирует `CreateImagesProvider`.
- `create_completion`: Создает результат завершения, обрабатывая подсказки для создания изображений в сообщениях.
- `create_async`: Асинхронно создает ответ, обрабатывая подсказки для создания изображений в сообщениях.

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
        self.provider = provider
        self.create_images = create_images
        self.create_images_async = create_async
        self.system_message = system_message
        self.include_placeholder = include_placeholder
        self.__name__ = provider.__name__
        self.url = provider.url
        self.working = provider.working
        self.supports_stream = provider.supports_stream
```

**Назначение**: Инициализирует экземпляр класса `CreateImagesProvider`.

**Параметры**:
- `provider` (ProviderType): Провайдер, который будет использоваться для обработки текста и других задач, не связанных с созданием изображений.
- `create_images` (callable): Функция, вызываемая для создания изображений в синхронном режиме.
- `create_async` (callable): Функция, вызываемая для создания изображений в асинхронном режиме.
- `system_message` (str, optional): Системное сообщение, добавляемое в начало сообщений для указания возможности генерации изображений. По умолчанию используется значение `system_message`.
- `include_placeholder` (bool, optional): Флаг, определяющий, следует ли включать placeholder (например, `<img data-prompt="...">`) в вывод. По умолчанию `True`.

**Как работает функция**:

1.  **Присвоение значений параметрам**:
    - Значения переданных параметров присваиваются атрибутам экземпляра класса:
        - `self.provider = provider`
        - `self.create_images = create_images`
        - `self.create_images_async = create_async`
        - `self.system_message = system_message`
        - `self.include_placeholder = include_placeholder`
        - `self.__name__ = provider.__name__`
        - `self.url = provider.url`
        - `self.working = provider.working`
        - `self.supports_stream = provider.supports_stream`

Схема работы функции:

```
Начало инициализации
↓
Присвоение provider
↓
Присвоение create_images
↓
Присвоение create_images_async
↓
Присвоение system_message
↓
Присвоение include_placeholder
↓
Присвоение __name__
↓
Присвоение url
↓
Присвоение working
↓
Присвоение supports_stream
↓
Конец инициализации
```

**Примеры**:
```python
# Пример инициализации CreateImagesProvider с использованием фиктивных функций и провайдера
class MockProvider:
    __name__ = "MockProvider"
    url = "http://example.com"
    working = True
    supports_stream = False

def mock_create_images(prompt: str):
    return f"Image created synchronously with prompt: {prompt}"

async def mock_create_async(prompt: str):
    return f"Image created asynchronously with prompt: {prompt}"

provider = CreateImagesProvider(
    provider = MockProvider(),
    create_images = mock_create_images,
    create_async = mock_create_async,
    system_message = "This is a test system message.",
    include_placeholder = False
)
```
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
            it calls messages to detect image creation prompts. When such a prompt is found, 
            it calls the synchronous image creation function and includes the resulting image in the output.
        """
        messages.insert(0, {"role": "system", "content": self.system_message})
        buffer = ""
        for chunk in self.provider.create_completion(model, messages, stream, **kwargs):
            if isinstance(chunk, ImageResponse):
                yield chunk
            elif isinstance(chunk, str) and buffer or "<" in chunk:
                buffer += chunk
                if ">" in buffer:
                    match = re.search(r'<img data-prompt="(.*?)">', buffer)
                    if match:
                        placeholder, prompt = match.group(0), match.group(1)
                        start, append = buffer.split(placeholder, 1)
                        if start:
                            yield start
                        if self.include_placeholder:
                            yield placeholder
                        if debug.logging:
                            print(f"Create images with prompt: {prompt}")
                        yield from self.create_images(prompt)
                        if append:
                            yield append
                    else:
                        yield buffer
                    buffer = ""
            else:
                yield chunk
```

**Назначение**: Создает результат завершения, обрабатывая запросы на создание изображений, найденные в сообщениях.

**Параметры**:
- `model` (str): Модель, используемая для создания завершения.
- `messages` (Messages): Список сообщений для обработки, которые могут содержать запросы на создание изображений.
- `stream` (bool, optional): Указывает, следует ли использовать потоковый режим. По умолчанию `False`.
- `**kwargs`: Дополнительные именованные аргументы, передаваемые провайдеру.

**Возвращает**:
- `CreateResult`: Куски обработанных сообщений, включая данные изображений, если применимо (yield).

**Как работает функция**:

1.  **Добавление системного сообщения**:
    - В начало списка сообщений добавляется системное сообщение, объясняющее возможность генерации изображений:
      `messages.insert(0, {"role": "system", "content": self.system_message})`
2.  **Инициализация буфера**:
    - Инициализируется пустая строка `buffer` для накопления данных.
3.  **Обработка чанков**:
    - Цикл по чанкам, возвращаемым методом `create_completion` базового провайдера:
      `for chunk in self.provider.create_completion(model, messages, stream, **kwargs):`
        - Если чанк является экземпляром `ImageResponse`, он возвращается:
          `if isinstance(chunk, ImageResponse): yield chunk`
        - Если чанк является строкой и содержит `<` или `buffer` не пуст:
            - Чанк добавляется в буфер: `buffer += chunk`
            - Если в буфере есть `>`:
                - Поиск тега `<img data-prompt="(.*?)">` в буфере: `match = re.search(r'<img data-prompt="(.*?)">', buffer)`
                - Если тег найден:
                    - Извлечение placeholder и prompt из найденного тега: `placeholder, prompt = match.group(0), match.group(1)`
                    - Разделение буфера на части до и после placeholder: `start, append = buffer.split(placeholder, 1)`
                    - Возврат части до placeholder, если она есть: `if start: yield start`
                    - Возврат placeholder, если `self.include_placeholder` равен `True`: `if self.include_placeholder: yield placeholder`
                    - Вывод сообщения в консоль (если включено логирование): `if debug.logging: print(f"Create images with prompt: {prompt}")`
                    - Вызов функции `self.create_images` для создания изображений и возврат результатов: `yield from self.create_images(prompt)`
                    - Возврат части после placeholder, если она есть: `if append: yield append`
                    - Очистка буфера: `buffer = ""`
                - Если тег не найден, возвращается весь буфер: `else: yield buffer`
            - Иначе, чанк возвращается без изменений: `else: yield chunk`

Схема работы функции:

```
Начало create_completion
↓
Добавление системного сообщения
↓
Инициализация буфера
↓
Начало цикла обработки чанков
│
├───>  Чанк - ImageResponse?
│     └───> Да: возврат чанка
│     └───> Нет: Чанк - строка и содержит "<" или буфер не пуст?
│           └───> Да: Добавление чанка в буфер
│           │     └───> В буфере есть ">"?
│           │           └───> Да: Поиск тега <img data-prompt="(.*?)">
│           │           │     └───> Тег найден?
│           │           │           └───> Да: Извлечение placeholder и prompt
│           │           │           │     └───> Разделение буфера
│           │           │           │     └───> Возврат части до placeholder (если есть)
│           │           │           │     └───> Возврат placeholder (если нужно)
│           │           │           │     └───> Вызов create_images и возврат результата
│           │           │           │     └───> Возврат части после placeholder (если есть)
│           │           │           │     └───> Очистка буфера
│           │           │           └───> Нет: Возврат буфера
│           │           └───> Нет: (продолжение цикла)
│           └───> Нет: возврат чанка
│
└───> Конец цикла
```

**Примеры**:
```python
# Пример использования create_completion с мок-провайдером и мок-функциями
class MockProvider:
    def create_completion(self, model, messages, stream, **kwargs):
        yield "This is a test message with <img data-prompt='test image prompt'> and some additional text."

def mock_create_images(prompt: str):
    yield f"Image created synchronously with prompt: {prompt}"

async def mock_create_async(prompt: str):
    return f"Image created asynchronously with prompt: {prompt}"

provider = CreateImagesProvider(
    provider = MockProvider(),
    create_images = mock_create_images,
    create_async = mock_create_async,
    system_message = "This is a test system message.",
    include_placeholder = True
)

result = provider.create_completion(model="test_model", messages=[{"role": "user", "content": "test"}])
for item in result:
    print(item)
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
        messages.insert(0, {"role": "system", "content": self.system_message})
        response = await self.provider.create_async(model, messages, **kwargs)
        matches = re.findall(r'(<img data-prompt="(.*?)">)', response)
        results = []
        placeholders = []
        for placeholder, prompt in matches:
            if placeholder not in placeholders:
                if debug.logging:
                    print(f"Create images with prompt: {prompt}")
                results.append(self.create_images_async(prompt))
                placeholders.append(placeholder)
        results = await asyncio.gather(*results)
        for idx, result in enumerate(results):
            placeholder = placeholder[idx]
            if self.include_placeholder:
                result = placeholder + result
            response = response.replace(placeholder, result)
        return response
```

**Назначение**: Асинхронно создает ответ, обрабатывая запросы на создание изображений, найденные в сообщениях.

**Параметры**:
- `model` (str): Модель, используемая для создания ответа.
- `messages` (Messages): Список сообщений для обработки, которые могут содержать запросы на создание изображений.
- `**kwargs`: Дополнительные именованные аргументы, передаваемые провайдеру.

**Возвращает**:
- `str`: Обработанная строка ответа, включающая данные сгенерированных изображений (если применимо).

**Как работает функция**:

1.  **Добавление системного сообщения**:
    - В начало списка сообщений добавляется системное сообщение, объясняющее возможность генерации изображений:
      `messages.insert(0, {"role": "system", "content": self.system_message})`
2.  **Получение ответа от базового провайдера**:
    - Асинхронно вызывается метод `create_async` базового провайдера:
      `response = await self.provider.create_async(model, messages, **kwargs)`
3.  **Поиск тегов изображений**:
    - Поиск всех тегов `<img data-prompt="(.*?)">` в ответе:
      `matches = re.findall(r'(<img data-prompt="(.*?)">)', response)`
4.  **Создание задач для генерации изображений**:
    - Цикл по найденным тегам:
      `for placeholder, prompt in matches:`
        - Если placeholder еще не обрабатывался:
          `if placeholder not in placeholders:`
            - Вывод сообщения в консоль (если включено логирование):
              `if debug.logging: print(f"Create images with prompt: {prompt}")`
            - Добавление асинхронной задачи `self.create_images_async(prompt)` в список `results`.
            - Добавление `placeholder` в список `placeholders`.
5.  **Ожидание завершения всех задач**:
    - Асинхронное ожидание завершения всех задач генерации изображений:
      `results = await asyncio.gather(*results)`
6.  **Замена placeholder'ов на результаты**:
    - Цикл по результатам генерации изображений:
      `for idx, result in enumerate(results):`
        - Получение соответствующего `placeholder`: `placeholder = placeholder[idx]`
        - Если нужно включать placeholder в результат: `if self.include_placeholder: result = placeholder + result`
        - Замена `placeholder` на результат в строке `response`: `response = response.replace(placeholder, result)`
7.  **Возврат обработанного ответа**:
    - Возврат строки `response` с замененными placeholder'ами на сгенерированные изображения: `return response`

Схема работы функции:

```
Начало create_async
↓
Добавление системного сообщения
↓
Получение ответа от базового провайдера
↓
Поиск тегов изображений
↓
Создание задач для генерации изображений
↓
Ожидание завершения всех задач
↓
Замена placeholder'ов на результаты
↓
Возврат обработанного ответа
↓
Конец create_async
```

**Примеры**:
```python
# Пример использования create_async с мок-провайдером и мок-функциями
import asyncio

class MockProvider:
    async def create_async(self, model, messages, **kwargs):
        return "This is a test message with <img data-prompt='test image prompt'> and some additional text."

async def mock_create_async(prompt: str):
    return f"Image created asynchronously with prompt: {prompt}"

provider = CreateImagesProvider(
    provider = MockProvider(),
    create_images = lambda x: x,  # Mock для синхронной функции
    create_async = mock_create_async,
    system_message = "This is a test system message.",
    include_placeholder = True
)

async def main():
    result = await provider.create_async(model="test_model", messages=[{"role": "user", "content": "test"}])
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```